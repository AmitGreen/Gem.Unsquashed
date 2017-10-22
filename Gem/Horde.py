#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Horde')
def gem():
    #
    #   Horde:
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


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    class Horde_0(Object):
        __slots__ = (())


        is_horde = true
        k2       = absent


        @static_method
        def glimpse(k):
            return none


        lookup = glimpse



    class Horde_1(Object):
        __slots__ = ((
            'a',                        #   Any
            'v',                        #   Any
        ))


        is_horde = true
        k2       = absent


        def __init__(t, a, v):
            assert a is not absent

            t.a = a
            t.v = v


        def glimpse(t, k):
            if t.a is k: return t.v

            assert k is not absent

            return none


        def inject(t, b, w):
            assert t.a != b

            return Horde_23(t.a, b, t.v, w)


        def lookup(t, k):
            if t.a == k: return t.v

            assert k is not absent

            return none


        def insert(t, b, w):
            assert t.a is not b

            return Horde_23(t.a, b, t.v, w)


        def provide(t, b, w):
            a = t.a
            if a == b: return t

            return Horde_23(a, b, t.v, w)


        def provision(t, b, w):
            a = t.a
            if a is b: return t

            return Horde_23(a, b, t.v, w)


    class Horde_23(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Absent | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Vacant | Any
        ))


        is_horde = true
        k2       = absent


        def __init__(t, a, b, v, w):
            assert (a is not b) and (a is not absent) and (b is not absent)

            t.a = a
            t.b = b
            t.c = absent
            t.v = v
            t.w = w


        def glimpse(t, k):
            if t.a is k: return t.v
            if t.b is k: return t.w

            assert k is not absent

            if t.c is k: return t.x

            return none


        def inject(t, d, y):
            assert (t.a != d) and (t.b != d) and (t.c != d)

            c = t.c

            if c is absent:
                t.c = d
                t.x = y
                return t

            r.a = t.a
            r.b = t.b
            r.c = c
            r.d = d
            t.e = absent
            r.v = t.v
            r.w = t.w
            r.x = t.x
            r.y = y

            return r


        def insert(t, d, y):
            assert (t.a is not d) and (t.b is not d) and (t.c is not d)

            c = t.c

            if c is absent:
                t.c = d
                t.x = y
                return t

            r.a = t.a
            r.b = t.b
            r.c = c
            r.d = d
            t.e = absent
            r.v = t.v
            r.w = t.w
            r.x = t.x
            r.y = y

            return r


        def iterate_items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            ka = nub(a)
            kb = nub(b)

            if c is absent:
                if ka < kb:
                    yield ((a, t.v))
                    yield ((b, t.w))
                    return

                yield ((b, t.w))
                yield ((a, t.v))
                return

            kc = nub(c)

            if ka < kb:
                if kb < kc:
                    yield ((a, t.v))
                    yield ((b, t.w))
                    yield ((c, t.x))
                    return

                if ka < kc:
                    yield ((a, t.v))
                    yield ((c, t.x))
                else:
                    yield ((c, t.x))
                    yield ((a, t.v))

                yield ((b, t.w))
                return

            if ka < kc:
                yield ((b, t.w))
                yield ((a, t.v))
                yield ((c, t.x))
                return

            if kb < kc:
                yield ((b, t.w))
                yield ((c, t.x))
            else:
                yield ((c, t.x))
                yield ((b, t.w))

            yield ((a, t.v))


        def lookup(t, k):
            if t.a == k: return t.v
            if t.b == k: return t.w

            assert k is not absent

            if t.c == k: return t.x

            return none


        def provide(t, d, y):
            a = t.a
            if a == d: return t

            b = t.b
            if b == d: return t

            c = t.c
            if c == d: return t

            assert d is not absent

            if c is absent:
                t.c = d
                t.x = y
                return t

            r = new_Horde_4567()

            r.a = a
            r.b = b
            r.c = c
            r.d = d
            t.e = absent
            r.v = t.v
            r.w = t.w
            r.x = t.x
            r.y = y

            return r


        def provision(t, d, y):
            a = t.a
            if a is d: return t

            b = t.b
            if b is d: return t

            c = t.c
            if c is d: return t

            assert d is not absent

            if c is absent:
                t.c = d
                t.x = y
                return t

            r = new_Horde_4567()

            r.a = a
            r.b = b
            r.c = c
            r.d = d
            t.e = absent
            r.v = t.v
            r.w = t.w
            r.x = t.x
            r.y = y

            return r


    class Horde_4567(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'd',                        #   Any
            'e',                        #   Absent | Any
            'e6',                       #   Absent | Vacant | Any
            'e7'                        #   Absent | Vacant | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
            'y',                        #   Any
            'z',                        #   Any
            'z6',                       #   Any
            'z7',                       #   Any
        ))


        is_horde = true
        k2       = absent


        def glimpse(t, k):
            if t.a is k:        return t.v
            if t.b is k:        return t.w
            if t.c is k:        return t.x
            if t.d is k:        return t.y

            assert k is not absent

            e = t.e
            if e is k:          return t.z
            if e is absent:     return none

            e6 = t.e6
            if e6 is k:         return t.z6
            if e6 is absent:    return none

            if t.e7 is k:       return t.z7

            return none


        def inject(t, e8, z8):
            assert (t.a != e8) and (t.b != e8) and (t.c != e8) and (t.d != e8)

            if t.e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t
            assert t.e != e8

            if t.e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t
            assert t.e6 != e8

            if t.e7 is absent:
                t.e7 = e8
                t.z7 = z8
                t.e8 = absent
                return t
            assert t.e7 != e8

            r = new_Horde_Many()

            t[a]  = t.v
            t[b]  = t.w
            t[c]  = t.x
            t[d]  = t.y
            t[e]  = t.z
            t[e6] = t.z6
            t[e7] = t.z7
            t[e8] = z8

            return r


        def insert(t, e8, z8):
            assert (t.a is not e8) and (t.b is not e8) and (t.c is not e8) and (t.d is not e8)

            if t.e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t
            assert t.e is not e8

            if t.e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t
            assert t.e6 is not e8

            if t.e7 is absent:
                t.e7 = e8
                t.z7 = z8
                t.e8 = absent
                return t
            assert t.e7 is not e8

            r = new_Horde_Many()

            t[a]  = t.v
            t[b]  = t.w
            t[c]  = t.x
            t[d]  = t.y
            t[e]  = t.z
            t[e6] = t.z6
            t[e7] = t.z7
            t[e8] = z8

            return r


        def lookup(t, k):
            if t.a == k:        return t.v
            if t.b == k:        return t.w
            if t.c == k:        return t.x
            if t.d == k:        return t.y

            assert k is not absent

            e = t.e
            if e == k:          return t.z
            if e is absent:     return none

            e6 = t.e6
            if e6 == k:         return t.z6
            if e6 is absent:    return none

            if t.e7 == k:       return t.z7

            return none


        def provide(t, e8, z8):
            a = t.a
            if a == e8: return t

            b = t.b
            if b == e8: return t

            c = t.c
            if c == e8: return t

            d = t.d
            if d == e8: return t

            assert e8 is not absent

            e = t.e
            if e == e8: return t
            if e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t

            e6 = t.e6
            if e6 == e8: return t
            if e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t

            e7 = t.e7
            if e7 == e8: return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            r = new_Horde_Many()

            t[a]  = t.v
            t[b]  = t.w
            t[c]  = t.x
            t[d]  = t.y
            t[e]  = t.z
            t[e6] = t.z6
            t[e7] = t.z7
            t[e8] = z8

            return r


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

            r = new_Horde_Many()

            t[a]  = t.v
            t[b]  = t.w
            t[c]  = t.x
            t[d]  = t.y
            t[e]  = t.z
            t[e6] = t.z6
            t[e7] = t.z7
            t[e8] = z8

            return r


    class Horde_Many(Map):
        __slots__ = (())


        is_horde = true
        k2       = absent


        glimpse = map__lookup
        lookup  = map__lookup


        def inject(t, k, v):
            assert map_lookup(k) is none

            map__store(t, k, v)
            return t


        insert = inject


        def provide(t, k, v):
            map__provide(t, k, v)
            return t


        provision = provide


    empty_horde = Horde_0()


    new_Horde_1    = Method(Object.__new__, Horde_1)
    new_Horde_23   = Method(Object.__new__, Horde_23)
    new_Horde_4567 = Method(Object.__new__, Horde_4567)
    new_Horde_Many = Method(Object.__new__, Horde_Many)


    def create_horde_1(a, v):
        assert a is not absent

        t = new_Horde_1()

        t.a = a
        t.v = v

        return t


    @export
    def create_horde_23(a, b, v, w):
        assert (a is not b) and (a is not absent) and (b is not absent)

        t = new_Horde_23()

        t.a = a
        t.b = b
        t.c = absent
        t.v = v
        t.w = w

        return t


    Horde_0.provision = Horde_0.provide = Horde_0.inject = Horde_0.insert = static_method(create_horde_1)
