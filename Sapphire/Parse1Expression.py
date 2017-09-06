#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 7


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
                    return ExpressionDot(left, operator, name)

                operator_2 = tokenize_operator()

                if operator_2.is_dot:
                    if qn() is not none:
                        raise_unknown_line(1)

                    name_2 = tokenize_name()

                    if qn() is not none:
                        return ExpressionDot_2(left, operator, name, operator_2, name_2)

                    operator_3 = tokenize_operator()

                    if operator_3.is_dot:
                        if qn() is not none:
                            raise_unknown_line(2)

                        name_3 = tokenize_name()

                        if qn() is not none:
                            return ExpressionDot_3(left, operator, name, operator_2, name_2, operator_3, name_3)

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
                                    raise_unknown_line(4)

                                if not operator.is_postfix_operator:
                                    wk(operator)

                                    return left
                        elif operator_4.is_postfix_operator:
                            left = ExpressionDot_3(left, operator, name, operator_2, name_2, operator_3, name_3)

                            operator = operator_4
                        else:
                            wk(operator_4)

                            return ExpressionDot_3(left, operator, name, operator_2, name_2, operator_3, name_3)

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
                                raise_unknown_line(5)

                            if not operator.is_postfix_operator:
                                wk(operator)

                                return left

                    elif operator_3.is_postfix_operator:
                        left = ExpressionDot_2(left, operator, name, operator_2, name_2)

                        operator = operator_3
                    else:
                        wk(operator_3)

                        return ExpressionDot_2(left, operator, name, operator_2, name_2)

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
                            raise_unknown_line(6)

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

                elif operator_2.is_postfix_operator:
                    left = ExpressionDot(left, operator, name)

                    operator = operator_2
                else:
                    wk(operator_2)

                    return ExpressionDot(left, operator, name)


        raise_unknown_line(6)


    @share
    def parse1_index_expression__left__operator(left, left_square_bracket):
        atom = tokenize_atom()

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(1)


    #
    #   2.  Power-Expression (Python 2.7.14rc1 grammer calls this 'power')
    #

    #
    #   3.  Unary-Expression (Python 2.7.14rc1 grammer calls this 'factor')
    #

    #
    #   4.  Multiply-Expression (Python 2.7.14rc1 grammer calls this 'term')
    #

    #
    #   5.  Arithmetic-Expression (Python 2.7.14rc1 grammer calls this 'arith_expr')
    #

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
    #   9.  Expression (Logical-Inclusive-Or) (Python 2.7.14rc1 grammer calls this 'expr')
    #

    #
    #   10.  Compare-Expression (Python 2.7.14rc1 grammer calls this 'comparasion')
    #
    @share
    def parse1_compare_expression__left__operator(left, compare_operator):
        right    = tokenize_atom()
        operator = tokenize_operator()

        if operator.is_right_parenthesis:
            assert qk() is none

            wk(operator)

            return compare_operator.compare_expression_meta(left, compare_operator, right)

        raise_unknown_line(2)


    #
    #   11.  Not-Expression (Python 2.7.14rc1 grammer calls this 'not_test')
    #
    @share
    def parse1_not_expression__operator(not_operator):
        if show is 7:
            my_line('%s, %s', not_operator, portray_raw_string(qs()[qj(): ]))

        right = parse1_atom()

        operator = qk()

        if operator is not none:
            if qn() is not none:
                raise_unknown_line(1)

            if operator.is_end_of_not_expression:
                return NotExpression(not_operator, right)

            wk(none)
        else:
            newline = qn()

            if qn() is not none:
                return NotExpression(not_operator, right)

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line(2)

            if operator.is_end_of_not_expression:
                wk(operator)
                return NotExpression(not_operator, right)

        my_line('right: %s, operator: %s', right, operator)
        raise_unknown_line(3)


    #
    #   12. Boolean-And-Expression (Python 2.7.14rc1 grammer calls this 'and_test')
    #

    #
    #   13. Boolean-Or-Expression (Python 2.7.14rc1 grammer calls this 'or_test')
    #
    @share
    def parse1_or_expression__left__operator(left, or_operator):
        if show is 7:
            my_line('%r, %r, %s', left, or_operator, portray_string(qs()[qj():]))

        right = parse1_atom()

        if qk() is not qn() is not none:
            raise_unknown_line(1)

        operator = tokenize_operator()

        if qk() is not qn() is not none:
            raise_unknown_line(2)

        while not operator.is_end_of_expression:
            if operator.is_or_operator:
                left        = OrExpression(left, or_operator, right)
                or_operator = operator

                if qn() is not none:
                    raise_unknown_line(3)

                right = parse1_atom()

                operator = qk()

                if operator is none:
                    operator = tokenize_operator()

                    if qk() is not none:
                        my_line('qk: %r, qn: %r', qk(), qn())
                        raise_unknown_line(4)
                else:
                    wk(none)

                continue

            my_line('left: %r; or_operator: %r; right: %r; operator: %r; s: %s',
                    left, or_operator, right, operator, portray_string(qs()[qj():]))

            raise_unknown_line(5)

        if qk() is not none:
            my_line('qk: %r, qn: %r', qk(), qn())
            raise_unknown_line(6)

        wk(operator)

        return OrExpression(left, or_operator, right)


    #
    #   14.  Ternary-Expression (Python 2.7.14rc1 grammer calls this 'test')
    #   14.  Lambda-Expression  (Python 2.7.14rc1 grammer calls this 'lambdef')
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
    def parse1_any_ternary_expression():
        left = tokenize_atom()

        if qk() is not none:
            raise_unknown_line(1)

        if qn() is not none:
            raise_unknown_line(2)

        operator = tokenize_operator()

        if qk() is not none:
            raise_unknown_line(3)

        if qn() is not none:
            raise_unknown_line(4)

        if operator.is_end_of_expression:
            wk(operator)

            return left

        return parse1_any_ternary_expression__left__operator(left, operator)


    @share
    def parse1_any_ternary_expression__left__operator(left, operator):
        if operator.is_dot:
            left = parse1_dot_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        if operator.is_or_operator:
            left = parse1_or_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        my_line('left: %s; operator: %s; s: %s',
                left, operator, portray_string(qs()[qj():]))

        raise_unknown_line(1)


    #
    #   15.  Comprehension-Expression (Python 2.7.14rc1 grammer calls this 'testlist_comp')
    #
    @share
    def parse1_any_comprehension_expression():
        left = tokenize_atom()

        operator = tokenize_operator()

        if operator.is_end_of_expression:
            wk(operator)

            return left

        return parse1_any_comprehension_expression__left__operator(left, operator)


    @share
    def parse1_any_comprehension_expression__left__operator(left, operator):
        if operator.is_or_operator:
            left = parse1_or_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        my_line('left: %s; operator: %s; s: %s',
                left, operator, portray_string(qs()[qj():]))

        raise_unknown_line(1)
