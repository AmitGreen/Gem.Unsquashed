#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Atom')
def gem():
    show = 7


    @share
    def parse1_map_element():
        if qk() is not none:
            #my_line('qk: %r', qk())
            raise_unknown_line()

        token = parse1_atom()

        if token.is_right_brace:
            return token

        operator = qk()

        if operator is none:
            if qn() is not none:
                raise_unknown_line()

            operator = tokenize_operator()
        else:
            wk(none)

        if not operator.is_colon:
            token = parse1_ternary_expression__X__any_expression(token, operator)

            operator = qk()

            if operator is none:
                raise_unknown_line()

            wk(none)

        if not operator.is_colon:
            raise_unknown_line()

        return MapElement(token, operator, parse1_ternary_expression())


    @share
    def parse1_map__left_brace(left_brace):
        #
        #   1
        #
        left = parse1_map_element()

        if left.is_right_brace:
            return evoke_empty_map(left_brace, left)

        operator = qk()

        if operator is none:
            operator = tokenize_operator()
        else:
            wk(none)

        if operator.is_keyword_for:
            left = parse1_comprehension_expression__X__any_expression(left, operator)

            operator = qk()

            if operator is none:
                operator = tokenize_operator()
            else:
                wk(none)

        if operator.is_right_brace:
            return MapExpression_1(left_brace, left, operator)

        if not operator.is_comma:
            raise_unknown_line()

        many = [left_brace, left]

        while 7 is 7:
            token = parse1_map_element()

            if token.is_right_brace:
                many.append(conjure__comma__right_brace(operator, token))
                return MapExpression_Many(Tuple(many))

            many.append(operator)
            many.append(token)

            operator = qk()

            if operator is none:
                raise_unknown_line()

            wk(none)

            if operator.is_right_brace:
                many.append(operator)
                return MapExpression_Many(Tuple(many))

            if not operator.is_comma:
                raise_unknown_line()


    @share
    def parse1__parenthesized_expression__left_parenthesis(left_parenthesis):
        #
        #   1
        #

        #
        #   TODO:
        #       Replace this with 'parse1__parenthesis__first_atom' & handle a right-parenthesis as an empty tuple
        #
        middle_1 = parse1_atom()

        operator_1 = qk()

        if operator_1 is none:
            operator_1 = tokenize_operator()
        else:
            wk(none)

        if not operator_1.is_end_of_ternary_expression:
            middle_1 = parse1_ternary_expression__X__any_expression(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is_right_parenthesis:
            return ParenthesizedExpression(left_parenthesis, middle_1, operator_1)

        if not operator_1.is_comma:
            raise_unknown_line()

        #
        #   2
        #
        middle_2 = parse1_atom()

        if middle_2.is_right_parenthesis:
            return TupleExpression_1(
                       left_parenthesis,
                       middle_1,
                       conjure__comma__right_parenthesis(operator_1, middle_2),
                   )

        operator_2 = tokenize_operator()

        if not operator_2.is_end_of_ternary_expression:
            middle_2 = parse1_ternary_expression__X__any_expression(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is_right_parenthesis:
            return TupleExpression_2(left_parenthesis, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        #
        #   3
        #
        middle_3 = parse1_atom()

        if middle_3.is_right_parenthesis:
            return TupleExpression_2(
                       left_parenthesis,
                       middle_1,
                       operator_1,
                       middle_2,
                       conjure__comma__right_parenthesis(operator_2, middle_3),
                   )

        many = [left_parenthesis, middle_1, operator_1, middle_2, operator_2]

        while 7 is 7:
            operator_7 = tokenize_operator()

            if not operator_7.is_end_of_ternary_expression:
                middle_3 = parse1_ternary_expression__X__any_expression(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is_right_parenthesis:
                many.append(operator_7)
                return TupleExpression_Many(Tuple(many))

            if not operator_7.is_comma:
                raise_unknown_line()

            middle_3 = parse1_atom()

            if middle_3.is_right_parenthesis:
                many.append(conjure__comma__right_parenthesis(operator_7, middle_3))
                return TupleExpression_Many(Tuple(many))

            many.append(operator_7)


    @share
    def parse1__list_expression__left_square_bracket(left_square_bracket):
        #
        #   1
        #
        middle_1 = parse1_atom()

        if middle_1.is_right_square_bracket:
            return evoke_empty_list(left_square_bracket, middle_1)

        operator_1 = tokenize_operator()

        if not operator_1.is_end_of_comprehension_expression:
            middle_1 = parse1_comprehension_expression__X__any_expression(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is_right_square_bracket:
            return ListExpression_1(left_square_bracket, middle_1, operator_1)

        if not operator_1.is_comma:
            #my_line('line: %d; middle_1: %r; operator_1: %r', ql(), middle_1, operator_1)
            raise_unknown_line()

        #
        #   2
        #
        middle_2 = parse1_atom()

        if middle_2.is_right_square_bracket:
            return ListExpression_1(
                       left_square_bracket,
                       middle_1,
                       conjure__comma__right_square_bracket(operator_1, middle_2),
                   )

        operator_2 = tokenize_operator()

        if not operator_2.is_end_of_ternary_expression:
            middle_2 = parse1_ternary_expression__X__any_expression(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is_right_square_bracket:
            return ListExpression_2(left_square_bracket, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        #
        #   3
        #
        middle_3 = parse1_atom()

        if middle_3.is_right_square_bracket:
            return ListExpression_2(
                       left_square_bracket,
                       middle_1,
                       operator_1,
                       middle_2,
                       conjure__comma__right_square_bracket(operator_2, middle_3),
                   )

        many = [left_square_bracket, middle_1, operator_1, middle_2, operator_2]

        while 7 is 7:
            operator_7 = tokenize_operator()

            if not operator_7.is_end_of_ternary_expression:
                middle_3 = parse1_ternary_expression__X__any_expression(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is_right_square_bracket:
                many.append(operator_7)
                return ListExpression_Many(Tuple(many))

            if not operator_7.is_comma:
                raise_unknown_line()

            middle_3 = parse1_atom()

            if middle_3.is_right_square_bracket:
                many.append(conjure__comma__right_square_bracket(operator_7, middle_3))
                return ListExpression_Many(Tuple(many))

            many.append(operator_7)


    @share
    def parse1_atom():
        assert qk() is none
        assert qn() is none

        m = atom_match(qs(), qj())

        if m is none:
            #my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[qj() :]))
            raise_unknown_line()

        token = analyze_atom(m)

        if token.is__atom__or__special_operator:
            return token

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        if token.is_left_square_bracket:
            return parse1__list_expression__left_square_bracket(token)

        if token.is_left_brace:
            return parse1_map__left_brace(token)

        if token.is_keyword_not:
            return parse1_not_expression__operator(token)

        if token.is_minus_sign:
            return parse1_negative_expression__operator(token)

        if token.is_tilde_sign:
            return parse1_twos_complement_expression__operator(token)

        if token.is_star_sign:
            return TupleArgument(token, parse1_ternary_expression())

        #my_line('token: %r', token)
        raise_unknown_line()
