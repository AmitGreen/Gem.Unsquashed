#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Series')
def gem():
    #
    #   Series:
    #
    #       A list that can only grow
    #


    list_append      = List.append
    list_delete_item = List.__delitem__
    list_length      = List.__len__


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


    @export
    def dump_series_statistics():
        line('series statistics: new: %d, delete %d, reused: %d', qn(), qd(), qr())


    class Series(Object):
        __slots__ = ((
            'total',                    #   Integer
            'append',                   #   Function
            'create_tuple',             #   Function
            'length',                   #   Function
            '_zap',                     #   Function
        ))


        #
        #   Special methods __del__ & __len__ must be defined as normal method (not as slots).
        #
        #   The actual methods call the slots for the implementation.
        #
        def __del__(t):
            t._zap()


        def __len__(t):
            return t.length()


    new_Series           = Method(Object.__new__, Series)
    Series__write_append = Series.append.__set__
    Series__write_length = Series.length.__set__
    Series__write_total  = Series.total .__set__


    def produce_series():
        wn(qn() + 1)

        t    = new_Series()
        many = [0, 0, 0, 0, 0, 0, 0, 0]

        append_many = Method(list_append, many)
        delete_many = Method(list_delete_item, many)
        length_many = Method(list_length, many)
        query_many  = many.__getitem__
        write_many  = many.__setitem__

        append__t__to__unused = Method(append_unused, t)
        delete_8              = Method(delete_many, Slice(8, none))        #   del many[8:]
        create_tuple__many    = Method(Tuple, many)

        wa  = Method(Series__write_append, t)
        wl  = Method(Series__write_length, t)
        wt  = Method(Series__write_total,  t)

        wl8 = Method(wl, length_many)

        wt0 = Method(wt, 0)
        wt1 = Method(wt, 1)
        wt2 = Method(wt, 2)
        wt3 = Method(wt, 3)
        wt4 = Method(wt, 4)
        wt5 = Method(wt, 5)
        wt6 = Method(wt, 6)
        wt7 = Method(wt, 7)
        wt8 = Method(wt, 8)

        qm0 = Method(query_many, 0)
        qm1 = Method(query_many, 1)
        qm2 = Method(query_many, 2)
        qm3 = Method(query_many, 3)
        qm4 = Method(query_many, 4)
        qm5 = Method(query_many, 5)
        qm6 = Method(query_many, 6)
        qm7 = Method(query_many, 7)

        wm0 = Method(write_many, 0)
        wm1 = Method(write_many, 1)
        wm2 = Method(write_many, 2)
        wm3 = Method(write_many, 3)
        wm4 = Method(write_many, 4)
        wm5 = Method(write_many, 5)
        wm6 = Method(write_many, 6)
        wm7 = Method(write_many, 7)

        wm00 = Method(wm0, 0)
        wm10 = Method(wm1, 0)
        wm20 = Method(wm2, 0)
        wm30 = Method(wm3, 0)
        wm40 = Method(wm4, 0)
        wm50 = Method(wm5, 0)
        wm60 = Method(wm6, 0)
        wm70 = Method(wm7, 0)


        wa9 = Method(wa, append_many)


        def append_e8(e8):
            wm7(e8)
            wt8()
            wa9()
            wl8()
            return t


        wa8 = Method(wa, append_e8)


        def append_e7(e7):
            wm6(e7)
            wt7()
            wa8()
            return t


        wa7 = Method(wa, append_e7)


        def append_e6(e6):
            wm5(e6)
            wt6()
            wa7()
            return t


        wa6 = Method(wa, append_e6)


        def append_e5(e5):
            wm4(e5)
            wt5()
            wa6()
            return t


        wa5 = Method(wa, append_e5)


        def append_d(d):
            wm3(d)
            wt4()
            wa5()
            return t


        wa4 = Method(wa, append_d)


        def append_c(c):
            wm2(c)
            wt3()
            wa4()
            return t


        wa3 = Method(wa, append_c)


        def append_b(b):
            wm1(b)
            wt2()
            wa3()
            return t


        wa2 = Method(wa, append_b)


        def append_a(a):
            wm0(a)
            wt1()
            wa2()
            return t


        wa1 = Method(wa, append_a)


        def create_tuple():
            total = t.total

            if total is 8:
                return create_tuple__many()

            if total < 4:
                if total < 2:
                    if total is 0:
                        return (())

                    assert total is 1

                    return (( qm0(), ))

                if total is 2:
                    return (( qm0(), qm1() ))

                assert total is 3

                return (( qm0(), qm1(), qm2() ))

            if total < 6:
                if total is 4:
                    return (( qm0(), qm1(), qm2(), qm3() ))

                assert total is 5

                return (( qm0(), qm1(), qm2(), qm3(), qm4() ))

            if total is 6:
                return (( qm0(), qm1(), qm2(), qm3(), qm4(), qm5() ))

            assert total is 7

            return (( qm0(), qm1(), qm2(), qm3(), qm4(), qm5(), qm6() ))


        def length__total():
            return t.total


        wlt = Method(wl, length__total)


        def zap():
            wd(qd() + 1)

            wm00()
            wm10()
            wm20()
            wm30()
            wm40()
            wm50()
            wm60()
            wm70()
            delete_8()

            wt0()
            wa1()
            wlt()

            append__t__to__unused()

        wt0()
        wa1()
        wlt()

        t.create_tuple = create_tuple
        t._zap         = zap

        return t


    @export
    def create_series_0():
        if length_unused() is 0:
            return produce_series()

        wr(qr() + 1)
        return pop_unused()


    @export
    def create_series_1(a):
        if length_unused() is 0:
            return produce_series().append(a)

        wr(qr() + 1)
        return pop_unused().append(a)


    @export
    def create_series_2(a, b):
        if length_unused() is 0:
            return produce_series().append(a).append(b)

        wr(qr() + 1)
        return pop_unused().append(a).append(b)


    @export
    def create_series_3(a, b, c):
        if length_unused() is 0:
            return produce_series().append(a).append(b).append(c)

        wr(qr() + 1)
        return pop_unused().append(a).append(b).append(c)


    @export
    def create_series_4(a, b, c, d):
        if length_unused() is 0:
            return produce_series().append(a).append(b).append(c).append(d)

        wr(qr() + 1)
        return pop_unused().append(a).append(b).append(c).append(d)


    @export
    def create_series_5(a, b, c, d, e5):
        if length_unused() is 0:
            t = produce_series()
        else:
            wr(qr() + 1)
            t = pop_unused()

        return t.append(a).append(b).append(c).append(d).append(e5)


    @export
    def create_series_6(a, b, c, d, e5, e6):
        if length_unused() is 0:
            t = produce_series()
        else:
            wr(qr() + 1)
            t = pop_unused()

        return t.append(a).append(b).append(c).append(d).append(e5).append(e6)


    @export
    def create_series_7(a, b, c, d, e5, e6, e7):
        if length_unused() is 0:
            t = produce_series()
        else:
            wr(qr() + 1)
            t = pop_unused()

        return t.append(a).append(b).append(c).append(d).append(e5).append(e6).append(e7)


    @export
    def create_series_8(a, b, c, d, e5, e6, e7, e8):
        if length_unused() is 0:
            t = produce_series()
        else:
            wr(qr() + 1)
            t = pop_unused()

        return t.append(a).append(b).append(c).append(d).append(e5).append(e6).append(e7).append(e8)
