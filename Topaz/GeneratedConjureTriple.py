#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedConjureTriple')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    @share
    def produce_simplified_conjure_triple__312(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple__312(k1, k2, k3):
            p = lookup(k3)
            if p is none:
                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                return provide(k3, q)
            if p.k1 is k1:
                if p.k2 is k2: return p

                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                store(k3, create_horde_2(1, p.k2, k2, p, q))
                return q

            if not p.is_herd:
                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                herd = create_herd_2(p.k1, k1, p, q)
                store(k3, herd)
                return q

            if p.skip is 0:
                q = p.glimpse(k1, absent)
                if q.k2 is k2: return q

                if not q.is_herd:
                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    if q is absent:
                        p_ = p.insert(k1, r)
                        if p is not p_: store(k3, p_)
                        return r

                    herd = create_herd_2(q.k2, k2, q, r)
                    p.displace(k1, herd)
                    return r

                r = q.glimpse(k2)
                if r is not none:
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                q_ = q.insert(k2, r)
                if q is not q_: p.displace(k1, q_)
                return r

            assert p.skip is 1

            p_k1 = p.sample().k1
            if p_k1 is not k1:
                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                store(k3, create_herd_2(p_k1, k1, p.remove_skip(), r))
                return r

            r = p.glimpse(k2)
            if r is not none:
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                return r

            r = Meta(k1, k2, k3)
            assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
            p_ = p.insert(k2, r)
            if p is not p_:
                assert p_.sample().k1 is k1
                store(k3, p_)
            return r


        return simplified_conjure_triple__312


    @share
    def produce_simplified_conjure_triple(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple(k1, k2, k3):
            p = lookup(k1)
            if p is none:
                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                return provide(k1, q)
            if p.k2 is k2:
                if p.k3 is k3: return p

                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                store(k1, create_horde_2(1, p.k3, k3, p, q))
                return q

            if not p.is_herd:
                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q

            if p.skip is 0:
                q = p.glimpse(k2, absent)
                if q.k3 is k3: return q

                if not q.is_herd:
                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    if q is absent:
                        p_ = p.insert(k2, r)
                        if p is not p_: store(k1, p_)
                        return r

                    herd = create_herd_2(q.k3, k3, q, r)
                    p.displace(k2, herd)
                    return r

                r = q.glimpse(k3)
                if r is not none:
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                q_ = q.insert(k3, r)
                if q is not q_: p.displace(k2, q_)
                return r

            assert p.skip is 1

            p_k2 = p.sample().k2
            if p_k2 is not k2:
                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                store(k1, create_herd_2(p_k2, k2, p.remove_skip(), r))
                return r

            r = p.glimpse(k3)
            if r is not none:
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                return r

            r = Meta(k1, k2, k3)
            assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
            p_ = p.insert(k3, r)
            if p is not p_:
                assert p_.sample().k2 is k2
                store(k1, p_)
            return r


        return simplified_conjure_triple
