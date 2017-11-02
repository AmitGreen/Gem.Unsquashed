
#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.DroveMany')
def gem():
    require_gem('Gem.Method')


    map__length  = Map.__len__
    map__provide = Map.setdefault
    map__lookup  = Map.get


    class Drove_Many(Map):
        __slots__ = ((
            'total',                #   Integer
            'values',               #   List of Any excluding Absent
            '_append',              #   Method
        ))


        def __repr__(t):
            return arrange('<Drove_Many %d, %s; %s>',
                           t.total,
                           ', '.join(portray(v)   for v in t.values),
                           '; '.join(arrange('%r : %r', k, v)   for [k, v] in t.items_sorted_by_key()))


        if __debug__:
            def provision(t, k, v):
                v__2 = map__provide(t, k, v)

                assert v is v__2

                total = map__length(t)

                if t.total == total:
                    return t

                t.total = total
                t._append(v)
                return t
        else:
            def provision(t, k, v):
                map__provide(t, k, v)

                total = map__length(t)

                if t.total == total:
                    return t

                t.total = total
                t._append(v)
                return t


        glimpse             = map__lookup
        items_sorted_by_key = items_sorted_by_key__herd_many

        def ordered_values(t):
            return Tuple(t.values)


    new_Drove_Many = Method(Map.__new__, Drove_Many)


    @share
    def create_drove_many(a, b, c, d, e, e6, e7, e8, v, w, x, y, z, z6, z7, z8):
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
        assert (v is not absent) and (w is not absent) and (x is not absent) and (y is not absent)
        assert (z is not absent) and (z6 is not absent) and (z7 is not absent) and (z8 is not absent)

        t = new_Drove_Many()

        t.total   = 8
        t.values  = values = [v, w, x, y, z, z6, z7, z8]
        t._append = values.append

        t[a]  = v
        t[b]  = w
        t[c]  = x
        t[d]  = y
        t[e]  = z
        t[e6] = z6
        t[e7] = z7
        t[e8] = z8

        return t
