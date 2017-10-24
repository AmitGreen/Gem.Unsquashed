#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd')
def gem():
    #
    #   Herd:
    #
    #       Liquid (modifiable)
    #       Map (Associative Array)
    #       Unordered
    #       Key must not include absent
    #
    #   .inject
    #   .lookup
    #   .provide
    #       Use == for comparing keys
    #
    #       All the verbs here do NOT have an 'is' inside them.
    #
    #   .glimpse
    #   .insert
    #   .provision
    #       Unique Keys: Use 'is' for comparing keys
    #
    #       NOTE: All the verbs here have an 'is' inside them.
    #


    require_gem('Gem.Method')


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    def displace_v(t, a, v):
        assert t.a is a
        t.v = v


    def displace_w(t, b, w):
        assert t.b is b
        t.w = w


    def displace_x(t, c, x):
        assert t.c is c
        t.x = x


    def displace_y(t, d, y):
        assert t.d is d
        t.y = y


    def displace_z(t, e, z):
        assert t.e is e
        t.z = z


    def displace_z6(t, e6, z6):
        assert t.e6 is e6
        t.z6 = z6


    def displace_z7(t, e7, z7):
        assert t.e7 is e7
        t.z7 = z7


    class Herd_0(Object):
        __slots__ = (())


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        @static_method
        def items_sorted_by_key():
            return (())


    class Herd_1(Object):
        __slots__ = ((
            'a',                        #   Any
            'v',                        #   Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        def __init__(t, a, v):
            assert a is not absent

            t.a = a
            t.v = v


        def displace(t, k, v):
            assert t.a is k

            t.v = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v

            assert k is not absent

            return d


        def insert(t, b, w):
            assert (b is not absent) and (t.a is not b)

            return create_herd_2(t.a, b, t.v, w)


        def items_sorted_by_key(t):
            return (( ((t.a, t.v)), ))


        def provision(t, b, w):
            a = t.a
            if a is b: return t

            return create_herd_2(a, b, t.v, w)


        def provision_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r

                return v.provision_triple_step2(displace_v, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_2(a, k2, t.v, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            r = Meta(k1, k2, k3)

            displace(parent, k2, create_herd_2(a, k3, t.v, r))

            return r


    class Herd_2(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        def displace(t, k, v):
            if t.a is k:
                t.v = v
                return

            assert t.b is k

            t.w = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w

            assert k is not absent

            return d


        def insert(t, c, x):
            assert (c is not absent) and (t.a is not c) and (t.b is not c)

            return create_herd_3(t.a, t.b, c, t.v, t.w, x)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))

            if nub(a) < nub(b):
                return ((av, bw))

            return ((bw, av))


        def provision(t, c, x):
            a = t.a
            if a is c: return t

            b = t.b
            if b is c: return t

            return create_herd_3(a, b, c, t.v, t.w, x)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            r = Meta(k1, k2)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            r = Meta(k1, k2)

            displace(k2, create_herd_3(a, b, k1, t.v, t.w, r))

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

                return v.provision_triple_step2(displace_v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.provision_triple_step2(displace_w, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            r = Meta(k1, k2, k3)

            displace(parent, k2, create_herd_3(a, b, k3, t.v, t.w, r))

            return r


    class Herd_3(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        def displace(t, k, v):
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


        def insert(t, d, y):
            assert (d is not absent) and (t.a is not d) and (t.b is not d) and (t.c is not d)

            return create_herd_4567(t.a, t.b, t.c, d, t.v, t.w, t.x, y)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))
            cx = ((c, t.x))
            ka = nub(a)
            kb = nub(b)
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


        def provision(t, d, y):
            a = t.a
            if a is d: return t

            b = t.b
            if b is d: return t

            c = t.c
            if c is d: return t

            return create_herd_4567(a, b, c, d, t.v, t.w, t.x, y)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            c = t.c
            if c is k2: return t.x

            r = Meta(k1, k2)

            displace(k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            c = t.c
            if c is k1: return t.x

            r = Meta(k1, k2)

            displace(k2, create_herd_4567(a, b, c, k1, t.v, t.w, t.x, r))

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

                return v.provision_triple_step2(displace_v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.provision_triple_step2(displace_w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x

                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r

                return x.provision_triple_step2(displace_x, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            r = Meta(k1, k2, k3)

            displace(parent, k2, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))

            return r


    class Herd_4567(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'd',                        #   Any
            'e',                        #   Absent | Any
            'e6',                       #   Absent | Vacant | Any
            'e7',                       #   Absent | Vacant | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
            'y',                        #   Any
            'z',                        #   Any
            'z6',                       #   Any
            'z7',                       #   Any
        ))


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        def displace(t, k, v):
            if t.a is k:
                t.v = v
                return

            if t.b is k:
                t.w = v
                return

            if t.c is k:
                t.x = v
                return

            if t.d is k:
                t.y = v
                return

            if t.e is k:
                t.z = v
                return

            if t.e6 is k:
                t.z6 = v
                return

            assert t.e7 is k

            t.z7 = v


        def glimpse(t, k, d = none):
            if t.a is k:        return t.v
            if t.b is k:        return t.w
            if t.c is k:        return t.x
            if t.d is k:        return t.y

            assert k is not absent

            e = t.e
            if e is k:          return t.z
            if e is absent:     return d

            e6 = t.e6
            if e6 is k:         return t.z6
            if e6 is absent:    return d

            if t.e7 is k:       return t.z7

            return d


        def insert(t, e8, z8):
            assert (t.a is not e8) and (t.b is not e8) and (t.c is not e8) and (t.d is not e8)
            assert e8 is not absent

            e = t.e
            if e is absent:
                t.e  = e8
                t.e6 = absent
                t.z  = z8
                return t
            assert t.e is not e8

            e6 = t.e6
            if e6 is absent:
                t.e6 = e8
                t.e7 = absent
                t.z6 = z8
                return t
            assert t.e6 is not e8

            e7 = t.e7
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t
            assert t.e7 is not e8

            return create_herd_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def items_sorted_by_key(t):
            a   = t.a
            nub = a.nub

            e = t.e

            if e is absent:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]
            else:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y)), ((e, t.z))]

                e6 = t.e6

                if e6 is absent:
                    r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y)), ((e, t.z))]
                else:
                    e7 = t.e7

                    if e7 is absent:
                        r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y)), ((e, t.z)), ((e6, t.z6))]
                    else:
                        r = [
                                ((a,   t.v)),
                                ((t.b, t.w)),
                                ((t.c, t.x)),
                                ((t.d, t.y)),
                                ((e,   t.z)),
                                ((e6,  t.z6)),
                                ((e7,  t.z7)),
                            ]


            if nub is 0:
                def key(pair):
                    return pair[0]
            else:
                def key(pair):
                    if nub.__self__.__objclass__ != pair[0].__class__:
                        line('FIXING: %r', pair[0])
                        return pair[0].name

                    return nub(pair[0])


            return sorted_list(r, key = key)


        def provision(t, e8, z8):
            a = t.a
            if a is e8: return t

            b = t.b
            if b is e8: return t

            c = t.c
            if c is e8: return t

            d = t.d
            if d is e8: return t

            assert e8 is not absent

            e = t.e
            if e is e8: return t
            if e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t

            e6 = t.e6
            if e6 is e8: return t
            if e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t

            e7 = t.e7
            if e7 is e8: return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            return create_herd_many(a, b, c, d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            d = t.d
            if d is k2:     return t.y

            e = t.e
            if e is k2:     return t.z
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k2:    return t.z6
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k2:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k2
                t.z7 = Meta(k1, k2)
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1:     return t.v

            b = t.b
            if b is k1:     return t.w

            c = t.c
            if c is k1:     return t.x

            d = t.d
            if d is k1:     return t.y

            e = t.e
            if e is k1:     return t.z
            if e is absent:
                t.e  = k1
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k1:    return t.z6
            if e6 is absent:
                t.e6 = k1
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k1:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k1
                t.z7 = Meta(k1, k2)
                return r

            displace(k2, create_herd_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

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
                return v.provision_triple_step2(displace_v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w
                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r
                return w.provision_triple_step2(displace_w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x
                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r
                return x.provision_triple_step2(displace_x, t, Meta, k1, k2, k3)

            d = t.d
            if d is k2:
                y = t.y
                if y.k3 is k3:  return y
                if not y.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.y = create_herd_2(y.k3, k3, y, r)
                    return r
                return y.provision_triple_step2(displace_y, t, Meta, k1, k2, k3)

            e = t.e
            if e is k2:
                z = t.z
                if z.k3 is k3:  return z
                if not z.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.z = create_herd_2(z.k3, k3, z, r)
                    return r
                return z.provision_triple_step2(displace_z, t, Meta, k1, k2, k3)
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k2:
                z6 = t.z6
                if z6.k3 is k3:  return z6
                if not z6.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z6 = create_herd_2(z6.k3, k3, z6, r)
                    return r
                return z6.provision_triple_step2(displace_z6, t, Meta, k1, k2, k3)
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k2:
                z7 = t.z7
                if z7.k3 is k3:  return z7
                if not z7.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z7 = create_herd_2(z7.k3, k3, z7, r)
                    return r
                return z7.provision_triple_step2(displace_z7, t, Meta, k1, k2, k3)
            r = Meta(k1, k2, k3)                                                        #   r created here
            if e7 is absent:
                t.e7 = k2
                t.z7 = r = Meta(k1, k2, k3)
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            d = t.d
            if d is k3:     return t.y

            e = t.e
            if e is k3:     return t.z
            if e is absent:
                t.e  = k3
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k3:    return t.z6
            if e6 is absent:
                t.e6 = k3
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k3:    return t.z7

            r = Meta(k1, k2, k3)

            if e7 is absent:
                t.e7 = k3
                t.z7 = r
                return r

            displace(parent, k2, create_herd_many(a, b, c, d, e, e6, e7, k3, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


    class Herd_Many(Map):
        __slots__ = (())


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        if __debug__:
            def displace(t, k, v):
                assert k in t

                t[k] = v
        else:
            displace = map__store


        glimpse = map__lookup
        lookup  = map__lookup


        def inject(t, k, v):
            assert map__lookup(t, k) is none

            map__store(t, k, v)
            return t


        insert              = inject
        items_sorted_by_key = items_sorted_by_key__herd_many


        def provision(t, k, v):
            map__provide(t, k, v)
            return t


        def provision_dual(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2)))


        def provision_dual__21(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k1)) or (map__provide(t, k1, Meta(k1, k2)))


        def provision_triple(t, displace, Meta, k1, k2, k3):
            second = map__lookup(t, k2, absent)

            if second.k3 is k3:
                return second

            if not second.is_herd:
                r = Meta(k1, k2, k3)

                if second is absent:
                    return map__provide(t, k2, r)

                map__store(t, k2, create_herd_2(second.k3, k3, second, r))

                return r

            return second.provision_triple_step2(map__store, t, Meta, k1, k2, k3)


        def provision_triple_step2(t, _displace, _parent, Meta, k1, k2, k3):
            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


    empty_herd = Herd_0()


    new_Herd_1    = Method(Object.__new__, Herd_1)
    new_Herd_2    = Method(Object.__new__, Herd_2)
    new_Herd_3    = Method(Object.__new__, Herd_3)
    new_Herd_4567 = Method(Object.__new__, Herd_4567)
    new_Herd_Many = Method(Map   .__new__, Herd_Many)


    @export
    def create_herd_1(a, v):
        assert a is not absent

        t = new_Herd_1()

        t.a = a
        t.v = v

        return t


    @export
    def create_herd_2(a, b, v, w):
        assert (a is not absent) and (a is not b) and (b is not absent)

        t = new_Herd_2()

        t.a = a
        t.b = b
        t.v = v
        t.w = w

        return t


    def create_herd_3(a, b, c, v, w, x):
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert (c is not absent)

        t = new_Herd_3()

        t.a = a
        t.b = b
        t.c = c
        t.v = v
        t.w = w
        t.x = x

        return t


    @share
    def create_herd_4567(a, b, c, d, v, w, x, y):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent

        t = new_Herd_4567()

        t.a = a
        t.b = b
        t.c = c
        t.d = d
        t.e = absent
        t.v = v
        t.w = w
        t.x = x
        t.y = y

        return t


    def create_herd_many(a, b, c, d, e, e6, e7, e8, v, w, x, y, z, z6, z7, z8):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d) and (a is not e)
        assert (a is not e6) and (a is not e7) and (a is not e8)
        assert (b is not absent) and (b is not c) and (b is not d) and (b is not e) and (b is not e6)
        assert (b is not e7) and (b is not e8)
        assert (c is not absent) and (c is not d) and (c is not e) and (c is not e6) and (c is not e7)
        assert (c is not e8)
        assert (d is not absent) and (d is not e) and (d is not e6) and (d is not e7) and (d is not e8)
        assert (e is not absent) and (e is not e6) and (e is not e7) and (e is not e8)
        assert (e6 is not absent) and (e6 is not e7) and (e6 is not e8)
        assert (e7 is not absent) and (e7 is not e8)
        assert e8 is not absent

        t = new_Herd_Many()

        t[a]  = v
        t[b]  = w
        t[c]  = x
        t[d]  = y
        t[e]  = z
        t[e6] = z6
        t[e7] = z7
        t[e8] = z8

        return t


    Herd_0.provision = Herd_0.provide = Herd_0.inject = HerHerdrt = static_method(create_herd_1)

    export(
        'empty_herd',      empty_herd
    )
