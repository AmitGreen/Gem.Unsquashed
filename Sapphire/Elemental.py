#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Elemental')
def gem():
    require_gem('Sapphire.Core')


    @share
    class KeywordAndOperatorBase(Token):
        is_any_parameter_colon_0                   = false
        is__any__right_parenthesis__colon__newline = false
        is_arguments_0                             = false
        is__arguments_0__or__left_parenthesis      = false
        is_arithmetic_operator                     = false
        is_atom                                    = false
        is__atom__or__special_operator             = false
        is_colon                                   = false
        is_colon_newline                           = false
        is_comma                                   = false
        is__comma__or__right_parenthesis           = false
        is_compare_operator                        = false
        is_dot                                     = false
        is_end_of_arithmetic_expression            = false
        is_end_of_boolean_and_expression           = false
        is_end_of_boolean_or_expression            = false
        is_end_of_compare_expression               = false
        is_end_of_comprehension_expression_list    = false
        is_end_of_normal_expression                = false
        is_end_of_normal_expression_list           = false
        is_end_of_ternary_expression               = false
        is_end_of_ternary_expression_list          = false
        is_end_of_unary_expression                 = false
        is_equal_sign                              = false
        is_keyword_and                             = false
        is_keyword_as                              = false
        is_keyword_else                            = false
        is_keyword_if                              = false
        is_keyword_in                              = false
        is_keyword_not                             = false
        is_keyword_or                              = false
        is_left_brace                              = false
        is_left_parenthesis                        = false
        is_left_square_bracket                     = false
        is_minus_sign                              = false
        is_modify_operator                         = false
        is_parameter_colon_0_newline               = false
        is_plus_sign                               = false
        is_postfix_operator                        = false
        is_right_brace                             = false
        is__right_parenthesis__colon               = false
        is__right_parenthesis__colon__newline      = false
        is_right_parenthesis                       = false
        is_right_square_bracket                    = false
        is_token_newline                           = false


        def __repr__(t):
            if '\n' in t.s:
                return arrange('<%s>', portray_string(t.s))

            return arrange('<%s>', t.s)


        def display_token(t):
            if t.s == t.display_name:
                return arrange('<%s>', t.display_name)

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


    @share
    class DoubleQuote(Token):
        __slots__                      = (())
        display_name                   = '"'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return arrange('<%s>', t.s)


    class KeywordAnd(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'and'
        is_end_of_arithmetic_expression  = true
        is_end_of_compare_expression     = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_and                   = true
        keyword                          = 'and'


    class KeywordAs(KeywordAndOperatorBase):
        __slots__     = (())
        display_name  = 'as'
        is_keyword_as = true
        keyword       = 'as'


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
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_else                  = true
        keyword                          = 'else'


    class KeywordElseColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'else:'
        keyword      = 'else:'


    class KeywordExceptColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'except:'
        keyword      = 'except:'


    class KeywordFor(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'for'
        keyword      = 'for'


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
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class KeywordOr(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = 'or'
        is_end_of_arithmetic_expression  = true
        is_end_of_boolean_and_expression = true
        is_end_of_compare_expression     = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        is_keyword_or                    = true
        keyword                          = 'or'


    class KeywordReturn(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'return'
        keyword      = 'return'


    class KeywordTryColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'try:'
        keyword      = 'try:'


    class KeywordWith(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'with'
        keyword      = 'with'


    @share
    class Number(Token):
        __slots__                      = (())
        display_name                   = 'number'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return t.s



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
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression            = true
        is_end_of_ternary_expression_list       = true
        is_end_of_unary_expression              = true
        keyword                                 = ':'


    class OperatorColonNewline(KeywordAndOperatorBase):
        __slots__                               = (())
        is_colon_newline                        = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression            = true
        is_end_of_ternary_expression_list       = true
        is_end_of_unary_expression              = true
        keyword                                 = 'colon-newline'


        def __repr__(t):
            return arrange('<OperatorColonNewline %s>', portray_raw_string(t.s))


        def display_token(t):
            return portray_raw_string(t.s)


    class OperatorComma(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = ','
        is__comma__or__right_parenthesis = true
        is_comma                         = true
        is_end_of_arithmetic_expression  = true
        is_end_of_boolean_and_expression = true
        is_end_of_boolean_or_expression  = true
        is_end_of_compare_expression     = true
        is_end_of_normal_expression      = true
        is_end_of_ternary_expression     = true
        is_end_of_unary_expression       = true
        keyword                          = ','


    @share
    class OperatorCompareEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '=='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true
        keyword                          = '=='


        def display_token(t):
            if t.s == ' == ':
                return '=='

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


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
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        is_equal_sign                           = true
        keyword                                 = '='


    class OperatorHeadIndex(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = ':]'
        is_colon                                = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        keyword                                 = ':]'


    class OperatorLeftBrace(KeywordAndOperatorBase):
        __slots__                      = (())
        display_name                   = '{'       #   }
        is_atom                        = false
        is__atom__or__special_operator = true
        is_left_brace                  = true
        keyword                        = '{'       #   }


    class OperatorLeftParenthesis(KeywordAndOperatorBase):
        __slots__                             = (())
        display_name                          = '('       #   )
        is__arguments_0__or__left_parenthesis = true
        is_atom                               = false
        is_left_parenthesis                   = true
        is_postfix_operator                   = true
        keyword                               = '('       #   )


    @export
    class OperatorLeftSquareBracket(KeywordAndOperatorBase):
        __slots__              = (())
        display_name           = '['              #   ]
        is_left_square_bracket = true
        is_postfix_operator    = true
        keyword                = '['              #   ]


    @share
    class OperatorLessThanOrEqual(KeywordAndOperatorBase):
        __slots__                        = (())
        display_name                     = '<='
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
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


    class OperatorMinusSign(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '-'
        is_minus_sign              = true
        is_end_of_unary_expression = true
        is_arithmetic_operator     = true
        keyword                    = '-'


    class OperatorModifyPlus(KeywordAndOperatorBase):
        __slots__          = (())
        display_name       = '+='
        is_modify_operator = true
        keyword            = '+='


    class OperatorPlusSign(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '+'
        is_arithmetic_operator     = true
        is_end_of_unary_expression = true
        is_plus_sign               = true
        keyword                    = '+'


    class OperatorRightBrace(KeywordAndOperatorBase):
        __slots__                               = (())
        #  {
        display_name                            = '}'
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
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
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
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
        __slots__                               = (())
        #   [
        display_name                            = ']'
        is__atom__or__special_operator          = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        is_right_square_bracket                 = true
        #   [
        keyword                                 = ']'


    class OperatorStar(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '*'
        is_end_of_unary_expression = true
        keyword                    = '*'


    @share
    class SingleQuote(Token):
        __slots__                      = (())
        display_name                   = "'"
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_right_parenthesis           = false
        is_right_square_bracket        = false


        def display_token(t):
            return arrange('<%s>', t.s)


    conjure_colon_newline        = produce_conjure_by_name('operator-colon-newline',        OperatorColonNewline) 
    conjure_colon                = produce_conjure_by_name('operator-colon',                OperatorColon) 
    conjure_comma                = produce_conjure_by_name('operator-comma',                OperatorComma) 
    conjure_compare_equal        = produce_conjure_by_name('operator-conmpare-equal',       OperatorCompareEqual) 
    conjure_dot                  = produce_conjure_by_name('operator-dot',                  OperatorDot) 
    conjure_equal_sign           = produce_conjure_by_name('operator-equal-sign',           OperatorEqualSign) 
    conjure_else_colon           = produce_conjure_by_name('keyword-else-colon',            KeywordElseColon) 
    conjure_except_colon         = produce_conjure_by_name('keyword-except-colon',          KeywordExceptColon) 
    conjure_head_index           = produce_conjure_by_name('operator-head-index',           OperatorHeadIndex) 
    conjure_keyword_and          = produce_conjure_by_name('keyword-and',                   KeywordAnd) 
    conjure_keyword_as           = produce_conjure_by_name('keyword-as',                    KeywordAs) 
    conjure_keyword_assert       = produce_conjure_by_name('keyword-assert',                KeywordAssert) 
    conjure_keyword_delete       = produce_conjure_by_name('keyword-delete',                KeywordDelete) 
    conjure_keyword_else         = produce_conjure_by_name('keyword-else',                  KeywordElse) 
    conjure_keyword_for          = produce_conjure_by_name('keyword-for',                   KeywordFor) 
    conjure_keyword_function     = produce_conjure_by_name('keyword-function',              KeywordFunction) 
    conjure_keyword_if           = produce_conjure_by_name('keyword-if',                    KeywordIf) 
    conjure_keyword_in           = produce_conjure_by_name('keyword-in',                    KeywordIn) 
    conjure_keyword_is           = produce_conjure_by_name('keyword-is',                    KeywordIs) 
    conjure_keyword_not          = produce_conjure_by_name('keyword-not',                   KeywordNot) 
    conjure_keyword_or           = produce_conjure_by_name('keyword-or',                    KeywordOr) 
    conjure_keyword_return       = produce_conjure_by_name('keyword-return',                KeywordReturn) 
    conjure_keyword_with         = produce_conjure_by_name('keyword-with',                  KeywordWith) 
    conjure_left_brace           = produce_conjure_by_name('operator-left-brace',           OperatorLeftBrace) 
    conjure_left_parenthesis     = produce_conjure_by_name('operator-left-parenthesis',     OperatorLeftParenthesis) 
    conjure_left_square_bracket  = produce_conjure_by_name('operator-left-square-bracket',  OperatorLeftSquareBracket) 
    conjure_less_than_or_equal   = produce_conjure_by_name('operator-less-than-or-equal',   OperatorLessThanOrEqual) 
    conjure_minus_sign           = produce_conjure_by_name('operator-minus-sign',           OperatorMinusSign) 
    conjure_modify_plus          = produce_conjure_by_name('operator-modify-plus',          OperatorModifyPlus) 
    conjure_operator_star        = produce_conjure_by_name('operator-star',                 OperatorStar) 
    conjure_plus_sign            = produce_conjure_by_name('operator-plus-sign',            OperatorPlusSign) 
    conjure_right_brace          = produce_conjure_by_name('operator-right-brace',          OperatorRightBrace) 
    conjure_right_parenthesis    = produce_conjure_by_name('operator-right-parenthesis',    OperatorRightParenthesis) 
    conjure_right_square_bracket = produce_conjure_by_name('operator-right-square-bracket', OperatorRightSquareBracket) 
    conjure_try_colon            = produce_conjure_by_name('keyword-try-colon',             KeywordTryColon) 

    find_atom_type = {
                         '"' : DoubleQuote,
                         "'" : SingleQuote,

                         #   (
                         ')' : conjure_right_parenthesis,
                         '.' : Number,

                         '0' : Number, '1' : Number, '2' : Number, '3' : Number, '4' : Number,
                         '5' : Number, '6' : Number, '7' : Number, '8' : Number, '9' : Number,

                         'A' : conjure_identifier, 'B' : conjure_identifier, 'C' : conjure_identifier,
                         'D' : conjure_identifier, 'E' : conjure_identifier, 'F' : conjure_identifier,
                         'G' : conjure_identifier, 'H' : conjure_identifier, 'I' : conjure_identifier,
                         'J' : conjure_identifier, 'K' : conjure_identifier, 'L' : conjure_identifier,
                         'M' : conjure_identifier, 'N' : conjure_identifier, 'O' : conjure_identifier,
                         'P' : conjure_identifier, 'Q' : conjure_identifier, 'R' : conjure_identifier,
                         'S' : conjure_identifier, 'T' : conjure_identifier, 'U' : conjure_identifier,
                         'V' : conjure_identifier, 'W' : conjure_identifier, 'X' : conjure_identifier,
                         'Y' : conjure_identifier, 'Z' : conjure_identifier, '_' : conjure_identifier,

                         #  [
                         ']' : conjure_right_square_bracket,

                         'a' : conjure_identifier, 'b' : conjure_identifier, 'c' : conjure_identifier,
                         'd' : conjure_identifier, 'e' : conjure_identifier, 'f' : conjure_identifier,
                         'g' : conjure_identifier, 'h' : conjure_identifier, 'i' : conjure_identifier,
                         'J' : conjure_identifier, 'k' : conjure_identifier, 'l' : conjure_identifier,
                         'm' : conjure_identifier, 'n' : conjure_identifier, 'o' : conjure_identifier,
                         'p' : conjure_identifier, 'q' : conjure_identifier, 'r' : conjure_identifier,
                         's' : conjure_identifier, 't' : conjure_identifier, 'u' : conjure_identifier,
                         'v' : conjure_identifier, 'w' : conjure_identifier, 'x' : conjure_identifier,
                         'y' : conjure_identifier, 'z' : conjure_identifier,
                     }.__getitem__


    find_operator_conjure_function = {
                                         '('    : conjure_left_parenthesis,
                                         ')'    : conjure_right_parenthesis,
                                         '+'    : conjure_plus_sign,
                                         '+='   : conjure_modify_plus,
                                         ','    : conjure_comma,
                                         '-'    : conjure_minus_sign,
                                         '.'    : conjure_dot,
                                         ':'    : conjure_colon,
                                         '<='   : conjure_less_than_or_equal,
                                         '='    : conjure_equal_sign,
                                         '=='   : conjure_compare_equal,
                                         'and'  : conjure_keyword_and,
                                         'as'   : conjure_keyword_as,
                                         'else' : conjure_keyword_else,
                                         'if'   : conjure_keyword_if,
                                         'in'   : conjure_keyword_in,
                                         'is'   : conjure_keyword_is,
                                         'not'  : conjure_keyword_not,
                                         'or'   : conjure_keyword_or,
                                         '['    : conjure_left_square_bracket,
                                         ']'    : conjure_right_square_bracket,
                                     }.__getitem__


    #   {[(
    is_close_operator = { ')' : 7, ']' : 7, '}' : 7 }.get


    lookup_keyword_conjure_function = {
                                          'not' : conjure_keyword_not,
                                      }.get


    share(
        'conjure_colon',                    conjure_colon,
        'conjure_colon_newline',            conjure_colon_newline,
        'conjure_comma',                    conjure_comma,
        'conjure_dot',                      conjure_dot,
        'conjure_else_colon',               conjure_else_colon,
        'conjure_equal_sign',               conjure_equal_sign,
        'conjure_except_colon',             conjure_except_colon,
        'conjure_head_index',               conjure_head_index,
        'conjure_keyword_as',               conjure_keyword_as,
        'conjure_keyword_assert',           conjure_keyword_assert,
        'conjure_keyword_delete',           conjure_keyword_delete,
        'conjure_keyword_for',              conjure_keyword_for,
        'conjure_keyword_if',               conjure_keyword_if,
        'conjure_keyword_is',               conjure_keyword_is,
        'conjure_keyword_not',              conjure_keyword_not,
        'conjure_keyword_return',           conjure_keyword_return,
        'conjure_keyword_with',             conjure_keyword_with,
        'conjure_left_brace',               conjure_left_brace,
        'conjure_left_parenthesis',         conjure_left_parenthesis,
        'conjure_left_square_bracket',      conjure_left_square_bracket,
        'conjure_operator_star',            conjure_operator_star,
        'conjure_right_brace',              conjure_right_brace,
        'conjure_right_parenthesis',        conjure_right_parenthesis,
        'conjure_right_square_bracket',     conjure_right_square_bracket,
        'conjure_try_colon',                conjure_try_colon,
        'find_atom_type',                   find_atom_type,
        'find_operator_conjure_function',   find_operator_conjure_function,
        'is_close_operator',                is_close_operator,
        'lookup_keyword_conjure_function',  lookup_keyword_conjure_function,
    )
