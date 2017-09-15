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


        ends_in_newline         = false
        is_comma                = false
        is_identifier           = false
        is_keyword              = false
        is_right_parenthesis    = false
        is_right_square_bracket = false
        newlines                = 0
        line_marker             = false


        def __init__(t, s):
#           assert '\n' not in s

            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.display_name, t.s)


        def display_full_token(t):
            return arrange('<%s %s>', t.display_name, portray_string(t.s))


        display_token = __repr__


        def write(t, w):
            w(t.s)


    @export
    class Identifier(Token):
        __slots__ = (())


        display_name                          = 'Identifier'
        is__atom__or__special_operator        = true
        is_atom                               = true
        is_colon                              = false
        is_identifier                         = true
        is_right_brace                        = false
        is__right_parenthesis__colon__newline = false


        def display_token(t):
            return t.s


    @export
    class TokenIndented(Token):
        display_name      = 'indented'
        is_token_indented = true


    class TokenWhitespace(Token):
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


    class TokenWhitespaceLine(Token):
        display_name = 'whitespace-line'


        def __init__(t, s):
            assert '\n' in s

            t.s = s


    @export
    class UnknownLine(Token):
        display_name    = 'unknown-line'
        ends_in_newline = true


        def __init__(t, s):
            assert '\n' not in s[:-1]
            assert s[-1] == '\n'

            t.s = s



    [
            conjure_identifier, lookup_identifier,
    ] = produce_cache_functions(
            'identifier', Identifier,

            produce_conjure_by_name = true,
            produce_lookup          = true,
        )


    conjure_whitespace      = produce_conjure_by_name('whitespace',      TokenWhitespace)
    conjure_whitespace_line = produce_conjure_by_name('whitespace_line', TokenWhitespaceLine)


    export(
        'conjure_identifier',       conjure_identifier,
        'conjure_whitespace',       conjure_whitespace,
        'conjure_whitespace_line',  conjure_whitespace_line,
        'lookup_identifier',        lookup_identifier,
    )
