#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Elemental')
def gem():
    require_gem('Sapphire.ActionWord')
    require_gem('Sapphire.LineMarker')


    def construct_action_word__line_marker_1(t, s):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert (s.count('\n') is 1) and (s[-1] == '\n')

        t.s = s


    @share
    class KeywordAndOperatorBase(Token):
        is_all_index                               = false
        is__any__right_parenthesis__colon__newline = false
        is_arguments_0                             = false
        is__arguments_0__or__left_parenthesis      = false
        is_arithmetic_operator                     = false
        is_atom                                    = false
        is__atom__or__special_operator             = false
        is_colon                                   = false
        is_colon__line_marker                      = false
        is_colon__right_square_bracket             = false
        is_comma                                   = false
        is__comma__or__right_parenthesis           = false
        is_comma__right_square_bracket             = false
        is_compare_operator                        = false
        is_dot                                     = false
        is_end_of_arithmetic_expression            = false
        is_end_of_boolean_and_expression           = false
        is_end_of_boolean_or_expression            = false
        is_end_of_compare_expression               = false
        is_end_of_comprehension_expression         = false
        is_end_of_comprehension_expression_list    = false
        is_end_of_logical_and_expression           = false
        is_end_of_logical_or_expression            = false
        is_end_of_multiply_expression              = false
        is_end_of_normal_expression                = false
        is_end_of_normal_expression_list           = false
        is_end_of_ternary_expression               = false
        is_end_of_ternary_expression_list          = false
        is_end_of_unary_expression                 = false
        is_equal_sign                              = false
        is_keyword_and                             = false
        is_keyword_as                              = false
        is_keyword_else                            = false
        is_keyword_for                             = false
        is_keyword_if                              = false
        is_keyword_in                              = false
        is_keyword_not                             = false
        is_keyword_or                              = false
        is_left_brace                              = false
        is_left_parenthesis                        = false
        is_left_square_bracket                     = false
        is_logical_and_operator                    = false
        is_logical_or_operator                     = false
        is_minus_sign                              = false
        is_modify_operator                         = false
        is_multiply_operator                       = false
        is__optional_comma__right_parenthesis      = false
        is__optional_comma__right_square_bracket   = false
        is__parameter_0__colon__line_marker        = false
        is_postfix_operator                        = false
        is_power_operator                          = false
        is_right_brace                             = false
        is__right_parenthesis__colon               = false
        is__right_parenthesis__colon__newline      = false
        is_right_parenthesis                       = false
        is_right_square_bracket                    = false
        is_star_sign                               = false
        is_tail_index                              = false
        is_tilde_sign                              = false
        is_token_newline                           = false


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, portray_string(t.s))


        def display_token(t):
            if t.s == t.display_name:
                return arrange('<%s>', t.display_name)

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


    class KeywordAnd(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'and'
        is_end_of_arithmetic_expression  = true
        is_end_of_compare_expression     = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_and                   = true
        keyword                          = 'and'


    class KeywordAs(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = 'as'
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
        is_keyword_as                           = true
        keyword                                 = 'as'


    class KeywordAssert(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'assert'
        keyword      = 'assert'


    @export
    class KeywordClass(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'class'
        keyword      = 'class'


    class KeywordDelete(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'delete'
        keyword      = 'del'


    class KeywordElse(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'else'
        is_end_of_arithmetic_expression  = true
        is_end_of_boolean_and_expression = true
        is_end_of_boolean_or_expression  = true
        is_end_of_compare_expression     = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_else                  = true
        keyword                          = 'else'


    class KeywordElseColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'else:'
        keyword      = 'else:'


    class KeywordElseColon_LineMarker_1(KeywordAndOperatorBase):
        __slots__       = (())
        display_name    = r'else:\n'
        ends_in_newline = true
        keyword         = r'else:\n'
        line_marker     = true
        newlines        = 1


        __init__ = construct_action_word__line_marker_1


    class KeywordElseIf(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'else-if'
        keyword      = 'elif'


    class KeywordExcept(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'except'
        keyword      = 'except'


    class KeywordExceptColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'except:'
        keyword      = 'except:'


    class KeywordExceptColon_LineMarker_1(KeywordAndOperatorBase):
        __slots__       = (())
        display_name    = r'except:\n'
        ends_in_newline = true
        keyword         = r'except:\n'
        line_marker     = true
        newlines        = 1


        __init__ = construct_action_word__line_marker_1


    class KeywordFinallyColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'finally:'
        keyword      = 'finally:'


    class KeywordFinallyColon_LineMarker_1(KeywordAndOperatorBase):
        __slots__       = (())
        display_name    = r'finally:\n'
        ends_in_newline = true
        keyword         = r'finally:\n'
        line_marker     = true
        newlines        = 1


        __init__ = construct_action_word__line_marker_1


    class KeywordFor(KeywordAndOperatorBase):
        __slots__                         = (())
        display_name                      = 'for'
        is_end_of_arithmetic_expression   = true
        is_end_of_boolean_and_expression  = true
        is_end_of_boolean_or_expression   = true
        is_end_of_compare_expression      = true
        is_end_of_logical_and_expression  = true
        is_end_of_logical_or_expression   = true
        is_end_of_multiply_expression     = true
        is_end_of_normal_expression_list  = true
        is_end_of_normal_expression       = true
        is_end_of_ternary_expression      = true
        is_end_of_ternary_expression_list = true        #   Not really, but for consistency
        is_end_of_unary_expression        = true
        is_keyword_for                    = true
        keyword                           = 'for'


    @export
    class KeywordFrom(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'from'
        keyword      = 'from'


    @export
    class KeywordFunction(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'function'
        keyword      = 'def'


    class KeywordIf(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'if'
        is_end_of_arithmetic_expression  = true
        is_end_of_boolean_and_expression = true
        is_end_of_boolean_or_expression  = true
        is_end_of_compare_expression     = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_if                    = true
        keyword                          = 'if'


    @share
    class KeywordIn(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'in'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_in                    = true
        keyword                          = 'in'


    @share
    class KeywordIs(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'is'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = 'is'


    @export
    class KeywordImport(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'import'
        keyword      = 'import'


    class KeywordNot(KeywordAndOperatorBase):
        __slots__      = (())
        display_name   = 'not'
        is_keyword_not = true
        keyword        = 'not'


        #
        #   NOTE:
        #       The following are actually being set for the 'not in' keyword, which the 'not' keyword is a
        #       sub-part of.
        #
        #       This means than when [partially] parsing the 'not in' keyword by just parsing the first keyword,
        #       it will still be treated properly in expression parsing (which has not yet parsed the following
        #       'in' keyword).
        #
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class KeywordOr(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'or'
        is_end_of_arithmetic_expression  = true
        is_end_of_boolean_and_expression = true
        is_end_of_compare_expression     = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_or                    = true
        keyword                          = 'or'


    class KeywordRaise(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'raise'
        keyword      = 'raise'


    class KeywordRaise_LineMarker_1(KeywordAndOperatorBase):
        __slots__       = (())
        display_name    = r'raise\n'
        ends_in_newline = true
        keyword         = r'raise\n'
        line_marker     = true
        newlines        = 1


        __init__ = construct_action_word__line_marker_1


    class KeywordReturn(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'return'
        keyword      = 'return'


    class KeywordTryColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'try:'
        keyword      = 'try:'


    class KeywordTryColon_LineMarker_1(KeywordAndOperatorBase):
        __slots__       = (())
        display_name    = r'try:\n'
        ends_in_newline = true
        keyword         = r'try:\n'
        line_marker     = true
        newlines        = 1


        __init__ = construct_action_word__line_marker_1


    class KeywordWhile(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'while'
        keyword      = 'while'


    @share
    class KeywordWith(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'with'
        keyword      = 'with'


    @share
    class KeywordYield(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'yield'
        keyword      = 'yield'


    class OperatorAddModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '+='
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
        is_equal_sign                           = true
        is_modify_operator                      = true
        keyword                                 = '+='


    @export
    class OperatorAtSign(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '@'
        keyword      = '@'


    class OperatorColon(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = ':'
        is_colon                                = true
        is__atom__or__special_operator          = true
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
        is_end_of_ternary_expression            = true
        is_end_of_ternary_expression_list       = true
        is_end_of_unary_expression              = true
        keyword                                 = ':'


    class OperatorColon_LineMarker_1(KeywordAndOperatorBase):
        __slots__                               = (())
        is_colon__line_marker                   = true
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
        is_end_of_ternary_expression            = true
        is_end_of_ternary_expression_list       = true
        is_end_of_unary_expression              = true
        keyword                                 = r'colon:\n'
        ends_in_newline                         = true
        line_marker                             = true
        newlines                                = 1


        __init__ = construct_action_word__line_marker_1



        def __repr__(t):
            return arrange('<OperatorColon_LineMarker_1 %s>', portray_raw_string(t.s))


        def display_token(t):
            return portray_raw_string(t.s)


    class OperatorComma(KeywordAndOperatorBase):
        __slots__                          = (())
        display_name                       = ','
        is__comma__or__right_parenthesis   = true
        is_comma                           = true
        is_end_of_arithmetic_expression    = true
        is_end_of_boolean_and_expression   = true
        is_end_of_boolean_or_expression    = true
        is_end_of_comprehension_expression = true
        is_end_of_compare_expression       = true
        is_end_of_logical_and_expression   = true
        is_end_of_logical_or_expression    = true
        is_end_of_multiply_expression      = true
        is_end_of_normal_expression        = true
        is_end_of_ternary_expression       = true
        is_end_of_unary_expression         = true
        frill_estimate                     = 1
        keyword                            = ','


    @share
    class OperatorCompareEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '=='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '=='


        def display_token(t):
            if t.s == ' == ':
                return '=='

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


    @share
    class OperatorCompareNotEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '!='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '!='


    @share
    class OperatorDivide(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '/'
        is_multiply_operator       = true
        is_end_of_unary_expression = true
        keyword                    = '/'


    class OperatorDot(KeywordAndOperatorBase):
        __slots__           = (())
        display_name        = '.'
        is_dot              = true
        is_postfix_operator = true
        keyword             = '.'


    class OperatorEqualSign(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '='
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
        is_equal_sign                           = true
        keyword                                 = '='


    @share
    class OperatorGreaterThan(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '>'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '>'


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' > ':
                return '{>}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorGreaterThanOrEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '>='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '>='


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' > ':
                return '{>}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorIntegerDivide(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '//'
        is_multiply_operator       = true
        is_end_of_unary_expression = true
        keyword                    = '//'


    class OperatorLeftBrace(KeywordAndOperatorBase):
        __slots__     = (())
        display_name  = '{'                                 #   }
        is_atom       = false
        is_left_brace = true
        keyword       = '{'                                 #   }


    class OperatorLeftParenthesis(KeywordAndOperatorBase):
        __slots__                             = (())
        display_name                          = '('         #   )
        is__arguments_0__or__left_parenthesis = true
        is_atom                               = false
        is_left_parenthesis                   = true
        is_postfix_operator                   = true
        keyword                               = '('         #   )


    @export
    class OperatorLeftSquareBracket(KeywordAndOperatorBase):
        __slots__              = (())
        display_name           = '['                        #   ]
        is_left_square_bracket = true
        is_postfix_operator    = true
        keyword                = '['                        #   ]


    @share
    class OperatorLessThan(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '<'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '<'


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' < ':
                return '{<}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorLessThanOrEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '<='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_multiply_expression    = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '<='


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' <= ':
                return '{<=}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorLogicalAndSign(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '&'
        is_logical_and_operator          = true
        is_end_of_unary_expression       = true
        is_end_of_multiply_expression    = true
        is_end_of_arithmetic_expression  = true
        keyword                          = '&'


    @share
    class OperatorLogicalOrSign(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '|'
        is_logical_or_operator           = true
        is_end_of_unary_expression       = true
        is_end_of_multiply_expression    = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        keyword                          = '|'


    class OperatorLogicalOrModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '|='
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
        is_equal_sign                           = true
        is_modify_operator                      = true
        keyword                                 = '|='


    @share
    class OperatorMinusSign(KeywordAndOperatorBase):
        __slots__                     = (())
        display_name                  = '-'
        is_minus_sign                 = true
        is_end_of_unary_expression    = true
        is_end_of_multiply_expression = true
        is_arithmetic_operator        = true
        keyword                       = '-'


    @share
    class OperatorPercentSign(KeywordAndOperatorBase):
        __slots__                     = (())
        display_name                  = '%'
        is_multiply_operator          = true
        is_end_of_unary_expression    = true
        keyword                       = '%'


    @share
    class OperatorPower(KeywordAndOperatorBase):
        __slots__         = (())
        display_name      = '**'
        is_power_operator = true
        keyword           = '**'


    @share
    class OperatorPlusSign(KeywordAndOperatorBase):
        __slots__                     = (())
        display_name                  = '+'
        is_arithmetic_operator        = true
        is_end_of_unary_expression    = true
        is_end_of_multiply_expression = true
        keyword                       = '+'


    class OperatorRightBrace(KeywordAndOperatorBase):
        __slots__                               = (())
        #  {
        display_name                            = '}'
        is__atom__or__special_operator          = true
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
        is_right_brace                          = true
        #  {
        keyword                                 = '}'


    class OperatorRightParenthesis(KeywordAndOperatorBase):
        __slots__                               = (())
        #  (
        display_name                            = ')'
        is__atom__or__special_operator          = true
        is__comma__or__right_parenthesis        = true
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
        is__optional_comma__right_parenthesis   = true
        is_right_parenthesis                    = true
        #  (
        keyword                                 = ')'


    @export
    class OperatorRightParenthesisColon(KeywordAndOperatorBase):
        __slots__                    = (())
        #  ([
        display_name                 = '):'
        is__right_parenthesis__colon = true
        #  ([
        keyword                      = '):'


    @export
    class OperatorRightSquareBracket(KeywordAndOperatorBase):
        __slots__                                = (())
        #   [
        display_name                             = ']'
        is__optional_comma__right_square_bracket = true
        is__atom__or__special_operator           = true
        is_end_of_arithmetic_expression          = true
        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression_list  = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression_list         = true
        is_end_of_normal_expression              = true
        is_end_of_ternary_expression_list        = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is_right_square_bracket                  = true
        #   [
        keyword                                  = ']'


    @share
    class OperatorStarSign(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '*'
        is_end_of_unary_expression = true
        is_multiply_operator       = true
        is_star_sign               = true
        keyword                    = '*'


    class OperatorSubtractModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '-='
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
        is_equal_sign                           = true
        is_modify_operator                      = true
        keyword                                 = '-='


    @share
    class OperatorTildeSign(KeywordAndOperatorBase):
        __slots__     = (())
        display_name  = '~'
        is_tilde_sign = true
        keyword       = '~'


    initialize_action_word__Meta(
        ((
             ((     '!=',       OperatorCompareNotEqual     )),
             ((     '&',        OperatorLogicalAndSign      )),
             ((     '%',        OperatorPercentSign         )),
             ((     '(',        OperatorLeftParenthesis     )),
             ((     ')',        OperatorRightParenthesis    )),
             ((     '*',        OperatorStarSign            )),
             ((     '**',       OperatorPower               )),
             ((     '+',        OperatorPlusSign            )),
             ((     '+=',       OperatorAddModify           )),
             ((     ',',        OperatorComma               )),
             ((     '-',        OperatorMinusSign           )),
             ((     '-=',       OperatorSubtractModify      )),
             ((     '.',        OperatorDot                 )),
             ((     '/',        OperatorDivide              )),
             ((     '//',       OperatorIntegerDivide       )),
             ((     ':',        OperatorColon               )),
             ((     '<',        OperatorLessThan            )),
             ((     '<=',       OperatorLessThanOrEqual     )),
             ((     '=',        OperatorEqualSign           )),
             ((     '==',       OperatorCompareEqual        )),
             ((     '>',        OperatorGreaterThan         )),
             ((     '>=',       OperatorGreaterThanOrEqual  )),
             ((     'and',      KeywordAnd                  )),
             ((     'as',       KeywordAs                   )),
             ((     'else',     KeywordElse                 )),
             ((     'for',      KeywordFor                  )),
             ((     'if',       KeywordIf                   )),
             ((     'in',       KeywordIn                   )),
             ((     'is',       KeywordIs                   )),
             ((     'not',      KeywordNot                  )),
             ((     'or',       KeywordOr                   )),
             ((     '[',        OperatorLeftSquareBracket   )),
             ((     ']',        OperatorRightSquareBracket  )),
             ((     '{',        OperatorLeftBrace           )),
             ((     '|',        OperatorLogicalOrSign       )),
             ((     '|=',       OperatorLogicalOrModify     )),
             ((     '}',        OperatorRightBrace          )),
             ((     '~',        OperatorTildeSign           )),
        )),
    )


    del Shared.initialize_action_word__Meta


    conjure_equal_sign  = produce_conjure_action_word('equal_sign',  OperatorEqualSign)
    conjure_dot         = produce_conjure_action_word('dot',         OperatorDot)
    conjure_keyword_as  = produce_conjure_action_word('keyword_as',  KeywordAs)
    conjure_keyword_for = produce_conjure_action_word('keyword_for', KeywordFor)
    conjure_keyword_if  = produce_conjure_action_word('keyword_if',  KeywordIf)
    conjure_keyword_is  = produce_conjure_action_word('keyword_is',  KeywordIs)
    conjure_star_sign   = produce_conjure_action_word('star_sign',   OperatorStarSign)

    [
            conjure_colon, conjure_colon__ends_in_newline,
    ] = produce_conjure_action_word('colon', OperatorColon, produce_ends_in_newline = true)

    [
            conjure_comma, conjure_comma__ends_in_newline,
    ] = produce_conjure_action_word('comma', OperatorComma, produce_ends_in_newline = true)

    [
            conjure_keyword_in, conjure_keyword_in__ends_in_newline,
    ] = produce_conjure_action_word('keyword_in', KeywordIn, produce_ends_in_newline = true)

    [
            conjure_keyword_not, conjure_keyword_not__ends_in_newline,
    ] = produce_conjure_action_word('keyword_not', KeywordNot, produce_ends_in_newline = true)

    [
        conjure_left_brace, conjure_left_brace__ends_in_newline,
    ] = produce_conjure_action_word('left_brace', OperatorLeftBrace, produce_ends_in_newline = true)

    [
        conjure_left_parenthesis, conjure_left_parenthesis__ends_in_newline,
    ] = produce_conjure_action_word('left_parenthesis', OperatorLeftParenthesis, produce_ends_in_newline = true)

    [
        conjure_left_square_bracket, conjure_left_square_bracket__ends_in_newline,
    ] = produce_conjure_action_word('left_square_bracket', OperatorLeftSquareBracket, produce_ends_in_newline = true)

    conjure_colon__line_marker = produce_conjure_action_word__line_marker(
            'colon',
            OperatorColon_LineMarker_1,
        )

    [
        conjure_right_brace, conjure_right_brace__ends_in_newline,
    ] = produce_conjure_action_word('right_brace', OperatorRightBrace, produce_ends_in_newline = true)

    [
        conjure_right_parenthesis, conjure_right_parenthesis__ends_in_newline,
    ] = produce_conjure_action_word(
            'right_parenthesis',
            OperatorRightParenthesis,
            
            produce_ends_in_newline = true,
        )

    [
        conjure_right_square_bracket, conjure_right_square_bracket__ends_in_newline,
    ] = produce_conjure_action_word(
            'right_square_bracket',
            OperatorRightSquareBracket,
            
            produce_ends_in_newline = true,
        )

    #
    #   Fix these to have 'WithPythonNewline' version
    #
    conjure_else_colon = produce_conjure_action_word('keyword-else-colon', KeywordElseColon)

    conjure__else__colon__line_marker = produce_conjure_action_word__line_marker(
            'keyword-else-colon-line-marker',
            KeywordElseColon_LineMarker_1,
        )

    conjure_except_colon = produce_conjure_action_word('keyword-except-colon', KeywordExceptColon)

    conjure__except__colon__line_marker = produce_conjure_action_word__line_marker(
            'keyword-except-colon-line-marker',
            KeywordExceptColon_LineMarker_1,
        )

    conjure_finally_colon = produce_conjure_action_word('keyword-finally-colon', KeywordFinallyColon)

    conjure__finally__colon__line_marker = produce_conjure_action_word__line_marker(
            'keyword-finally-colon-line-marker',
            KeywordFinallyColon_LineMarker_1,
        )

    conjure_try_colon = produce_conjure_action_word('keyword-try-colon', KeywordTryColon)

    conjure__try__colon__line_marker = produce_conjure_action_word__line_marker(
            'keyword-try-colon-line-marker',
            KeywordTryColon_LineMarker_1,
        )

    conjure_keyword_assert   = produce_conjure_action_word('keyword-assert',   KeywordAssert)
    conjure_keyword_delete   = produce_conjure_action_word('keyword-delete',   KeywordDelete)
    conjure_keyword_else_if  = produce_conjure_action_word('keyword-else-if',  KeywordElseIf)
    conjure_keyword_except   = produce_conjure_action_word('keyword-except',   KeywordExcept)
    conjure_keyword_function = produce_conjure_action_word('keyword-function', KeywordFunction)
    conjure_keyword_raise    = produce_conjure_action_word('keyword-raise',    KeywordRaise)

    conjure__raise__line_marker = produce_conjure_action_word__line_marker(
            'keyword-raise-line-marker',
            KeywordRaise_LineMarker_1,
        )

    conjure_keyword_return   = produce_conjure_action_word('keyword-return',   KeywordReturn)

    conjure_keyword_while    = produce_conjure_action_word('keyword-while',    KeywordWhile)
    conjure_keyword_with     = produce_conjure_action_word('keyword-with',     KeywordWith)
    conjure_keyword_yield    = produce_conjure_action_word('keyword-yield',    KeywordYield)


    find_atom_type = {
            '"' : conjure_double_quote,
            "'" : conjure_single_quote,

            #   (
            ')' : conjure_right_parenthesis,
            '.' : conjure_number,

            '0' : conjure_number, '1' : conjure_number, '2' : conjure_number, '3' : conjure_number,
            '4' : conjure_number, '5' : conjure_number, '6' : conjure_number, '7' : conjure_number,
            '8' : conjure_number, '9' : conjure_number,

            'A' : conjure_name, 'B' : conjure_name, 'C' : conjure_name, 'D' : conjure_name, 'E' : conjure_name,
            'F' : conjure_name, 'G' : conjure_name, 'H' : conjure_name, 'I' : conjure_name, 'J' : conjure_name,
            'K' : conjure_name, 'L' : conjure_name, 'M' : conjure_name, 'N' : conjure_name, 'O' : conjure_name,
            'P' : conjure_name, 'Q' : conjure_name, 'R' : conjure_name, 'S' : conjure_name, 'T' : conjure_name,
            'U' : conjure_name, 'V' : conjure_name, 'W' : conjure_name, 'X' : conjure_name, 'Y' : conjure_name,
            'Z' : conjure_name, '_' : conjure_name, 

            #  [
            ']' : conjure_right_square_bracket,

            'a' : conjure_name, 'b' : conjure_name, 'c' : conjure_name, 'd' : conjure_name, 'e' : conjure_name,
            'f' : conjure_name, 'g' : conjure_name, 'h' : conjure_name, 'i' : conjure_name, 'j' : conjure_name,
            'k' : conjure_name, 'l' : conjure_name, 'm' : conjure_name, 'n' : conjure_name, 'o' : conjure_name,
            'p' : conjure_name, 'q' : conjure_name, 'r' : conjure_name, 's' : conjure_name, 't' : conjure_name,
            'u' : conjure_name, 'v' : conjure_name, 'w' : conjure_name, 'x' : conjure_name, 'y' : conjure_name,
            'z' : conjure_name,
        }.__getitem__


    #   {[((
    is_right_parenthesis_7  = { ')' : 7 }.get
    is_colon_7              = { ':' : 7 }.get
    is_close_operator       = { ')' : 7, ']' : 7, '}' : 7 }.get


    lookup_keyword_conjure_function = {
                                          'not' : conjure_keyword_not,
                                      }.get


    share(
        'conjure_colon',                                    conjure_colon,
        'conjure_colon__ends_in_newline',                   conjure_colon__ends_in_newline,
        'conjure_colon__line_marker',                       conjure_colon__line_marker,
        'conjure_comma',                                    conjure_comma,
        'conjure_comma__ends_in_newline',                   conjure_comma__ends_in_newline,
        'conjure_dot',                                      conjure_dot,
        'conjure_else_colon',                               conjure_else_colon,
        'conjure__else__colon__line_marker',                conjure__else__colon__line_marker,
        'conjure_equal_sign',                               conjure_equal_sign,
        'conjure_except_colon',                             conjure_except_colon,
        'conjure__except__colon__line_marker',              conjure__except__colon__line_marker,
        'conjure_finally_colon',                            conjure_finally_colon,
        'conjure__finally__colon__line_marker',             conjure__finally__colon__line_marker,
        'conjure_keyword_as',                               conjure_keyword_as,
        'conjure_keyword_assert',                           conjure_keyword_assert,
        'conjure_keyword_delete',                           conjure_keyword_delete,
        'conjure_keyword_else_if',                          conjure_keyword_else_if,
        'conjure_keyword_except',                           conjure_keyword_except,
        'conjure_keyword_for',                              conjure_keyword_for,
        'conjure_keyword_if',                               conjure_keyword_if,
        'conjure_keyword_in',                               conjure_keyword_in,
        'conjure_keyword_in__ends_in_newline',              conjure_keyword_in__ends_in_newline,
        'conjure_keyword_is',                               conjure_keyword_is,
        'conjure_keyword_not',                              conjure_keyword_not,
        'conjure_keyword_not__ends_in_newline',             conjure_keyword_not__ends_in_newline,
        'conjure_keyword_raise',                            conjure_keyword_raise,
        'conjure_keyword_return',                           conjure_keyword_return,
        'conjure_keyword_while',                            conjure_keyword_while,
        'conjure_keyword_with',                             conjure_keyword_with,
        'conjure_keyword_yield',                            conjure_keyword_yield,
        'conjure_left_brace',                               conjure_left_brace,
        'conjure_left_brace__ends_in_newline',              conjure_left_brace__ends_in_newline,
        'conjure_left_parenthesis',                         conjure_left_parenthesis,
        'conjure_left_parenthesis__ends_in_newline',        conjure_left_parenthesis__ends_in_newline,
        'conjure_left_square_bracket',                      conjure_left_square_bracket,
        'conjure_left_square_bracket__ends_in_newline',     conjure_left_square_bracket__ends_in_newline,
        'conjure__raise__line_marker',                      conjure__raise__line_marker,
        'conjure_right_brace',                              conjure_right_brace,
        'conjure_right_brace__ends_in_newline',             conjure_right_brace__ends_in_newline,
        'conjure_right_parenthesis',                        conjure_right_parenthesis,
        'conjure_right_parenthesis__ends_in_newline',       conjure_right_parenthesis__ends_in_newline,
        'conjure_right_square_bracket',                     conjure_right_square_bracket,
        'conjure_right_square_bracket__ends_in_newline',    conjure_right_square_bracket__ends_in_newline,
        'conjure_star_sign',                                conjure_star_sign,
        'conjure_try_colon',                                conjure_try_colon,
        'conjure__try__colon__line_marker',                 conjure__try__colon__line_marker,
        'find_atom_type',                                   find_atom_type,
        'is_close_operator',                                is_close_operator,
        'is_colon_7',                                       is_colon_7,
        'is_right_parenthesis_7',                           is_right_parenthesis_7,
        'lookup_keyword_conjure_function',                  lookup_keyword_conjure_function,
    )
