#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedNew')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    produce_NEW_conjure_dual__21         = 0
    produce_NEW_conjure_quadruple        = 0
    produce_NEW_conjure_quadruple__4123  = 0
    produce_NEW_conjure_triple           = 0
    produce_NEW_conjure_triple__312      = 0


    share(
        'produce_NEW_conjure_dual__21',         produce_NEW_conjure_dual__21,
        'produce_NEW_conjure_quadruple',        produce_NEW_conjure_quadruple,
        'produce_NEW_conjure_quadruple__4123',  produce_NEW_conjure_quadruple__4123,
        'produce_NEW_conjure_triple',           produce_NEW_conjure_triple,
        'produce_NEW_conjure_triple__312',      produce_NEW_conjure_triple__312,
    )


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
            coverage_dual[0] += 1
            p = lookup(k1)
            if p is none:
                coverage_dual[1] += 1
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                return provide(k1, q)
            if not p.is_herd:
                coverage_dual[2] += 1
                if p.k2 is k2:
                    coverage_dual[3] += 1
                    return p
                coverage_dual[4] += 1
                q = Meta(k1, k2)
                assert (q.k1 is k1) and (q.k2 is k2)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q
            coverage_dual[5] += 1

            q = p.glimpse(k2)
            if q is not none:
                coverage_dual[6] += 1
                assert (q.k1 is k1) and (q.k2 is k2)
                return q
            coverage_dual[7] += 1

            q = Meta(k1, k2)
            assert (q.k1 is k1) and (q.k2 is k2)
            p_ = p.insert(k2, q)
            if p is not p_:
                coverage_dual[8] += 1
                store(k1, p_)
            coverage_dual[9] += 1

            return q


        return NEW_conjure_dual


    coverage_dual = [0] * 10


    export(
        'coverage_dual', coverage_dual
    )
