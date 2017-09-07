#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Atom')
def gem():
    show = 0


    def parse1__parenthesized_expression__left_parenthesis(left_parenthesis):
        #
        #   1
        #

        #
        #   TODO:
        #       Replace this with 'parse1__parenthesis__first_atom' & handle a right-parenthesis as an empty tuple
        #
        middle_1 = parse1_atom()

        operator_1 = tokenize_operator()

        if not operator_1.is_end_of_expression__OLD:
            middle_1 = parse1_any_comprehension_expression__left__operator(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is_right_parenthesis:
            return PathenthesizedExpression(left_parenthesis, middle_1, operator_1)

        if not operator_1.is_comma:
            raise_unknown_line(1)

        #
        #   2
        #
        middle_2 = tokenize_comma_atom()

        if middle_2.is_right_parenthesis:
            return TupleExpression_1(left_parenthesis, middle_1, Comma_RightParenthesis(operator_1, middle_2))

        operator_2 = tokenize_operator()

        if not operator_2.is_end_of_expression__OLD:
            middle_2 = parse1_any_comprehension_expression__left__operator(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is_right_parenthesis:
            return TupleExpression_2(left_parenthesis, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line(2)

        #
        #   3
        #
        middle_3 = tokenize_comma_atom()

        if middle_3.is_right_parenthesis:
            return TupleExpression_2(
                       left_parenthesis,
                       middle_1,
                       operator_1,
                       middle_2,
                       Comma_RightParenthesis(operator_2, middle_3),
                   )

        many = [left_parenthesis, middle_1, operator_1, middle_2, operator_2]

        while 7 is 7:
            operator_7 = tokenize_operator()

            if not operator_7.is_end_of_expression__OLD:
                middle_3 = parse1_any_comprehension_expression__left__operator(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is_right_parenthesis:
                many.append(operator_7)
                return TupleExpression_Many(Tuple(many))

            if not operator_7.is_comma:
                raise_unknown_line(3)

            middle_3 = tokenize_comma_atom()

            if middle_3.is_right_parenthesis:
                many.append(Comma_RightParenthesis(operator_7, middle_3))
                return TupleExpression_Many(Tuple(many))

            many.append(operator_7)


    @share
    def parse1_argument_atom():
        #
        #<different-from: parse1_atom>
        #
        token = tokenize_argument_atom()

        if token.is__atom__or__right_close_operator:
            return token
        #</different-from>

        #
        #<same-as: parse1_atom>
        #
        if token.is_keyword_not:
            return parse1_not_expression__operator(token)

        if token.is_minus_sign:
            return parse1_negative_expression__operator(token)

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        raise_unknown_line(1)
        #</same-as>


    @share
    def parse1_index_atom():
        #
        #<different-from: parse1_atom>
        #
        token = tokenize_index_atom()

        if token.is__atom__or__right_close_operator:
            return token
        #</different-from>

        #
        #<same-as: parse1_atom>
        #
        if token.is_keyword_not:
            return parse1_not_expression__operator(token)

        if token.is_minus_sign:
            return parse1_negative_expression__operator(token)

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        my_line('token: %s; %s', token, token.is__atom__or__right_close_operator)
        raise_unknown_line(1)
        #</same-as>


    @share
    def parse1_atom():
        #
        #<different-from: parse1_argument_atom>
        #
        token = tokenize_atom()

        if token.is_atom:
            return token
        #</different-from>

        #
        #<same-as: parse1_argument_atom>
        #
        if token.is_keyword_not:
            return parse1_not_expression__operator(token)

        if token.is_minus_sign:
            return parse1_negative_expression__operator(token)

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        raise_unknown_line(1)
        #</same-as>
