#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedNew')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    produce_NEW_conjure_dual__21         = 0
    produce_NEW_conjure_triple           = 0


    share(
        'produce_NEW_conjure_dual__21',         produce_NEW_conjure_dual__21,
        'produce_NEW_conjure_triple',           produce_NEW_conjure_triple,
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
            a = lookup(k1)
            if a is none: return provide(k1, Meta(k1, k2))
            if a.k2 is k2: return a

            ae = a.herd_estimate
            if ae is 0:
                b = Meta(k1, k2)
                store(k1, create_herd_2(a.k2, k2, a, b))
                return b

            #herd only
            if ae is 8: return (map__lookup(a, k2)) or (map__provide(a, k2, Meta(k1, k2)))

            if a.a is k2: return a.v
            if a.b is k2: return a.w
            if ae is 2:
                b = Meta(k1, k2)
                store(k1, create_herd_3(a.a, a.b, k2, a.v, a.w, b))
                return b

            if a.c is k2: return a.x
            if ae is 3:
                b = Meta(k1, k2)
                store(k1, create_herd_4(a.a, a.b, a.c, k2, a.v, a.w, a.x, b))
                return b

            assert ae is 7

            if a.d is k2: return a.y

            ae = a.e
            if ae is k2: return a.z
            if ae is absent:
                a.e = k2
                a.e6 = absent
                a.z = b = Meta(k1, k2)
                return b

            ae6 = a.e6
            if ae6 is k2: return a.z6
            if ae6 is absent:
                a.e6 = k2
                a.e7 = absent
                a.z6 = b = Meta(k1, k2)
                return b

            ae7 = a.e7
            if ae7 is k2: return a.z7

            b = Meta(k1, k2)

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
