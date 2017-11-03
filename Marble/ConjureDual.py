#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    show_assert = 0


    class KeyData(Object):
        __slots__ = ((
            'f',                        #   DelayedOutput
            'chain',                    #   Tuple of String+
            'keys',                     #   String
        ))


        def __init__(t, f, chain, keys):
            t.f     = f
            t.chain = chain
            t.keys  = keys


        def create_assert(t, v):
            if show_assert:
                t.f.line('assert %s',
                         ' and '.join(arrange('(%s.%s is %s)', v, k, k)   for k in t.chain))


        def create_assert_r(t):
            if show_assert:
                t.f.line('assert %s',
                         ' and '.join(arrange('(r.%s is %s)', k, k)   for k in t.chain))


        def create_r(t):
            t.f.line('r = Meta(%s)', t.keys)
            t.create_assert_r()


    def create_if_a(t, a, k1, k2, k3 = none, k4 = none, skip = 1):
        f = t.f

        if (k3 is none):
            f.line('if %s.%s is %s: return %s', a, k2, k2, a)
        else:
            f.blank()

            with f.indent(arrange('if %s.%s is %s:', a, k2, k2)):
                f.blank_suppress()
                create_if_a(t, a, k1, k3, k4, skip = skip + 1)
                t.create_r()
                f.line('store(%s, create_horde_2(%d, %s.%s, %s, %s, r))', k1, skip, a, k3, k3, a)
                f.line('return r')

        f.blank()


    def create_last(t, p2, previous, current, k_previous, k_last, k_sample = 0):
        if p2 is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p2)

        f = t.f

        f.line('%s = %s.glimpse(%s)', current, previous, k_last)
        if show_assert:
            with f.indent(arrange('if %s is not none:', current)):
                t.create_assert(current)
                f.line('return %s', current)
        else:
            f.line('if %s is not none: return %s', current, current)

        f.blank()
        t.create_r()
        f.line('%s_ = %s.insert(%s, r)', previous, previous, k_last)

        if k_sample is 0:
            f.line('if %s is not %s_: %s(%s, %s_)', previous, previous, displace, k_previous, previous)
        else:
            with f.indent(arrange('if %s is not %s_:', previous, previous)):
                f.line('assert %s_.sample().%s is %s', previous, k_sample, k_sample)
                f.line('%s(%s, %s_)', displace, k_previous, previous)

        f.line('return r')


    def create_conjure(f, prefix, suffix, k1, k2, k3 = none, k4 = none):
        if k3 is none:
            chain = ((k1, k2))
        elif k4 is none:
            chain = ((k1, k2, k3))
        else:
            chain = ((k1, k2, k3, k4))

        keys = 'k1, k2'
        if k3 is not none:  keys += ', k3'
        if k4 is not none:  keys += ', k4'

        t = KeyData(f, chain, keys)

        a    = 'a'
        b    = 'b'
        c    = 'c'
        name = arrange('%s_%s', prefix, suffix)

        f.blank2()

        f.line('@share')
        with f.indent(arrange('def produce_%s(name, Meta, cache):', name)):
            f.line('lookup = cache.get')
            f.line('store  = cache.__setitem__')

            f.blank2()

            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(%s):', name, keys)):
                f.line('%s = lookup(%s, absent)', a, k1)

                create_if_a(t, a, k1, k2, k3, k4)

                with f.indent(arrange('if not %s.is_herd:', a)):
                    t.create_r()

                    f.line('store(%s, (r   if %s is absent else   create_herd_2(%s.%s, %s, %s, r)))',
                           k1, a, a, k2, k2, a)
                    f.line('return r')

                f.blank()

                if k3 is none:
                    create_last(t, 0, a, b, k1, k2)
                else:
                    with f.indent(arrange('if %s.skip is 0:', a)):
                        f.line('%s = %s.glimpse(%s, absent)', b, a, k2)
                        f.line('if %s.%s is %s: return %s', b, k3, k3, b)

                        f.blank()

                        with f.indent(arrange('if not %s.is_herd:', b)):
                            t.create_r()
                            f.blank()

                            with f.indent(arrange('if %s is absent:', b)):
                                f.line('%s_ = %s.insert(%s, r)', a, a, k2)
                                f.line('if %s is not %s_: store(%s, %s_)', a, a, k1, a)
                                f.line('return r')

                            f.blank()

                            f.line('%s.displace(%s, create_herd_2(%s.%s, %s, %s, r))', a, k2, b, k3, k3, b)
                            f.line('return r')

                        f.blank()

                        create_last(t, a, b, c, k2, k3)

                    f.blank()
                    f.line('assert %s.skip is 1', a)
                    f.blank()
                    f.line('%s_%s = %s.sample().%s', a, k2, a, k2)
                    with f.indent(arrange('if %s_%s is %s:', a, k2, k2)):
                        create_last(t, 0, a, c, k1, k3, k_sample = k2)

                    f.blank()
                    t.create_r()
                    f.line('store(%s, create_herd_2(%s_%s, %s, %s.remove_skip(), r))', k1, a, k2, k2, a)
                    f.line('return r')

            f.blank2()

            f.line('return %s', name)


    @export
    def create_conjure_dual(path, year, author, module_name):
        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@gem(%r)', module_name)

            with f.indent('def gem():'):
                f.blank_suppress()

                create_conjure(f, 'simplified_conjure', 'dual',        'k1', 'k2')
                create_conjure(f, 'simplified_conjure', 'dual__21',    'k2', 'k1')
                create_conjure(f, 'simplified_conjure', 'triple',      'k1', 'k2', 'k3')
                create_conjure(f, 'simplified_conjure', 'triple__312', 'k3', 'k1', 'k2')

                #create_conjure(f, 'simplified_conjure', 'quadruple',  'k1', 'k2', 'k3', 'k4')

            data = f.finish()

        partial(data)
