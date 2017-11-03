#
#   Copyright (c) Amit Green 2017.  All rights reserved.
#
@gem('Topaz.GeneratedConjureDual')
def gem():
    @share
    def produce_simplified_conjure_dual(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual(k1, k2):
            a = lookup(k1, absent)

            if a.k2 is k2:
                return a

            if not a.is_herd:
                r = Meta(k1, k2)

                store(k1, (r   if a is absent else   create_herd_2(a.k2, k2, a, r)))

                return r

            r = a.glimpse(k2)

            if r is not none:
                assert r.k2 is k2

                return r

            r = Meta(k1, k2)

            a_ = a.insert(k2, r)

            if a is not a_:
                store(k1, a_)

            return r


        return simplified_conjure_dual


    @share
    def produce_simplified_conjure_dual__21(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_dual__21(k1, k2):
            a = lookup(k2, absent)

            if a.k1 is k1:
                return a

            if not a.is_herd:
                r = Meta(k1, k2)

                store(k2, (r   if a is absent else   create_herd_2(a.k1, k1, a, r)))

                return r

            r = a.glimpse(k1)

            if r is not none:
                assert r.k1 is k1

                return r

            r = Meta(k1, k2)

            a_ = a.insert(k1, r)

            if a is not a_:
                store(k2, a_)

            return r


        return simplified_conjure_dual__21
