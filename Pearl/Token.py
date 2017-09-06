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
        is_identifier        = false
        is_keyword           = false
        is_right_parenthesis = false


        def __init__(t, s):
            assert type(s) is String

            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.display_name, t.s)


        display_token = __repr__


        def write(t, w):
            w(t.s)


    @export
    class Identifier(Token):
        __slots__ = (())


        display_name                          = 'Identifier'
        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is_identifier                         = true
        is_right_parenthesis                  = false
        is__right_parenthesis__colon__newline = false


        def display_token(t):
            return t.s


    @export
    class TokenIndented(Token):
        display_name      = 'indented'
        is_token_indented = true


    class TokenWhitespace(Token):
        display_name = 'whitespace'


    @export
    class UnknownLine(Token):
        display_name = 'unknown-line'


    [
            conjure_identifier, lookup_identifier,
    ] = produce_cache_functions(
            'identifier', Identifier,

            produce_conjure_by_name = true,
            produce_lookup          = true,
        )


    conjure_whitespace = produce_conjure_by_name('whitespace', TokenWhitespace)


    export(
        'conjure_identifier',   conjure_identifier,
        'conjure_whitespace',   conjure_whitespace,
        'lookup_identifier',    lookup_identifier,
    )
