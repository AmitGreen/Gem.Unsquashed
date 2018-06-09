#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Sapphire.Atom')
def gem():
    require_gem('Sapphire.ClassOrder')
    require_gem('Sapphire.Method')


    lookup_adjusted_meta = Shared.lookup_adjusted_meta      #   due to privileged
    store_adjusted_meta  = Shared.store_adjusted_meta       #   due to privileged


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    def construct__quote_with_newlines(t, s, newlines):
        t.s        = s
        t.newlines = newlines


    def count_newlines__quote_with_newlines(t):
        assert t.s[-1] != '\n'
        assert t.ends_in_newline is t.line_marker is false
        assert t.newlines == t.s.count('\n')

        return t.newlines


    @privileged
    def produce_conjure_quote__with_newlines(name, Meta):
        def conjure_quote__with_newlines(s):
            assert s[-1] != '\n'

            r = lookup_atom(s)

            if r is not none:
                return r

            Quote_WithNewlines = lookup_adjusted_meta(Meta)

            if Quote_WithNewlines is none:
                class Quote_WithNewlines(Meta):
                    __slots__ = ((
                        'newlines',                                 #   Integer > 0
                    ))


                    __init__       = construct__quote_with_newlines
                    count_newlines = count_newlines__quote_with_newlines


                if __debug__:
                    Quote_WithNewlines.__name__ = intern_arrange('%s_WithNewlines', Meta.__name__)

                store_adjusted_meta(Meta, Quote_WithNewlines)

            s = intern_string(s)

            return provide_atom(s, Quote_WithNewlines(s, s.count('\n')))


        if __debug__:
            conjure_quote__with_newlines.__name__ = intern_arrange('conjure_%s__with_newlines', name)

        return conjure_quote__with_newlines


    @share
    def count_newlines__line_marker(t):
        assert (t.ends_in_newline is t.line_marker is true)
        assert t.s[-1] == '\n'
        assert t.newlines == t.s.count('\n')

        return t.newlines


    @share
    class DoubleQuote(PearlToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = '"'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false
        is_special_operator            = false


        def display_token(t):
            return arrange('<%s>', t.s)


        mutate          = mutate__self
        scout_variables = scout_variables__0


    class EndOfData(PearlToken):
        __slots__                        = (())
        indentation                      = none
        is_comment_line                  = false
        is_comment__or__empty_line       = false
        is_any_else                      = false
        is_any_except_or_finally         = false
        is_else_header_or_fragment       = false
        is_end_of_data                   = true
        is_end_of_data__or__unknown_line = true
        is_statement_header              = false


        def __repr__(t):
            return t.s


    @share
    class Identifier(PearlToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'Identifier'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_identifier                  = true
        is_right_brace                 = false
        is_special_operator            = false


        def add_parameters(t, art):
            art.add_parameter(t)


        def display_token(t):
            return t.s


        find_identifier = return_self


        def is_name(t, s):
            return t.s == s


        mutate = mutate__self


        scout_default_values = scout_default_values__0


        def scout_variables(t, art):
            art.fetch_variable(t)


        transform = transform__self


        def write_variables(t, art):
            art.write_variable(t)


        write_import = write_variables


    @share
    class Number(PearlToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'number'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false
        is_special_operator            = false


        def display_token(t):
            return t.s


        mutate          = mutate__self
        scout_variables = scout_variables__0


    @share
    class SingleQuote(PearlToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = "'"
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_brace                 = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false
        is_single_quote                = true
        is_special_operator            = false


        def display_token(t):
            return arrange('<%s>', t.s)


        mutate          = mutate__self
        scout_variables = scout_variables__0


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


    conjure_double_quote                = produce_conjure_atom                ('double-quote', DoubleQuote)
    conjure_double_quote__with_newlines = produce_conjure_quote__with_newlines('double-quote', DoubleQuote)
    conjure_name                        = produce_conjure_atom                ('name',         Identifier)
    conjure_number                      = produce_conjure_atom                ('number',       Number)
    conjure_single_quote                = produce_conjure_atom                ('single-quote', SingleQuote)
    conjure_single_quote__with_newlines = produce_conjure_quote__with_newlines('single-quote', SingleQuote)


    end_of_data = EndOfData(intern_string('<end-of-data>'))


    share(
        'conjure_double_quote',                 conjure_double_quote,
        'conjure_double_quote__with_newlines',  conjure_double_quote__with_newlines,
        'conjure_name',                         conjure_name,
        'conjure_number',                       conjure_number,
        'conjure_single_quote',                 conjure_single_quote,
        'conjure_single_quote__with_newlines',  conjure_single_quote__with_newlines,
        'end_of_data',                          end_of_data,
    )
