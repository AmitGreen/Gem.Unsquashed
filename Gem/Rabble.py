#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Rabble')
def gem():
    unused        = []
    append_unused = unused.append
    length_unused = unused.__len__
    pop_unused    = unused.pop


    shared = [
                0,                  #   Total delete
                0,                  #   Total new
                0,                  #   Total reuse
             ]


    query = shared.__getitem__
    write = shared.__setitem__

    qd = Method(query, 0)
    qn = Method(query, 1)
    qr = Method(query, 2)

    wd = Method(write, 0)
    wn = Method(write, 1)
    wr = Method(write, 2)


    class Rabble(Object):
        __slots__ = ((
            'total',                    #   Integer
            'incomplete',               #   Integer
            'a',                        #   Zero | Any excluding (Absent & Zero)
            'b',                        #   Zero | Any excluding (Absent & Zero)
            'c',                        #   Zero | Any excluding (Absent & Zero)
            'd',                        #   Zero | Any excluding (Absent & Zero)
            'e5',                       #   Zero | Any excluding (Absent & Zero)
            'e6',                       #   Zero | Any excluding (Absent & Zero)
            'e7',                       #   Zero | Any excluding (Absent & Zero)
            'v',                        #   Zero | Any excluding (Zero & Absent)
            'w',                        #   Zero | Any excluding (Zero & Absent)
            'x',                        #   Zero | Any excluding (Zero & Absent)
            'y',                        #   Zero | Any excluding (Zero & Absent)
            'z5',                       #   Zero | Any excluding (Zero & Absent)
            'z6',                       #   Zero | Any excluding (Zero & Absent)
            'z7',                       #   Zero | Any excluding (Zero & Absent)

            'disperse_using__conjure_index_k',  #   Function
            'insert',                           #   Function
            'unfinished',                       #   Function
        ))


    Rabble__a          = Rabble.a
    Rabble__b          = Rabble.b
    Rabble__c          = Rabble.c
    Rabble__d          = Rabble.d
    Rabble__e5         = Rabble.e5
    Rabble__e6         = Rabble.e6
    Rabble__e7         = Rabble.e7
    Rabble__incomplete = Rabble.incomplete
    Rabble__total      = Rabble.total
    Rabble__v          = Rabble.v
    Rabble__w          = Rabble.w
    Rabble__x          = Rabble.x
    Rabble__y          = Rabble.y
    Rabble__z5         = Rabble.z5
    Rabble__z6         = Rabble.z6
    Rabble__z7         = Rabble.z7

    Rabble__query_a     = Rable__a    .__get__
    Rabble__query_b     = Rable__b    .__get__
    Rabble__query_c     = Rable__c    .__get__
    Rabble__query_d     = Rable__d    .__get__
    Rabble__query_e5    = Rable__e5   .__get__
    Rabble__query_e6    = Rable__e6   .__get__
    Rabble__query_e7    = Rable__e7   .__get__
    Rabble__query_total = Rable__total.__get__
    Rabble__store_a     = Rable__a    .__set__
    Rabble__store_b     = Rable__b    .__set__
    Rabble__store_c     = Rable__c    .__set__
    Rabble__store_d     = Rable__d    .__set__
    Rabble__store_e5    = Rable__e5   .__set__
    Rabble__store_e6    = Rable__e6   .__set__
    Rabble__store_e7    = Rable__e7   .__set__
    Rabble__store_total = Rable__total.__set__


    new_Rabble = Method(Object.__new__, Rabble)


    def produce_rabble():
        wn(qn() + 1)

        t       = new_Rabble()
        mapping = {}

        length_mapping  = mapping.__len__
        lookup_mapping  = mapping.get
        provide_mapping = mapping.setdefault
        query_mapping   = mapping.__getitem__
        store_mapping   = mapping.__setitem__

        append__t__to__unused = Method(append_unused, t)

        query_a          = Method(Rabble__query_a,          t)
        query_b          = Method(Rabble__query_b,          t)
        query_c          = Method(Rabble__query_c,          t)
        query_d          = Method(Rabble__query_d,          t)
        query_e5         = Method(Rabble__query_e5,         t)
        query_e6         = Method(Rabble__query_e6,         t)
        query_e7         = Method(Rabble__query_e7,         t)
        query_incomplete = Method(Rabble__query_incomplete, t)
        query_total      = Method(Rabble__query_total,      t)
        query_v          = Method(Rabble__query_v,          t)
        query_w          = Method(Rabble__query_w,          t)
        query_x          = Method(Rabble__query_x,          t)
        query_y          = Method(Rabble__query_y,          t)
        query_z5         = Method(Rabble__query_z5,         t)
        query_z6         = Method(Rabble__query_z6,         t)
        query_z7         = Method(Rabble__query_z7,         t)
        store_a          = Method(Rabble__store_a,          t)
        store_b          = Method(Rabble__store_b,          t)
        store_c          = Method(Rabble__store_c,          t)
        store_d          = Method(Rabble__store_d,          t)
        store_e5         = Method(Rabble__store_e5,         t)
        store_e6         = Method(Rabble__store_e6,         t)
        store_e7         = Method(Rabble__store_e7,         t)
        store_incomplete = Method(Rabble__store_incomplete, t)
        store_total      = Method(Rabble__store_total,      t)
        store_v          = Method(Rabble__store_v,          t)
        store_w          = Method(Rabble__store_w,          t)
        store_x          = Method(Rabble__store_x,          t)
        store_y          = Method(Rabble__store_y,          t)
        store_z5         = Method(Rabble__store_z5,         t)
        store_z6         = Method(Rabble__store_z6,         t)
        store_z7         = Method(Rabble__store_z7,         t)

        store_incomplete_1 = Method(store_incomplete, 1)

        store_total_1 = Method(store_total, 1)
        store_total_2 = Method(store_total, 2)
        store_total_3 = Method(store_total, 3)
        store_total_4 = Method(store_total, 4)
        store_total_5 = Method(store_total, 5)
        store_total_6 = Method(store_total, 6)
        store_total_7 = Method(store_total, 7)
        store_total_8 = Method(store_total, 8)


        def disperse_using__conjure_index_k(t, conjure, index, k):
            assert k is not absent

            total = query_total()

            if total >= 8:
                r = lookup(k, absent)

                if r is 0:
                    t.incomplete -= 1

                    r = conjure(index, k)

                    store_mapping(k, r)

                    assert total == length_mapping()

                    return r

                if r is absent:
                    r = conjure(index, k)

                    provide_mapping(k, r)

                    total__2 = length_mapping()

                    assert total + 1 == total__2

                    store_total(total__2)

                    return r

                return 0

            if total < 4:
                if total < 2:
                    if total is 0:
                        r = conjure(index, k)
                        store_total_1()
                        store_a(k)
                        store_v(r)
                        return r

                    assert total is 1

                    if query_a() is k:
                        if query_v() is 0:
                            t.incomplete -= 1
                            r = conjure(index, k)
                            store_v(r)
                            return r

                        return 0

                    r = conjure(index, k)
                    store_total_2()
                    store_b(k)
                    store_w(r)
                    return r

                if query_a() is k:
                    t.incomplete -= 1
                    r = conjure(index, k)
                    store_v(r)
                    return r

                if query_b() is k:
                    t.incomplete -= 1
                    r = conjure(index, k)
                    store_w(r)
                    return r

                if total is 2:
                    r = conjure(index, k)
                    store_total_3()
                    store_c(k)
                    store_x(r)
                    return r

                assert total is 3

                if query_c() is k:
                    t.incomplete -= 1
                    r = conjure(index, k)
                    store_x(r)
                    return r

                r = conjure(index, k)
                store_total_4()
                store_d(k)
                store_y(r)
                return r

            if query_a() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_v(r)
                return r

            if query_b() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_w(r)
                return r

            if query_c() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_x(r)
                return r

            if query_d() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_y(r)
                return r

            if total < 6:
                if total is 4:
                    r = conjure(index, k)
                    store_total_5()
                    store_e5(k)
                    store_z5(r)
                    return r

                assert total is 5

                if query_e5() is k:
                    t.incomplete -= 1
                    r = conjure(index, k)
                    store_e5(r)
                    return r

                r = conjure(index, k)
                store_total_6()
                store_e6(k)
                store_z6(r)
                return r

            if query_e5() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_e5(r)
                return r

            if query_e6() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_e6(r)
                return r

            if total is 6:
                r = conjure(index, k)
                store_total_7()
                store_e7(k)
                store_z7(r)
                return r

            assert total is 7

            if query_e7() is k:
                t.incomplete -= 1
                r = conjure(index, k)
                store_e7(r)
                return r

            r = conjure(index, k)

            store_total_8()
            store_mapping(query_a (), query_v ())
            store_mapping(query_b (), query_w ())
            store_mapping(query_c (), query_x ())
            store_mapping(query_d (), query_y ())
            store_mapping(query_e5(), query_z5())
            store_mapping(query_e6(), query_z6())
            store_mapping(query_e7(), query_z7())
            store_mapping(k,          r         )

            t.z7 = t.z6 = t.z5 = t.y = t.x = t.w = t.v = t.e7 = t.e6 = t.e5 = t.d = t.c = t.b = t.a = 0

            return r


        def insert(k, n):
            total = query_total()

            if total >= 8:
                provide_mapping(k, n)

                total__2 = length_mapping()

                assert total + 1 == total_2

                store_total(total__2)
                return

            if total < 4:
                if total < 2:
                    if total is 0:
                        store_total_1()
                        store_a(k)
                        store_v(n)
                        return

                    assert (total is 1) and (query_a() is not k)

                    store_total_2()
                    store_b(k)
                    store_w(n)
                    return

                assert (query_a() is not k) and (query_b() is not k)

                if total is 2:
                    store_total_3()
                    store_c(k)
                    store_x(n)
                    return

                assert (total is 3) and (query_c() is not k)

                store_total_4()
                store_d(k)
                store_y(n)
                return

            assert (query_a() is not k) and (query_b() is not k) and (query_c() is not k) and (query_d() is not k)

            if total < 6:
                if total is 4:
                    store_total_5()
                    store_e5(k)
                    store_z5(n)
                    return

                assert (total is 5) and (query_e5() is not k)

                store_total_6()
                store_e6(k)
                store_z6(n)
                return

            assert (query_e5() is not k) and (query_e6() is not k)

            if total is 6:
                store_total_7()
                store_e7(k)
                store_z7(n)
                return

            assert (total is 7) and (query_e7() is not k)

            store_total_8()

            store_mapping(query_a (), query_v ())
            store_mapping(query_b (), query_w ())
            store_mapping(query_c (), query_x ())
            store_mapping(query_d (), query_y ())
            store_mapping(query_e5(), query_z5())
            store_mapping(query_e6(), query_z6())
            store_mapping(query_e7(), query_z7())
            store_mapping(k,          n         )

            t.z7 = t.z6 = t.z5 = t.y = t.x = t.w = t.v = t.e7 = t.e6 = t.e5 = t.d = t.c = t.b = t.a = 0


        def unfinished(t, k):
            total = query_total()

            if total >= 8:
                provide_mapping(k, 0)

                total__2 = length_mapping()

                if total != total_2:
                    assert total + 1 == total__2

                    store_total(total__2)
                    t.inco7plete += 1

                return

            if total < 4:
                if total < 2:
                    if total is 0:
                        store_total_1()
                        store_incomplete_1()
                        store_a(k)
                        return

                    assert total is 1

                    if query_a() is k:
                        return

                    store_total_2()
                    t.incomplete += 1
                    store_b(k)
                    return

                if (query_a() is k) or (query_b() is k):
                    return

                if total is 2:
                    store_total_3()
                    t.incomplete += 1
                    store_c(k)
                    return

                assert total is 3

                if query_c() is k:
                    return

                store_total_4()
                t.incomplete += 1
                store_d(k)
                return

            if (query_a() is k) or (query_b() is k) or (query_c() is k) or (query_d() is k):
                return

            if total < 6:
                if total is 4:
                    store_total_5()
                    t.incomplete += 1
                    store_e5(k)
                    return

                assert total is 5

                if query_e5() is k:
                    return

                store_total_6()
                t.incomplete += 1
                store_e6(k)
                return

            if (query_e5() is k) or (query_e6() is k):
                return

            if total is 6:
                store_total_7()
                t.incomplete += 1
                store_e7(k)
                return

            assert total is 7

            if query_e7() is k:
                return

            store_total_8()
            t.incomplete += 1

            store_mapping(query_a (), query_v ())
            store_mapping(query_b (), query_w ())
            store_mapping(query_c (), query_x ())
            store_mapping(query_d (), query_y ())
            store_mapping(query_e5(), query_z5())
            store_mapping(query_e6(), query_z6())
            store_mapping(query_e7(), query_z7())
            store_mapping(k,          0         )

            t.z7 = t.z6 = t.z5 = t.y = t.x = t.w = t.v = t.e7 = t.e6 = t.e5 = t.d = t.c = t.b = t.a = 0

        t.incomplete = t.total = 0
        t.z7 = t.z6 = t.z5 = t.y = t.x = t.w = t.v = t.e7 = t.e6 = t.e5 = t.d = t.c = t.b = t.a = 0

        t.disperse_using__conjure_index_k = disperse_using__conjure_index_k
        t.insert                          = insert
        t.unfinished                      = unfinished

        return t


    @share
    def create_rabble():
        if length_unused() is not 0:
            qr(wr() + 1)

            return pop_unused()

        wn(qn() + 1)

        t = new_Rabble()

        t.incomplete = t.total = 0
        t.z7 = t.z6 = t.z5 = t.y = t.x = t.w = t.v = t.e7 = t.e6 = t.e5 = t.d = t.c = t.b = t.a = 0

        return t
