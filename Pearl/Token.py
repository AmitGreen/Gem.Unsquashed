#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Token')
def gem():
    @export
    class Token(Object):
        __slots__ = ((
            's',
        ))


        is_comma             = false
        is_keyword           = false
        is_right_parenthesis = false


        def __init__(t, s):
            assert type(s) is String

            t.s = s


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, portray_string(t.s))


        def write(t, w):
            w(t.s)


    @export
    class TokenNewline(Token):
        is_token_newline = true


    @export
    class UnknownLine(Token):
        pass
