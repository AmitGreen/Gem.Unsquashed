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


        def write(t, w):
            w(t.s)


    @share
    class Identifier(Token):
        __slots__ = (())


        is_identifier = true


        def __repr__(t):
            return t.s


    [
            conjure_identifier, insert_interned_identifier, lookup_identifier,
    ] = produce_cache_functions(
            'Pearl.Token.identifier_cache', Identifier,

            produce_conjure_by_name = true,
            produce_insert_interned = true,
            produce_lookup          = true,
        )


    @export
    class TokenIndented(Token):
        display_name      = 'indented'
        is_token_indented = true


    @export
    class UnknownLine(Token):
        display_name = 'unknown-line'


    export(
        'conjure_identifier',           conjure_identifier,
        'insert_interned_identifier',   insert_interned_identifier,
        'lookup_identifier',            lookup_identifier,
    )