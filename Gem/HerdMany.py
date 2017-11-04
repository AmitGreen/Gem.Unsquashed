#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.HerdMany')
def gem():
    require_gem('Gem.DroveMany')


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    class Herd_Many(Map):
        __slots__ = (())


        herd_estimate = 8
        is_herd_many  = true
        is_herd       = true
        is_horde      = false
        k1            = absent
        k2            = absent
        k3            = absent
        k4            = absent
        skip          = 0


        def __repr__(t):
            return arrange('<Herd_Many %s>', '; '.join(arrange('%r : %r', k, v)   for [k, v] in t.items_sorted_by_key()))


        count_nested = count_nested__map
        disperse     = disperse__herd_many


        if __debug__:
            def displace(t, k, v):
                assert (k in t) and (v is not absent)

                t[k] = v
        else:
            displace = map__store


        def distribute_dual(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2)))


        def distribute_dual__21(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k1)) or (map__provide(t, k1, Meta(k1, k2)))


        def distribute_triple(t, displace, Meta, k1, k2, k3):
            second = map__lookup(t, k2, absent)

            if second.k3 is k3:
                return second

            if not second.is_herd:
                r = Meta(k1, k2, k3)

                if second is absent:
                    return map__provide(t, k2, r)

                map__store(t, k2, create_herd_2(second.k3, k3, second, r))

                return r

            return second.distribute_triple_step2(map__store, t, Meta, k1, k2, k3)


        def distribute_triple__312(t, displace, Meta, k1, k2, k3):
            second = map__lookup(t, k1, absent)

            if second.k2 is k2:
                return second

            if not second.is_herd:
                r = Meta(k1, k2, k3)

                if second is absent:
                    return map__provide(t, k1, r)

                map__store(t, k1, create_herd_2(second.k2, k2, second, r))

                return r

            return second.distribute_triple_step2__312(map__store, t, Meta, k1, k2, k3)


        def distribute_triple_step2(t, _displace, _parent, Meta, k1, k2, k3):
            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def distribute_triple_step2__312(t, _displace, _parent, Meta, k1, k2, k3):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))


        if is_python_2:
            @property
            def first(t):
                #assert 0   -- Untested

                return t.itervalues().next()
        else:
            @property
            def first(t):
                #assert 0   -- Untested

                return iterate(t.values()).__next__()


        glimpse = map__lookup
        lookup  = map__lookup


        def inject(t, k, v):
            assert (map__lookup(t, k) is none) and (k is not absent) and (v is not absent)

            map__store(t, k, v)
            return t


        insert              = inject
        items_sorted_by_key = items_sorted_by_key__herd_many


        def scrub(t):
            append_remove = 0
            value         = t.__getitem__
            store         = t.__setitem__

            for k in t.keys():
                v       = value(k)
                v_scrub = v.scrub

                if v_scrub is 0:
                    if reference_count(v) is not 3:
                        continue

                    if append_remove is 0:
                        remove_many = [k]
                        append_remove = remove_many.append
                        continue

                    append_remove(k)
                    continue

                v = v_scrub()

                if v is 0:
                    if append_remove is 0:
                        remove_many = [k]
                        append_remove = remove_many.append
                        continue

                    append_remove(k)
                    continue

                store(k, v)

            if append_remove is 0:
                return t

            if length(remove_many) == length(t):
                t.clear()
                return 0

            zap = t.__delitem__

            for v in remove_many:
                zap(v)

            if length(t) is 1:
                if is_python_2:
                    v = t.itervalues().next()
                else:
                    v = iterate(t.values()).__next__()

                v_increment = v.increment_skip
                return (v   if v_increment is 0 else    v_increment())

            return t


    new_Herd_Many = Method(Map   .__new__, Herd_Many)


    @share
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
        assert (v is not absent) and (w is not absent) and (x is not absent) and (y is not absent)
        assert (z is not absent) and (z6 is not absent) and (z7 is not absent) and (z8 is not absent)

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
