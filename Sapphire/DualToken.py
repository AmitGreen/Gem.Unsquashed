#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualToken')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Whitespace')


    create_ActionWord_WithNewlines = Shared.create_ActionWord_WithNewlines  #   Due to privileged
    lookup_adjusted_meta           = Shared.lookup_adjusted_meta            #   Due to privileged
    lookup_line_marker             = Shared.lookup_line_marker              #   Due to privileged
    lookup_normal_token            = Shared.lookup_normal_token             #   Due to privileged
    provide_line_marker            = Shared.provide_line_marker             #   Due to privileged
    provide_normal_token           = Shared.provide_normal_token            #   Due to privileged
    qi                             = Shared.qi                              #   Due to privileged
    qs                             = Shared.qs                              #   Due to privileged


    def construct_dual_token(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b


    def construct_dual_token__with_newlines(t, s, a, b, newlines, ends_in_newline):
        assert t.line_marker is false
        assert s == a.s + b.s
        assert ends_in_newline is (b.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a               = a
        t.b               = b
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_dual_operator__line_marker_1(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s
        assert s.count('\n') is 1
        assert b.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b


    def construct_dual_token__line_marker__many(t, s, a, b, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines >= 1)
        assert s == a.s + b.s
        assert s.count('\n') == newlines
        assert b.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.newlines = newlines


    class BaseDualOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
        ))


        def __init__(t, s, a, b):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s == a.s + b.s

            t.s = s
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def display_full_token(t):
            display_name = t.display_name
            a_s          = t.a.s
            b_s          = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a_s = t.a.s
            b_s = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


    class Arguments_0(BaseDualOperator):
        __slots__                             = (())
        display_name                          = '(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true


    class Atom_Whitespace(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'atom-whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Colon_RightSquareBracket(BaseDualOperator):
        __slots__                               = (())
        #   [
        display_name                            = ':]'
        is_colon__right_square_bracket          = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_comprehension_expression      = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_multiply_expression           = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true


    class Comma_RightBrace(BaseDualOperator):
        __slots__    = (())
        #   {
        display_name = ',}'


    class Comma_RightParenthesis(BaseDualOperator):
        __slots__                             = (())
        #   (
        display_name                          = ',)'
        is_end_of_arithmetic_expression       = true
        is_end_of_boolean_and_expression      = true
        is_end_of_boolean_or_expression       = true
        is_end_of_compare_expression          = true
        is_end_of_comprehension_expression    = true
        is_end_of_logical_and_expression      = true
        is_end_of_logical_or_expression       = true
        is_end_of_multiply_expression         = true
        is_end_of_normal_expression           = true
        is_end_of_ternary_expression          = true
        is_end_of_unary_expression            = true
        is__optional_comma__right_parenthesis = true


    class Comma_RightSquareBracket(BaseDualOperator):
        __slots__                                = (())
        #   [
        display_name                             = ',]'
        is_end_of_arithmetic_expression          = true
        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression              = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is__optional_comma__right_square_bracket = true


    class EmptyList(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '[,]'
        is__atom__or__special_operator = true
        is_atom                        = true


    class EmptyMap(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '{:}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class EmptyTuple(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Identifier_Whitespace(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'identifier-whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    @share
    class Is_Not(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'is-not'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class LeftSquareBracket_Colon(BaseDualOperator):
        __slots__           = (())
        display_name        = '[:'                             #   ]
        is_postfix_operator = true
        is_tail_index       = true


    @share
    class Not_In(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'not-in'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class KeywordReturn_LineMarker_1(BaseDualOperator):
        __slots__       = (())
        display_name    = r'return\n'
        ends_in_newline = true
        line_marker     = true
        newlines        = 1


        __init__ = construct_dual_operator__line_marker_1


    class RightParenthesis_Colon_LineMarker_1(BaseDualOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true
        line_marker                                = true
        newlines                                   = 1


        __init__ = construct_dual_operator__line_marker_1


    class Whitespace_Atom(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'whitespace-atom'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Whitespace_Identifier(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'whitespace-identifier'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    def create_dual_token__with_newlines(Meta, s, a, b):
        assert s == a.s + b.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 0 else
                           (
                                 lookup_adjusted_meta(Meta)
                              or create_ActionWord_WithNewlines(Meta, construct_dual_token__with_newlines)
                           )(s, a, b, newlines, s[-1] == '\n')
               )


    def create_dual_token__line_marker(Meta, s, a, b):
        assert (s == a.s + b.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 1 else
                       (
                             lookup_adjusted_meta(Meta)
                          or create_ActionWord_LineMarker_Many(Meta, construct_dual_token__line_marker__many)
                       )(s, a, b, newlines)
               )


    @privileged
    def produce_conjure_dual_token(
            name, Meta, conjure_first, conjure_second, conjure_second__ends_in_newline,
            
            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false,
    ):
        assert type(line_marker) is Boolean

        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_dual_token = create_dual_token__line_marker
            lookup            = lookup_line_marker
            provide           = provide_line_marker
        else:
            create_dual_token = create_dual_token__with_newlines


        def conjure_dual_token(middle, end):
            full = qs()[qi() : end]

            r = lookup(full)
           
            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            return provide(
                       full,
                       create_dual_token(
                           Meta,
                           full,
                           conjure_first(s[qi() : middle]),
                           (conjure_second__ends_in_newline   if end is none else   conjure_second)(s[middle : end]),
                       ),
                   )


        if __debug__:
            conjure_dual_token.__name__ = intern_arrange('conjure_%s', name)


        return conjure_dual_token


    @privileged
    def produce_evoke_dual_token(
            name, Meta,
            
            lookup  = lookup_normal_token,
            provide = provide_normal_token,
    ):
        def evoke_dual_token(a, b):
            s = a.s + b.s

            r = lookup(s)

            if r is not none:
                if not ((r.a is a) and (r.b is b)):
                    my_line('s: %r; a: %r; b: %r; r: %r; T1: %r; T2: %r', s, a, b, r, r.a is a, r.b is b)

                assert (r.a is a) and (r.b is b)

                return r

            s = intern_string(s)

            return provide(s, create_dual_token__with_newlines(Meta, s, a, b))


        if __debug__:
            evoke_dual_token.__name__ = intern_arrange('evoke_%s', name)

        return evoke_dual_token


    @privileged
    def produce_insert_dual_token(
            name, Meta,
            
            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false,
    ):
        assert type(line_marker) is Boolean

        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_dual_token = create_dual_token__line_marker
            lookup            = lookup_line_marker
            provide           = provide_line_marker
        else:
            create_dual_token = create_dual_token__with_newlines


        def insert_dual_token(s, a, b):
            assert (s == a.s + b.s) and (lookup(s) is none)

            s = intern_string(s)

            return provide(s, create_dual_token(Meta, s, a, b))


        if __debug__:
            insert_dual_token.__name__ = intern_arrange('insert_%s', name)

        return insert_dual_token


    conjure__colon__right_square_bracket = produce_conjure_dual_token(
                                               'colon__right_square_bracket',
                                               Colon_RightSquareBracket,
                                               conjure_colon,
                                               conjure_right_square_bracket,
                                               conjure_right_square_bracket__ends_in_newline,
                                           )

    conjure_arguments_0 = produce_conjure_dual_token(
                              'arguments_0',
                              Arguments_0,
                              conjure_left_parenthesis,
                              conjure_right_parenthesis,
                              conjure_right_parenthesis__ends_in_newline,

                              lookup  = lookup_arguments_0_token,
                              provide = provide_arguments_0_token,
                          )

    conjure__comma__right_brace = produce_conjure_dual_token(
                                      'comma__right_brace',
                                      Comma_RightBrace,
                                      conjure_comma,
                                      conjure_right_brace,
                                      conjure_right_brace__ends_in_newline,
                                  )

    conjure__comma__right_square_bracket = produce_conjure_dual_token(
                                               'comma__right_square_bracket',
                                               Comma_RightSquareBracket,
                                               conjure_comma,
                                               conjure_right_square_bracket,
                                               conjure_right_square_bracket__ends_in_newline,
                                           )

    conjure__comma__right_parenthesis = produce_conjure_dual_token(
                                            'comma__right_parenthesis',
                                            Comma_RightParenthesis,
                                            conjure_comma,
                                            conjure_right_parenthesis,
                                            conjure_right_parenthesis__ends_in_newline,
                                        )

    conjure__double_quote__whitespace = produce_conjure_dual_token(
                                            'double-quote-whitespace',
                                            Atom_Whitespace,
                                            conjure_double_quote,
                                            conjure_whitespace,
                                            conjure_whitespace__ends_in_newline,
                                        )

    conjure_empty_list = produce_conjure_dual_token(
                             '[]',
                             EmptyList,
                             conjure_left_square_bracket,
                             conjure_right_square_bracket,
                             conjure_right_square_bracket__ends_in_newline,
                         )

    conjure_empty_map = produce_conjure_dual_token(
                            '{}',
                            EmptyMap,
                            conjure_left_brace,
                            conjure_right_brace,
                            conjure_right_brace__ends_in_newline,
                        )

    conjure_empty_tuple = produce_conjure_dual_token(
                              '()',
                              EmptyTuple,
                              conjure_left_parenthesis,
                              conjure_right_parenthesis,
                              conjure_right_parenthesis__ends_in_newline,
                          )

    conjure_identifier_whitespace = produce_conjure_dual_token(
                                        'identifier-whitespace',
                                        Identifier_Whitespace,
                                        conjure_identifier,
                                        conjure_whitespace,
                                        conjure_whitespace__ends_in_newline,
                                    )

    conjure_number_whitespace = produce_conjure_dual_token(
                                   'number-whitespace',
                                   Atom_Whitespace,
                                   conjure_number,
                                   conjure_whitespace,
                                   conjure_whitespace__ends_in_newline,
                                )

    conjure_is_not = produce_conjure_dual_token(
                        'is_not',
                        Is_Not,
                        conjure_keyword_is,
                        conjure_keyword_not,
                        conjure_keyword_not__ends_in_newline,
                    )

    conjure__left_square_bracket__colon = produce_conjure_dual_token(
                                              '[:',                           #   ]
                                              LeftSquareBracket_Colon,
                                              conjure_left_square_bracket,
                                              conjure_colon,
                                              conjure_colon__ends_in_newline,
                                          )

    conjure_not_in = produce_conjure_dual_token(
                        'not_in',
                        Not_In,
                        conjure_keyword_not,
                        conjure_keyword_in,
                        conjure_keyword_in__ends_in_newline,
                    )

    conjure__single_quote__whitespace = produce_conjure_dual_token(
                                            'single-quote-whitespace',
                                            Atom_Whitespace,
                                            conjure_single_quote,
                                            conjure_whitespace,
                                            conjure_whitespace__ends_in_newline,
                                        )

    evoke_arguments_0 = produce_evoke_dual_token(
                            'arguments_0',
                            Arguments_0,

                            lookup  = lookup_arguments_0_token,
                            provide = provide_arguments_0_token,
                        )

    evoke__colon__right_square_bracket = produce_evoke_dual_token(
                                             'colon__right_square_bracket',
                                             Colon_RightSquareBracket,
                                         )

    evoke__comma__right_brace = produce_evoke_dual_token('comma__right_brace', Comma_RightBrace)

    evoke__comma__right_parenthesis = produce_evoke_dual_token(
                                          'comma__right_parenthesis',
                                          Comma_RightParenthesis,
                                      )

    evoke__comma__right_square_bracket = produce_evoke_dual_token(
                                             'comma__right_square_bracket',
                                             Comma_RightSquareBracket,
                                         )

    evoke_empty_list            = produce_evoke_dual_token('[]',                    EmptyList)
    evoke_empty_map             = produce_evoke_dual_token('{}',                    EmptyMap)
    evoke_identifier_whitespace = produce_evoke_dual_token('identifier-whitespace', Identifier_Whitespace)

    evoke__left_square_bracket__colon = produce_evoke_dual_token(
                                            '[:',                           #   ]
                                            LeftSquareBracket_Colon,
                                        )

    evoke_whitespace_atom       = produce_evoke_dual_token('whitespace-atom',       Whitespace_Atom)
    evoke_whitespace_identifier = produce_evoke_dual_token('whitespace-identifier', Whitespace_Identifier)

    insert_return__line_marker = produce_insert_dual_token(
                                    'return__line_marker',
                                    KeywordReturn_LineMarker_1,

                                    line_marker = true,
                                 )


    find_conjure_comma_something = {
                                       #   (
                                       ')' : conjure__comma__right_parenthesis,

                                       #   [
                                       ']' : conjure__comma__right_square_bracket,
                                   }.__getitem__

    find_conjure_atom_whitespace = {
                                       '"' : conjure__double_quote__whitespace,
                                       "'" : conjure__single_quote__whitespace,

                                       '.' : conjure_number_whitespace,
                                       '0' : conjure_number_whitespace, '1' : conjure_number_whitespace,
                                       '2' : conjure_number_whitespace, '3' : conjure_number_whitespace,
                                       '4' : conjure_number_whitespace, '5' : conjure_number_whitespace,
                                       '6' : conjure_number_whitespace, '7' : conjure_number_whitespace,
                                       '8' : conjure_number_whitespace, '9' : conjure_number_whitespace,

                                       'A' : conjure_identifier_whitespace, 'B' : conjure_identifier_whitespace,
                                       'C' : conjure_identifier_whitespace, 'D' : conjure_identifier_whitespace,
                                       'E' : conjure_identifier_whitespace, 'F' : conjure_identifier_whitespace,
                                       'G' : conjure_identifier_whitespace, 'H' : conjure_identifier_whitespace,
                                       'I' : conjure_identifier_whitespace, 'J' : conjure_identifier_whitespace,
                                       'K' : conjure_identifier_whitespace, 'L' : conjure_identifier_whitespace,
                                       'M' : conjure_identifier_whitespace, 'N' : conjure_identifier_whitespace,
                                       'O' : conjure_identifier_whitespace, 'P' : conjure_identifier_whitespace,
                                       'Q' : conjure_identifier_whitespace, 'R' : conjure_identifier_whitespace,
                                       'S' : conjure_identifier_whitespace, 'T' : conjure_identifier_whitespace,
                                       'U' : conjure_identifier_whitespace, 'V' : conjure_identifier_whitespace,
                                       'W' : conjure_identifier_whitespace, 'X' : conjure_identifier_whitespace,
                                       'Y' : conjure_identifier_whitespace, 'Z' : conjure_identifier_whitespace,
                                       '_' : conjure_identifier_whitespace,

                                       'a' : conjure_identifier_whitespace, 'b' : conjure_identifier_whitespace,
                                       'c' : conjure_identifier_whitespace, 'd' : conjure_identifier_whitespace,
                                       'e' : conjure_identifier_whitespace, 'f' : conjure_identifier_whitespace,
                                       'g' : conjure_identifier_whitespace, 'h' : conjure_identifier_whitespace,
                                       'i' : conjure_identifier_whitespace, 'j' : conjure_identifier_whitespace,
                                       'k' : conjure_identifier_whitespace, 'l' : conjure_identifier_whitespace,
                                       'm' : conjure_identifier_whitespace, 'n' : conjure_identifier_whitespace,
                                       'o' : conjure_identifier_whitespace, 'p' : conjure_identifier_whitespace,
                                       'q' : conjure_identifier_whitespace, 'r' : conjure_identifier_whitespace,
                                       's' : conjure_identifier_whitespace, 't' : conjure_identifier_whitespace,
                                       'u' : conjure_identifier_whitespace, 'v' : conjure_identifier_whitespace,
                                       'w' : conjure_identifier_whitespace, 'x' : conjure_identifier_whitespace,
                                       'y' : conjure_identifier_whitespace, 'z' : conjure_identifier_whitespace,
                                    }.__getitem__

    static_evoke_whitespace_atom = static_method(evoke_whitespace_atom)

    Identifier .evoke_whitespace_atom = static_method(evoke_whitespace_identifier)
    DoubleQuote.evoke_whitespace_atom = static_evoke_whitespace_atom
    SingleQuote.evoke_whitespace_atom = static_evoke_whitespace_atom
    Number     .evoke_whitespace_atom = static_evoke_whitespace_atom


    share(
        'conjure_arguments_0',                      conjure_arguments_0,
        'conjure__colon__right_square_bracket',     conjure__colon__right_square_bracket,
        'conjure__comma__right_brace',              conjure__comma__right_brace,
        'conjure__comma__right_parenthesis',        conjure__comma__right_parenthesis,
        'conjure_empty_list',                       conjure_empty_list,
        'conjure_empty_map',                        conjure_empty_map,
        'conjure_empty_tuple',                      conjure_empty_tuple,
        'conjure_identifier_whitespace',            conjure_identifier_whitespace,
        'conjure_is_not',                           conjure_is_not,
        'conjure__left_square_bracket__colon',      conjure__left_square_bracket__colon,
        'conjure_not_in',                           conjure_not_in,
        'evoke_arguments_0',                        evoke_arguments_0,
        'evoke__comma__right_brace',                evoke__comma__right_brace,
        'evoke__comma__right_parenthesis',          evoke__comma__right_parenthesis,
        'evoke__comma__right_square_bracket',       evoke__comma__right_square_bracket,
        'evoke_empty_list',                         evoke_empty_list,
        'evoke_empty_map',                          evoke_empty_map,
        'evoke_identifier_whitespace',              evoke_identifier_whitespace,
        'evoke__left_square_bracket__colon',        evoke__left_square_bracket__colon,
        'evoke_whitespace_identifier',              evoke_whitespace_identifier,
        'evoke_whitespace_identifier',              evoke_whitespace_identifier,
        'find_conjure_atom_whitespace',             find_conjure_atom_whitespace,
        'find_conjure_comma_something',             find_conjure_comma_something,
        'insert_return__line_marker',               insert_return__line_marker,
    )
