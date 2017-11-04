#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd_4567')
def gem():
    #require_gem('Gem.HerdMany')


    def item_0(pair):
        return pair[0]


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
            y = t.y

            if t.e is absent:
                return (
                             (v.count_nested()   if v.is_herd else   1)
                           + (w.count_nested()   if w.is_herd else   1)
                           + (x.count_nested()   if x.is_herd else   1)
                           + (y.count_nested()   if y.is_herd else   1)
                       )

            z = t.z

            if t.e6 is absent:
                return (
                             (v.count_nested()   if v.is_herd else   1)
                           + (w.count_nested()   if w.is_herd else   1)
                           + (x.count_nested()   if x.is_herd else   1)
                           + (y.count_nested()   if y.is_herd else   1)
                           + (z.count_nested()   if z.is_herd else   1)
                       )


            z6 = t.z6

            if t.e7 is absent:
                return (
                             (v .count_nested()   if v .is_herd else   1)
                           + (w .count_nested()   if w .is_herd else   1)
                           + (x .count_nested()   if x .is_herd else   1)
                           + (y .count_nested()   if y .is_herd else   1)
                           + (z .count_nested()   if z .is_herd else   1)
                           + (z6.count_nested()   if z6.is_herd else   1)
                       )

            z7 = t.z7

            return (
                         (v .count_nested()   if v .is_herd else   1)
                       + (w .count_nested()   if w .is_herd else   1)
                       + (x .count_nested()   if x .is_herd else   1)
                       + (y .count_nested()   if y .is_herd else   1)
                       + (z .count_nested()   if z .is_herd else   1)
                       + (z6.count_nested()   if z6.is_herd else   1)
                       + (z7.count_nested()   if z7.is_herd else   1)
                   )


        def disperse(t, e8, z8):
            if (t.a is e8) or (t.b is e8) or (t.c is e8) or (t.d is e8):
                return t

            assert (e8 is not absent) and (z8 is not absent)

            e = t.e
            if e is e8:
                return t
            if e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t

            e6 = t.e6
            if e6 is e8:
                return t
            if e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t

            e7 = t.e7
            if e7 is e8:
                return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            return create_herd_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def displace(t, k, v):
            assert v is not absent

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

            assert k is not absent

            if t.e is k:
                t.z = v
                return

            if t.e6 is k:
                t.z6 = v
                return

            assert t.e7 is k

            t.z7 = v


        def distribute_dual(t, displace, Meta, k1, k2):
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
                t.z7 = r
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def distribute_dual__21(t, displace, Meta, k1, k2):
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
                t.z7 = r
                return r

            displace(k2, create_herd_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

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
                return v.distribute_triple_step2(displace_4v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w
                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r
                return w.distribute_triple_step2(displace_4w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x
                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r
                return x.distribute_triple_step2(displace_4x, t, Meta, k1, k2, k3)

            d = t.d
            if d is k2:
                y = t.y
                if y.k3 is k3:  return y
                if not y.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.y = create_herd_2(y.k3, k3, y, r)
                    return r
                return y.distribute_triple_step2(displace_4y, t, Meta, k1, k2, k3)

            e = t.e
            if e is k2:
                z = t.z
                if z.k3 is k3:  return z
                if not z.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.z = create_herd_2(z.k3, k3, z, r)
                    return r
                return z.distribute_triple_step2(displace_4z, t, Meta, k1, k2, k3)
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
                return z6.distribute_triple_step2(displace_4z6, t, Meta, k1, k2, k3)
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
                return z7.distribute_triple_step2(displace_4z7, t, Meta, k1, k2, k3)
            r = Meta(k1, k2, k3)                                                        #   r created here
            if e7 is absent:
                t.e7 = k2
                t.z7 = r
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

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
                return v.distribute_triple_step2__312(displace_4v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w
                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r
                return w.distribute_triple_step2__312(displace_4w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k1:
                x = t.x
                if x.k2 is k2:  return x
                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k2, k2, x, r)
                    return r
                return x.distribute_triple_step2__312(displace_4x, t, Meta, k1, k2, k3)

            d = t.d
            if d is k1:
                y = t.y
                if y.k2 is k2:  return y
                if not y.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.y = create_herd_2(y.k2, k2, y, r)
                    return r
                return y.distribute_triple_step2__312(displace_4y, t, Meta, k1, k2, k3)

            e = t.e
            if e is k1:
                z = t.z
                if z.k2 is k2:  return z
                if not z.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.z = create_herd_2(z.k2, k2, z, r)
                    return r
                return z.distribute_triple_step2__312(displace_4z, t, Meta, k1, k2, k3)
            if e is absent:
                t.e  = k1
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k1:
                z6 = t.z6
                if z6.k2 is k2:  return z6
                if not z6.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z6 = create_herd_2(z6.k2, k2, z6, r)
                    return r
                return z6.distribute_triple_step2__312(displace_4z6, t, Meta, k1, k2, k3)
            if e6 is absent:
                t.e6 = k1
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k1:
                z7 = t.z7
                if z7.k2 is k2:  return z7
                if not z7.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z7 = create_herd_2(z7.k2, k2, z7, r)
                    return r
                return z7.distribute_triple_step2__312(displace_4z7, t, Meta, k1, k2, k3)
            r = Meta(k1, k2, k3)                                                        #   r created here
            if e7 is absent:
                t.e7 = k1
                t.z7 = r
                return r

            displace(k3, create_herd_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def distribute_triple_step2(t, displace, parent, Meta, k1, k2, k3):
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

            if parent.is_herd_many:
                displace(
                    parent,
                    k2,
                    create_herd_many(a, b, c, d, e, e6, e7, k3, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r),
                )

                return r

            displace(parent, create_herd_many(a, b, c, d, e, e6, e7, k3, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))
            return r


        def distribute_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
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
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k2:    return t.z6
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k2:    return t.z7

            r = Meta(k1, k2, k3)

            if e7 is absent:
                t.e7 = k2
                t.z7 = r
                return r

            if parent.is_herd_many:
                displace(
                    parent,
                    k1,
                    create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r),
                )

                return r

            displace(parent, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))
            return r


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


        def increment_skip(t, skip = 1):
            assert 1 <= skip <= 2

            r = create_horde_4(skip, t.a, t.b, t.c, t.d, t.v, t.w, t.x, t.y)

            if t.e is absent:
                return r

            if t.e is not absent:
                r = r.disperse(t.e, t.z)

                if t.e6 is not absent:
                    r = r.disperse(t.e6, t.z6)

                    if t.e7 is not absent:
                        return r.disperse(t.e7, t.z7)

            return r


        def insert(t, e8, z8):
            assert (t.a is not e8) and (t.b is not e8) and (t.c is not e8) and (t.d is not e8)
            assert (e8 is not absent) and (z8 is not absent)

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


        def install(t, e8, z8):
            assert (e8 is not absent) and (z8 is not absent)

            if t.a is e8:
                t.v = z8
                return t

            if t.b is e8:
                t.w = z8
                return t

            if t.c is e8:
                t.x = z8
                return t

            if t.d is e8:
                t.y = z8
                return t

            e = t.e
            if e is e8:
                t.z = z8
                return t
            if e is absent:
                t.e  = e8
                t.e6 = absent
                t.z  = z8
                return t

            e6 = t.e6
            if e6 is e8:
                t.z6 = z8
                return t
            if e6 is absent:
                t.e6 = e8
                t.e7 = absent
                t.z6 = z8
                return t

            e7 = t.e7
            if e7 is e8:
                t.z7 = z8
                return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            return create_drove_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def items_sorted_by_key(t):
            a = t.a
            e = t.e

            if e is absent:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]
            else:
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


            nub = (0   if type(a) is Integer else   a.nub)

            if nub is 0:
                r.sort(key = item_0)

                return r


            def nub_of_item_0(pair):
                return nub(pair[0])


            r.sort(key = nub_of_item_0)

            return r


        def ordered_values(t):
            if t.e is absent:
                return ((t.v, t.w, t.x, t.y))

            if t.e6 is absent:
                return ((t.v, t.w, t.x, t.y, t.z))

            if t.e7 is absent:
                return ((t.v, t.w, t.x, t.y, t.z, t.z6))

            return ((t.v, t.w, t.x, t.y, t.z, t.z6, t.z7))


        def provision(t, e8, z8):
            a = t.a
            if a is e8: return t

            b = t.b
            if b is e8: return t

            c = t.c
            if c is e8: return t

            d = t.d
            if d is e8: return t

            assert (e8 is not absent) and (z8 is not absent)

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

            return create_drove_many(a, b, c, d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def scrub(t):
            v = t.v
            w = t.w
            x = t.x
            y = t.y

            v_scrub = v.scrub
            w_scrub = w.scrub
            x_scrub = x.scrub
            y_scrub = y.scrub

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

            if y_scrub is 0:
                if reference_count(y) is 3:
                    y = 0
            else:
                y = y_scrub()

            #if 7 is 7:
            #    my_line('v,w,x,y: %r,%r,%r,%r', v, w, x, y)
            #    if t.e is not absent:
            #        my_line('z:%r', t.z)
            #        if t.e6 is not absent:
            #            my_line('z6:%r', t.z6)
            #            if t.e7 is not absent:
            #                my_line('z7:%r', t.z7)

            if t.e is absent:
                if v is 0:
                    if w is 0:
                        if x is 0:
                            if y is 0:
                                #my_line('0')
                                return 0

                            #my_line('y')
                            y_increment = y.increment_skip
                            return (y   if y_increment is 0 else    y_increment())

                        if y is 0:
                            #my_line('x')
                            x_increment = x.increment_skip
                            return (x   if x_increment is 0 else    x_increment())

                        #my_line('c/x,d/y')
                        return create_herd_2(t.c, t.d, x, y)

                    if x is 0:
                        if y is 0:
                            #my_line('w')
                            w_increment = w.increment_skip
                            return (w   if w_increment is 0 else    w_increment())

                        #my_line('b/w,d/y')
                        return create_herd_2(t.b, t.d, w, y)

                    if y is 0:
                        #my_line('b/w,c/x')
                        return create_herd_2(t.b, t.c, w, x)

                    #my_line('b/w,c/x,d/y')
                    return create_herd_3(t.b, t.c, t.d, w, x, y)

                if w is 0:
                    if x is 0:
                        if y is 0:
                            #my_line('v')
                            v_increment = v.increment_skip
                            return (v   if v_increment is 0 else    v_increment())

                        #my_line('a/v,d/y')
                        return create_herd_2(t.a, t.d, v, y)

                    if y is 0:
                        #my_line('a/v,c/x')
                        return create_herd_2(t.a, t.c, v, x)

                    #my_line('a/v,c/x,d/y')
                    return create_herd_3(t.a, t.c, t.d, v, x, y)

                if x is 0:
                    if y is 0:
                        #my_line('a/v,b/w')
                        return create_herd_2(t.a, t.b, v, w)

                    #my_line('a/v,b/y,d/y')
                    return create_herd_3(t.a, t.b, t.d, v, w, y)

                if y is 0:
                    #my_line('a/v,b/y,c/x')
                    return create_herd_3(t.a, t.b, t.c, v, w, x)

                #my_line('t')
                t.v = v
                t.w = w
                t.x = x
                t.y = y
                return t

            z       = t.z
            z_scrub = z.scrub

            if z_scrub is 0:
                if reference_count(z) is 3:
                    z = 0
            else:
                z = z_scrub()

            #if 7 is 7:
            #    my_line('v,w,x,y,z: %r,%r,%r,%r,%r', v, w, x, y, z)
            #    if t.e6 is not absent:
            #        my_line('z6:%r', t.z6)
            #        if t.e7 is not absent:
            #            my_line('z7:%r', t.z7)

            #   a/v:    unknown
            if v is 0:
                #
                #   This should be:
                #
                #       index = 0
                #
                #   However, instead the code that should be below:
                #
                #       if index is 0:
                #           if w is not 0:
                #               a     = t.b
                #               v     = w
                #               index = 1
                #
                #   is inline'd into here and then rewritten as:
                #
                #       if w is 0:
                #           index = 0
                #       else:
                #           a     = t.b
                #           v     = w
                #           index = 1
                #
                if w is 0:
                    index = 0
                else:
                    a     = t.b
                    v     = w
                    index = 1
            else:
                #   .a/.v:    keep
                #   .b/.w:    unknown
                if w is 0:
                    a     = t.a
                    index = 1
                else:
                    #   .a/.v:    keep
                    #   .b/.w:    keep
                    #   .c/.x:    unknown
                    if x is 0:
                        #my_line('a=a;b=b;x:0;index=2; %r:%r & %r:%r', t.a, v, t.b, w)
                        a     = t.a
                        b     = t.b
                        index = 2
                    else:
                        #   .a/.v:    keep
                        #   .b/.w:    keep
                        #   .c/.x:    keep
                        #   .d/.y:    unknown
                        if y is 0:
                            #my_line('a=a;b=b;c=c;y:0;index=3; %r:%r; %r:%r; %r:%r', t.a, v, t.b, w, t.c, x)
                            a     = t.a
                            b     = t.b
                            c     = t.c
                            index = 3
                        else:
                            #   .a/.v:    keep
                            #   .b/.w:    keep
                            #   .c/.x:    keep
                            #   .d/.y:    keep
                            #   .e/.z:    unknown
                            if z is 0:
                                a     = t.a
                                b     = t.b
                                c     = t.c
                                d     = t.d
                                index = 4
                            else:
                                e6 = t.e6
                                if e6 is absent:
                                    t.v = v
                                    t.w = w
                                    t.x = x
                                    t.y = y
                                    t.z = z
                                    return t

                                #   .a /.v :  keep
                                #   .b /.w :  keep
                                #   .c /.x :  keep
                                #   .d /.y :  keep
                                #   .e /.z :  keep
                                #   .e6/.z6:  unknown
                                z6       = t.z6
                                z6_scrub = z6.scrub

                                if z6_scrub is 0:
                                    if reference_count(z6) is 3:
                                        z6 = 0
                                else:
                                    z6 = z6_scrub()

                                if z6 is 0:
                                    a     = t.a
                                    b     = t.b
                                    c     = t.c
                                    d     = t.d
                                    e     = t.e
                                    index = 5
                                else:
                                    t.v  = v
                                    t.w  = w
                                    t.x  = x
                                    t.y  = y
                                    t.z  = z
                                    t.z6 = z6

                                    if t.e7 is absent:
                                        return t

                                    #   .a /.v :  keep
                                    #   .b /.w :  keep
                                    #   .c /.x :  keep
                                    #   .d /.y :  keep
                                    #   .e /.z :  keep
                                    #   .e6/.z6:  keep
                                    #   .e7/.z7:  unknown
                                    z7       = t.z7
                                    z7_scrub = z7.scrub

                                    if z7_scrub is 0:
                                        if reference_count(z7) is 3:
                                            z7 = 0
                                    else:
                                        z7 = z7_scrub()

                                    if z7 is 0:
                                        t.e7 = absent
                                        del t.z7
                                        return t

                                    t.z7 = z7
                                    return t

            #
            #   At this point:
            #
            #       index is 0:
            #               Ignore .a/.v
            #               Ignore .b/.w
            #               Examination from .c/.x
            #
            #       index is 1
            #               keep either   .a/v or .b/w
            #               ignore either .a/v or .b/w
            #               Examination from .c/.x
            #
            #       index is 2:
            #               keep   .a/.v
            #               keep   .b/.w
            #               ignore .c/.x
            #               Examination from .d/.y
            #
            #       index is 3:
            #               keep   .a/.v
            #               keep   .b/.w
            #               keep   .c/.x
            #               ignore .d/.y
            #               Examination from .e/.z
            #
            #       index is 4:
            #               keep   .a/.v
            #               keep   .b/.w
            #               keep   .c/.x
            #               keep   .d/.y
            #               ignore .e/.z
            #               Examination from .e6/.z6
            #
            #       index is 5:
            #               keep   .a /.v
            #               keep   .b /.w
            #               keep   .c /.x
            #               keep   .d /.y
            #               keep   .e /.z
            #               ignore .e6/.z6
            #               Examination from .e7/.z7
            #

            #
            #   .a/.v:  keep or scrub
            #   .b/.w:  unknown (unless index >= 1)
            #
            #   The following is done above (see comments there):
            #
            #       if index is 0:
            #           if w is not 0:
            #               a     = t.b
            #               v     = w
            #               index = 1
            #

            #   .a/.v:  keep or scrub
            #   .v/.w:  keep or scrub
            #   .c/.x:  unknown (unless index >= 2)
            if index is 0:
                if x is not 0:
                    a     = t.c
                    v     = x
                    index = 1
            elif index is 1:
                if x is not 0:
                    b     = t.c
                    w     = x
                    index = 2


            #   .a/.v:  keep or scrub
            #   .v/.w:  keep or scrub
            #   .c/.x:  keep or scrub
            #   .d/.y:  unknown (unless index >= 3)
            if index is 0:
                if y is not 0:
                    a     = t.d
                    v     = y
                    index = 1
            elif index is 1:
                if y is not 0:
                    b     = t.d
                    w     = y
                    index = 2
            elif index is 2:
                if y is not 0:
                    c     = t.d
                    x     = y
                    index = 3

                    #my_line('c=d;x=y;index=3; %r:%r', c, x)

            #   .a/.v:  keep or scrub
            #   .v/.w:  keep or scrub
            #   .c/.x:  keep or scrub
            #   .d/.y:  keep or scrub
            #   .e/.z:  unknown (unless index >= 4)
            if index is 0:
                if z is not 0:
                    a     = t.e
                    v     = z
                    index = 1
            elif index is 1:
                if z is not 0:
                    b     = t.e
                    w     = z
                    index = 2
            elif index is 2:
                if z is not 0:
                    c     = t.e
                    x     = z
                    index = 3
            elif index is 3:
                if z is not 0:
                    d     = t.e
                    y     = z
                    index = 4
                #else:
                #    my_line('z:0;index:3')

            #   .a /.v :    keep or scrub
            #   .v /.w :    keep or scrub
            #   .c /.x :    keep or scrub
            #   .d /.y :    keep or scrub
            #   .e /.z :    keep or scrub
            #   .e6/.z6:    unknown (unless index is 5)
            if index is 5:
                assert t.e6 is not absent
            else:
                if t.e6 is absent:
                    if index is 0:
                        return 0

                    if index is 1:
                        v_increment = v.increment_skip
                        return (v   if v_increment is 0 else    v_increment())

                    if index is 2:
                        return create_herd_2(a, b, v, w)

                    if index is 3:
                        return create_herd_3(a, b, c, v, w, x)

                    assert index is 4

                    t.a = a
                    t.b = b
                    t.c = c
                    t.d = d

                    t.v = v
                    t.w = w
                    t.x = x
                    t.y = y

                    t.e = absent
                    del t.z

                    return t

                z6       = t.z6
                z6_scrub = z6.scrub

                if z6_scrub is 0:
                    if reference_count(z6) is 3:
                        z6 = 0
                else:
                    z6 = z6_scrub()

                if index is 0:
                    if z6 is not 0:
                        a     = t.e6
                        v     = z6
                        index = 1
                elif index is 1:
                    if z6 is not 0:
                        b     = t.e6
                        w     = z6
                        index = 2
                elif index is 2:
                    if z6 is not 0:
                        c     = t.e6
                        x     = z6
                        index = 3
                elif index is 3:
                    if z6 is not 0:
                        d     = t.e6
                        y     = z6
                        index = 4
                    #else:
                    #    my_line('z6:0;index:3')
                else:
                    assert index is 4

                    if z6 is not 0:
                        e     = t.e6
                        z     = z6
                        index = 5

            #   .a /.v :    keep or scrub
            #   .v /.w :    keep or scrub
            #   .c /.x :    keep or scrub
            #   .d /.y :    keep or scrub
            #   .e /.z :    keep or scrub
            #   .e6/.z6:    keep or scrub
            #   .e7/.z7:    unknown
            if t.e7 is absent:
                if index is 0:
                    return 0

                if index is 1:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                if index is 2:
                    return create_herd_2(a, b, v, w)

                if index is 3:
                    return create_herd_3(a, b, c, v, w, x)

                t.a = a
                t.b = b
                t.c = c
                t.d = d

                t.v = v
                t.w = w
                t.x = x
                t.y = y

                if index is 4:
                    t.e = absent
                    del t.z, t.z6
                    return t

                assert index is 5

                t.e = e
                t.z = z

                t.e6 = absent
                del t.z6
                return t

            z7       = t.z7
            z7_scrub = z7.scrub

            if z7_scrub is 0:
                if reference_count(z7) is 3:
                    z7 = 0
            else:
                z7 = z7_scrub()

            #my_line('z7:%r', z7)

            if index is 0:
                if z7 is 0:
                    return 0

                z7_increment = z7.increment_skip
                return (z7   if z7_increment is 0 else    z7_increment())

            if index is 1:
                if z7 is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment())

                return create_herd_2(a, t.e7, v, z7)

            if index is 2:
                if z7 is 0:
                    return create_herd_2(a, b, v, w)

                return create_herd_3(a, b, t.e7, v, w, z7)

            if index is 3:
                if z7 is 0:
                    return create_herd_3(a, b, c, v, w, x)

                t.a = a
                t.b = b
                t.c = c
                t.d = t.e7

                t.v = v
                t.w = w
                t.x = x
                t.y = z7

                t.e = absent
                del t.z, t.z6, t.z7

                return t

            t.a = a
            t.b = b
            t.c = c
            t.d = d

            t.v = v
            t.w = w
            t.x = x
            t.y = y

            if index is 4:
                if z7 is 0:
                    t.e = absent
                    del t.z, t.z6, t.z7
                    return t

                t.e = t.e7
                t.z = z7

                t.e6 = absent
                del t.z6, t.z7
                return t

            assert index is 5

            t.e = e
            t.z = z

            if z7 is 0:
                t.e6 = absent
                del t.z6, t.z7
                return t

            t.e6 = t.e7
            t.z6 = z7

            t.e7 = absent
            del t.z7
            return t


        @property
        def total(t):
            if t.e  is absent:   return 4
            if t.e6 is absent:   return 5
            if t.e7 is absent:   return 6

            return 7


        values = ordered_values


    Herd_4567.first = Herd_4567.v


    new_Herd_4567 = Method(Object.__new__, Herd_4567)


    @share
    def create_herd_4(a, b, c, d, v, w, x, y):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent
        assert (v is not absent) and (w is not absent) and (x is not absent) and (y is not absent)

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


    displace_4v  = Herd_4567.v .__set__
    displace_4w  = Herd_4567.w .__set__
    displace_4x  = Herd_4567.x .__set__
    displace_4y  = Herd_4567.y .__set__
    displace_4z  = Herd_4567.z .__set__
    displace_4z6 = Herd_4567.z6.__set__
    displace_4z7 = Herd_4567.z7.__set__
