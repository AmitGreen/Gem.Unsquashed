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


    construct_Exception = Exception.__init__


    class UnknownLineException(Exception):
        __slots__ = ((
            'unknown_line',             #   Unknown_line
        ))


        def __init__(t, message, unknown_line):
            construct_Exception(t, message)

            t.unknown_line = unknown_line


    class ParseContext(Object):
        __slots__ = ((
            'cadence',                  #   Cadence
            'iterate_lines',            #   Generator
            'many',                     #   Tuple of *
            'append',                   #   Method
        ))


        def __init__(t, iterate_lines):
            t.cadence = cadence_constructing

            t.iterate_lines = iterate_lines
            t.many          = many                = []
            t.append        = many.append

            t.cadence = cadence_initialized


        def __enter__(t):
            assert t.cadence.is_initialized_exited_or_exception

            t.cadence = cadence_entered


        def __exit__(t, e_type, e, e_traceback):
            with maybe_exit_exception(e_type, e, e_traceback):
                cadence = t.cadence

                t.cadence = cadence_exception

                assert cadence is cadence_entered

                if e is none:
                   t.cadence = cadence_exited
                   return

                if type(e) is not UnknownLineException:
                    return

                t.append(e.unknown_line)

                return true


        def __iter__(t):
            loop = 0

            while t.cadence is not cadence_exited:
                yield loop
                loop += 1


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


        return ParseContext(GENERATOR_next_line())


    @export
    def create_UnknownLine(number):
        line('%s #%s', frame_1().f_code.co_name, number)

        unknown_line_error = UnknownLineException(
                                 arrange('parse incomplete %s #%d', frame_1().f_code.co_name, number),
                                 UnknownLine(qs()),
                             )

        raising_exception(unknown_line_error)

        raise unknown_line_error


    @export
    def create_UnknownLine_0():
        line('unknown_line %s', frame_1().f_code.co_name)

        unknown_line_error = UnknownLineException(
                                 arrange('parse incomplete %s', frame_1().f_code.co_name),
                                 UnknownLine(qs()),
                             )

        raising_exception(unknown_line_error)

        raise unknown_line_error


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
