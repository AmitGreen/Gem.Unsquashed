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


    def increment_skip__horde_many(t):
        assert t.skip is 0

        t.skip += 1

        return t


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


        def count_nested(t):
            v = t.v
            w = t.w

            if t.c is absent:
                if v.is_herd:
                    if w.is_herd:
                        return v.count_nested() + w.count_nested()

                    return v.count_nested() + 1

                if w.is_herd:
                    return 1 + w.count_nested()

                return 2

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


        increment_skip = increment_skip__horde_many


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

            displace(k1, create_horde_4(1, a, b, c, k3, v, t.w, t.x, r))

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

            displace(k3, create_horde_4(1, a, b, c, k2, v, t.w, t.x, r))

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

            if parent.is_herd_many:
                displace(parent, k2, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))
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

            if parent.is_herd_many:
                displace(parent, k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))
            return r


        def scrub(t):
            v       = t.v
            v_scrub = v.scrub
            if v_scrub is 0:
                if reference_count(v) is 3:
                    v = 0
            else:
                v = v_scrub()

            w       = t.w
            w_scrub = w.scrub
            if w_scrub is 0:
                if reference_count(w) is 3:
                    w = 0
            else:
                w = w_scrub()

            if t.c is absent:
                if v is 0:
                    if w is 0:
                        return 0

                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment())

                if w is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                t.v = v
                t.w = w
                return t

            x       = t.x
            x_scrub = x.scrub
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

                #
                #   scrub .a/.v
                #
                t.a = t.b
                t.v = w

                t.b = t.c
                t.w = x

                t.c = absent
                del t.x
                return t

            if w is 0:
                if x is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                #
                #   scrub .b/.w
                #
                t.v = v

                t.b = t.c
                t.w = x

                t.c = absent
                del t.x
                return t

            if x is 0:
                #
                #   scrub .c/.x
                #
                t.v = v

                t.w = w

                t.c = absent
                del t.x
                return t

            t.v = v
            t.w = w
            t.x = x
            return t


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


        count_nested        = count_nested__map
        increment_skip      = increment_skip__horde_many
        items_sorted_by_key = items_sorted_by_key__herd_many
        provision           = provision__herd_many


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


        def scrub(t):
            append_remove = 0
            value         = t.__getitem__
            store         = t.__setitem__
            
            #
            #   Need to delete t.sample, for reference counting purposes
            #
            del t.sample

            for k in t.keys():
                v       = value(k)
                v_scrub = v.scrub

                if v_scrub is 0:
                    if reference_count(v) is not 3:
                        sample = v
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

                sample = v
                store(k, v)

            if append_remove is 0:
                t.sample = sample
                return t

            if length(remove_many) == length(t):
                return 0

            zap = t.__delitem__

            for k in remove_many:
                zap(k)

            if length(t) is 1:
                if is_python_2:
                    v = t.itervalues().next()
                else:
                    v = iterate(t.values()).__next__()

                v_increment = v.increment_skip
                return (v   if v_increment is 0 else    v_increment())

            #
            #   Restore a sample
            #
            t.sample = sample
            return t


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


    @share
    def create_horde_3(skip, a, b, c, v, w, x):
        assert skip is 1
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert (c is not absent)

        t = new_Horde_23()

        t.skip = skip
        t.a    = a
        t.b    = b
        t.c    = c
        t.v    = v
        t.w    = w
        t.x    = x

        return t


    @share
    def create_horde_4(skip, a, b, c, d, v, w, x, y):
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
