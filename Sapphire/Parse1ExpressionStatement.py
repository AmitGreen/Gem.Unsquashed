#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1ExpressionStatement')
def gem():
    show = 0


    def parse1_statement_assign__left__equal_sign(indented, left, equal_sign):
        right = parse1_ternary_expression_list()

        newline = qn()

        if newline is not none:
            return ModifyStatement(indented, left, equal_sign, right, newline)

        my_line('indented: %r; left: %r; equal_sign: %r; right: %s; s: %s',
                indented, left, equal_sign, right, portray_string(qs()[qj():]))
        raise_unknown_line(2)


    def parse1_statement_modify__left__operator(indented, left, modify_operator):
        right = parse1_ternary_expression_list()

        newline = qn()

        if newline is not none:
            return ModifyStatement(indented, left, modify_operator, right, newline)

        my_line('indented: %r; left: %r; modify_operator: %r; right: %s; s: %s',
                indented, left, modify_operator, right, portray_string(qs()[qj():]))
        raise_unknown_line(2)


    @share
    def parse1_statement_expression__atom(indented, left):
        if left.is_atom:
            pass
        elif left.is_keyword_not:
            left = parse1_not_expression__operator(left)
        elif left.is_minus_sign:
            left = parse1_negative_expression__operator(left)
        elif left.is_left_parenthesis:
            left = parse1__parenthesized_expression__left_parenthesis(left)
        elif left.is_left_square_bracket:
            left = parse1__list_expression__left_square_bracket(left)
        else:
            raise_unknown_line(1)

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            newline = qn()

            if newline is not none:
                return StatementExpression(indented, left, newline)

            operator = tokenize_operator()

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left__operator(left, operator, indented)

            if left.is_statement:
                return left

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return StatementExpression(indented, left, newline)

                raise_unknown_line(1)

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return StatementExpression(indented, left, newline)

                raise_unknown_line(2)

            wk(none)

        if operator.is_keyword_or:
            left = parse1_boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return StatementExpression(indented, left, newline)

                raise_unknown_line(3)

            wk(none)

        if operator.is_keyword_if:
            left = parse1_ternary_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return StatementExpression(indented, left, newline)

                raise_unknown_line(4)

            wk(none)

        if operator.is_equal_sign:
            return parse1_statement_assign__left__equal_sign(indented, left, operator)

        if operator.is_modify_operator:
            return parse1_statement_modify__left__operator(indented, left, operator)

        my_line('operator: %s', operator)
        raise_unknown_line(5)
