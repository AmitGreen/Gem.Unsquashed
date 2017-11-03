#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Hailstone')
def gem():
    #
    #   Hailstone:
    #
    #       A frozen map, with sorted keys
    #


    map__construct = Map.__init__
    map__lookup    = Map.get


    class Hailstone_0(Object):
        __slots__ = (())
        total     = 0


        @static_method
        def glimpse(k, d):
            return d


        @static_method
        def ordered_values_0():
            return (())


    class Hailstone_1(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent
        ))


        total = 1


        def glimpse(t, k, missing):
            if t.a is k:    return t.v

            assert k is not absent

            return missing


        def ordered_values_0(t):
            yield t.v


    class Hailstone_2(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent
        ))


        total = 2


        def __init__(t, a, v, b, w):
            t.a = a
            t.v = v

            t.b = b
            t.w = w


        def glimpse(t, k, missing):
            if t.a is k:    return t.v
            if t.b is k:    return t.w

            assert k is not absent

            return missing


        def ordered_values_0(t):
            yield t.v
            yield t.w


    class Hailstone_3(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent

            'c',                        #   Any excluding Absent
            'x',                        #   Any excluding Absent
        ))


        total = 3


        def __init__(t, a, v, b, w, c, x):
            t.a = a
            t.v = v

            t.b = b
            t.w = w

            t.c = c
            t.x = x


        def glimpse(t, k, missing):
            if t.a is k:    return t.v
            if t.b is k:    return t.w
            if t.c is k:    return t.x

            assert k is not absent

            return missing


        def ordered_values_0(t):
            yield t.v
            yield t.w
            yield t.x


    class Hailstone_4(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent

            'c',                        #   Any excluding Absent
            'x',                        #   Any excluding Absent

            'd',                        #   Any excluding Absent
            'y',                        #   Any excluding Absent
        ))


        total = 4


        def __init__(t, a, v, b, w, c, x, d, y):
            t.a = a
            t.v = v

            t.b = b
            t.w = w

            t.c = c
            t.x = x

            t.d = d
            t.y = y


        def glimpse(t, k, missing):
            if t.a is k:    return t.v
            if t.b is k:    return t.w
            if t.c is k:    return t.x
            if t.d is k:    return t.y

            assert k is not absent

            return missing


        def ordered_values_0(t):
            yield t.v
            yield t.w
            yield t.x
            yield t.y


    class Hailstone_5(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent

            'c',                        #   Any excluding Absent
            'x',                        #   Any excluding Absent

            'd',                        #   Any excluding Absent
            'y',                        #   Any excluding Absent

            'e5',                       #   Any excluding Absent
            'z5',                       #   Any excluding Absent
        ))


        total = 5


        def __init__(t, a, v, b, w, c, x, d, y, e5, z5):
            t.a = a
            t.v = v

            t.b = b
            t.w = w

            t.c = c
            t.x = x

            t.d = d
            t.y = y

            t.e5 = e5
            t.z5 = z5


        def glimpse(t, k, missing):
            if t.a  is k:   return t.v
            if t.b  is k:   return t.w
            if t.c  is k:   return t.x
            if t.d  is k:   return t.y
            if t.e5 is k:   return t.e5

            assert k is not absent

            return missing


        def ordered_values_0(t):
            yield t.v
            yield t.w
            yield t.x
            yield t.y
            yield t.z5


    class Hailstone_6(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent

            'c',                        #   Any excluding Absent
            'x',                        #   Any excluding Absent

            'd',                        #   Any excluding Absent
            'y',                        #   Any excluding Absent

            'e5',                       #   Any excluding Absent
            'z5',                       #   Any excluding Absent

            'e6',                       #   Any excluding Absent
            'z6',                       #   Any excluding Absent
        ))


        total = 6


        def __init__(t, a, v, b, w, c, x, d, y, e5, z5, e6, z6):
            t.a = a
            t.v = v

            t.b = b
            t.w = w

            t.c = c
            t.x = x

            t.d = d
            t.y = y

            t.e5 = e5
            t.z5 = z5

            t.e6 = e6
            t.z6 = z6


        def glimpse(t, k, missing):
            if t.a  is k:   return t.v
            if t.b  is k:   return t.w
            if t.c  is k:   return t.x
            if t.d  is k:   return t.y
            if t.e5 is k:   return t.e5
            if t.e6 is k:   return t.e6

            assert k is not absent

            return missing


        def ordered_values(t):
            yield t.v
            yield t.w
            yield t.x
            yield t.y
            yield t.z5
            yield t.z6


    class Hailstone_7(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent

            'b',                        #   Any excluding Absent
            'w',                        #   Any excluding Absent

            'c',                        #   Any excluding Absent
            'x',                        #   Any excluding Absent

            'd',                        #   Any excluding Absent
            'y',                        #   Any excluding Absent

            'e5',                       #   Any excluding Absent
            'z5',                       #   Any excluding Absent

            'e6',                       #   Any excluding Absent
            'z6',                       #   Any excluding Absent

            'e7',                       #   Any excluding Absent
            'z7',                       #   Any excluding Absent
        ))


        total = 7


        def __init__(t, a, v, b, w, c, x, d, y, e5, z5, e6, z6, e7, z7):
            t.a = a
            t.v = v

            t.b = b
            t.w = w

            t.c = c
            t.x = x

            t.d = d
            t.y = y

            t.e5 = e5
            t.z5 = z5

            t.e6 = e6
            t.z6 = z6

            t.e7 = e7
            t.z7 = z7


        def glimpse(t, k, missing):
            if t.a  is k:   return t.v
            if t.b  is k:   return t.w
            if t.c  is k:   return t.x
            if t.d  is k:   return t.y
            if t.e5 is k:   return t.e5
            if t.e6 is k:   return t.e6
            if t.e7 is k:   return t.e7

            assert k is not absent

            return missing


        def ordered_values(t):
            yield t.v
            yield t.w
            yield t.x
            yield t.y
            yield t.z5
            yield t.z6
            yield t.z7


    class Hailstone_Many(Map):
        __slots__ = ((
            'total',                    #   Integer
            '_ordered_values',          #   Tuple of (Any excluding Absent)
        ))


        def __init__(t, mapping, ordered_values)
            assert length(mapping) == length(ordered_values)

            Map__init(t, mapping)

            t.total           = length(mapping)
            t._ordered_values = ordered_values


        glimpse = map__lookup


        def ordered_values_0(t):
            return t._ordered_values


    new_Hailstone_1 = Method(Object.__new__, Hailstone_1)
    new_Hailstone_2 = Method(Object.__new__, Hailstone_2)
    new_Hailstone_3 = Method(Object.__new__, Hailstone_3)


    def create_hailstone_1(a, v):
        assert (a is not absent) and (v is not absent)

        t = new_Hailstone_1()

        t.a = a
        t.v = v

        return t


    def create_hailstone_2(nub, a, v, b, w):
        assert (a is not absent) and (a is not b)
        assert (b is not absent)
        assert (v is not absent) and (w is not absent)

        t = new_Hailstone_1()

        if nub(a) < nub(b):
            t.a = a
            t.v = v

            t.b = b
            t.w = w
            return t

        t.a = b
        t.v = w

        t.b = a
        t.w = v
        return t


    def create_hailstone_3(nub, a, v, b, w, c, x):
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert (c is not absent)
        assert (v is not absent) and (w is not absent) and (x is not absent)

        ka = nub(a)
        kb = nub(b)
        kc = nub(c)

        t = new_Hailstone_1()

        if ka < kb:
            if kb < kc:
                t.a = a
                t.v = v

                t.b = b
                t.w = w

                t.c = c
                t.x = x
                return t

            if ka < kc:
                t.a = a
                t.v = v

                t.b = c
                t.w = x

                t.c = b
                t.x = w
                return t

            t.a = c
            t.v = x

            t.b = a
            t.w = v

            t.c = b
            t.x = w
            return t

        if ka < kc:
            t.a = b
            t.v = w

            t.b = a
            t.w = v

            t.c = c
            t.x = x
            return t

        if kb < kc:
            t.a = b
            t.v = w

            t.b = c
            t.w = x

            t.c = a
            t.x = v
            return t

        t.a = c
        t.v = x

        t.b = b
        t.w = w

        t.c = a
        t.x = v
        return t


    def create_hailstone_4(nub, a, v, b, w, c, x, d, y):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert (d is not absent)
        assert (v is not absent) and (w is not absent) and (x is not absent) and (y is not absent)

        t = new_Hailstone_1()

        keys = [a, b, c, d]
        keys.sort(key = nub)

        k = keys[0]
        if k is a:
            t.a = a
            t.v = v
        elif k is b:
            t.a = b
            t.v = w
        elif k is c:
            t.a = c
            t.v = x
        else:
            assert k is d

            t.a = d
            t.v = y

        k = keys[1]
        if k is a:
            t.b = a
            t.w = v
        elif k is b:
            t.b = b
            t.w = w
        elif k is c:
            t.b = c
            t.w = x
        else:
            assert k is d

            t.b = d
            t.w = y

        k = keys[2]
        if k is a:
            t.c = a
            t.x = v
        elif k is b:
            t.c = b
            t.x = w
        elif k is c:
            t.c = c
            t.x = x
        else:
            assert k is d

            t.c = d
            t.x = y

        k = keys[3]
        if k is a:
            t.d = a
            t.y = v
        elif k is b:
            t.d = b
            t.y = w
        elif k is c:
            t.d = c
            t.y = x
        else:
            assert k is d

            t.d = d
            t.y = y


    def create_hailstone_5(nub, a, v, b, w, c, x, d, y, e5, z5):
        assert (a  is not absent) and (a is not b ) and (a is not c ) and (a is not d ) and (a is not e5)
        assert (b  is not absent) and (b is not c ) and (b is not d ) and (b is not e5)
        assert (c  is not absent) and (c is not d ) and (c is not e5)
        assert (d  is not absent) and (d is not e5)
        assert (e5 is not absent)
        assert (v  is not absent) and (w is not absent) and (x is not absent) and (y is not absent)
        assert (z5 is not absent)

        t = new_Hailstone_1()

        keys = [a, b, c, d, e5]
        keys.sort(key = nub)

        k = keys[0]
        if k is a:
            t.a = a
            t.v = v
        elif k is b:
            t.a = b
            t.v = w
        elif k is c:
            t.a = c
            t.v = x
        elif k is d:
            t.a = d
            t.v = y
        else:
            assert k is e5

            t.a = e5
            t.v = z5

        k = keys[1]
        if k is a:
            t.b = a
            t.w = v
        elif k is b:
            t.b = b
            t.w = w
        elif k is c:
            t.b = c
            t.w = x
        elif k is d:
            t.b = d
            t.w = y
        else:
            assert k is e5

            t.b = e5
            t.w = z5

        k = keys[2]
        if k is a:
            t.c = a
            t.x = v
        elif k is b:
            t.c = b
            t.x = w
        elif k is c:
            t.c = c
            t.x = x
        elif k is d:
            t.c = d
            t.x = y
        else:
            assert k is e5

            t.c = e5
            t.x = z5

        k = keys[3]
        if k is a:
            t.d = a
            t.y = v
        elif k is b:
            t.d = b
            t.y = w
        elif k is c:
            t.d = c
            t.y = x
        elif k is d:
            t.d = d
            t.y = y
        else:
            assert k is e5

            t.d = e5
            t.y = z5

        k = keys[4]
        if k is a:
            t.e5 = a
            t.z5 = v
        elif k is b:
            t.e5 = b
            t.z5 = w
        elif k is c:
            t.e5 = c
            t.z5 = x
        elif k is d:
            t.e5 = d
            t.z5 = y
        else:
            assert k is e5

            t.e5 = e5
            t.z5 = z5


    def create_hailstone_6(nub, a, v, b, w, c, x, d, y, e5, z5, e6, z6):
        assert (a  is not absent) and (a  is not b ) and (a is not c ) and (a is not d ) and (a is not e5)
        assert (a  is not e6)
        assert (b  is not absent) and (b  is not c ) and (b is not d ) and (b is not e5) and (b is not e6)
        assert (c  is not absent) and (c  is not d ) and (c is not e5) and (c is not e6)
        assert (d  is not absent) and (d  is not e5) and (d is not e6)
        assert (e5 is not absent) and (e5 is not e6)
        assert (e6 is not absent)
        assert (v  is not absent) and (w  is not absent) and (x is not absent) and (y is not absent)
        assert (z5 is not absent) and (z6 is not absent)

        t = new_Hailstone_1()

        keys = [a, b, c, d, e5, e6]
        keys.sort(key = nub)

        k = keys[0]
        if k is a:
            t.a = a
            t.v = v
        elif k is b:
            t.a = b
            t.v = w
        elif k is c:
            t.a = c
            t.v = x
        elif k is d:
            t.a = d
            t.v = y
        elif k is e5:
            t.a = e5
            t.v = z5
        else:
            assert k is e6

            t.a = e6
            t.v = z6

        k = keys[1]
        if k is a:
            t.b = a
            t.w = v
        elif k is b:
            t.b = b
            t.w = w
        elif k is c:
            t.b = c
            t.w = x
        elif k is d:
            t.b = d
            t.w = y
        elif k is e5:
            t.b = e5
            t.w = z5
        else:
            assert k is e6

            t.b = e6
            t.w = z6

        k = keys[2]
        if k is a:
            t.c = a
            t.x = v
        elif k is b:
            t.c = b
            t.x = w
        elif k is c:
            t.c = c
            t.x = x
        elif k is d:
            t.c = d
            t.x = y
        elif k is e5:
            t.c = e5
            t.x = z5
        else:
            assert k is e6

            t.c = e6
            t.x = z6

        k = keys[3]
        if k is a:
            t.d = a
            t.y = v
        elif k is b:
            t.d = b
            t.y = w
        elif k is c:
            t.d = c
            t.y = x
        elif k is d:
            t.d = d
            t.y = y
        elif k is e5:
            t.d = e5
            t.y = z5
        else:
            assert k is e6

            t.d = e6
            t.y = z6

        k = keys[4]
        if k is a:
            t.e5 = a
            t.z5 = v
        elif k is b:
            t.e5 = b
            t.z5 = w
        elif k is c:
            t.e5 = c
            t.z5 = x
        elif k is d:
            t.e5 = d
            t.z5 = y
        elif k is e5:
            t.e5 = e5
            t.z5 = z5
        else:
            assert k is e6

            t.e5 = e6
            t.z5 = z6

        k = keys[5]
        if k is a:
            t.e6 = a
            t.z6 = v
        elif k is b:
            t.e6 = b
            t.z6 = w
        elif k is c:
            t.e6 = c
            t.z6 = x
        elif k is d:
            t.e6 = d
            t.z6 = y
        elif k is e5:
            t.e6 = e5
            t.z6 = z5
        else:
            assert k is e6

            t.e6 = e6
            t.z6 = z6


    def create_hailstone_7(nub, a, v, b, w, c, x, d, y, e5, z5, e6, z6, e7, z7):
        assert (a  is not absent) and (a  is not b ) and (a  is not c ) and (a is not d ) and (a is not e5)
        assert                        (a  is not e6) and (a  is not e7)
        assert (b  is not absent) and (b  is not c ) and (b  is not d ) and (b is not e5) and (b is not e6)
        assert                        (b  is not e7)
        assert (c  is not absent) and (c  is not d ) and (c  is not e5) and (c is not e6) and (c is not e7)
        assert (d  is not absent) and (d  is not e5) and (d  is not e6) and (d is not e7)
        assert (e5 is not absent) and (e5 is not e6) and (e5 is not e7)
        assert (e6 is not absent) and (e6 is not e7)
        assert (e7 is not absent)
        assert (v  is not absent) and (w  is not absent) and (x  is not absent) and (y is not absent)
        assert (z5 is not absent) and (z6 is not absent) and (z7 is not absent)

        t = new_Hailstone_1()

        keys = [a, b, c, d, e5, e6, e7]
        keys.sort(key = nub)

        k = keys[0]
        if k is a:
            t.a = a
            t.v = v
        elif k is b:
            t.a = b
            t.v = w
        elif k is c:
            t.a = c
            t.v = x
        elif k is d:
            t.a = d
            t.v = y
        elif k is e5:
            t.a = e5
            t.v = z5
        elif k is e6:
            t.a = e6
            t.v = z6
        else:
            assert k is e7

            t.a = e7
            t.v = z7

        k = keys[1]
        if k is a:
            t.b = a
            t.w = v
        elif k is b:
            t.b = b
            t.w = w
        elif k is c:
            t.b = c
            t.w = x
        elif k is d:
            t.b = d
            t.w = y
        elif k is e5:
            t.b = e5
            t.w = z5
        elif k is e6:
            t.b = e6
            t.w = z6
        else:
            assert k is e7

            t.b = e7
            t.w = z7

        k = keys[2]
        if k is a:
            t.c = a
            t.x = v
        elif k is b:
            t.c = b
            t.x = w
        elif k is c:
            t.c = c
            t.x = x
        elif k is d:
            t.c = d
            t.x = y
        elif k is e5:
            t.c = e5
            t.x = z5
        elif k is e6:
            t.c = e6
            t.x = z6
        else:
            assert k is e7

            t.c = e7
            t.x = z7

        k = keys[3]
        if k is a:
            t.d = a
            t.y = v
        elif k is b:
            t.d = b
            t.y = w
        elif k is c:
            t.d = c
            t.y = x
        elif k is d:
            t.d = d
            t.y = y
        elif k is e5:
            t.d = e5
            t.y = z5
        elif k is e6:
            t.d = e6
            t.y = z6
        else:
            assert k is e7

            t.d = e7
            t.y = z7

        k = keys[4]
        if k is a:
            t.e5 = a
            t.z5 = v
        elif k is b:
            t.e5 = b
            t.z5 = w
        elif k is c:
            t.e5 = c
            t.z5 = x
        elif k is d:
            t.e5 = d
            t.z5 = y
        elif k is e5:
            t.e5 = e5
            t.z5 = z5
        elif k is e6:
            t.e5 = e6
            t.z5 = z6
        else:
            assert k is e7

            t.e5 = e7
            t.z5 = z7

        k = keys[5]
        if k is a:
            t.e6 = a
            t.z6 = v
        elif k is b:
            t.e6 = b
            t.z6 = w
        elif k is c:
            t.e6 = c
            t.z6 = x
        elif k is d:
            t.e6 = d
            t.z6 = y
        elif k is e5:
            t.e6 = e5
            t.z6 = z5
        elif k is e6:
            t.e6 = e6
            t.z6 = z6
        else:
            assert k is e7

            t.e6 = e7
            t.z6 = z7

        k = keys[6]
        if k is a:
            t.e7 = a
            t.z7 = v
        elif k is b:
            t.e7 = b
            t.z7 = w
        elif k is c:
            t.e7 = c
            t.z7 = x
        elif k is d:
            t.e7 = d
            t.z7 = y
        elif k is e5:
            t.e7 = e5
            t.z7 = z5
        elif k is e6:
            t.e7 = e6
            t.z7 = z6
        else:
            assert k is e7

            t.e7 = e7
            t.z7 = z7


    def create_hailstone_many(nub, mapping):
        keys = List(mapping)
        keys.sort(key = nub)

        value = mapping.__getitem__

        t = new_Hailstone_Many()

        map__construct(t, mapping)

        t.total           = length(t)
        t._ordered_values = Tuple(value(k)   for k in keys)

        return t
