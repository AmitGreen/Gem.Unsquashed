#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedNew')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    produce_NEW_conjure_dual             = 0
    produce_NEW_conjure_dual__21         = 0
    produce_NEW_conjure_quadruple        = 0
    produce_NEW_conjure_quadruple__4123  = 0
    produce_NEW_conjure_triple__312      = 0


    share(
        'produce_NEW_conjure_dual',             produce_NEW_conjure_dual,
        'produce_NEW_conjure_dual__21',         produce_NEW_conjure_dual__21,
        'produce_NEW_conjure_quadruple',        produce_NEW_conjure_quadruple,
        'produce_NEW_conjure_quadruple__4123',  produce_NEW_conjure_quadruple__4123,
        'produce_NEW_conjure_triple__312',      produce_NEW_conjure_triple__312,
    )


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

                q = Meta(k1, k2, k3)
                store(k1, create_horde_2(1, p.k3, k3, p, q))
                return q

            if not p.is_herd:
                q = Meta(k1, k2, k3)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
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

                    herd = create_herd_2(q.k3, k3, q, r)
                    p.displace(k2, herd)
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
