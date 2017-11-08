#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedNew')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    produce_NEW_conjure_quadruple        = 0
    produce_NEW_conjure_quadruple__4123  = 0
    produce_NEW_conjure_triple__312      = 0


    share(
        'produce_NEW_conjure_quadruple',        produce_NEW_conjure_quadruple,
        'produce_NEW_conjure_quadruple__4123',  produce_NEW_conjure_quadruple__4123,
        'produce_NEW_conjure_triple__312',      produce_NEW_conjure_triple__312,
    )


    @share
    def produce_NEW_conjure_dual__21(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('NEW_conjure_%s', name)
        def NEW_conjure_dual__21(k1, k2):
            p = lookup(k2)
            if p is none: return provide(k2, Meta(k1, k2))
            if p.k1 is k1: return p

            ph = p.herd_estimate
            if ph is 0:
                q = Meta(k1, k2)
                store(k2, create_herd_2(p.k1, k1, p, q))
                return q

            #herd only
            if ph is 8: return (map__lookup(p, k1)) or (map__provide(p, k1, Meta(k1, k2)))

            if p.a is k1: return p.v
            if p.b is k1: return p.w
            if ph is 2:
                q = Meta(k1, k2)
                store(k2, create_herd_3(p.a, p.b, k1, p.v, p.w, q))
                return q

            if p.c is k1: return p.x
            if ph is 3:
                q = Meta(k1, k2)
                store(k2, create_herd_4(p.a, p.b, p.c, k1, p.v, p.w, p.x, q))
                return q

            assert ph is 7

            if p.d is k1: return p.y

            pe = p.e
            if pe is k1: return p.z
            if pe is absent:
                p.e = k1
                p.e6 = absent
                p.z = q = Meta(k1, k2)
                return q

            pe6 = p.e6
            if pe6 is k1: return p.z6
            if pe6 is absent:
                p.e6 = k1
                p.e7 = absent
                p.z6 = q = Meta(k1, k2)
                return q

            pe7 = p.e7
            if pe7 is k1: return p.z7

            q = Meta(k1, k2)

            if pe7 is absent:
                p.e7 = k1
                p.z7 = q
                return q

            store(
                     k2,
                     create_herd_many(
                         p.a, p.b, p.c, p.d, pe, pe6, pe7, k1,
                         p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                     )
                 )

            return q


        return NEW_conjure_dual__21


    @share
    def produce_NEW_conjure_dual(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('NEW_conjure_%s', name)
        def NEW_conjure_dual(k1, k2):
            p = lookup(k1)
            if p is none: return provide(k1, Meta(k1, k2))
            if p.k2 is k2: return p

            ph = p.herd_estimate
            if ph is 0:
                q = Meta(k1, k2)
                store(k1, create_herd_2(p.k2, k2, p, q))
                return q

            #herd only
            if ph is 8: return (map__lookup(p, k2)) or (map__provide(p, k2, Meta(k1, k2)))

            if p.a is k2: return p.v
            if p.b is k2: return p.w
            if ph is 2:
                q = Meta(k1, k2)
                store(k1, create_herd_3(p.a, p.b, k2, p.v, p.w, q))
                return q

            if p.c is k2: return p.x
            if ph is 3:
                q = Meta(k1, k2)
                store(k1, create_herd_4(p.a, p.b, p.c, k2, p.v, p.w, p.x, q))
                return q

            assert ph is 7

            if p.d is k2: return p.y

            pe = p.e
            if pe is k2: return p.z
            if pe is absent:
                p.e = k2
                p.e6 = absent
                p.z = q = Meta(k1, k2)
                return q

            pe6 = p.e6
            if pe6 is k2: return p.z6
            if pe6 is absent:
                p.e6 = k2
                p.e7 = absent
                p.z6 = q = Meta(k1, k2)
                return q

            pe7 = p.e7
            if pe7 is k2: return p.z7

            q = Meta(k1, k2)

            if pe7 is absent:
                p.e7 = k2
                p.z7 = q
                return q

            store(
                     k1,
                     create_herd_many(
                         p.a, p.b, p.c, p.d, pe, pe6, pe7, k2,
                         p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                     )
                 )

            return q


        return NEW_conjure_dual


    @share
    def produce_NEW_conjure_triple(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('NEW_conjure_%s', name)
        def NEW_conjure_triple(k1, k2, k3):
            p = lookup(k1)
            if p is none: return provide(k1, Meta(k1, k2, k3))
            if p.k2 is k2:
                if p.k3 is k3: return p

                r = Meta(k1, k2, k3)
                store(k1, create_horde_2(1, p.k3, k3, p, r))
                return r

            if not p.is_herd:
                q = Meta(k1, k2, k3)
                store(k1, create_herd_2(p.k2, k2, p, q))
                return q

            if p.skip is 0:
                q = p.glimpse(k2, absent)
                if q.k3 is k3: return q

                if not q.is_herd:
                    r = Meta(k1, k2, k3)
                    if q is absent:
                        p_ = p.insert(k2, r)
                        if p is not p_: store(k1, p_)
                        return r
                    p.displace(k2, create_herd_2(q.k3, k3, q, r))
                    return r

                r = q.glimpse(k3)
                if r is not none: return r

                r = Meta(k1, k2, k3)
                q_ = q.insert(k3, r)
                if q is not q_: p.displace(k2, q_)
                return r

            assert p.skip is 1

            p_k2 = p.sample().k2
            if p_k2 is not k2:
                r = Meta(k1, k2, k3)
                store(k1, create_herd_2(p_k2, k2, p.remove_skip(), r))
                return r

            r = p.glimpse(k3)
            if r is not none: return r

            r = Meta(k1, k2, k3)
            p_ = p.insert(k3, r)
            if p is not p_:
                assert p_.sample().k2 is k2
                store(k1, p_)
            return r


        return NEW_conjure_triple
