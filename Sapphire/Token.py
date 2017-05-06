#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Token')
def gem():
    @share
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


    @share
    class TokenNewline(Token):
        is_token_newline = true


    @share
    class UnknownLine(Token):
        pass
