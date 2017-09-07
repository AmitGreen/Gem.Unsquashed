#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    #
    #   1.  Postfix-Expression (Python 2.7.14rc1 grammer calls this 'trailer')
    #   1.  Dot-Expression
    #   1.  Call-Expression
    #   1.  Method_Call-Expression
    #   1.  Index-Expression
    #
    #       postfix-expression
    #           : atom
    #           | dot-expression
    #           | call-expression
    #           | method-call-expression
    #           | index-expression
    #
    #       dot-expression
    #           : postfix-expression '.' name
    #
    #       call-expression
    #           : postfix-expression '(' [ argument-list ] ')'
    #
    #       method-call-expression:
    #           : postfix-expression '.' name '(' [ argument-list ] ')'
    #
    @share
    def parse1_postfix_expression__left__operator(left, operator):
        assert operator.is_postfix_operator

        while 7 is 7:
            assert qk() is none
            assert qn() is none

            if operator.is_dot:
                name = tokenize_name()

                if qn() is not none:
                    return MemberExpression_1(left, operator, name)

                operator_2 = tokenize_operator()

                if operator_2.is_dot:
                    if qn() is not none:
                        raise_unknown_line(1)

                    name_2 = tokenize_name()

                    if qn() is not none:
                        return MemberExpression_2(left, operator, name, operator_2, name_2)

                    operator_3 = tokenize_operator()

                    if operator_3.is_dot:
                        if qn() is not none:
                            raise_unknown_line(2)

                        name_3 = tokenize_name()

                        if qn() is not none:
                            return MemberExpression_3(left, operator, name, operator_2, name_2, operator_3, name_3)

                        operator_4 = tokenize_operator()

                        if operator_4.is__arguments_0__or__left_parenthesis:
                            if operator_4.is_left_parenthesis:
                                assert qd() > 0
                                assert qn() is none

                                operator_4 = parse1_arguments__left_parenthesis(operator_4)

                            left = MethodCall_3(left, operator, name, operator_2, name_2, operator_3, name_3, operator_4)

                            operator = qk()

                            if operator is not none:
                                if not operator.is_postfix_operator:
                                    return left

                                wk(none)
                            else:
                                if qn() is not none:
                                    return left

                                operator = tokenize_operator()

                                if qn() is not none:
                                    raise_unknown_line(3)

                                if not operator.is_postfix_operator:
                                    wk(operator)

                                    return left
                        elif operator_4.is_postfix_operator:
                            left = MemberExpression_3(left, operator, name, operator_2, name_2, operator_3, name_3)

                            operator = operator_4
                        else:
                            wk(operator_4)

                            return MemberExpression_3(left, operator, name, operator_2, name_2, operator_3, name_3)

                    elif operator_3.is__arguments_0__or__left_parenthesis:
                        if operator_3.is_left_parenthesis:
                            assert qd() > 0
                            assert qn() is none

                            operator_3 = parse1_arguments__left_parenthesis(operator_3)

                        left = MethodCall_2(left, operator, name, operator_2, name_2, operator_3)

                        operator = qk()

                        if operator is not none:
                            if not operator.is_postfix_operator:
                                return left

                            wk(none)
                        else:
                            if qn() is not none:
                                return left

                            operator = tokenize_operator()

                            if qn() is not none:
                                raise_unknown_line(4)

                            if not operator.is_postfix_operator:
                                wk(operator)

                                return left

                    elif operator_3.is_postfix_operator:
                        left = MemberExpression_2(left, operator, name, operator_2, name_2)

                        operator = operator_3
                    else:
                        wk(operator_3)

                        return MemberExpression_2(left, operator, name, operator_2, name_2)

                elif operator_2.is__arguments_0__or__left_parenthesis:
                    if operator_2.is_left_parenthesis:
                        assert qd() > 0
                        assert qn() is none

                        operator_2 = parse1_arguments__left_parenthesis(operator_2)

                    left = MethodCall_2(left, operator, name, operator_2)

                    operator = qk()

                    if operator is not none:
                        if not operator.is_postfix_operator:
                            return left

                        wk(none)
                    else:
                        if qn() is not none:
                            return left

                        operator = tokenize_operator()

                        if qn() is not none:
                            raise_unknown_line(5)

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

                elif operator_2.is_postfix_operator:
                    left = MemberExpression_1(left, operator, name)

                    operator = operator_2
                else:
                    wk(operator_2)

                    return MemberExpression_1(left, operator, name)

            if operator.is__arguments_0__or__left_parenthesis:
                if operator.is_left_parenthesis:
                    assert qd() > 0
                    assert qn() is none

                    operator = parse1_arguments__left_parenthesis(operator)

                left = CallExpression(left, operator)

                operator = qk()

                if operator is not none:
                    if not operator.is_postfix_operator:
                        return left

                    wk(none)
                else:
                    if qn() is not none:
                        return left

                    operator = tokenize_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            if operator.is_left_square_bracket:
                if qn() is not none:
                    raise_unknown_line(6)

                middle = parse1_atom()

                operator_2 = qk()

                if operator_2 is none:
                    if qn() is not none:
                        raise_unknown_line(7)

                    operator_2 = tokenize_operator()
                else:
                    wk(none)

                if operator_2.is_right_square_bracket:
                    left = IndexExpression(left, NormalIndex(operator, middle, operator_2))
                elif operator_2.is_colon:
                    if qn() is not none:
                        raise_unknown_line(8)

                    middle_2 = parse1_atom()

                    if middle_2.is_right_square_bracket:
                        left = IndexExpression(
                                   left,
                                   HeadIndex(
                                       operator,
                                       middle,
                                       Colon_RightSquareBracket(operator_2, middle_2),
                                   ),
                               )
                    else:
                        operator_3 = qk()

                        if operator_3 is none:
                            if qn() is not none:
                                raise_unknown_line(9)

                            operator_3 = tokenize_operator()
                        else:
                            wk(none)

                        if operator_3.is_right_square_bracket:
                            left = IndexExpression(
                                       left,
                                       RangeIndex(operator, middle, operator_2, middle_2, operator_3),
                                   )
                        else:
                            middle_2 = parse1_any_ternary_expression__left__operator(middle_2, operator_3)

                            operator_3 = qk()

                            if operator_3 is none:
                                raise_unknown_line(10)

                            wk(none)

                            if not operator_3.is_right_square_bracket:
                                raise_unknown_line(11)

                            left = IndexExpression(
                                       left,
                                       RangeIndex(operator, middle, operator_2, middle_2, operator_3),
                                   )
                else:
                    middle = parse1_any_ternary_expression__left__operator(middle, operator_2)

                    operator_2 = qk()

                    if operator_2 is none:
                        raise_unknown_line(12)

                    wk(none)

                    if not operator_2.is_right_square_bracket:
                        raise_unknown_line(13)

                    left = IndexExpression(left, NormalIndex(operator, middle, operator_2))

                if qn() is not none:
                    return left

                operator = qk()

                if operator is not none:
                    if not operator.is_postfix_operator:
                        return left

                    wk(none)
                else:
                    if qn() is not none:
                        return left

                    operator = tokenize_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            assert operator.is_postfix_operator

        raise_unknown_line(15)


    #
    #   2.  Power-Expression (Python 2.7.14rc1 grammer calls this 'power')
    #

    #
    #   3.  Unary-Expression (Python 2.7.14rc1 grammer calls this 'factor')
    #
    @share
    def parse1_negative_expression__operator(negative_operator):
        if show is 7:
            my_line('%s, %s', negative_operator, portray_raw_string(qs()[qj(): ]))

        right = parse1_atom()

        operator = qk()

        if operator is none:
            newline = qn()

            if qn() is not none:
                return NegativeExpression(negative_operator, right)

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line(4)

            if operator.is_end_of_unary_expression:
                wk(operator)
                return NegativeExpression(negative_operator, right)
        else:
            if operator.is_end_of_unary_expression:
                return NegativeExpression(negative_operator, right)

            wk(none)

        my_line('right: %r, operator: %s:%r', right, operator)
        raise_unknown_line(1)


    def parse1_unary_expression():
        left = parse1_atom()

        operator = qk()

        if operator is none:
            newline = qn()

            if qn() is not none:
                return left

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line(1)

            if operator.is_end_of_unary_expression:
                wk(operator)
                return left
        else:
            if operator.is_end_of_unary_expression:
                return NegativeExpression(negative_operator, right)

            wk(none)

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            if qn() is not none:
                return left

            operator = qk()

            if operator.is_end_of_unary_expression:
                return left

            wk(none)

        raise_unknown_line(2)


    #
    #   4.  Multiply-Expression (Python 2.7.14rc1 grammer calls this 'term')
    #

    #
    #   5.  Arithmetic-Expression (Python 2.7.14rc1 grammer calls this 'arith_expr')
    #
    @share
    def parse1_arithmetic_expression__left__operator(left, add_operator):
        if show is 7:
            my_line('left: %r; add_operator: %r; s: %s',
                    left, add_operator, portray_string(qs()[qj() : ]))

        right = parse1_unary_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return AddExpression(left, add_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return AddExpression(left, add_operator, right)
        else:
            if operator.is_end_of_compare_expression:
                return AddExpression(left, add_operator, right)

            wk(none)

        many = [left, add_operator, right, operator]

        while 7 is 7:
            many.append(parse1_unary_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return ArithmeticExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_arithmetic_expression:
                    wk(operator)

                    return ArithmeticExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_arithmetic_expression:
                    return ArithmeticExpression_Many(Tuple(many))

                wk(none)

            many.append(operator)

    #
    #   6.  Shift-Expression (Python 2.7.14rc1 grammer calls this 'shift_expr')
    #

    #
    #   7.  Logical-And-Expression (Python 2.7.14rc1 grammer calls this 'and_expr')
    #

    #
    #   8.  Logical-Exclusive-Or-Expression (Python 2.7.14rc1 grammer calls this 'xor_expr')
    #

    #
    #   9.  Normal-Expression (Logical-Inclusive-Or) (Python 2.7.14rc1 grammer calls this 'expr')
    #
    @share
    def parse1_normal_expression():
        left = parse1_atom()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_normal_expression:
                wk(operator)

                return left
        else:
            if operator.is_end_of_normal_expression:
                return left

            wk(none)

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            if qn() is not none:
                return left

            operator = qk()

            if operator.is_end_of_normal_expression:
                return left

            wk(none)

        raise_unknown_line(1)


    #
    #   10. Normal-Expression-List
    #
    @share
    def parse1_normal_expression_list():
        left = parse1_atom()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_normal_expression_list:
                wk(operator)

                return left
        else:
            if operator.is_end_of_normal_expression_list:
                return left

            wk(none)

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            if qn() is not none:
                return left

            operator = qk()

            if operator.is_end_of_normal_expression_list:
                return left

            wk(none)

        my_line('left: %s; operator: %s', left, operator)
        raise_unknown_line(1)


    #
    #   11.  Compare-Expression (Python 2.7.14rc1 grammer calls this 'comparasion')
    #
    @share
    def parse1_compare_expression__left__operator(left, compare_operator):
        if show is 7:
            my_line('left: %r; compare_operator: %r; s: %s',
                    left, compare_operator, portray_string(qs()[qj() : ]))

        right = parse1_normal_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return compare_operator.compare_expression_meta(left, compare_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return compare_operator.compare_expression_meta(left, compare_operator, right)
        else:
            if operator.is_end_of_compare_expression:
                return compare_operator.compare_expression_meta(left, compare_operator, right)

            wk(none)

        many = [left, compare_operator, right, operator]

        while 7 is 7:
            many.append(parse1_normal_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return CompareExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_compare_expression:
                    wk(operator)

                    return CompareExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_compare_expression:
                    return CompareExpression_Many(Tuple(many))

                wk(none)

            many.append(operator)


    #
    #   12.  Not-Expression (Python 2.7.14rc1 grammer calls this 'not_test')
    #
    #       not-expression
    #           : compare-expression
    #           | 'not' not-test
    #
    #   NOTE:
    #       Uses .is_end_of_compare_expression on purpose (there is no .is_end_of_not_expression, as it would be
    #       identicial to .is_end_of_compare_expression)
    #
    @share
    def parse1_not_expression__operator(not_operator):
        if show is 7:
            my_line('%s, %s', not_operator, portray_raw_string(qs()[qj(): ]))

        right = parse1_atom()

        operator = qk()

        if operator is none:
            newline = qn()

            if qn() is not none:
                return NotExpression(not_operator, right)

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line(4)

            if operator.is_end_of_compare_expression:
                wk(operator)
                return NotExpression(not_operator, right)
        else:
            if operator.is_end_of_compare_expression:
                return NotExpression(not_operator, right)

            wk(none)

        my_line('right: %s, operator: %s', right, operator)
        raise_unknown_line(5)


    #
    #   13. Boolean-And-Expression (Python 2.7.14rc1 grammer calls this 'and_test')
    #

    #
    #   14. Boolean-Or-Expression (Python 2.7.14rc1 grammer calls this 'or_test')
    #
    @share
    def parse1_or_expression__left__operator(left, or_operator):
        if show is 7:
            my_line('%r, %r, %s', left, or_operator, portray_string(qs()[qj():]))

        right = parse1_atom()

        if qk() is not none:
            raise_unknown_line(1)

        if qn() is not none:
            raise_unknown_line(2)

        operator = tokenize_operator()

        if qn() is not none:
            raise_unknown_line(3)

        while not operator.is_end_of_boolean_or_expression:
            if operator.is_or_operator:
                left        = OrExpression(left, or_operator, right)
                or_operator = operator

                if qn() is not none:
                    raise_unknown_line(4)

                right = parse1_atom()

                operator = qk()

                if operator is none:
                    operator = tokenize_operator()

                    if qk() is not none:
                        my_line('qk: %r, qn: %r', qk(), qn())
                        raise_unknown_line(5)
                else:
                    wk(none)

                continue

            my_line('left: %r; or_operator: %r; right: %r; operator: %r; s: %s',
                    left, or_operator, right, operator, portray_string(qs()[qj():]))

            raise_unknown_line(6)

        if qk() is not none:
            my_line('qk: %r, qn: %r', qk(), qn())
            raise_unknown_line(7)

        wk(operator)

        return OrExpression(left, or_operator, right)


    #
    #   15.  Ternary-Expression (Python 2.7.14rc1 grammer calls this 'test')
    #   15.  Lambda-Expression  (Python 2.7.14rc1 grammer calls this 'lambdef')
    #
    #           ternary-expression
    #               : boolean-or-expression
    #               | boolean-or-expression 'if' boolean-or-expression 'else' ternary-expression
    #               | lambda-expression
    #
    #
    #           lambda-Expression
    #               : 'lambda' [variable-argument-list] ':' ternary-expression
    #
    @share
    def parse1_ternary_expression():
        left = parse1_atom()

        if qn() is not none:
            return left

        operator = tokenize_operator()

        if operator.is_end_of_ternary_expression:
            wk(operator)

            return left

        return parse1_any_ternary_expression__left__operator(left, operator)


    @share
    def parse1_any_ternary_expression__left__operator(left, operator):
        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_or_operator:
            left = parse1_or_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        my_line('left: %s; operator: %s; s: %s',
                left, operator, portray_string(qs()[qj():]))

        raise_unknown_line(1)


    #
    #   16.  Ternary-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist')
    #
    @share
    def parse1_ternary_expression_list():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if qn() is not none:
                raise_unknown_line(1)

            if operator.is_end_of_ternary_expression_list:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            if qn() is not none:
                return left

            operator = qk()

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        raise_unknown_line(1)


    #
    #   17.  Comprehension-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist_comp')
    #
    @share
    def parse1_comprehension_expression_list():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_comprehension_expression_list:
                my_line('=1=operator: %r', operator)
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if qn() is not none:
                raise_unknown_line(1)

            if operator.is_end_of_comprehension_expression_list:
                my_line('=2=operator: %r', operator)
                wk(operator)

                return left

        return parse1_any_comprehension_expression_list__left__operator(left, operator)


    @share
    def parse1_any_comprehension_expression_list__left__operator(left, operator):
        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_comprehension_expression_list:
                return left

            wk(none)

        if operator.is_or_operator:
            left = parse1_or_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_comprehension_expression_list:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_comprehension_expression_list:
                return left

            wk(none)

        my_line('left: %s; operator: %s; s: %s', left, operator, portray_string(qs()[qj():]))
        assert 0
        raise_unknown_line(1)
