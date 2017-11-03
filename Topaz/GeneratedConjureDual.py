#
#   Copyright (c) Amit Green 2017.  All rights reserved.
#
@gem('Topaz.GeneratedConjureDual')
def gem():
    @share
    def produce_simplified_conjure_dual_v3(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual_v3(k1, k2):
            first = lookup(k1, absent)

            if first.k2 is k2:
                return first

            if not first.is_herd:
                r = Meta(k1, k2)

                store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))

                return r

            r = first.glimpse(k2)

            if r is not none:
                assert r.k2 is k2

                return r

            r = Meta(k1, k2)

            first__2 = first.insert(k2, r)

            if first is not first__2:
                store(k1, first__2)

            return r


        return simplified_conjure_dual_v3
