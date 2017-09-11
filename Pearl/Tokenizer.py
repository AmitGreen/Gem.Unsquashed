#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Tokenizer')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    tokenizer = [none, 0, 0, 0, none, none, none]

    query = tokenizer.__getitem__
    write = tokenizer.__setitem__

    qs = Method(query, 0)
    qd = Method(query, 1)
    qi = Method(query, 2)
    qj = Method(query, 3)
    qk = Method(query, 4)
    ql = Method(query, 5)
    qn = Method(query, 6)

    ws = Method(write, 0)
    wd = Method(write, 1)
    wi = Method(write, 2)
    wj = Method(write, 3)
    wk = Method(write, 4)
    wl = Method(write, 5)
    wn = Method(write, 6)

    wd0 = Method(wd, 0)
    wd1 = Method(wd, 1)
    wi0 = Method(wi, 0)
    wj0 = Method(wj, 0)


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
            'iterate_lines',            #   None | Generator
            'many',                     #   Tuple of *
            'append',                   #   Method
        ))


        def __init__(t):
            t.cadence = cadence_constructing

            t.iterate_lines = none
            t.many          = many                = []
            t.append        = many.append

            t.cadence = cadence_initialized


        def __enter__(t):
            assert t.cadence.is_initialized_exited_or_exception

            t.cadence = cadence_entered


        def __exit__(t, e_type, e, e_traceback):
            with exit_clause(e_type, e, e_traceback):
                cadence = t.cadence

                t.cadence = cadence_exception

                assert cadence is cadence_entered

                if e is none:
                   t.cadence = cadence_exited
                   return

                if type(e) is not UnknownLineException:
                    return

                wd0()
                t.append(e.unknown_line)

                return true


        def __iter__(t):
            loop = 0

            while t.cadence is not cadence_exited:
                yield loop
                loop += 1


        def reset(t, iterate_lines):
            assert t.cadence.is_initialized_exited_or_exception

            del t.many[:]

            t.iterate_lines = iterate_lines

            return t


    parse_context = ParseContext()


    @export
    def z_initialize(data):
        data_lines = data.splitlines(true)
        maximum_i  = length(data_lines)
        q_data     = data_lines.__getitem__


        def GENERATOR_next_line():
            for line_number in iterate_range(maximum_i):
                s = q_data(line_number)

                ws(s)
                wi0()
                wj0()
                wl(line_number)
                wk(none)
                wn(none)

                yield s

            wd(none)
            ws(none)
            wi(none)
            wj(none)
            wl(none)
            wk(none)
            wn(none)


        return parse_context.reset(GENERATOR_next_line())


    @export
    def raise_unknown_line():
        caller_frame = caller_frame_1()
        caller_name  = caller_frame.f_code.co_name

        line('%s #%s', caller_name, caller_frame.f_lineno)

        unknown_line_error = UnknownLineException(
                                 arrange('parse incomplete %s #%d', caller_name, caller_frame.f_lineno),
                                 UnknownLine(qs()),
                             )

        raising_exception(unknown_line_error)

        raise unknown_line_error


    export(
        'parse_context',    parse_context,

        'qd',               qd,
        'qi',               qi,
        'qj',               qj,
        'qk',               qk,
        'ql',               ql,
        'qn',               qn,
        'qs',               qs,

        'wd',               wd,
        'wd0',              wd0,
        'wd1',              wd1,
        'wi',               wi,
        'wj',               wj,
        'wk',               wk,
        'wn',               wn,
        'ws',               ws,
    )
