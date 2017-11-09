#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
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
            p = lookup(k2)
            if p is none:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                return provide(k2, q)
            if not p.is_herd:
                q = Meta(k1, k2)
                assert (q.k2 is k2) and (q.k1 is k1)
                herd = create_herd_2(p.k1, k1, p, q)
                store(k2, herd)
                return q

            q = p.glimpse(k1)
            if q is not none:
                assert (q.k2 is k2) and (q.k1 is k1)
                return q

            q = Meta(k1, k2)
            assert (q.k2 is k2) and (q.k1 is k1)
            p_ = p.insert(k1, q)
            if p is not p_: store(k2, p_)
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
            p = lookup(k1)
            if p is none:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return provide(k1, q)
            if not p.is_herd:
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q

            q = p.glimpse(k2)
            if q is not none:
                assert (q.k1 is k1) and (q.k2 is k2)
                return q

            q = Meta(k1, k2)
            assert (q.k1 is k1) and (q.k2 is k2)
            p_ = p.insert(k2, q)
            if p is not p_: store(k1, p_)
            return q


        return simplified_conjure_dual
