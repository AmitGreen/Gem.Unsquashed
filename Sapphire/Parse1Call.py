#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 0


    require_gem('Sapphire.Tokenize1Expression')


    @share
    def parse1_expression_call(left, left_parenthesis):
        return ExpressionCall(left, parse1_arguments__left_parenthesis(left_parenthesis))


    @share
    def parse1_argument7(left):
        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_left_parenthesis:
                left = parse1_expression_call(left, operator)
                continue

            if operator.is_left_square_bracket:
                left = parse1_expression_index(left, operator)
                continue

            if operator.is__comma__or__right_parenthesis:
                wk(operator)

                return left

            if operator.is_arguments_0:
                left = ExpressionCall(left, operator)
                continue

            my_line('operator: %r', operator)
            raise_unknown_line(1)

    
    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        argument_1 = parse1_argument_first_atom()

        if argument_1.is_right_parenthesis:
            raise_unknown_line(1)

        while 7 is 7:
            operator_1 = tokenize_operator()

            if operator_1.is_left_parenthesis:
                argument_1 = parse1_expression_call(argument_1, operator_1)
                continue

            if operator_1.is_left_square_bracket:
                argument_1 = parse1_expression_index(argument_1, operator_1)
                continue

            if operator_1.is_right_parenthesis:
                return Arguments_1(left_parenthesis, argument_1, operator_1)

            if operator_1.is_comma:
                break

            raise_unknown_line(2)

        argument_2 = parse1_argument_first_atom()

        if argument_2.is_right_parenthesis:
            raise_unknown_line(3)

        argument_2 = parse1_argument7(argument_2)
        operator_2 = qk()

        wk(none)

        if operator_2.is_right_parenthesis:
            if show is 7:
                my_line('=> %r; %r; %s',
                        Arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2),
                        qn(),
                        portray_raw_string(qs()[qj():]))

            return Arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line(4)

        argument_3 = parse1__argument_first_atom()

        if argument_3.is_right_parenthesis:
            return Arguments_2(
                       left_parenthesis,
                       argument_1,
                       operator_1,
                       argument_2,
                       Comma_RightParenthesis(operator_2, argument_3),
                   )

        raise_unknown_line(5)
