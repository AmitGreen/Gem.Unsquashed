#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    require_gem('Sapphire.Core')


    @share
    def parse1_compare_expression(left, compare_operator):
        right    = tokenize_atom()
        operator = tokenize_operator()

        if operator.is_right_parenthesis:
            assert qk() is none

            wk(operator)

            return compare_operator.compare_expression_meta(left, compare_operator, right)

        raise_unknown_line(2)


    @share
    def parse1_or_expression(left, or_operator):
        if show is 7:
            my_line('%r, %r, %s', left, or_operator, portray_string(qs()[qj():]))

        right    = parse1_atom()
        operator = tokenize_operator()

        if show is 7:
            my_line('%r, %r, %r, %r, %s',
                    left, or_operator, right, operator, portray_string(qs()[qj():]))

        if (operator.is_right_parenthesis) or (operator.is_colon_newline):
            assert qk() is none

            wk(operator)

            return OrExpression(left, or_operator, right)

        raise_unknown_line(2)


    @share
    def parse1__argument__first_atom():
        #
        #<different-from: parse1_atom>
        #
        token = tokenize__argument__first_atom()

        if token.is__atom__or__right_parenthesis:
            return token
        #</different-from>

        if token.is_left_parenthesis:
            left     = parse1_atom()
            operator = tokenize_operator()

            while 7 is 7:
                if operator.is_right_parenthesis:
                    return PathenthesizedExpression(token, left, operator)

                if operator.is_compare_operator:
                    left     = parse1_compare_expression(left, operator)
                    operator = qk()

                    wk(none)
                    continue

                raise_unknown_line(2)

        raise_unknown_line(3)


    @share
    def parse1_atom():
        token = tokenize_atom()

        if token.is_atom:
            return token

        if token.is_left_parenthesis:
            left     = parse1_atom()
            operator = tokenize_operator()

            while not operator.is_comma:
                if operator.is_right_parenthesis:
                    return PathenthesizedExpression(token, left, operator)

                if operator.is_compare_operator:
                    left     = parse1_compare_expression(left, operator)
                    operator = qk()

                    wk(none)
                    continue

                raise_unknown_line(2)

            token_2 = tokenize__comma__first_atom()

            if token_2.is_right_parenthesis:
                return Tuple_1(token, left, Comma_RightParenthesis(operator, token_2))

            raise_unknown_line(3)

        raise_unknown_line(4)


    @share
    def parse1_expression_index(left, left_square_bracket):
        atom = tokenize_atom()

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(1)


    def parse1_statement_assign__left__equal_sign(indented, left, equal_sign):
        atom    = parse1_atom()
        newline = qn()

        if newline is not none:
            return AssignStatement(indented, left, equal_sign, atom, newline)

        my_line('indented: %r; left: %r; equal_sign: %r; atom: %s; s: %s',
                indented, left, equal_sign, atom, portray_string(qs()[qj():]))

        raise_unknown_line(2)


    @share
    def parse1_statement_expression__symbol(indented, left):
        s = qs()

        if show:
            my_line('indented: %r, left: %r; s: %r',
                    indented, left, s[qj():])

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_dot:
                right = tokenize_name()

                if qn() is not none:
                    raise_unknown_line(1)

                if show is 7:
                    my_line('left: %r; operator: %s; right: %s; s: %s',
                            left, operator, right, portray_string(s[m3.end():]))

                operator_2 = tokenize_operator()

                if qn() is not none:
                    raise_unknown_line(2)

                if operator_2.is_left_parenthesis:
                    arguments = parse1_arguments__left_parenthesis(operator_2)
                    newline   = qn()

                    if newline is none:
                        raise_unknown_line(3)

                    return StatementMethodCall(indented, left, operator, right, arguments, newline)
                
                raise_unknown_line(4)

            if operator.is_arguments_0:
                newline = qn()

                if newline is not none:
                    return StatementCall(indented, left, operator, newline)

                left = ExpressionCall(left, operator)
                continue

            if operator.is_left_parenthesis:
                arguments = parse1_arguments__left_parenthesis(operator)
                newline   = qn()

                if newline is not none:
                    return StatementCall(indented, left, arguments, newline)

                left = ExpressionCall(left, arguments)
                continue

            if operator.is_equal_sign:
                return parse1_statement_assign__left__equal_sign(indented, left, operator)

            raise_unknown_line(6)
