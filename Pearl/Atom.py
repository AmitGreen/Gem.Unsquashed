#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Pearl.Atom')
def gem():
    require_gem('Pearl.Method')
    require_gem('Pearl.Nub')


    def count_newlines__zero(t):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert (t.s is intern_string(t.s))

        return 0


    @export
    class PearlToken(Object):
        __slots__ = ((
            's',
        ))


        ends_in_newline                  = false
        herd_estimate                    = 0
        is_comma                         = false
        is_comment_line                  = false
        is_comment__or__empty_line       = false
        is_empty_line                    = false
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        is_herd                          = false
        is_identifier                    = false
        is_indentation                   = false
        is_keyword                       = false
        is_keyword_return                = false
        is_right_parenthesis             = false
        is_right_square_bracket          = false
        line_marker                      = false
        newlines                         = 0


        def __init__(t, s):
            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.s)


        count_newlines = count_newlines__zero


        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        def display_full_token(t):
            return arrange('<%s %s>', t.display_name, portray_string(t.s))


        def dump_token(t, f, newline = true):
            if t.ends_in_newline:
                if t.newlines is 1:
                    f.partial('{%s}', portray_string(t.s)[1:-1])
                else:
                    many = t.s.splitlines(true)

                    f.partial('{')

                    for s in many[:-1]:
                        f.line(portray_string(s)[1:-1])

                    f.partial('%s}', portray_string(many[-1])[1:-1])

                if newline:
                    f.line()
                    return false

                return true

            if t.newlines is 0:
                f.partial('{%s}', portray_string(t.s)[1:-1])
                return

            many = t.s.splitlines(true)

            f.partial('{')

            for s in many[:-1]:
                f.line(portray_string(s)[1:-1])

            f.partial('%s}', portray_string(many[-1])[1:-1])


        display_token = __repr__
        is_name       = is_name__0
        nub           = static_conjure_nub
        order         = order__s


        def write(t, w):
            w(t.s)
