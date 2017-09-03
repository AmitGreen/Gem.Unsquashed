#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1ExpressionStatement')
def gem():
    show = 0


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
