#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.ConjureQuadruple')
def gem():
    @export
    def produce_conjure_unique_quadruple(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        if lookup is absent:    lookup = cache.get
        if store  is absent:    store  = cache.__setitem__


        @rename('conjure_%s', name)
        def conjure_unique_quadruple(k1, k2, k3, k4):
            first = lookup(k1, absent)

            if first.k2 is k2:
                if first.k3 is k3:
                    if first.k4 is k4:
                        return first

                    r = Meta(k1, k2, k3, k4)
                    store(k1, create_horde_2(2, first.k4, k4, first, r))
                    return r

                r = Meta(k1, k2, k3, k4)
                store(k1, create_horde_2(1, first.k3, k3, first, r))
                return r

            if not first.is_herd:
                r = Meta(k1, k2, k3, k4)
                store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))
                return r

            if first.skip is 0:
                second = first.glimpse(k2, absent)

                if second.k3 is k3:
                    if second.k4 is k4:
                        return second

                    r = Meta(k1, k2, k3, k4)
                    first.displace(k2, create_horde_2(1, second.k4, k4, second, r))
                    return r

                if not second.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if second is absent:
                        first__2 = first.insert(k2, r)

                        if first is not first__2:
                            store(k1, first__2)

                        return r

                    first.displace(k2, create_herd_2(second.k3, k3, second, r))
                    return r

                if second.skip is 0:
                    third = second.glimpse(k3, absent)

                    if third.k4 is k4:
                        assert (third.k1 is k1) and (third.k2 is k2)

                        return third

                    if not third.is_herd:
                        r = Meta(k1, k2, k3, k4)

                        if third is absent:
                            second__2 = second.insert(k3, r)

                            if second is not second__2:
                                first.displace(k2, second__2)

                            return r

                        second.displace(k3, create_herd_2(third.k4, k4, third, r))
                        return r

                    fourth = third.glimpse(k4)

                    if fourth is not none:
                        return fourth

                    r = Meta(k1, k2, k3, k4)

                    third__2 = third.insert(k4, r)

                    if third is not third__2:
                        second.displace(k3, third__2)

                    return r

                assert second.skip is 1

                second_k3 = second.sample().k3

                if second_k3 is k3:
                    fourth = second.glimpse(k4)

                    if fourth is not none:
                        return fourth

                    r = Meta(k1, k2, k3, k4)

                    second__2 = second.insert(k4, r)

                    if second is not second__2:
                        first.displace(k2, second__2)

                    return r

                r = Meta(k1, k2, k3, k4)
                first.displace(k2, create_herd_2(second_k3, k3, second.remove_skip(), r))
                return r

            first_sample = first.sample()
            first_k2     = first_sample.k2

            if first_k2 is not k2:
                r = Meta(k1, k2, k3, k4)
                store(k1, create_herd_2(first_k2, k2, first.remove_skip(), r))
                return r

            if first.skip is 1:
                third = first.glimpse(k3, absent)

                if third.k4 is k4:
                    assert (third.k1 is k1) and (third.k2 is k2)

                    return third

                if not third.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if third is absent:
                        first__2 = first.insert(k3, r)

                        if first is not first__2:
                            store(k1, first__2)

                        return r

                    first.displace(k3, create_herd_2(third.k4, k4, third, r))
                    return r

                fourth = third.glimpse(k4)

                if fourth is not none:
                    return fourth

                r = Meta(k1, k2, k3, k4)

                third__2 = third.insert(k4, r)

                if third is not third__2:
                    first.displace(k3, third__2)

                return r

            assert first.skip is 2

            first_k3 = first_sample.k3

            if first_k3 is not k3:
                r = Meta(k1, k2, k3, k4)
                store(k1, create_horde_2(1, first_k3, k3, first.remove_skip(2), r))
                return r

            fourth = first.glimpse(k4)

            if fourth is not none:
                return fourth

            r = Meta(k1, k2, k3, k4)

            first__2 = first.insert(k4, r)

            if first is not first__2:
                store(k1, first__2)

            return r


        return conjure_unique_quadruple


    @export
    def produce_conjure_unique_quadruple__4123(
            name, Meta, cache,

            lookup = absent,
            store  = absent,
    ):
        if lookup is absent:    lookup = cache.get
        if store  is absent:    store  = cache.__setitem__


        @rename('conjure_%s__4123', name)
        def conjure_unique_quadruple__4123(k1, k2, k3, k4):
            first = lookup(k4, absent)

            if first.k1 is k1:
                if first.k2 is k2:
                    if first.k3 is k3:
                        return first

                    r = Meta(k1, k2, k3, k4)
                    store(k4, create_horde_2(2, first.k3, k3, first, r))
                    return r

                r = Meta(k1, k2, k3, k4)
                store(k4, create_horde_2(1, first.k2, k2, first, r))
                return r

            if not first.is_herd:
                r = Meta(k1, k2, k3, k4)
                store(k4, (r   if first is absent else   create_herd_2(first.k1, k1, first, r)))
                return r

            if first.skip is 0:
                second = first.glimpse(k1, absent)

                if second.k2 is k2:
                    if second.k3 is k3:
                        return second

                    r = Meta(k1, k2, k3, k4)
                    first.displace(k1, create_horde_2(1, second.k3, k3, second, r))
                    return r

                if not second.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if second is absent:
                        first__2 = first.insert(k1, r)

                        if first is not first__2:
                            store(k4, first__2)

                        return r

                    first.displace(k1, create_herd_2(second.k2, k2, second, r))
                    return r

                if second.skip is 0:
                    third = second.glimpse(k2, absent)

                    if third.k3 is k3:
                        assert (third.k4 is k4) and (third.k1 is k1)

                        return third

                    if not third.is_herd:
                        r = Meta(k1, k2, k3, k4)

                        if third is absent:
                            second__2 = second.insert(k2, r)

                            if second is not second__2:
                                first.displace(k1, second__2)

                            return r

                        second.displace(k2, create_herd_2(third.k3, k3, third, r))
                        return r

                    fourth = third.glimpse(k3)

                    if fourth is not none:
                        return fourth

                    r = Meta(k1, k2, k3, k4)

                    third__2 = third.insert(k3, r)

                    if third is not third__2:
                        second.displace(k2, third__2)

                    return r

                assert second.skip is 1

                second_k2 = second.sample().k2

                if second_k2 is k2:
                    fourth = second.glimpse(k3)

                    if fourth is not none:
                        return fourth

                    r = Meta(k1, k2, k3, k4)

                    second__2 = second.insert(k3, r)

                    if second is not second__2:
                        first.displace(k1, second__2)

                    return r

                r = Meta(k1, k2, k3, k4)
                first.displace(k1, create_herd_2(second_k2, k2, second.remove_skip(), r))
                return r

            first_sample = first.sample()
            first_k1     = first_sample.k1

            if first_k1 is not k1:
                r = Meta(k1, k2, k3, k4)
                store(k4, create_herd_2(first_k1, k1, first.remove_skip(), r))
                return r

            if first.skip is 1:
                third = first.glimpse(k2, absent)

                if third.k3 is k3:
                    assert (third.k4 is k4) and (third.k1 is k1)

                    return third

                if not third.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if third is absent:
                        first__2 = first.insert(k2, r)

                        if first is not first__2:
                            store(k4, first__2)

                        return r

                    first.displace(k2, create_herd_2(third.k3, k3, third, r))
                    return r

                fourth = third.glimpse(k3)

                if fourth is not none:
                    return fourth

                r = Meta(k1, k2, k3, k4)

                third__2 = third.insert(k3, r)

                if third is not third__2:
                    first.displace(k2, third__2)

                return r

            assert first.skip is 2

            first_k2 = first_sample.k2

            if first_k2 is not k2:
                r = Meta(k1, k2, k3, k4)
                store(k4, create_horde_2(1, first_k2, k2, first.remove_skip(2), r))
                return r

            fourth = first.glimpse(k3)

            if fourth is not none:
                return fourth

            r = Meta(k1, k2, k3, k4)

            first__2 = first.insert(k3, r)

            if first is not first__2:
                store(k4, first__2)

            return r


        return conjure_unique_quadruple__4123
