#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedConjureDual')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    @share
    def produce_simplified_conjure_dual__21(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual__21(k1, k2):
            #create_next(<KeyData <CommonKeyData 7 7 7 2 ('k2', 'k1') k1, k2> 0; 0 0 p q 0 0; 0 k2 k1 0 0>, 0, 0)
            p = lookup(k2)
            if p is none:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                return provide(k2, q)
            ph = p.herd_estimate

            if ph is 0:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                herd = create_herd_2(p.k1, k1, p, q)
                store(k2, herd)
                return q

            #create_last: herd only
            if ph is 8:
                q = map__lookup(p, k1)
                if q is not none:
                    assert (q.k2 is k2) and (q.k1 is k1)
                    return q

                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                map__store(p, k1, q)
                return q

            if p.a is k1:
                q = p.v
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            if p.b is k1:
                q = p.w
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            if ph is 2:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                store(k2, create_herd_3(p.a, p.b, k1, p.v, p.w, q))
                return q

            if p.c is k1:
                q = p.x
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            if ph is 3:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                store(k2, create_herd_4(p.a, p.b, p.c, k1, p.v, p.w, p.x, q))
                return q

            assert ph is 7

            pd = p.d
            if pd is k1:
                q = p.y
                assert (q.k2 is k2) and (q.k1 is k1)
                return q
            if pd is absent:
                p.d = k1
                p.y = q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            pe = p.e
            if pe is k1:
                q = p.z
                assert (q.k2 is k2) and (q.k1 is k1)
                return q
            if pe is absent:
                p.e = k1
                p.e6 = absent
                p.z = q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            pe6 = p.e6
            if pe6 is k1:
                q = p.z6
                assert (q.k2 is k2) and (q.k1 is k1)
                return q
            if pe6 is absent:
                p.e6 = k1
                p.e7 = absent
                p.z6 = q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            pe7 = p.e7
            if pe7 is k1:
                q = p.z7
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            q = Meta(k1, k2)
            assert (q.k2 is k2) and (q.k1 is k1)

            if pe7 is absent:
                p.e7 = k1
                p.z7 = q
                return q

            store(
                     k2,
                     create_herd_many(
                         p.a, p.b, p.c, pd, pe, pe6, pe7, k1,
                         p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                     ),
                 )

            return q


        return simplified_conjure_dual__21


    @share
    def produce_simplified_conjure_dual(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual(k1, k2):
            #create_next(<KeyData <CommonKeyData 7 7 7 2 ('k1', 'k2') k1, k2> 0; 0 0 p q 0 0; 0 k1 k2 0 0>, 0, 0)
            p = lookup(k1)
            if p is none:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return provide(k1, q)
            ph = p.herd_estimate

            if ph is 0:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q

            #create_last: herd only
            if ph is 8:
                q = map__lookup(p, k2)
                if q is not none:
                    assert (q.k1 is k1) and (q.k2 is k2)
                    return q

                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                map__store(p, k2, q)
                return q

            if p.a is k2:
                q = p.v
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            if p.b is k2:
                q = p.w
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            if ph is 2:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                store(k1, create_herd_3(p.a, p.b, k2, p.v, p.w, q))
                return q

            if p.c is k2:
                q = p.x
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            if ph is 3:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                store(k1, create_herd_4(p.a, p.b, p.c, k2, p.v, p.w, p.x, q))
                return q

            assert ph is 7

            pd = p.d
            if pd is k2:
                q = p.y
                assert (q.k1 is k1) and (q.k2 is k2)
                return q
            if pd is absent:
                p.d = k2
                p.y = q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            pe = p.e
            if pe is k2:
                q = p.z
                assert (q.k1 is k1) and (q.k2 is k2)
                return q
            if pe is absent:
                p.e = k2
                p.e6 = absent
                p.z = q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            pe6 = p.e6
            if pe6 is k2:
                q = p.z6
                assert (q.k1 is k1) and (q.k2 is k2)
                return q
            if pe6 is absent:
                p.e6 = k2
                p.e7 = absent
                p.z6 = q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            pe7 = p.e7
            if pe7 is k2:
                q = p.z7
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            q = Meta(k1, k2)
            assert (q.k1 is k1) and (q.k2 is k2)

            if pe7 is absent:
                p.e7 = k2
                p.z7 = q
                return q

            store(
                     k1,
                     create_herd_many(
                         p.a, p.b, p.c, pd, pe, pe6, pe7, k2,
                         p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                     ),
                 )

            return q


        return simplified_conjure_dual
