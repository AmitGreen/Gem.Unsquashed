#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualToken')
def gem():
    require_gem('Sapphire.Elemental')


    class BaseDualOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',                    #   Operator+
            'second',                   #   Operator+
        ))


        line_marker = false
        newlines    = 0


        def __init__(t, s, first, second):
            assert '\n' not in s
            assert s == first.s + second.s

            t.s      = s
            t.first  = first
            t.second = second


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.first, t.second)


        def display_full_token(t):
            display_name = t.display_name
            first_s      = t.first.s
            second_s     = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            first_s  = t.first .s
            second_s = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def write(t, w):
            w(t.first.s + t.second.s)


    class Arguments_0(BaseDualOperator):
        __slots__                             = (())
        display_name                          = '(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true


    class Colon_RightSquareBracket(BaseDualOperator):
        __slots__                               = (())
        #   [
        display_name                            = ':]'
        is__colon__right_square_bracket         = true
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
        __slots__    = (())
        #   (
        display_name = ',)'


    class Comma_RightSquareBracket(BaseDualOperator):
        __slots__    = (())
        #   [
        display_name = ',]'


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


    @share
    class IsNot(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'is not'
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
    class NotIn(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'not in'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class RightParenthesis_Colon_LineMarker_1(BaseDualOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true
        line_marker                                = true
        newlines                                   = 1


        def __init__(t, s, first, second):
            assert s.count('\n') is 1
            assert s == first.s + second.s
            assert second.s[-1] == '\n'

            t.s      = s
            t.first  = first
            t.second = second


    def construct_dual_token__with_newlines(t, s, first, second, newlines, ends_in_newline):
        assert newlines >= 1
        assert ends_in_newline is (s[-1] == '\n')

        t.s               = s
        t.first           = first
        t.second          = second
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_dual_token__line_marker__many(t, s, first, second, newlines):
        assert newlines >= 1
        assert s[-1] == '\n'

        t.s        = s
        t.first    = first
        t.second   = second
        t.newlines = newlines


    def create_dual_token__with_newlines(Meta, first, second):
        s = intern_string(first.s + second.s)

        newlines = s.count('\n')

        return (
                   Meta(s, first, second)
                       if newlines is 0 else
                           (
                                 lookup_adjusted_meta(Meta)
                              or create_Meta_WithNewlines(Meta, construct_dual_token__with_newlines)
                           )(s, first, second, newlines, s[-1] == '\n')
               )


    def create_dual_token__line_marker(Meta, first, second):
        s = intern_string(first.s + second.s)

        newlines = s.count('\n')

        return (
                   Meta(s, first, second)
                       if newlines is 1 else
                       (
                             lookup_adjusted_meta(Meta)
                          or create_Meta_Many(Meta, construct_dual_token__line_marker__many)
                       )(s, first, second, newlines)
               )


    @privileged
    def produce_conjure_dual_token(name, Meta, line_marker = false):
        assert type(line_marker) is Boolean

        cache     = {}
        provide_1 = cache.setdefault
        lookup_1  = cache.get
        store_1   = cache.__setitem__

        create_dual_token = (
                create_dual_token__line_marker   if line_marker else
                create_dual_token__with_newlines
            )


        def conjure_dual_token(first, second):
            v = lookup_1(first)

            if v is none:
                return provide_1(first, create_dual_token(Meta, first, second))

            if type(v) is Map:
                return (v.get(second)) or (v.setdefault(second, create_dual_token(Meta, first, second)))

            if v.second is second:
                return v

            r = create_dual_token(Meta, first, second)

            store_1(first, { v.second : v , second : r })

            return r


        if __debug__:
            conjure_dual_token.__name__ = intern_arrange('conjure_%s', name)


        return conjure_dual_token


    conjure_arguments_0 = produce_conjure_dual_token('arguments_0', Arguments_0)

    conjure__colon__right_square_bracket = produce_conjure_dual_token(
            'conjure__colon__right_square_bracket',
            Colon_RightSquareBracket,
        )

    conjure__comma__right_brace       = produce_conjure_dual_token('comma__right_brace',       Comma_RightBrace)
    conjure__comma__right_parenthesis = produce_conjure_dual_token('comma__right_parenthesis', Comma_RightParenthesis)

    conjure__comma__right_square_bracket = produce_conjure_dual_token(
            'comma__right_square_bracket',
            Comma_RightSquareBracket,
        )

    conjure_empty_list  = produce_conjure_dual_token('empty_list',  EmptyList)
    conjure_empty_map   = produce_conjure_dual_token('empty_map',   EmptyMap)
    conjure_empty_tuple = produce_conjure_dual_token('empty_tuple', EmptyTuple)
    conjure_is_not      = produce_conjure_dual_token('is_not',      IsNot)

    conjure__left_square_bracket__colon = produce_conjure_dual_token(
            '[:',                           #   ]
            LeftSquareBracket_Colon,
        )

    conjure_not_in = produce_conjure_dual_token('not_in', NotIn)

    conjure__right_parenthesis__colon__line_marker = produce_conjure_dual_token(
            'right_parenthesis__colon__line_marker',
            RightParenthesis_Colon_LineMarker_1,
            true,
        )


    share(
        'conjure_arguments_0',                              conjure_arguments_0,
        'conjure__colon__right_square_bracket',             conjure__colon__right_square_bracket,
        'conjure__comma__right_brace',                      conjure__comma__right_brace,
        'conjure__comma__right_parenthesis',                conjure__comma__right_parenthesis,
        'conjure__comma__right_square_bracket',             conjure__comma__right_square_bracket,
        'conjure_empty_list',                               conjure_empty_list,
        'conjure_empty_map',                                conjure_empty_map,
        'conjure_empty_tuple',                              conjure_empty_tuple,
        'conjure_is_not',                                   conjure_is_not,
        'conjure__left_square_bracket__colon',              conjure__left_square_bracket__colon,
        'conjure_not_in',                                   conjure_not_in,
        'conjure__right_parenthesis__colon__line_marker',   conjure__right_parenthesis__colon__line_marker,
    )
