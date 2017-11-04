#
#   Copyright (c) Amit Green 2017.  All rights reserved.
#
@gem('Topaz.GeneratedConjureDual')
def gem():
    @share
    def produce_simplified_conjure_dual__21(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__

        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual__21(k1, k2):
            a = lookup(k2, absent)
            if a.k1 is k1: return a

            if not a.is_herd:
                r = Meta(k1, k2)
                assert (r.k2 is k2) and (r.k1 is k1)
                store(k2, (r   if a is absent else   create_herd_2(a.k1, k1, a, r)))
                return r

            b = a.glimpse(k1)
            if b is not none:
                assert (b.k2 is k2) and (b.k1 is k1)
                return b

            r = Meta(k1, k2)
            assert (r.k2 is k2) and (r.k1 is k1)
            a_ = a.insert(k1, r)
            if a is not a_: store(k2, a_)
            return r


        return simplified_conjure_dual__21


    @share
    def produce_simplified_conjure_dual(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__

        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual(k1, k2):
            a = lookup(k1, absent)
            if a.k2 is k2: return a

            if not a.is_herd:
                r = Meta(k1, k2)
                assert (r.k1 is k1) and (r.k2 is k2)
                store(k1, (r   if a is absent else   create_herd_2(a.k2, k2, a, r)))
                return r

            b = a.glimpse(k2)
            if b is not none:
                assert (b.k1 is k1) and (b.k2 is k2)
                return b

            r = Meta(k1, k2)
            assert (r.k1 is k1) and (r.k2 is k2)
            a_ = a.insert(k2, r)
            if a is not a_: store(k1, a_)
            return r


        return simplified_conjure_dual
