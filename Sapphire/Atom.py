#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Atom')
def gem():
    require_gem('Sapphire.TokenCache')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    @export
    class SapphireToken(Object):
        __slots__ = ((
            's',
        ))


        ends_in_newline         = false
        is_comma                = false
        is_identifier           = false
        is_keyword              = false
        is_right_parenthesis    = false
        is_right_square_bracket = false
        is_token_indentation    = false
        line_marker             = false
        newlines                = 0


        def __init__(t, s):
            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.s)


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert (t.s is intern_string(t.s))

            return 0

            
        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        def display_full_token(t):
            return arrange('<%s %s>', t.display_name, portray_string(t.s))


        display_token = __repr__


        def write(t, w):
            w(t.s)


    @share
    class DoubleQuote(SapphireToken):
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
    class Identifier(SapphireToken):
        __slots__                             = (())
        display_name                          = 'Identifier'
        is__atom__or__special_operator        = true
        is_atom                               = true
        is_colon                              = false
        is_identifier                         = true
        is_right_brace                        = false
        is__right_parenthesis__colon__newline = false


        def display_token(t):
            return t.s


    @share
    class Number(SapphireToken):
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
    class SingleQuote(SapphireToken):
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
    conjure_name         = produce_conjure_atom('name',         Identifier)
    conjure_number       = produce_conjure_atom('number',       Number)
    conjure_single_quote = produce_conjure_atom('single-quote', SingleQuote)


    share(
        'conjure_double_quote',     conjure_double_quote,
        'conjure_name',             conjure_name,
        'conjure_number',           conjure_number,
        'conjure_single_quote',     conjure_single_quote,
    )
