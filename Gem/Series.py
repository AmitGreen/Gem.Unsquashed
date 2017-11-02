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


    def invalid_append():
        raise_runtime_error('Series.append: .append no longer valid; .finish already called')


    def invalid_finish():
        raise_runtime_error('Series.finish: .finish not valid a secondt time (already called once)')


    def invalid_length():
        raise_runtime_error('Series.length: .finish no longer valid; .finish already called')


    @export
    def dump_series_statistics():
        line('series statistics: new: %d, delete %d, reused: %d', qn(), qd(), qr())


    class Series(Object):
        __slots__ = ((
            'total',                    #   Integer
            'append',                   #   Function
            'finish',                   #   Function
            'length',                   #   Function
            '_construct_0',             #   Function
            '_construct_1',             #   Function
            '_construct_2',             #   Function
            '_construct_3',             #   Function
            '_construct_4',             #   Function
            '_construct_5',             #   Function
            '_construct_6',             #   Function
            '_construct_7',             #   Function
            '_construct_8',             #   Function
        ))


    new_Series           = Method(Object.__new__, Series)
    Series__write_append = Series.append.__set__
    Series__write_finish = Series.finish.__set__
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

        write_append = Method(Series__write_append, t)
        write_length = Method(Series__write_length, t)
        write_finish = Method(Series__write_finish, t)
        write_total  = Method(Series__write_total,  t)

        write_append_invalid = Method(write_append, invalid_append)
        write_finish_invalid = Method(write_finish, invalid_finish)
        write_length_many    = Method(write_length, length_many)
        write_length_invalid = Method(write_length, invalid_length)

        write_total_0 = Method(write_total, 0)
        write_total_1 = Method(write_total, 1)
        write_total_2 = Method(write_total, 2)
        write_total_3 = Method(write_total, 3)
        write_total_4 = Method(write_total, 4)
        write_total_5 = Method(write_total, 5)
        write_total_6 = Method(write_total, 6)
        write_total_7 = Method(write_total, 7)
        write_total_8 = Method(write_total, 8)

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


        write_append_many = Method(write_append, append_many)


        def append_e8(e8):
            wm7(e8)
            write_total_8()
            write_append_many()
            write_length_many()
            return t


        write_append_e8 = Method(write_append, append_e8)


        def append_e7(e7):
            wm6(e7)
            write_total_7()
            write_append_e8()
            return t


        write_append_e7 = Method(write_append, append_e7)


        def append_e6(e6):
            wm5(e6)
            write_total_6()
            write_append_e7()
            return t


        write_append_e6 = Method(write_append, append_e6)


        def append_e5(e5):
            wm4(e5)
            write_total_5()
            write_append_e6()
            return t


        write_append_e5 = Method(write_append, append_e5)


        def append_d(d):
            wm3(d)
            write_total_4()
            write_append_e5()
            return t


        write_append_d = Method(write_append, append_d)


        def append_c(c):
            wm2(c)
            write_total_3()
            write_append_d()
            return t


        write_append_c = Method(write_append, append_c)


        def append_b(b):
            wm1(b)
            write_total_2()
            write_append_c()
            return t


        write_append_b = Method(write_append, append_b)


        def append_a(a):
            wm0(a)
            write_total_1()
            write_append_b()
            return t


        write_append_a = Method(write_append, append_a)


        def finish():
            total = t.total

            if total is 8:
                r = create_tuple__many()

                wm00()
                wm10()
                wm20()
                wm30()
                wm40()
                wm50()
                wm60()
                wm70()
                delete_8()
            elif total < 4:
                if total < 2:
                    if total is 0:
                        r = (())
                    else:
                        r = (( qm0(), ))
                        wm00()
                else:
                    if total is 2:
                        r = (( qm0(), qm1() ))
                    else:
                        assert total is 3

                        r = (( qm0(), qm1(), qm2() ))
                        wm20()

                    wm00()
                    wm10()
            else:
                if total < 6:
                    if total is 4:
                        r = (( qm0(), qm1(), qm2(), qm3() ))
                    else:
                        assert total is 5

                        r = (( qm0(), qm1(), qm2(), qm3(), qm4() ))
                        wm40()
                else:
                    if total is 6:
                        r = (( qm0(), qm1(), qm2(), qm3(), qm4(), qm5() ))
                    else:
                        assert total is 7

                        r = (( qm0(), qm1(), qm2(), qm3(), qm4(), qm5(), qm6() ))
                        w60()
                    wm40()
                    wm50()

                wm00()
                wm10()
                wm20()
                wm30()

            write_append_invalid()
            write_finish_invalid()
            write_length_invalid()
            wd(qd() + 1)
            append__t__to__unused()

            return r


        write_finish_finish = Method(write_finish, finish)


        def length__total():
            return t.total


        write_length_total = Method(write_length, length__total)


        def construct_0():
            write_total_0()
            write_append_a()
            write_finish_finish()
            write_length_total()
            return t


        def construct_1(a):
            wm0(a)
            write_total_1()
            write_append_b()
            write_finish_finish()
            write_length_total()
            return t


        def construct_2(a, b):
            wm0(a)
            wm1(b)
            write_total_2()
            write_append_c()
            write_finish_finish()
            write_length_total()
            return t


        def construct_3(a, b, c):
            wm0(a)
            wm1(b)
            wm2(c)
            write_total_3()
            write_append_d()
            write_finish_finish()
            write_length_total()
            return t


        def construct_4(a, b, c, d):
            wm0(a)
            wm1(b)
            wm2(c)
            wm3(d)
            write_total_4()
            write_append_e()
            write_finish_finish()
            write_length_total()
            return t


        def construct_5(a, b, c, d, e5):
            wm0(a)
            wm1(b)
            wm2(c)
            wm3(d)
            wm4(e5)
            write_total_5()
            write_append_e6()
            write_finish_finish()
            write_length_total()
            return t


        def construct_6(a, b, c, d, e5, e6):
            wm0(a)
            wm1(b)
            wm2(c)
            wm3(d)
            wm4(e5)
            wm5(e6)
            write_total_6()
            write_append_e7()
            write_finish_finish()
            write_length_total()
            return t


        def construct_7(a, b, c, d, e5, e6, e7):
            wm0(a)
            wm1(b)
            wm2(c)
            wm3(d)
            wm4(e5)
            wm5(e6)
            wm6(e7)
            write_total_7()
            write_append_e8()
            write_finish_finish()
            write_length_total()
            return t


        def construct_8(a, b, c, d, e5, e6, e7, e8):
            wm0(a)
            wm1(b)
            wm2(c)
            wm3(d)
            wm4(e5)
            wm5(e6)
            wm6(e7)
            wm7(e8)
            write_total_8()
            write_append_many()
            write_length_many()


        t._construct_0 = construct_0
        t._construct_1 = construct_1
        t._construct_2 = construct_2
        t._construct_3 = construct_3
        t._construct_4 = construct_4
        t._construct_5 = construct_5
        t._construct_6 = construct_6
        t._construct_7 = construct_7
        t._construct_8 = construct_8

        return t


    @export
    def create_series_0():
        if length_unused() is 0:
            return produce_series()._construct_0()

        wr(qr() + 1)
        return pop_unused()._construct_0()


    @export
    def create_series_1(a):
        if length_unused() is 0:
            return produce_series()._construct_1(a)

        wr(qr() + 1)
        return pop_unused()._construct_1(a)


    @export
    def create_series_2(a, b):
        if length_unused() is 0:
            return produce_series()._construct_2(a, b)

        wr(qr() + 1)
        return pop_unused()._construct_2(a, b)


    @export
    def create_series_3(a, b, c):
        if length_unused() is 0:
            return produce_series()._construct_3(a, b, c)

        wr(qr() + 1)
        return pop_unused()._construct_3(a, b, c)


    @export
    def create_series_4(a, b, c, d):
        if length_unused() is 0:
            return produce_series()._construct_4(a, b, c, d)

        wr(qr() + 1)
        return pop_unused()._construct_4(a, b, c, d)


    @export
    def create_series_5(a, b, c, d, e5):
        if length_unused() is 0:
            return produce_series()._construct_5(a, b, c, d, e5)

        wr(qr() + 1)
        return pop_unused()._construct_5(a, b, c, d, e5)


    @export
    def create_series_6(a, b, c, d, e5, e6):
        if length_unused() is 0:
            return produce_series()._construct_6(a, b, c, d, e5, e6)

        wr(qr() + 1)
        return pop_unused()._construct_6(a, b, c, d, e5, e6)


    @export
    def create_series_7(a, b, c, d, e5, e6, e7):
        if length_unused() is 0:
            return produce_series()._construct_7(a, b, c, d, e5, e6, e7)

        wr(qr() + 1)
        return pop_unused()._construct_7(a, b, c, d, e5, e6, e7)


    @export
    def create_series_8(a, b, c, d, e5, e6, e7, e8):
        if length_unused() is 0:
            return produce_series()._construct_8(a, b, c, d, e5, e6, e7, e8)

        wr(qr() + 1)
        return pop_unused()._construct_8(a, b, c, d, e5, e6, e7, e8)
