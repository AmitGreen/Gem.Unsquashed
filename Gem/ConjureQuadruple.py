#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.ConjureQuadruple')
def gem():
    require_gem('Gem.Global')


    @export
    def produce_conjure_unique_quadruple__4123(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        if lookup is absent:    lookup = cache.get
        if store  is absent:    store  = cache.__setitem__


        @rename('conjure_%s', name)
        def conjure_unique_quadruple__4123(k1, k2, k3, k4):
            a = lookup(k4, absent)

            if a.k1 is k1:
                if a.k2 is k2:
                    if a.k3 is k3:
                        return a

                    r = Meta(k1, k2, k3, k4)
                    store(k4, create_horde_2(2, a.k3, k3, a, r))
                    return r

                r = Meta(k1, k2, k3, k4)
                store(k4, create_horde_2(1, a.k2, k2, a, r))
                return r

            if not a.is_herd:
                r = Meta(k1, k2, k3, k4)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                store(k4, (r   if a is absent else   create_herd_2(a.k1, k1, a, r)))
                return r

            if a.skip is 0:
                b = a.glimpse(k1, absent)

                if b.k2 is k2:
                    if b.k3 is k3:
                        return b

                    r = Meta(k1, k2, k3, k4)
                    a.displace(k1, create_horde_2(1, b.k3, k3, b, r))
                    return r

                if not b.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if b is absent:
                        a_ = a.insert(k1, r)

                        if a is not a_:
                            store(k4, a_)

                        return r

                    a.displace(k1, create_herd_2(b.k2, k2, b, r))
                    return r

                if b.skip is 0:
                    c = b.glimpse(k2, absent)

                    if c.k3 is k3:
                        assert (c.k4 is k4) and (c.k1 is k1)

                        return c

                    if not c.is_herd:
                        r = Meta(k1, k2, k3, k4)

                        if c is absent:
                            b_ = b.insert(k2, r)

                            if b is not b_:
                                a.displace(k1, b_)

                            return r

                        b.displace(k2, create_herd_2(c.k3, k3, c, r))
                        return r

                    d = c.glimpse(k3)

                    if d is not none:
                        return d

                    r = Meta(k1, k2, k3, k4)

                    c_ = c.insert(k3, r)

                    if c is not c_:
                        b.displace(k2, c_)

                    return r

                assert b.skip is 1

                second_k2 = b.sample().k2

                if second_k2 is k2:
                    d = b.glimpse(k3)

                    if d is not none:
                        return d

                    r = Meta(k1, k2, k3, k4)

                    b_ = b.insert(k3, r)

                    if b is not b_:
                        a.displace(k1, b_)

                    return r

                r = Meta(k1, k2, k3, k4)
                a.displace(k1, create_herd_2(second_k2, k2, b.remove_skip(), r))
                return r

            a_sample = a.sample()
            first_k1     = a_sample.k1

            if first_k1 is not k1:
                r = Meta(k1, k2, k3, k4)
                store(k4, create_herd_2(first_k1, k1, a.remove_skip(), r))
                return r

            if a.skip is 1:
                c = a.glimpse(k2, absent)

                if c.k3 is k3:
                    assert (c.k4 is k4) and (c.k1 is k1)

                    return c

                if not c.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if c is absent:
                        a_ = a.insert(k2, r)

                        if a is not a_:
                            store(k4, a_)

                        return r

                    a.displace(k2, create_herd_2(c.k3, k3, c, r))
                    return r

                d = c.glimpse(k3)

                if d is not none:
                    return d

                r = Meta(k1, k2, k3, k4)

                c_ = c.insert(k3, r)

                if c is not c_:
                    a.displace(k2, c_)

                return r

            assert a.skip is 2

            a_k2 = a_sample.k2

            if a_k2 is not k2:
                r = Meta(k1, k2, k3, k4)
                store(k4, create_horde_2(1, a_k2, k2, a.remove_skip(2), r))
                return r

            d = a.glimpse(k3)

            if d is not none:
                return d

            r = Meta(k1, k2, k3, k4)

            a_ = a.insert(k3, r)

            if a is not a_:
                store(k4, a_)

            return r


        return conjure_unique_quadruple__4123
