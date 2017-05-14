#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Tokenizer')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    tokenizer = [none, none, none, none]

    query = tokenizer.__getitem__
    write = tokenizer.__setitem__

    qs = Method(query, 0)
    qi = Method(query, 1)
    qj = Method(query, 2)
    qk = Method(query, 3)

    ws = Method(write, 0)
    wi = Method(write, 1)
    wj = Method(write, 2)
    wk = Method(write, 3)


    @export
    def z_initialize(data):
        data_lines = data.splitlines(true)
        maximum_i  = length(data_lines)
        q_data     = data_lines.__getitem__


        def GENERATOR_next_line():
            for i in iterate_range(maximum_i):
                s = q_data(i)

                ws(s)
                wi(i)
                wj(0)

                yield s

            ws(none)
            wi(none)
            wj(none)

            raise stop_iteration


        return GENERATOR_next_line()


    @export
    def create_UnknownLine(f = absent, number = absent):
        if f is absent:
            assert number is absent
        else:
            line('%s #%s', f.__name__, number)

        return UnknownLine(qs())


    @export
    def parse_incomplete(f, number):
        line('%s #%s', f.__name__, number)

        return none


    export(
        'qj',   qj,
        'qk',   qk,
        'qs',   qs,

        'wj',   wj,
        'wk',   wk,
    )
