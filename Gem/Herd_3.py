#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd')
def gem():
    class Herd_3(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        is_horde     = false
        k1           = absent
        k2           = absent
        k3           = absent
        k4           = absent
        skip         = 0


        def count_nested(t):
            v = t.v
            w = t.w
            x = t.x

            if v.is_herd:
                if w.is_herd:
                    if x.is_herd:
                        return v.count_nested() + w.count_nested() + x.count_nested()

                    return v.count_nested() + w.count_nested() + 1

                if x.is_herd:
                    return v.count_nested() + 1 + x.count_nested()

                return v.count_nested() + 2

            if w.is_herd:
                if x.is_herd:
                    return 1 + w.count_nested() + x.count_nested()

                return 2 + w.count_nested()         #  1 + w.count_nested() + 1

            if x.is_herd:
                return 2 + x.count_nested()

            return 3


        def displace(t, k, v):
            assert v is not absent

            if t.a is k:
                t.v = v
                return

            if t.b is k:
                t.w = v
                return

            assert t.c is k

            t.x = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w
            if t.c is k: return t.x

            assert k is not absent

            return d


        def increment_skip(t, skip = 1):
            assert 1 <= skip <= 2

            return create_horde_3(skip, t.a, t.b, t.c, t.v, t.w, t.x)


        def insert(t, d, y):
            assert (d is not absent) and (t.a is not d) and (t.b is not d) and (t.c is not d) and (y is not absent)

            return create_herd_4(t.a, t.b, t.c, d, t.v, t.w, t.x, y)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = (0   if type(a) is Integer else   a.nub)

            av = ((a, t.v))
            bw = ((b, t.w))
            cx = ((c, t.x))
            ka = (a   if nub is 0 else   nub(a))
            kb = (b   if nub is 0 else   nub(b))
            kc = (c   if nub is 0 else   nub(c))

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


        def provision(t, d, y):
            a = t.a
            if a is d: return t

            b = t.b
            if b is d: return t

            c = t.c
            if c is d: return t

            return create_herd_4(a, b, c, d, t.v, t.w, t.x, y)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            c = t.c
            if c is k2: return t.x

            r = Meta(k1, k2)

            displace(k1, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            c = t.c
            if c is k1: return t.x

            r = Meta(k1, k2)

            displace(k2, create_herd_4(a, b, c, k1, t.v, t.w, t.x, r))

            return r


        def provision_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r

                return v.provision_triple_step2(displace_3v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.provision_triple_step2(displace_3w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x

                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r

                return x.provision_triple_step2(displace_3x, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k1:
                v = t.v
                if v.k2 is k2:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k2, k2, v, r)
                    return r

                return v.provision_triple_step2__312(displace_3v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r

                return w.provision_triple_step2__312(displace_3w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k1:
                x = t.x
                if x.k2 is k2:  return x

                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k2, k2, x, r)
                    return r

                return x.provision_triple_step2__312(displace_3x, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k3, create_herd_4(a, b, c, k1, t.v, t.w, t.x, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k2, create_herd_4(a, b, c, k3, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4(a, b, c, k3, t.v, t.w, t.x, r))
            return r


        def provision_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k1, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))
            return r


        def scrub(t):
            v = t.v
            w = t.w
            x = t.x

            v_scrub = v.scrub
            w_scrub = w.scrub
            x_scrub = x.scrub

            if v_scrub is 0:
                if reference_count(v) is 3:
                    v = 0
            else:
                v = v_scrub()

            if w_scrub is 0:
                if reference_count(w) is 3:
                    w = 0
            else:
                w = w_scrub()

            if x_scrub is 0:
                if reference_count(x) is 3:
                    x = 0
            else:
                x = x_scrub()

            if v is 0:
                if w is 0:
                    if x is 0:
                        return 0

                    x_increment = x.increment_skip
                    return (x   if x_increment is 0 else    x_increment())

                if x is 0:
                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment())

                return create_herd_2(t.b, t.c, w, x)

            if w is 0:
                if x is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                return create_herd_2(t.a, t.c, v, x)

            if x is 0:
                return create_herd_2(t.a, t.b, v, w)

            t.v = v
            t.w = w
            t.x = x
            return t


        def values(t):
            return ((t.v, t.w, t.x))


    Herd_3.first = Herd_3.v


    new_Herd_3 = Method(Object.__new__, Herd_3)


    @share
    def create_herd_3(a, b, c, v, w, x):
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert c is not absent
        assert (v is not absent) and (w is not absent) and (x is not absent)

        t = new_Herd_3()

        t.a = a
        t.b = b
        t.c = c
        t.v = v
        t.w = w
        t.x = x

        return t


    displace_3v = Herd_3.v.__set__
    displace_3w = Herd_3.w.__set__
    displace_3x = Herd_3.x.__set__
