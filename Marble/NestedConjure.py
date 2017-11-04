#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    require_gem('Marble.Core')


    show_assert = 7


    class KeyData(Object):
        __slots__ = ((
            'f',                        #   DelayedOuput
            'share',                    #   Boolean
            'chain',                    #   Tuple of String+
            'keys',                     #   String

            'p2',                       #   Zero | String+
            'p',                        #   Zero | String+
            'a',                        #   String+
            'b',                        #   String+
            'c',                        #   Zero | String+
            'd',                        #   Zero | String+
            'k0',                       #   Zero | String+
            'k1',                       #   String+
            'k2',                       #   String+
            'k3',                       #   Zero | String+
            'k4',                       #   Zero | String+
        ))


        def __init__(t, f, share, chain, keys, p2, p, a, b, c, d, _, k0, k1, k2, k3, k4):
            assert _ is 0

            t.f     = f
            t.share = share
            t.chain = chain
            t.keys  = keys

            t.p2 = p2
            t.p  = p
            t.a  = a
            t.b  = b
            t.c  = c
            t.d  = d
            t.k0 = k0
            t.k1 = k1
            t.k2 = k2
            t.k3 = k3
            t.k4 = k4


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


        def remove_b_k2(t):
            if 0:
                k_sample = t.k_sample

                if k_sample is 0:
                    k_sample = t.k2
                elif type(k_sample) is not Tuple:
                    k_sample = ((k_sample, t.k2))
                else:
                    k_sample += ((t.k2,))

            return KeyData(
                      t.f, t.share, t.chain, t.keys,
                      t.p2, t.p,  t.a,  t.c,  t.d,  0,
                      0,    t.k0, t.k1, t.k3, t.k4, 0,
                   )


        def remove_p2_k0(t):
            return KeyData(
                      t.f, t.share, t.chain, t.keys,
                      t.p, t.a,  t.b,  t.c,  t.d,  0,
                      0,   t.k1, t.k2, t.k3, t.k4, 0,
                   )


    def create_KeyData(f, share, k1, k2, k3 = 0, k4 = 0):
        if k3 is 0:
            chain = ((k1, k2))
        elif k4 is 0:
            chain = ((k1, k2, k3))
        else:
            chain = ((k1, k2, k3, k4))

        keys = 'k1, k2'
        if k3 is not 0:  keys += ', k3'
        if k4 is not 0:  keys += ', k4'

        return KeyData(
                   f, share, chain, keys,
                   0, 0, 'a', 'b', (0   if k3 is 0 else   'c'), (0   if k4 is 0 else   'd'),
                   0, 0, k1,  k2,  k3,                          k4,
               )


    def create_if_glimpse(t, skip = 1):
        f  = t.f
        p  = t.p
        a  = t.a
        k1 = t.k1
        k2 = t.k2
        k3 = t.k3
        k4 = t.k4

        if k3 is 0:
            f.line('if %s.%s is %s: return %s', a, k2, k2, a)
            f.blank()
            return

        if p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

        f.blank()

        with f.indent(arrange('if %s.%s is %s:', a, k2, k2)):
            f.blank_suppress()
            create_if_glimpse(t.remove_b_k2(), skip = skip + 1)
            t.create_r()
            f.line('%s(%s, create_horde_2(%d, %s.%s, %s, %s, r))', displace, k1, skip, a, k3, k3, a)
            f.line('return r')

        f.blank()


    def create_last(t, k_sample = 0):
        f  = t.f
        p  = t.p
        a  = t.a
        b  = t.b
        k1 = t.k1
        k2 = t.k2

        if t.p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

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


    def create_next(t, k_sample = 0):
        f  = t.f
        p2 = t.p2
        p  = t.p
        a  = t.a
        b  = t.b
        c  = t.c
        k0 = t.k0
        k1 = t.k1
        k2 = t.k2
        k3 = t.k3
        k4 = t.k4

        if p is 0:
            f.line('%s = lookup(%s, absent)', a, k1)
        else:
            f.line('%s = %s.glimpse(%s, absent)', a, p, k1)

        f.blank_suppress()
        create_if_glimpse(t)

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
            create_last(t)
            return

        with f.indent(arrange('if %s.skip is 0:', a)):
            create_next(t.remove_p2_k0())

        f.blank()

        t2 = t.remove_b_k2()

        if k4 is 0:
            f.line('assert %s.skip is 1', a)
            create_sample(t, 0)
            create_last(t2, k_sample = k2)
            return

        create_sample(t, 1)

        with f.indent(arrange('if %s.skip is 1:', a)):
            create_next(t2.remove_p2_k0(), k_sample = k2)

        f.blank()
        f.line('assert %s.skip is 2', a)

        create_sample(t2, 2, skip = 2)
        create_last(t2.remove_b_k2(), k_sample = ((k2,k3)) )


    def create_sample(t, multiple, skip = 1):
        f  = t.f
        p  = t.p
        a  = t.a
        k1 = t.k1
        k2 = t.k2

        if p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

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
        t    = create_KeyData(f, share, k1, k2, k3, k4)
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
            with f.indent(arrange('def %s(%s):', name, t.keys)):
                create_next(t)

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
                    create_conjure(f, prefix, 'dual__21', 'k2', 'k1', share = share)

                if (which == 2) or (which == '2'):
                    create_conjure(f, prefix, 'dual', 'k1', 'k2', share = share)

                if which == 3:
                    create_conjure(f, prefix, 'triple__312', 'k3', 'k1', 'k2', share = share)

                if (which == 3) or (which == '3'):
                    create_conjure(f, prefix, 'triple', 'k1', 'k2', 'k3', share = share)

                if (which == 4) or (which == '4'):
                    create_conjure(f, prefix, 'quadruple', 'k1', 'k2', 'k3', 'k4', share = share)

                if (which == 4) or (which == '4123'):
                    create_conjure(f, prefix, 'quadruple__4123', 'k4', 'k1', 'k2', 'k3', share = share)

            data = f.finish()

        if show is 7:
            partial(data)


    @export
    def create_nested_conjure(year, author):
        #create_nested_conjure__X(year, author, 'NEW_conjure', 'Topaz.GeneratedNew', '4', share = 7, show = 7)

        create_nested_conjure__X(year, author, 'simplified_conjure', 'Topaz.GeneratedConjureDual',      2, share = 7)
        create_nested_conjure__X(year, author, 'simplified_conjure', 'Topaz.GeneratedConjureTriple',    3, share = 7)
        create_nested_conjure__X(year, author, 'simplified_conjure', 'Topaz.GeneratedConjureQuadruple', 4, share = 7)

        create_nested_conjure__X(year, author, 'conjure', 'Gem.GeneratedConjureQuadruple', '4123', show = 0)
