#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedConjureTriple')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many, create_horde_2, create_horde_many, displace_4y, displace_4z, displace_4z6, displace_4z7


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    @share
    def produce_simplified_conjure_triple__312(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple__312(k1, k2, k3):
            #create_next(<KeyData <CommonKeyData 7 7 7 3 ('k3', 'k1', 'k2') k1, k2, k3> 0; 0 0 p q r 0; 0 k3 k1 k2 0>, 0, 0)
            p = lookup(k3)
            if p is none:
                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                return provide(k3, q)
            if p.k1 is k1:
                if p.k2 is k2: return p

                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                store(k3, create_horde_2(1, p.k2, k2, p, q))
                return q

            ph = p.herd_estimate

            if ph is 0:
                q = Meta(k1, k2, k3)
                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                herd = create_herd_2(p.k1, k1, p, q)
                store(k3, herd)
                return q

            if p.skip is 0:
                #create_next(<KeyData <CommonKeyData 7 7 7 3 ('k3', 'k1', 'k2') k1, k2, k3> 1; 0 p q r 0 0; k3 k1 k2 0 0>, ph, 0)
                #create_next: shift: 1; herd only
                if ph is 8:
                    q = map__lookup(p, k1)
                    if q is none:
                        r = Meta(k1, k2, k3)
                        assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                        return map__provide(p, k1, r)
                    if q.k2 is k2: return q
                elif p.a is k1:
                    q = p.v
                    if q.k2 is k2: return q
                    pr = p.displace_v
                elif p.b is k1:
                    q = p.w
                    if q.k2 is k2: return q
                    pr = p.displace_w
                elif ph is 2:
                    q = Meta(k1, k2, k3)
                    assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                    store(k3, create_herd_3(p.a, p.b, k1, p.v, p.w, q))
                    return q
                elif p.c is k1:
                    q = p.x
                    if q.k2 is k2: return q
                    pr = p.displace_x
                elif ph is 3:
                    q = Meta(k1, k2, k3)
                    assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                    store(k3, create_herd_4(p.a, p.b, p.c, k1, p.v, p.w, p.x, q))
                    return q
                else:
                    assert ph is 7
                    if p.d is k1:
                        q = p.y
                        if q.k2 is k2: return q
                        pr = displace_4y
                    else:
                        pe = p.e
                        if pe is k1:
                            q = p.z
                            if q.k2 is k2: return q
                            pr = displace_4z
                        elif pe is absent:
                            p.e = k1
                            p.e6 = absent
                            p.z = q = Meta(k1, k2, k3)
                            assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                            return q
                        else:
                            pe6 = p.e6
                            if pe6 is k1:
                                q = p.z6
                                if q.k2 is k2: return q
                                pr = displace_4z6
                            elif pe6 is absent:
                                p.e6 = k1
                                p.e7 = absent
                                p.z6 = q = Meta(k1, k2, k3)
                                assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)
                                return q
                            else:
                                pe7 = p.e7
                                if pe7 is k1:
                                    q = p.z7
                                    if q.k2 is k2: return q
                                    pr = displace_4z7
                                else:
                                    q = Meta(k1, k2, k3)
                                    assert (q.k3 is k3) and (q.k1 is k1) and (q.k2 is k2)

                                    if pe7 is absent:
                                        p.e7 = k1
                                        p.z7 = q
                                        return q

                                    store(
                                             k3,
                                             create_herd_many(
                                                 p.a, p.b, p.c, p.d, pe, pe6, pe7, k1,
                                                 p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                                             )
                                         )

                                    return q

                qh = q.herd_estimate

                if qh is 0:
                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    herd = create_herd_2(q.k2, k2, q, r)

                    if ph is 8: map__store(p, k1, herd)
                    else:       pr(p, herd)

                    return r

                #create_last: herd or horde
                if qh is 8:
                    r = map__lookup(q, k2)
                    if r is not none:
                        assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                        return r

                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    map__store(q, k2, r)
                    return r

                if q.a is k2:
                    r = q.v
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                if q.b is k2:
                    r = q.w
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                if qh is 2:
                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    if ph is 8:
                        map__store(p, k1, create_herd_3(q.a, q.b, k2, q.v, q.w, r))
                    else:
                        pr(p, create_herd_3(q.a, q.b, k2, q.v, q.w, r))
                    return r

                qc = q.c
                if qc is k2:
                    r = q.x
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r
                if qc is absent:
                    q.c = k2
                    q.x = r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                if qh is 3:
                    r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    if ph is 8:
                        map__store(p, k1, create_herd_4(q.a, q.b, qc, k2, q.v, q.w, q.x, r))
                    else:
                        pr(p, create_herd_4(q.a, q.b, qc, k2, q.v, q.w, q.x, r))
                    return r

                assert qh is 7

                qd = q.d
                if qd is k2:
                    r = q.y
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r
                if qd is absent:
                    q.d = k2
                    q.y = r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                qe = q.e
                if qe is k2:
                    r = q.z
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r
                if qe is absent:
                    q.e = k2
                    q.e6 = absent
                    q.z = r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                qe6 = q.e6
                if qe6 is k2:
                    r = q.z6
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r
                if qe6 is absent:
                    q.e6 = k2
                    q.e7 = absent
                    q.z6 = r = Meta(k1, k2, k3)
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                qe7 = q.e7
                if qe7 is k2:
                    r = q.z7
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)

                if qe7 is absent:
                    q.e7 = k2
                    q.z7 = r
                    return r

                if ph is 8:
                    map__store(
                        p,
                        k1,
                        create_herd_many(
                            q.a, q.b, qc, qd, qe, qe6, qe7, k2,
                            q.v, q.w, q.x, q.y, q.z, q.z6, q.z7, r,
                        ),
                    )
                else:
                    pr(
                        p,
                        create_herd_many(
                            q.a, q.b, qc, qd, qe, qe6, qe7, k2,
                            q.v, q.w, q.x, q.y, q.z, q.z6, q.z7, r,
                        ),
                    )

                return r

            assert p.skip is 1

            p_k1 = p.sample().k1
            if p_k1 is not k1:
                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                store(k3, create_herd_2(p_k1, k1, p.remove_skip(), r))
                return r

            #create_last: horde only
            if ph is 8:
                r = map__lookup(p, k2)
                if r is not none:
                    assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                map__store(p, k2, r)
                return r

            assert ph is 3

            if p.a is k2:
                r = p.v
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                return r

            if p.b is k2:
                r = p.w
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                return r

            pc = p.c
            if pc is k2:
                r = p.x
                assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)
                return r

            r = Meta(k1, k2, k3)
            assert (r.k3 is k3) and (r.k1 is k1) and (r.k2 is k2)

            if pc is absent:
                p.c = k2
                p.x = r
                return r

            h = create_horde_many(1, p.a, p.b, pc, k2, p.v, p.w, p.x, r)
            assert h.sample().k1 is k1
            store(k3, h)
            return r


        return simplified_conjure_triple__312


    @share
    def produce_simplified_conjure_triple(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_triple(k1, k2, k3):
            #create_next(<KeyData <CommonKeyData 7 7 7 3 ('k1', 'k2', 'k3') k1, k2, k3> 0; 0 0 p q r 0; 0 k1 k2 k3 0>, 0, 0)
            p = lookup(k1)
            if p is none:
                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                return provide(k1, q)
            if p.k2 is k2:
                if p.k3 is k3: return p

                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                store(k1, create_horde_2(1, p.k3, k3, p, q))
                return q

            ph = p.herd_estimate

            if ph is 0:
                q = Meta(k1, k2, k3)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q

            if p.skip is 0:
                #create_next(<KeyData <CommonKeyData 7 7 7 3 ('k1', 'k2', 'k3') k1, k2, k3> 1; 0 p q r 0 0; k1 k2 k3 0 0>, ph, 0)
                #create_next: shift: 1; herd only
                if ph is 8:
                    q = map__lookup(p, k2)
                    if q is none:
                        r = Meta(k1, k2, k3)
                        assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                        return map__provide(p, k2, r)
                    if q.k3 is k3: return q
                elif p.a is k2:
                    q = p.v
                    if q.k3 is k3: return q
                    pr = p.displace_v
                elif p.b is k2:
                    q = p.w
                    if q.k3 is k3: return q
                    pr = p.displace_w
                elif ph is 2:
                    q = Meta(k1, k2, k3)
                    assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                    store(k1, create_herd_3(p.a, p.b, k2, p.v, p.w, q))
                    return q
                elif p.c is k2:
                    q = p.x
                    if q.k3 is k3: return q
                    pr = p.displace_x
                elif ph is 3:
                    q = Meta(k1, k2, k3)
                    assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                    store(k1, create_herd_4(p.a, p.b, p.c, k2, p.v, p.w, p.x, q))
                    return q
                else:
                    assert ph is 7
                    if p.d is k2:
                        q = p.y
                        if q.k3 is k3: return q
                        pr = displace_4y
                    else:
                        pe = p.e
                        if pe is k2:
                            q = p.z
                            if q.k3 is k3: return q
                            pr = displace_4z
                        elif pe is absent:
                            p.e = k2
                            p.e6 = absent
                            p.z = q = Meta(k1, k2, k3)
                            assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                            return q
                        else:
                            pe6 = p.e6
                            if pe6 is k2:
                                q = p.z6
                                if q.k3 is k3: return q
                                pr = displace_4z6
                            elif pe6 is absent:
                                p.e6 = k2
                                p.e7 = absent
                                p.z6 = q = Meta(k1, k2, k3)
                                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)
                                return q
                            else:
                                pe7 = p.e7
                                if pe7 is k2:
                                    q = p.z7
                                    if q.k3 is k3: return q
                                    pr = displace_4z7
                                else:
                                    q = Meta(k1, k2, k3)
                                    assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3)

                                    if pe7 is absent:
                                        p.e7 = k2
                                        p.z7 = q
                                        return q

                                    store(
                                             k1,
                                             create_herd_many(
                                                 p.a, p.b, p.c, p.d, pe, pe6, pe7, k2,
                                                 p.v, p.w, p.x, p.y, p.z, p.z6, p.z7, q,
                                             )
                                         )

                                    return q

                qh = q.herd_estimate

                if qh is 0:
                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    herd = create_herd_2(q.k3, k3, q, r)

                    if ph is 8: map__store(p, k2, herd)
                    else:       pr(p, herd)

                    return r

                #create_last: herd or horde
                if qh is 8:
                    r = map__lookup(q, k3)
                    if r is not none:
                        assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                        return r

                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    map__store(q, k3, r)
                    return r

                if q.a is k3:
                    r = q.v
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                if q.b is k3:
                    r = q.w
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                if qh is 2:
                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    if ph is 8:
                        map__store(p, k2, create_herd_3(q.a, q.b, k3, q.v, q.w, r))
                    else:
                        pr(p, create_herd_3(q.a, q.b, k3, q.v, q.w, r))
                    return r

                qc = q.c
                if qc is k3:
                    r = q.x
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r
                if qc is absent:
                    q.c = k3
                    q.x = r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                if qh is 3:
                    r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    if ph is 8:
                        map__store(p, k2, create_herd_4(q.a, q.b, qc, k3, q.v, q.w, q.x, r))
                    else:
                        pr(p, create_herd_4(q.a, q.b, qc, k3, q.v, q.w, q.x, r))
                    return r

                assert qh is 7

                qd = q.d
                if qd is k3:
                    r = q.y
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r
                if qd is absent:
                    q.d = k3
                    q.y = r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                qe = q.e
                if qe is k3:
                    r = q.z
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r
                if qe is absent:
                    q.e = k3
                    q.e6 = absent
                    q.z = r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                qe6 = q.e6
                if qe6 is k3:
                    r = q.z6
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r
                if qe6 is absent:
                    q.e6 = k3
                    q.e7 = absent
                    q.z6 = r = Meta(k1, k2, k3)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                qe7 = q.e7
                if qe7 is k3:
                    r = q.z7
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)

                if qe7 is absent:
                    q.e7 = k3
                    q.z7 = r
                    return r

                if ph is 8:
                    map__store(
                        p,
                        k2,
                        create_herd_many(
                            q.a, q.b, qc, qd, qe, qe6, qe7, k3,
                            q.v, q.w, q.x, q.y, q.z, q.z6, q.z7, r,
                        ),
                    )
                else:
                    pr(
                        p,
                        create_herd_many(
                            q.a, q.b, qc, qd, qe, qe6, qe7, k3,
                            q.v, q.w, q.x, q.y, q.z, q.z6, q.z7, r,
                        ),
                    )

                return r

            assert p.skip is 1

            p_k2 = p.sample().k2
            if p_k2 is not k2:
                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                store(k1, create_herd_2(p_k2, k2, p.remove_skip(), r))
                return r

            #create_last: horde only
            if ph is 8:
                r = map__lookup(p, k3)
                if r is not none:
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                    return r

                r = Meta(k1, k2, k3)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                map__store(p, k3, r)
                return r

            assert ph is 3

            if p.a is k3:
                r = p.v
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                return r

            if p.b is k3:
                r = p.w
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                return r

            pc = p.c
            if pc is k3:
                r = p.x
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)
                return r

            r = Meta(k1, k2, k3)
            assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3)

            if pc is absent:
                p.c = k3
                p.x = r
                return r

            h = create_horde_many(1, p.a, p.b, pc, k3, p.v, p.w, p.x, r)
            assert h.sample().k2 is k2
            store(k1, h)
            return r


        return simplified_conjure_triple
