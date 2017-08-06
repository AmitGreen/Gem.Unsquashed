#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Tokenizer')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    frame_1 = Method(python_frame, 1)

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


    class ParseContext(Object):
        __slots__ = ((
            'cadence',                  #   Cadence
            'e_type',                   #   None | Type
            'e_value',                  #   None | .e_type
            'e_traceback',              #   None | Python_Traceback
        ))


        def __init__(t):
            t.cadence     = cadence_initialized
            t.e_traceback = t.e_value = t.e_type = none


        def __enter__(t):
            assert t.life_cycle.is_cadence__initialized_exited_or_exception

            t.cadence = cadence__entered


        def __exit__(t, e_type, e_value, e_traceback):
            cadence = t.cadence

            t.cadence = cadence__exception

            assert cadence is cadence__entered


        def push_exception(t, e_type, e_value, e_traceback):
            if t.e_type is not none:
                try:
                    assert (e_type is not none) and (e_value is not none) and (e_traceback is not none)
                except:
                    pass


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
    def create_UnknownLine(number):
        line('%s #%s', frame_1().f_code.co_name, number)

        return UnknownLine(qs())


    @export
    def create_UnknownLine_0():
        return UnknownLine(qs())


    @export
    def parse_incomplete(number):
        line('%s #%s', frame_1().f_code.co_name, number)

        return none


    export(
        'qj',   qj,
        'qk',   qk,
        'qs',   qs,

        'wj',   wj,
        'wk',   wk,
    )
