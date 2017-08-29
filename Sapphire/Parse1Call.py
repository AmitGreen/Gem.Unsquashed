#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 0


    @share
    def parse1_call_expression__left__operator(left, left_parenthesis):
        return CallExpression(left, parse1_arguments__left_parenthesis(left_parenthesis))


    @share
    def parse1_argument7__left(left):
        operator = qk()

        if operator is none:
            operator = tokenize_operator()
        else:
            wk(none)

        if operator.is_equal_sign:
            if not left.is_identifier:
                raise_unknown_line()

            return KeywordArgument(left, operator, parse1_ternary_expression())

        if operator.is_end_of_ternary_expression:
            wk(operator)

            return left

        return parse1_ternary_expression__X__any_expression(left, operator)
    

    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        argument_1 = parse1_atom()

        if argument_1.is_right_parenthesis:
            return Arguments_0(left_parenthesis, argument_1)

        operator_1 = qk()

        if operator_1 is none:
            operator_1 = tokenize_operator()
        else:
            wk(none)

        if operator_1.is_equal_sign:
            if not left.is_identifier:
                raise_unknown_line()

            argument_1 = KeywordArgument(argument_1, operator_1, parse1_ternary_expression())

            operator_1 = qk()

            if operator_1 is none:
                operator_1 = tokenize_operator()
            else:
                wk(none)
        else:
            if not operator_1.is_end_of_comprehension_expression:
                argument_1 = parse1_comprehension_expression__X__any_expression(argument_1, operator_1)

                operator_1 = qk()

                if operator_1 is none:
                    operator_1 = tokenize_operator()
                else:
                    wk(none)

        if operator_1.is_right_parenthesis:
            return Arguments_1(left_parenthesis, argument_1, operator_1)

        if not operator_1.is_comma:
            raise_unknown_line()

        argument_2 = parse1_atom()

        if argument_2.is_right_parenthesis:
            return Arguments_1(
                       left_parenthesis,
                       argument_1,
                       Comma_RightParenthesis(operator_1, argument_2),
                   )

        argument_2 = parse1_argument7__left(argument_2)
        operator_2 = qk()

        wk(none)

        if operator_2.is_right_parenthesis:
            return Arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        argument_3 = parse1_atom()

        if argument_3.is_right_parenthesis:
            return Arguments_2(
                       left_parenthesis,
                       argument_1,
                       operator_1,
                       argument_2,
                       Comma_RightParenthesis(operator_2, argument_3),
                   )

        many = [left_parenthesis, argument_1, operator_1, argument_2, operator_2]

        while 7 is 7:
            argument_3 = parse1_argument7__left(argument_3)

            operator_7 = qk()

            wk(none)

            if operator_7.is_right_parenthesis:
                many.append(argument_3)
                many.append(operator_7)
                return Arguments_Many(Tuple(many))

            if not operator_7.is_comma:
                raise_unknown_line()

            many.append(argument_3)

            argument_3 = parse1_atom()

            if argument_3.is_right_parenthesis:
                many.append(Comma_RightParenthesis(operator_7, argument_3))
                return Arguments_Many(Tuple(many))

            many.append(operator_7)
