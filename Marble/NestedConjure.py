#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    require_gem('Marble.Core')


    show_assert       = 0
    use_herd_estimate = 7


    class CommonKeyData(Object):
        __slots__ = ((
            'f',                        #   DelayedOuput
            'share',                    #   Boolean
            'show_assert',              #   Boolean
            'use_herd_estimate',        #   Boolean

            'total',                    #   Integer
            'chain',                    #   Tuple of String+
            'keys',                     #   String
        ))


        def __init__(t, f, share, show_assert, use_herd_estimate, total, chain, keys):
            t.f                 = f
            t.share             = share
            t.show_assert       = show_assert
            t.use_herd_estimate = use_herd_estimate

            t.total = total
            t.chain = chain
            t.keys  = keys

        
    class KeyData(Object):
        __slots__ = ((
            'common',                   #   CommonKeyData

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


        def __init__(t, common, p2, p, a, b, c, d, _, k0, k1, k2, k3, k4):
            assert _ is 0

            t.common = common

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
            common = t.common

            if common.show_assert:
                common.f.line('assert %s',
                              ' and '.join(arrange('(%s.%s is %s)', v, k, k)   for k in common.chain))


        def create_assert_r(t):
            common = t.common

            if common.show_assert:
                common.f.line('assert %s',
                              ' and '.join(arrange('(r.%s is %s)', k, k)   for k in common.chain))


        def create_r(t, r = 'r', extra = 0):
            common = t.common

            if extra is 0:
                common.f.line('%s = Meta(%s)', r, common.keys)
            else:
                common.f.line('%s = %s = Meta(%s)', extra, r, common.keys)

            t.create_assert(r)


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
                      t.common,
                      t.p2, t.p,  t.a,  t.c,  t.d,  0,
                      0,    t.k0, t.k1, t.k3, t.k4, 0,
                   )


        def remove_p2_k0(t):
            return KeyData(
                      t.common,
                      t.p, t.a,  t.b,  t.c,  t.d,  0,
                      0,   t.k1, t.k2, t.k3, t.k4, 0,
                   )


    def create_KeyData(common, k1, k2, k3 = 0, k4 = 0):
        return KeyData(
                   common,
                   0, 0, 'a', 'b', (0   if k3 is 0 else   'c'), (0   if k4 is 0 else   'd'),
                   0, 0, k1,  k2,  k3,                          k4,
               )


    def create_if_glimpse(t, skip = 1):
        common = t.common

        f  = common.f
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


    def create_test_herd_member(t, herd_k, herd_v, displace = 0, herd_k_next = 0, create_result = 0):
        common = t.common

        f           = common.f
        show_assert = common.show_assert
        a           = t.a
        b           = t.b
        k2          = t.k2

        f.blank()

        if displace:
            ak = arrange('%s%s', a, herd_k)
            f.line('%s = %s.%s', ak, a, herd_k)
        else:
            ak = arrange('%s.%s', a, herd_k)

        if show_assert:
            with f.indent(arrange('if %s is %s:', ak, k2)):
                f.line('%s = %s.%s', b, a, herd_v)
                t.create_assert(b)
                f.line('return %s', b)
        else:
            f.line('if %s is %s: return %s.%s', ak, k2, a, herd_v)

        if displace:
            if create_result:
                f.blank()
                t.create_r(b)
                f.blank()
                with f.indent(arrange('if %s is absent:', ak)):
                    f.line('%s.%s = %s', a, herd_k, k2)
                    f.line('%s.%s = %s', a, herd_v, b)
                    f.line('return %s', b)
            else:
                with f.indent(arrange('if %s is absent:', ak)):
                    f.line('%s.%s = %s', a, herd_k, k2)

                    if herd_k_next is not 0:
                        f.line('%s.%s = absent', a, herd_k_next)

                    t.create_r(b, extra = arrange('%s.%s', a, herd_v))
                    f.line('return %s', b)
        else:
            assert create_result is 0

        f.blank()

        return ak


    def create_test_herd_glimpse(t, herd_k, herd_v, displace = 0, herd_k_next = 0, if_keyword = 'if'):
        common = t.common

        f           = common.f
        show_assert = common.show_assert
        p           = t.p
        a           = t.a
        b           = t.b
        k1          = t.k1
        k3          = t.k3

        if displace:
            indent     = f.indent('else:')
            pk         = arrange('%s%s', p, herd_k)
            if_keyword = 'if'
        else:
            indent = empty_context_manager
            pk     = arrange('%s.%s', p, herd_k)

        with indent:
            if displace:
                f.line('%s = %s.%s', pk, p, herd_k)

            with f.indent(arrange('%s %s is %s:', if_keyword, pk, k1)):
                f.line('%s = %s.%s', a, p, herd_v)

                if k3 is 0:
                    create_if_glimpse(t)
                    f.blank_suppress()
                    f.line('%se = %s.herd_estimate', a, a)

                f.line('%sd = %s.displace_%s', a, p, herd_v)

            if displace:
                with f.indent(arrange('elif %s is absent:', pk)):
                    f.line('%s.%s = %s', p, herd_k, k1)

                    if herd_k_next is not 0:
                        f.line('%s.%s = absent', p, herd_k_next)

                    t.create_r(a, extra = arrange('%s.%s', p, herd_v))
                    f.line('return %s', a)

        return pk


    def create_assert_k_sample(t, v, k_sample):
        common = t.common

        f = common.f

        if type(k_sample) is Tuple:
            f.line('assert %s',
                   ' and '.join(arrange('(%s.sample().%s is %s)', v, k, k)   for k in k_sample))
            return

        f.line('assert %s.sample().%s is %s', v, k_sample, k_sample)


    def create_last(t, estimate = 0, k_sample = 0):
        common = t.common

        f           = common.f
        show_assert = common.show_assert
        p           = t.p
        a           = t.a
        b           = t.b
        k1          = t.k1
        k2          = t.k2

        #if common.use_herd_estimate:    k_sample = 'FAKE'

        if t.p is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', p)

        if estimate is not 0:
            if common.total is 2:
                assert k_sample is 0

                last_herd  = 7
                last_horde = 0

                f.line('#herd only')
            else:
                last_herd  = (k_sample is 0)
                last_horde = 7

                if last_herd:
                    f.line('#herd or horde')
                else:
                    f.line('#horde only')

            if show_assert:
                with f.indent(arrange('if %s is 8:', estimate)):
                    f.line('%s = map__lookup(%s, %s)', b, a, k2)
                    with f.indent(arrange('if %s is not none:', b)):
                        t.create_assert(b)
                        f.line('return %s', b)

                    f.blank()

                    t.create_r(b)
                    f.line('map__store(%s, %s, %s)', a, k2, b)
                    f.line('return %s', b)
                    f.blank()
            else:
                f.line('if %s is 8: return (map__lookup(%s, %s)) or (map__provide(%s, %s, Meta(%s)))',
                       estimate, a, k2, a, k2, common.keys)


            if last_horde:
                f.line('assert %s is 3', estimate)
                f.blank()

            aa = create_test_herd_member(t, 'a', 'v')

            if not show_assert:
                f.blank_suppress()

            ab = create_test_herd_member(t, 'b', 'w')

            if last_herd:
                if not show_assert:
                    f.blank_suppress()

                with f.indent(arrange('if %s is 2:', estimate)):
                    t.create_r(b)
                    f.line('%s(%s, create_herd_3(%s, %s, %s, %s.v, %s.w, %s))',
                           displace, k1, aa, ab, k2, a, a, b)
                    f.line('return %s', b)

                #EXAMINE: How horde done with 3
                ac = create_test_herd_member(t, 'c', 'x', (0   if last_herd else   3))

                if not show_assert:
                    f.blank_suppress()

                with f.indent(arrange('if %s is 3:', estimate)):
                    t.create_r(b)

                    f.line('%s(%s, create_herd_4(%s, %s, %s, %s, %s.v, %s.w, %s.x, %s))',
                           displace, k1, aa, ab, ac, k2, a, a, a, b)
                    f.line('return %s', b)

                f.blank()

                f.line('assert %s is 7', estimate)

                ad  = create_test_herd_member(t, 'd',  'y')
                ae  = create_test_herd_member(t, 'e',  'z',  5, herd_k_next = 'e6')
                ae6 = create_test_herd_member(t, 'e6', 'z6', 6, herd_k_next = 'e7')
                ae7 = create_test_herd_member(t, 'e7', 'z7', 7, create_result = 7)

                f.blank()

                with f.indent(arrange('%s(', displace), arrange('%*s)', length(displace),  ' '), length(displace) + 4):
                    f.line('%s,', k1)
                    with f.indent('create_herd_many(', ')'):
                        f.line('%s, %s, %s, %s, %s, %s, %s, %s,', aa,  ab, ac, ad, ae, ae6, ae7, k2)
                        f.line('%s.v, %s.w, %s.x, %s.y, %s.z, %s.z6, %s.z7, %s,', a, a, a, a, a, a, a, b)

                f.blank()

                f.line('return %s', b)
                return

            skip = (length(k_sample)   if type(k_sample) is Tuple else   1)

            ac = create_test_herd_member(t, 'c', 'x', 3, create_result = 7)

            f.blank()

            f.line('h = create_horde_4(%d, %s, %s, %s, %s, %s.v, %s.w, %s.x, %s)',
                   skip, aa, ab, ac, k2, a, a, a, b)
            create_assert_k_sample(t, 'h', k_sample)
            f.line('%s(%s, h)', displace, k1)
            f.line('return %s', b)
            return

        f.line('%s = %s.glimpse(%s)', b, a, k2)
        if show_assert:
            with f.indent(arrange('if %s is not none:', b)):
                t.create_assert(b)
                f.line('return %s', b)
        else:
            f.line('if %s is not none: return %s', b, b)

        f.blank()
        t.create_r(b)

        a_ = arrange('%s_', a)

        f.line('%s = %s.insert(%s, %s)', a_, a, k2, b)

        if k_sample is 0:
            f.line('if %s is not %s: %s(%s, %s)', a, a_, displace, k1, a_)
        else:
            with f.indent(arrange('if %s is not %s:', a, a_)):
                create_assert_k_sample(t, a_, k_sample)
                f.line('%s(%s, %s)', displace, k1, a_)

        f.line('return %s', b)


    def create_next(t, p_estimate = 0, k_sample = 0):
        common      = t.common
        show_assert = common.show_assert
        f           = common.f
        p2          = t.p2
        p           = t.p
        a           = t.a
        b           = t.b
        c           = t.c
        k0          = t.k0
        k1          = t.k1
        k2          = t.k2
        k3          = t.k3
        k4          = t.k4

        if p is 0:
            assert p_estimate is 0
            assert k0         is 0

            f.line('%s = lookup(%s)', a, k1)

            if show_assert:
                with f.indent(arrange('if %s is none:', a)):
                    t.create_r(b)
                    f.line('return provide(%s, %s)', k1, b)
            else:
                f.line('if %s is none: return provide(%s, Meta(%s))', a, k1, common.keys)

            f.blank_suppress()
        elif p_estimate is 0:
            f.line('%s = %s.glimpse(%s, absent)', a, p, k1)
            f.blank_suppress()
        else:
            with f.indent(arrange('if %s is 8:', p_estimate)):
                f.line('%s = %s.glimpse(%s, absent)', a, p, k1)

                if k3 is 0:
                    create_if_glimpse(t)
                    f.blank_suppress()
                    f.line('%se = %s.herd_estimate', a, a)

                f.line('%sd = 0', a)

            if k_sample is 0:
                indent     = empty_context_manager
                if_keyword = 'elif'
            else:
                indent     = f.indent('else:')
                if_keyword = 'if'

            with indent:
                f.blank_suppress()

                if k_sample is not 0:
                    if k_sample is not 0:
                        f.line('assert %s is 3', p_estimate)
                        f.blank()

                pa = create_test_herd_glimpse(t, 'a', 'v', if_keyword = if_keyword)
                pb = create_test_herd_glimpse(t, 'b', 'w', if_keyword = 'elif')

                if k_sample is 0:
                    f.blank_suppress()
                    with f.indent(arrange('elif %s is 2:', p_estimate)):
                        f.line('%s  = absent', a)
                        f.line('%sd = %se = 0', a, a)

                    ac = create_test_herd_glimpse(t, 'c', 'x', (0   if common.total == 2 else   3))

                    with f.indent():
                        with f.indent(arrange('elif %s is 3:', p_estimate)):
                            f.line('%s  = absent', a)
                            f.line('%sd = %se = 0', a, a)
                        with f.indent('else:'):
                            f.line('assert %s is 7', p_estimate)
                            ad  = create_test_herd_glimpse(t, 'd', 'y')
                            ae  = create_test_herd_glimpse(t, 'e',  'z',  5, herd_k_next = 'e6')
                            with f.indent():
                                ae6 = create_test_herd_glimpse(t, 'e6', 'z6', 6, herd_k_next = 'e7')
                                with f.indent():
                                    ae7 = create_test_herd_glimpse(t, 'e7', 'z7', 7)
                                    with f.indent():
                                        with f.indent('else:'):
                                            f.line('%s  = absent', a)
                                            f.line('%sd = %se = 0', a, a)

                else:
                    with f.indent('else:'):
                        f.line('%s  = %s.glimpse(%s, absent)', a, p, k1)
                        f.line('%sd = 0', a)

            #H
            f.blank()

        create_if_glimpse(t)

        f.blank()

        if common.use_herd_estimate:
            estimate = arrange('%se', a)

            f.line('%s = %s.herd_estimate', estimate, a)
            if_not_herd = arrange('if %s is 0:', estimate)
        else:
            estimate    = 0
            if_not_herd = arrange('if not %s.is_herd:', a)

        with f.indent(if_not_herd):
            t.create_r(b)

            if p is 0:
                assert k0 is 0

                f.line('store(%s, create_herd_2(%s.%s, %s, %s, %s))', k1, a, k2, k2, a, b)
            else:
                if p2 is 0:
                    displace = 'store'
                else:
                    displace = arrange('%s.displace', p2)

                with f.indent(arrange('if %s is absent:', a)):
                    f.line('%s_ = %s.insert(%s, %s)', p, p, k1, b)
                    f.line('if %s is not %s_: %s(%s, %s_)', p, p, displace, k0, p)
                    f.line('return %s', b)

                f.line('%s.displace(%s, create_herd_2(%s.%s, %s, %s, %s))', p, k1, a, k2, k2, a, b)

            f.line('return %s', b)

        f.blank()

        if k3 is 0:
            create_last(t, estimate)
            return

        with f.indent(arrange('if %s.skip is 0:', a)):
            create_next(t.remove_p2_k0(), estimate)

        f.blank()

        t2 = t.remove_b_k2()

        if k4 is 0:
            f.line('assert %s.skip is 1', a)
            create_sample(t, 0)
            create_last(t2, estimate, k_sample = k2)
            return

        create_sample(t, 1)

        with f.indent(arrange('if %s.skip is 1:', a)):
            create_next(t2.remove_p2_k0(), k_sample = k2)

        f.blank()
        f.line('assert %s.skip is 2', a)

        create_sample(t2, 2, skip = 2)
        create_last(t2.remove_b_k2(), estimate, k_sample = ((k2,k3)) )


    def create_sample(t, multiple, skip = 1):
        common = t.common

        f  = common.f
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


    def create_conjure(
            f, prefix, suffix, k1, k2, k3 = 0, k4 = 0,
            
            share = 0, show_assert = 0, use_herd_estimate = 0,
    ):
        if k3 is 0:
            total = 2
            chain = ((k1, k2))
            keys  = 'k1, k2'
        elif k4 is 0:
            total = 3
            chain = ((k1, k2, k3))
            keys  = 'k1, k2, k3'
        else:
            total = 4
            chain = ((k1, k2, k3, k4))
            keys  = 'k1, k2, k4'

        common = CommonKeyData(f, share, show_assert, use_herd_estimate, total, chain, keys)

        t    = create_KeyData(common, k1, k2, k3, k4)
        name = arrange('%s_%s', prefix, suffix)

        f.blank2()

        f.line( ('@share'   if share is 7 else   '@export') )
        with f.indent(arrange('def produce_%s(', name), '):', 8):
            f.line('name, Meta, cache,')
            f.blank()
            f.line('lookup  = absent,')
            f.line('provide = absent,')
            f.line('store   = absent,')
        with f.indent():
            f.line('lookup  = cache.get')
            f.line('provide = cache.setdefault')
            f.line('store   = cache.__setitem__',)
            f.blank2()
            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(%s):', name, t.common.keys)):
                create_next(t)

            f.blank2()

            f.line('return %s', name)

        f.blank2()


    def create_nested_conjure__X(
            year, author, prefix, module_name, which,
            
            share       = 0,
            show_assert = show_assert,
            show        = 0,
            blanks      = 0,
    ):
        if type(which) is not Tuple:
            which = ((which,))

        path = path_join('..', arrange('%s.gpy', module_name.replace('.', '/')))

        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@gem(%r)', module_name)

            with f.indent('def gem():'):
                f.blank_suppress()

                create_herd_many = 0
                import_list      = ['create_herd_3', 'create_herd_4', 'create_herd_many']
                produce_zero     = []
              
                for loop in [1, 2]:
                    if loop == 2:
                        if create_herd_many:
                            import_list.append('create_herd_many')

                        f.line('from Gem import %s', ', '.join(import_list))

                        f.blank2()

                        f.line('map__lookup  = Map.get')
                        f.line('map__provide = Map.setdefault')
                        f.line('map__store   = Map.__setitem__')

                        f.blank2()

                        if produce_zero:
                            produce_zero.sort()

                            for s in produce_zero:
                                name = arrange('produce_%s_%s', prefix, s)

                                f.line('%-36s = 0', name)

                            f.blank2()

                        with f.indent('share(', ')'):
                            for v in produce_zero:
                                name = arrange('produce_%s_%s', prefix, v)
                                f.line('%-40s%s,', arrange('%r,', name), name)

                    if 21 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'dual__21', 'k2', 'k1',

                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = use_herd_estimate,
                            )
                    elif blanks:
                        if loop == 1:
                            produce_zero.append('dual__21')

                    if 2 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'dual', 'k1', 'k2',
         
                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = use_herd_estimate,
                            )
                    elif blanks:
                        if loop == 1:
                            produce_zero.append('dual__21')

                    if 213 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'triple__312', 'k3', 'k1', 'k2',
         
                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = 0,              #   Incomplete: use_herd_estimate,
                            )

                    if 3 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'triple', 'k1', 'k2', 'k3',

                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = 0,              #   Incomplete: use_herd_estimate,
                            )
                    elif blanks:
                        if loop == 1:
                            produce_zero.append('triple')

                    if 4 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'quadruple', 'k1', 'k2', 'k3', 'k4',
         
                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = use_herd_estimate,
                            )

                    if 4123 in which:
                        if loop == 2:
                            create_conjure(
                                f, prefix, 'quadruple__4123', 'k4', 'k1', 'k2', 'k3',
         
                                share             = share,
                                show_assert       = show_assert,
                                use_herd_estimate = use_herd_estimate,
                            )
                        

            data = f.finish()

        if show is 7:
            partial(data)


    @export
    def create_nested_conjure(year, author):
        create_nested_conjure__X(
            year, author, 'NEW_conjure', 'Topaz.GeneratedNew',

            #which = ((2, 21, 3)),
            which = 2,
            share = 7,
            show  = 7,
            blanks = 7,
        )

        if 7 is 0:
            create_nested_conjure__X(
                year, author, 'simplified_conjure', 'Topaz.GeneratedConjureDual',

                which = ((21, 2)),
                share = 7,
            )

            create_nested_conjure__X(
                year, author, 'simplified_conjure', 'Topaz.GeneratedConjureTriple',
                
                which = ((312, 3)),
                share = 7,
            )

            create_nested_conjure__X(
                year, author, 'simplified_conjure', 'Topaz.GeneratedConjureQuadruple',
                
                which = ((4123, 4)),
                share = 7,
            )

            create_nested_conjure__X(year, author, 'conjure', 'Gem.GeneratedConjureQuadruple', '4123', show = 0)
