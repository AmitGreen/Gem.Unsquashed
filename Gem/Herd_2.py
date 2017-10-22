#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd')
def gem():
    class Herd_2(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        is_horde     = false
        k1           = absent
        k2           = absent
        k3           = absent
        k4           = absent
        skip         = 0
        total        = 2


        def __repr__(t):
            return arrange('<Herd_2 %r : %r; %r : %r>', t.a, t.v, t.b, t.w)


        def count_nested(t):
            v = t.v
            w = t.w

            if v.is_herd:
                if w.is_herd:
                    return v.count_nested() + w.count_nested()

                return v.count_nested() + 1

            if w.is_herd:
                return 1 + w.count_nested()

            return 2


        def disperse(t, c, x):
            if (t.a is c) or (t.b is c):
                return t

            return create_herd_3(t.a, t.b, c, t.v, t.w, x)


        def displace(t, k, v):
            assert v is not absent

            if t.a is k:
                t.v = v
                return

            assert t.b is k

            t.w = v


        def distribute_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            r = Meta(k1, k2)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def distribute_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            r = Meta(k1, k2)

            displace(k2, create_herd_3(a, b, k1, t.v, t.w, r))

            return r


        def distribute_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r

                return v.distribute_triple_step2(displace_2v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.distribute_triple_step2(displace_2w, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def distribute_triple__312(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k1:
                v = t.v
                if v.k2 is k2:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k2, k2, v, r)
                    return r

                return v.distribute_triple_step2__312(displace_2v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r

                return w.distribute_triple_step2__312(displace_2w, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k3, create_herd_3(a, b, k1, t.v, t.w, r))

            return r


        def distribute_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k2, create_herd_3(a, b, k3, t.v, t.w, r))
                return r

            displace(parent, create_herd_3(a, b, k3, t.v, t.w, r))
            return r


        def distribute_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k1, create_herd_3(a, b, k2, t.v, t.w, r))
                return r

            displace(parent, create_herd_3(a, b, k2, t.v, t.w, r))
            return r


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w

            assert k is not absent

            return d


        def increment_skip(t, skip = 1):
            assert 1 <= skip <= 2

            return create_horde_2(skip, t.a, t.b, t.v, t.w)


        def insert(t, c, x):
            assert (c is not absent) and (t.a is not c) and (t.b is not c) and (x is not absent)

            return create_herd_3(t.a, t.b, c, t.v, t.w, x)


        def install(t, c, x):
            assert (c is not absent) and (x is not absent)

            if t.a is c:
                t.v = x
                return t

            if t.b is c:
                t.w = x
                return t

            return create_herd_3(t.a, t.b, c, t.v, t.w, x)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b

            nub = (0   if type(a) is Integer else   a.nub)

            av = ((a, t.v))
            bw = ((b, t.w))

            if ((a < b)   if nub is 0 else   (nub(a) < nub(b))):
                return ((av, bw))

            return ((bw, av))


        def ordered_values(t):
            return (( t.v, t.w ))


        def provision(t, c, x):
            a = t.a
            if a is c: return t

            b = t.b
            if b is c: return t

            return create_herd_3(a, b, c, t.v, t.w, x)


        def scrub(t):
            v = t.v
            w = t.w

            v_scrub = v.scrub
            w_scrub = w.scrub

            #my_line('v: %r; w: %r; v_scrub: %r; w_scrub: %r', v, w, v_scrub, w_scrub)

            if v_scrub is 0:
                if reference_count(v) is 3:
                    if w_scrub is 0:
                        if reference_count(w) is 3:
                            return 0

                        w_increment = w.increment_skip
                        return (w   if w_increment is 0 else    w_increment())

                    w = w_scrub()

                    if w is 0:
                        return 0

                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment())

                if w_scrub is 0:
                    if reference_count(w) is 3:
                        v_increment = v.increment_skip
                        return (v   if v_increment is 0 else    v_increment())

                    return t

                w = w_scrub()

                if w is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                t.w = w
                return t

            v = v_scrub()

            if v is 0:
                if w_scrub is 0:
                    if reference_count(w) is 3:
                        return 0

                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment())

                w = w_scrub()

                if w is 0:
                    return 0

                w_increment = w.increment_skip
                return (w   if w_increment is 0 else    w_increment())

            if w_scrub is 0:
                if reference_count(w) is 3:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                t.v = v
                return t

            w = w_scrub()

            if w is 0:
                v_increment = v.increment_skip
                return (v   if v_increment is 0 else    v_increment())

            t.v = v
            t.w = w
            return t


        values = ordered_values


    Herd_2.first = Herd_2.v


    new_Herd_2 = Method(Object.__new__, Herd_2)


    @export
    def create_herd_2(a, b, v, w):
        assert (a is not absent) and (a is not b) and (b is not absent) and (v is not absent) and (w is not absent)

        t = new_Herd_2()

        t.a = a
        t.b = b
        t.v = v
        t.w = w

        return t


    displace_2v = Herd_2.v.__set__
    displace_2w = Herd_2.w.__set__
