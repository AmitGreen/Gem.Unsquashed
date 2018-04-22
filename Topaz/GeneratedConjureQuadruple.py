#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Topaz.GeneratedConjureQuadruple')
def gem():
    from Gem import create_herd_3, create_herd_4, create_herd_many


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    @share
    def produce_simplified_conjure_quadruple(
            name, Meta, cache,

            lookup  = absent,
            provide = absent,
            store   = absent,
    ):
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_quadruple(k1, k2, k3, k4):
            #create_next(<KeyData <CommonKeyData 7 7 0 4 ('k1', 'k2', 'k3', 'k4') k1, k2, k3, k4> 0; 0 0 p q r s; 0 k1 k2 k3 k4>, 0, 0)
            p = lookup(k1)
            if p is none:
                q = Meta(k1, k2, k3, k4)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3) and (q.k4 is k4)
                return provide(k1, q)
            if p.k2 is k2:
                if p.k3 is k3:
                    if p.k4 is k4: return p

                    r = Meta(k1, k2, k3, k4)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                    store(k1, create_horde_2(2, p.k4, k4, p, r))
                    return r

                q = Meta(k1, k2, k3, k4)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3) and (q.k4 is k4)
                store(k1, create_horde_2(1, p.k3, k3, p, q))
                return q

            if not p.is_herd:
                q = Meta(k1, k2, k3, k4)
                assert (q.k1 is k1) and (q.k2 is k2) and (q.k3 is k3) and (q.k4 is k4)
                herd = create_herd_2(p.k2, k2, p, q)
                store(k1, herd)
                return q

            if p.skip is 0:
                #create_next(<KeyData <CommonKeyData 7 7 0 4 ('k1', 'k2', 'k3', 'k4') k1, k2, k3, k4> 1; 0 p q r s 0; k1 k2 k3 k4 0>, 0, 0)
                q = p.glimpse(k2, absent)

                if q.k3 is k3:
                    if q.k4 is k4: return q

                    r = Meta(k1, k2, k3, k4)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                    p.displace(k2, create_horde_2(1, q.k4, k4, q, r))
                    return r

                if not q.is_herd:
                    r = Meta(k1, k2, k3, k4)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                    if q is absent:
                        p_ = p.insert(k2, r)
                        if p is not p_: store(k1, p_)
                        return r

                    herd = create_herd_2(q.k3, k3, q, r)
                    p.displace(k2, herd)
                    return r

                if q.skip is 0:
                    #create_next(<KeyData <CommonKeyData 7 7 0 4 ('k1', 'k2', 'k3', 'k4') k1, k2, k3, k4> 2; p q r s 0 0; k2 k3 k4 0 0>, 0, 0)
                    r = q.glimpse(k3, absent)
                    if r.k4 is k4: return r

                    if not r.is_herd:
                        s = Meta(k1, k2, k3, k4)
                        assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                        if r is absent:
                            q_ = q.insert(k3, s)
                            if q is not q_: p.displace(k2, q_)
                            return s

                        herd = create_herd_2(r.k4, k4, r, s)
                        q.displace(k3, herd)
                        return s

                    s = r.glimpse(k4)
                    if s is not none:
                        assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                        return s

                    s = Meta(k1, k2, k3, k4)
                    assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                    r_ = r.insert(k4, s)
                    if r is not r_: q.displace(k3, r_)
                    return s

                assert q.skip is 1

                q_k3 = q.sample().k3
                if q_k3 is not k3:
                    r = Meta(k1, k2, k3, k4)
                    assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                    p.displace(k2, create_herd_2(q_k3, k3, q.remove_skip(), r))
                    return r

                s = q.glimpse(k4)
                if s is not none:
                    assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                    return s

                s = Meta(k1, k2, k3, k4)
                assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                q_ = q.insert(k4, s)
                if q is not q_:
                    assert q_.sample().k3 is k3
                    p.displace(k2, q_)
                return s

            p_sample = p.sample()
            p_k2     = p_sample.k2
            if p_k2 is not k2:
                r = Meta(k1, k2, k3, k4)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                store(k1, create_herd_2(p_k2, k2, p.remove_skip(), r))
                return r

            if p.skip is 1:
                #create_next(<KeyData <CommonKeyData 7 7 0 4 ('k1', 'k2', 'k3', 'k4') k1, k2, k3, k4> 2; 0 p r s 0 0; k1 k3 k4 0 0>, 0, k2)
                r = p.glimpse(k3, absent)
                if r.k4 is k4: return r

                if not r.is_herd:
                    s = Meta(k1, k2, k3, k4)
                    assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                    if r is absent:
                        p_ = p.insert(k3, s)
                        if p is not p_:
                            assert p_.sample().k2 is k2
                            store(k1, p_)
                        return s

                    herd = create_herd_2(r.k4, k4, r, s)
                    p.displace(k3, herd)
                    return s

                s = r.glimpse(k4)
                if s is not none:
                    assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                    return s

                s = Meta(k1, k2, k3, k4)
                assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                r_ = r.insert(k4, s)
                if r is not r_: p.displace(k3, r_)
                return s

            assert p.skip is 2

            p_k3 = p_sample.k3
            if p_k3 is not k3:
                r = Meta(k1, k2, k3, k4)
                assert (r.k1 is k1) and (r.k2 is k2) and (r.k3 is k3) and (r.k4 is k4)
                store(k1, create_horde_2(1, p_k3, k3, p.remove_skip(2), r))
                return r

            s = p.glimpse(k4)
            if s is not none:
                assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
                return s

            s = Meta(k1, k2, k3, k4)
            assert (s.k1 is k1) and (s.k2 is k2) and (s.k3 is k3) and (s.k4 is k4)
            p_ = p.insert(k4, s)
            if p is not p_:
                assert (p_.sample().k2 is k2) and (p_.sample().k3 is k3)
                store(k1, p_)
            return s


        return simplified_conjure_quadruple
