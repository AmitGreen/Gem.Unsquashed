#
#   Copyright (c) Amit Green 2017.  All rights reserved.
#
@gem('Topaz.GeneratedConjureTriple')
def gem():
    @share
    def produce_simplified_conjure_triple__312(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__

        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple__312(k1, k2, k3):
            a = lookup(k3, absent)
            if a.k1 is k1:
                if a.k2 is k2: return a

                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                store(k3, create_horde_2(1, a.k2, k2, a, r))
                return r

            if not a.is_herd:
                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                store(k3, (r   if a is absent else   create_herd_2(a.k1, k1, a, r)))
                return r

            if a.skip is 0:
                b = a.glimpse(k1, absent)
                if b.k2 is k2: return b

                if not b.is_herd:
                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    if b is absent:
                        a_ = a.insert(k1, r)
                        if a is not a_: store(k3, a_)
                        return r
                    a.displace(k1, create_herd_2(b.k2, k2, b, r))
                    return r

                c = b.glimpse(k2)
                if c is not none:
                    assert (c.k3 is k3) and (c.k1 is k1) and (c.k2 is k2)
                    return c

                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                b_ = b.insert(k2, r)
                if b is not b_: a.displace(k1, b_)
                return r

            assert a.skip is 1

            a_k1 = a.sample().k1
            if a_k1 is not k1:
                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                store(k3, create_herd_2(a_k1, k1, a.remove_skip(), r))
                return r

            c = a.glimpse(k2)
            if c is not none:
                assert (c.k3 is k3) and (c.k1 is k1) and (c.k2 is k2)
                return c

            r = Meta(k1, k2, k3)
            assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
            a_ = a.insert(k2, r)
            if a is not a_:
                assert a_.sample().k1 is k1
                store(k3, a_)
            return r


        return simplified_conjure_triple__312


    @share
    def produce_simplified_conjure_triple(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        lookup = cache.get
        store  = cache.__setitem__

        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple(k1, k2, k3):
            a = lookup(k1, absent)
            if a.k2 is k2:
                if a.k3 is k3: return a

                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                store(k1, create_horde_2(1, a.k3, k3, a, r))
                return r

            if not a.is_herd:
                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                store(k1, (r   if a is absent else   create_herd_2(a.k2, k2, a, r)))
                return r

            if a.skip is 0:
                b = a.glimpse(k2, absent)
                if b.k3 is k3: return b

                if not b.is_herd:
                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    if b is absent:
                        a_ = a.insert(k2, r)
                        if a is not a_: store(k1, a_)
                        return r
                    a.displace(k2, create_herd_2(b.k3, k3, b, r))
                    return r

                c = b.glimpse(k3)
                if c is not none:
                    assert (c.k1 is k1) and (c.k2 is k2) and (c.k3 is k3)
                    return c

                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                b_ = b.insert(k3, r)
                if b is not b_: a.displace(k2, b_)
                return r

            assert a.skip is 1

            a_k2 = a.sample().k2
            if a_k2 is not k2:
                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                store(k1, create_herd_2(a_k2, k2, a.remove_skip(), r))
                return r

            c = a.glimpse(k3)
            if c is not none:
                assert (c.k1 is k1) and (c.k2 is k2) and (c.k3 is k3)
                return c

            r = Meta(k1, k2, k3)
            assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
            a_ = a.insert(k3, r)
            if a is not a_:
                assert a_.sample().k2 is k2
                store(k1, a_)
            return r


        return simplified_conjure_triple
