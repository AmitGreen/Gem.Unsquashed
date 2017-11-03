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


    map__lookup = Map.get


    class Hailstone_0(Object):
        __slots__ = (())
        total     = 0


        @static_method
        def glimpse(k, d):
            return d


        @static_method
        def ordered_values():
            return (())


    class Hailstone_1(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'v',                        #   Any excluding Absent
        ))


        total = 1


        def __init__(t, a, v):
            t.a = a
            t.v = v


        def glimpse(t, k, missing):
            if t.a is k:    return t.v

            assert k is not absent

            return missing


        @static_method
        def ordered_values():
            return (( t.v, ))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w, t.x))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w, t.x, t.y))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w, t.x, t.y, t.z5))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w, t.x, t.y, t.z5, t.z6))


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


        @static_method
        def ordered_values():
            return ((t.v, t.w, t.x, t.y, t.z5, t.z6, t.z7))


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


        def ordered_values(t):
            return t._ordered_values
