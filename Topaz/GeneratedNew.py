#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedNew')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    @share
    def produce_NEW_conjure_dual__21(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('NEW_conjure_%s', name)
        def NEW_conjure_dual__21(k1, k2):
            a = lookup(k2, absent)
            if a.k1 is k1: return a

            ahe = a.herd_estimate
            if ahe is 0:
                b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                store(k2, (b   if a is absent else   create_herd_2(a.k1, k1, a, b)))
                return b

            if ahe is 8:
                b = a.glimpse(k1)
                if b is not none:
                    assert (b.k2 is k2) and (b.k1 is k1)
                    return b

                b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                a_ = a.insert(k1, b)
                assert a_ is a
                return b

            if a.a is k1:
                b = a.v
                assert (b.k2 is k2) and (b.k1 is k1)
                return b
            if a.b is k1:
                b = a.w
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            if ahe is 2:
                assert a.skip is 0

                b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                store(k2, create_herd_3(a.a, a.b, k1, a.v, a.w, b))
                return b

            if a.c is k1:
                b = a.x
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            if ahe is 3:
                b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                store(k2, create_herd_4(a.a, a.b, a.c, k1, a.v, a.w, a.x, b))
                return b

            assert (ahe is 7) and (a.skip is 0)

            if a.d is k1:
                b = a.y
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            ae = a.e
            if ae is k1:
                b = a.z
                assert (b.k2 is k2) and (b.k1 is k1)
                return b
            if ae is absent:
                a.e = k1
                a.e6 = absent
                a.z = b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            ae6 = a.e6
            if ae6 is k1:
                b = a.z6
                assert (b.k2 is k2) and (b.k1 is k1)
                return b
            if ae6 is absent:
                a.e6 = k1
                a.e7 = absent
                a.z6 = b = Meta(k1, k2)
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            ae7 = a.e7
            if ae7 is k1:
                b = a.z7
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            b = Meta(k1, k2)
            assert (b.k2 is k2) and (b.k1 is k1)

            if ae7 is absent:
                a.e7 = k1
                a.z7 = b
                return b

            store(
                     k2,
                     create_herd_many(
                         a.a, a.b, a.c, a.d, ae, ae6, ae7, k1,
                         a.v, a.w, a.x, a.y, a.z, a.z6, a.z7, b,
                     )
                 )

            return b


        return NEW_conjure_dual__21


    @share
    def produce_NEW_conjure_dual(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('NEW_conjure_%s', name)
        def NEW_conjure_dual(k1, k2):
            a = lookup(k1, absent)
            if a.k2 is k2: return a

            ahe = a.herd_estimate
            if ahe is 0:
                b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                store(k1, (b   if a is absent else   create_herd_2(a.k2, k2, a, b)))
                return b

            if ahe is 8:
                b = a.glimpse(k2)
                if b is not none:
                    assert (b.k1 is k1) and (b.k2 is k2)
                    return b

                b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                a_ = a.insert(k2, b)
                assert a_ is a
                return b

            if a.a is k2:
                b = a.v
                assert (b.k1 is k1) and (b.k2 is k2)
                return b
            if a.b is k2:
                b = a.w
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            if ahe is 2:
                assert a.skip is 0

                b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                store(k1, create_herd_3(a.a, a.b, k2, a.v, a.w, b))
                return b

            if a.c is k2:
                b = a.x
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            if ahe is 3:
                b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                store(k1, create_herd_4(a.a, a.b, a.c, k2, a.v, a.w, a.x, b))
                return b

            assert (ahe is 7) and (a.skip is 0)

            if a.d is k2:
                b = a.y
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            ae = a.e
            if ae is k2:
                b = a.z
                assert (b.k1 is k1) and (b.k2 is k2)
                return b
            if ae is absent:
                a.e = k2
                a.e6 = absent
                a.z = b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            ae6 = a.e6
            if ae6 is k2:
                b = a.z6
                assert (b.k1 is k1) and (b.k2 is k2)
                return b
            if ae6 is absent:
                a.e6 = k2
                a.e7 = absent
                a.z6 = b = Meta(k1, k2)
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            ae7 = a.e7
            if ae7 is k2:
                b = a.z7
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            b = Meta(k1, k2)
            assert (b.k1 is k1) and (b.k2 is k2)

            if ae7 is absent:
                a.e7 = k2
                a.z7 = b
                return b

            store(
                     k1,
                     create_herd_many(
                         a.a, a.b, a.c, a.d, ae, ae6, ae7, k2,
                         a.v, a.w, a.x, a.y, a.z, a.z6, a.z7, b,
                     )
                 )

            return b


        return NEW_conjure_dual
