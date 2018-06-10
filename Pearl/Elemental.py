#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Pearl.Elemental')
def gem():
    require_gem('Pearl.Atom')


    @export
    class KeywordAndOperatorBase(PearlToken):
        is_all_index                               = false
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
        is_comma__right_parenthesis                = false
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
        is_keyword_return                          = false
        is_left_brace                              = false
        is_left_parenthesis                        = false
        is_left_square_bracket                     = false
        is_line_marker                             = false
        is_logical_and_operator                    = false
        is_logical_or_operator                     = false
        is_minus_sign                              = false
        is_modify_operator                         = false
        is_multiply_operator                       = false
        is__optional_comma__right_parenthesis      = false
        is__optional_comma__right_square_bracket   = false
        is_parameters_0                            = false
        is_postfix_operator                        = false
        is_power_operator                          = false
        is_right_brace                             = false
        is_right_parenthesis                       = false
        is_right_square_bracket                    = false
        is_special_operator                        = false
        is_star_sign                               = false
        is_tail_index                              = false
        is_tilde_sign                              = false


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, portray_string(t.s))


        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        display_token = display_short_token