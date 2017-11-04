#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    require_gem('Marble.Core')


    show_assert = 7


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


    def create_if_glimpse(t, previous, a, k1, k2, k3 = 0, k4 = 0, skip = 1):
        f = t.f

        if k3 is 0:
            f.line('if %s.%s is %s: return %s', a, k2, k2, a)
            f.blank()
            return

        if previous is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', previous)

        f.blank()

        with f.indent(arrange('if %s.%s is %s:', a, k2, k2)):
            f.blank_suppress()
            create_if_glimpse(t, previous, a, k1, k3, k4, skip = skip + 1)
            t.create_r()
            f.line('%s(%s, create_horde_2(%d, %s.%s, %s, %s, r))', displace, k1, skip, a, k3, k3, a)
            f.line('return r')

        f.blank()


    def create_last(t, p, a, b, k1, k2, k_sample = 0):
        f = t.f

        if p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

        #f.line('#<last>')
        f.line('%s = %s.glimpse(%s)', b, a, k2)
        if show_assert:
            with f.indent(arrange('if %s is not none:', b)):
                t.create_assert(b)
                f.line('return %s', b)
        else:
            f.line('if %s is not none: return %s', b, b)

        f.blank()
        t.create_r()
        f.line('%s_ = %s.insert(%s, r)', a, a, k2)

        if k_sample is 0:
            f.line('if %s is not %s_: %s(%s, %s_)', a, a, displace, k1, a)
        else:
            with f.indent(arrange('if %s is not %s_:', a, a)):
                if type(k_sample) is Tuple:
                    f.line('assert %s',
                           ' and '.join(arrange('(%s_.sample().%s is %s)', a, k, k)   for k in k_sample))
                else:
                    f.line('assert %s_.sample().%s is %s', a, k_sample, k_sample)
                f.line('%s(%s, %s_)', displace, k1, a)

        f.line('return r')
        #f.line('#</last>')


    def create_next(t, p2, p, a, b, c, d, _, k0, k1, k2, k3, k4, k_sample = 0):
        assert _ is 0

        f = t.f

        if p is 0:
            f.line('%s = lookup(%s, absent)', a, k1)
        else:
            f.line('%s = %s.glimpse(%s, absent)', a, p, k1)

        f.blank_suppress()
        create_if_glimpse(t, p, a, k1, k2, k3, k4, skip = 1)

        f.blank()

        with f.indent(arrange('if not %s.is_herd:', a)):
            t.create_r()

            if p is 0:
                assert k0 is 0

                f.line('store(%s, (r   if %s is absent else   create_herd_2(%s.%s, %s, %s, r)))',
                       k1, a, a, k2, k2, a)
            else:
                if p2 is 0:
                    displace = 'store'
                else:
                    displace = arrange('%s.displace', p2)

                with f.indent(arrange('if %s is absent:', a)):
                    f.line('%s_ = %s.insert(%s, r)', p, p, k1)
                    f.line('if %s is not %s_: %s(%s, %s_)', p, p, displace, k0, p)
                    f.line('return r')

                f.line('%s.displace(%s, create_herd_2(%s.%s, %s, %s, r))', p, k1, a, k2, k2, a)

            f.line('return r')

        f.blank()

        if k3 is 0:
            create_last(t, p, a, b, k1, k2)
            return

        with f.indent(arrange('if %s.skip is 0:', a)):
            create_next(t, p, a, b, c, d, 0, 0, k1, k2, k3, k4, 0)

        f.blank()

        if k4 is 0:
            f.line('assert %s.skip is 1', a)
            create_sample(t, 0, p, a, k1, k2)
            create_last(t, p, a, c, k1, k3, k_sample = k2)
            return

        create_sample(t, 1, p, a, k1, k2)

        with f.indent(arrange('if %s.skip is 1:', a)):
            create_next(t, p, a, c, d, 0, 0, 0, k1, k3, k4, 0, 0, k_sample = k2)

        f.blank()
        f.line('assert %s.skip is 2', a)
        create_sample(t, 2, p, a, k1, k3, skip = 2)
        create_last(t, p, a, d, k1, k4, k_sample = ((k2,k3)) )


    def create_sample(t, multiple, p, a, k1, k2, skip = 1):
        if p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

        f = t.f

        f.blank()

        if multiple is 0:
            f.line('%s_%s = %s.sample().%s', a, k2, a, k2)
        elif multiple is 1:
            f.line('%s_sample = %s.sample()', a, a)
            f.line('%s_%s     = %s_sample.%s', a, k2, a, k2)
        else:
            assert multiple is 2
            f.line('%s_%s = %s_sample.%s', a, k2, a, k2)

        with f.indent(arrange('if %s_%s is not %s:', a, k2, k2)):
            t.create_r()
            if skip is 1:
                f.line('%s(%s, create_herd_2(%s_%s, %s, %s.remove_skip(), r))', displace, k1, a, k2, k2, a)
            else:
                f.line('%s(%s, create_horde_2(%d, %s_%s, %s, %s.remove_skip(%d), r))',
                       displace, k1, skip - 1, a, k2, k2, a, skip)

            f.line('return r')

        f.blank()


    def create_conjure(f, prefix, suffix, k1, k2, k3 = 0, k4 = 0, share = 7):
        if k3 is 0:
            chain = ((k1, k2))
        elif k4 is 0:
            chain = ((k1, k2, k3))
        else:
            chain = ((k1, k2, k3, k4))

        keys = 'k1, k2'
        if k3 is not 0:  keys += ', k3'
        if k4 is not 0:  keys += ', k4'

        t = KeyData(f, chain, keys)

        a    = 'a'
        b    = 'b'
        c    = 'c'
        d    = 'd'
        name = arrange('%s_%s', prefix, suffix)

        f.blank2()

        f.line( ('@share'   if share is 7 else   '@export') )
        with f.indent(arrange('def produce_%s(', name), '):', 8):
            f.line('name, Meta, cache,')
            f.blank()
            f.line('lookup = absent,')
            f.line('store  = absent,')
        with f.indent():
            f.line('lookup = cache.get')
            f.line('store  = cache.__setitem__',)
            f.blank()
            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(%s):', name, keys)):
                create_next(t, 0, 0, a, b, c, d, 0, 0, k1, k2, k3, k4)

            f.blank2()

            f.line('return %s', name)


    def create_nested_conjure__X(year, author, prefix, module_name, which, share = 0, show = 0):
        path = path_join('..', arrange('%s.gpy', module_name.replace('.', '/')))

        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@gem(%r)', module_name)

            with f.indent('def gem():'):
                f.blank_suppress()

                if which == 2:
                    create_conjure(f, prefix, 'dual__21',        'k2', 'k1', share = share)
                    create_conjure(f, prefix, 'dual',            'k1', 'k2', share = share)

                if which == 3:
                    create_conjure(f, prefix, 'triple__312',     'k3', 'k1', 'k2', share = share)
                    create_conjure(f, prefix, 'triple',          'k1', 'k2', 'k3', share = share)

                if which == 4:
                    create_conjure(f, prefix, 'quadruple',       'k1', 'k2', 'k3', 'k4', share = share)

                if (which == 4) or (which == '4123'):
                    create_conjure(f, prefix, 'quadruple__4123', 'k4', 'k1', 'k2', 'k3', share = share)

            data = f.finish()

        if show is 7:
            partial(data)


    @export
    def create_nested_conjure(author, year):
        create_nested_conjure__X(author, year, 'simplified_conjure', 'Topaz.GeneratedConjureDual',      2, share = 7)
        create_nested_conjure__X(author, year, 'simplified_conjure', 'Topaz.GeneratedConjureTriple',    3, share = 7)
        create_nested_conjure__X(author, year, 'simplified_conjure', 'Topaz.GeneratedConjureQuadruple', 4, share = 7)

        create_nested_conjure__X(author, year, 'conjure', 'Gem.GeneratedConjureQuadruple', '4123', show = 0)
