#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Atom')
def gem():
    require_gem('Sapphire.TokenCache')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    @share
    class DoubleQuote(Token):
        __slots__                      = (())
        display_name                   = '"'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return arrange('<%s>', t.s)


    @share
    class Number(Token):
        __slots__                      = (())
        display_name                   = 'number'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return t.s


    @share
    class SingleQuote(Token):
        __slots__                      = (())
        display_name                   = "'"
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return arrange('<%s>', t.s)


    @share
    @privileged
    def produce_conjure_atom(name, Meta):
        assert type(name) is String
        assert type(Meta) is Type


        def conjure_atom(s):
            r = lookup_atom(s)

            if r is not none:
                return r

            assert s.count('\n') is 0

            s = intern_string(s)

            return provide_atom(s, Meta(s))


        if __debug__:
            conjure_atom.__name__ = intern_arrange('conjure_%s', name)


        return conjure_atom


    conjure_double_quote = produce_conjure_atom('double-quote', DoubleQuote)
    conjure_identifier   = produce_conjure_atom('identifier',   Identifier)
    conjure_number       = produce_conjure_atom('number',       Number)
    conjure_single_quote = produce_conjure_atom('single-quote', SingleQuote)


    share(
        'conjure_double_quote',     conjure_double_quote,
        'conjure_identifier',       conjure_identifier,
        'conjure_number',           conjure_number,
        'conjure_single_quote',     conjure_single_quote,
    )
