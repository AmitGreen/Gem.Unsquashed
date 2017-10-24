#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Horde')
def gem():
    require_gem('Gem.Herd')


    #
    #   Horde:  Like a Herd, but has a 'skip' factor
    #


    map__lookup  = Map.get
    map__provide = Map.setdefault


    class Horde_23(Object):
        __slots__ = ((
            'skip',                     #   Integer { 0 | 1 }
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Absent | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Vacant | Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))
            ka = nub(a)
            kb = nub(b)

            if c is absent:
                if ka < kb:
                    return ((av, bw))

                return ((bw, av))

            cx = ((c, t.x))
            kc = nub(c)

            if ka < kb:
                if kb < kc:
                    return ((av, bw, cx))

                if ka < kc:
                    return ((av, cx, bw))

                return ((cx, av, bw))

            if ka < kc:
                return ((bw, av, cx))

            if kb < kc:
                return ((bw, cx, av))

            return ((cx, bw, av))


        def provision_triple(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            v    = t.v
            v_k2 = v.k2

            if v_k2 is not k2:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k1, create_herd_2(v_k2, k2, t, r))

                return r

            a = t.a
            if a is k3:     return v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k3
                t.x = r
                return r

            displace(k1, create_horde_many(1, a, b, c, k3, v, t.w, t.x, r))

            return r


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            v    = t.v
            v_k1 = v.k1

            if v_k1 is not k1:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k3, create_herd_2(v_k1, k1, t, r))

                return r

            a = t.a
            if a is k2:     return v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k2
                t.x = r
                return r

            displace(k3, create_horde_many(1, a, b, c, k2, v, t.w, t.x, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            assert t.skip is 0

            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.w

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k3
                t.x = r
                return r

            displace(parent, k2, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))

            return r


        def provision_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            assert t.skip is 0

            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.w

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k2
                t.x = r
                return r

            displace(parent, k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


    Horde_23.sample = Horde_23.v


    class Horde_Many(Map):
        __slots__ = ((
            'skip',                     #   Integer { 0 | 1 }
            'sample',                   #   Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent


        items_sorted_by_key = items_sorted_by_key__herd_many


        def provision_triple(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            sample_k2 = t.sample.k2

            if sample_k2 is not k2:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k1, create_herd_2(sample_k2, k2, t, r))

                return r

            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            sample_k1 = t.sample.k1

            if sample_k1 is not k1:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k3, create_herd_2(sample_k1, k1, t, r))

                return r

            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))


        def provision_triple_step2(t, _displace, _parent, Meta, k1, k2, k3):
            assert t.skip is 0

            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def provision_triple_step2__312(t, _displace, _parent, Meta, k1, k2, k3):
            assert t.skip is 0

            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))



    new_Horde_23   = Method(Object.__new__, Horde_23)
    new_Horde_Many = Method(Map   .__new__, Horde_Many)


    @export
    def create_horde_2(skip, a, b, v, w):
        assert (skip is 1) and (a is not absent) and (a is not b) and (b is not absent)

        t = new_Horde_23()

        t.skip = skip
        t.a    = a
        t.b    = b
        t.c    = absent
        t.v    = v
        t.w    = w

        return t


    def create_horde_many(skip, a, b, c, d, v, w, x, y):
        assert skip is 1
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent

        t = new_Horde_Many()

        t.skip   = skip
        t.sample = v
        t[a]     = v
        t[b]     = w
        t[c]     = x
        t[d]     = y

        return t
