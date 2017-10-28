#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.ConjureQuadruple')
def gem():
    def produce_conjure_unique_quadruple(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('conjure_%s', name)
        def conjure_unique_quadruple(k1, k2, k3, k4):
            first = lookup(k1, absent)

            if first.k2 is k2:
                if first.k3 is k3:
                    if first.k3 is k4:
                        return first

                    r = Meta(k1, k2, k3, k4)
                    store(k1, create_horde_2(2, first.k3, k4, first, r))
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
                    return second

                if not second.is_herd:
                    r = Meta(k1, k2, k3, k4)

                    if second is absent:
                        first__2 = first.insert(k2, r)

                        if first is not first__2:
                            store(k1, first__2)

                        return r

                    first.displace(k2, create_herd_2(second.k3, k3, second, r))
                    return r

                third = second.glimpse(k3, k4)

                if third is not none:
                    assert third.k3 is k3

                    return third

                r = Meta(k1, k2, k3, k4)

                second__2 = second.insert(k3, r)

                if second is not second__2:
                    first.displace(k2, second__2)

                return r

            assert first.skip is 1

            if first.sample.k2 is k2:
                third = first.glimpse(k3, k4)

                if third is not none:
                    assert (third.k2 is k2) and (third.k3 is k3, k4)

                    return third

                r = Meta(k1, k2, k3, k4)

                first__2 = first.insert(k3, r)

                if first is not first__2:
                    assert first__2.sample.k2 is k2

                    store(k1, first__2)

                return r

            r = Meta(k1, k2, k3, k4)
            store(k1, create_herd_2(first.sample.k2, k2, first.remove_skip(), r))
            return r


        return conjure_unique_quadruple
