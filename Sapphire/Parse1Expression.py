#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    require_gem('Sapphire.Core')


    @share
    def parse1_nested_atom():
        if show:
            line('%s: %r', my_name(), qs()[qj():])

        token = tokenize_nested_atom()

        if token.is_atom:
            return token

        line('%s: %s', my_name(), token)
        raise_unknown_line(1)


    @share
    def parse1_normal_atom():
        token = tokenize_normal_atom()

        if token.is_atom:
            return token

        if token.is_left_parenthesis:
            left     = parse1_nested_atom()
            #operator = 

            raise_unknown_line(1)

        raise_unknown_line(2)


    @share
    def parse1_expression_index(left, left_square_bracket):
        atom = tokenize_nested_atom()

        while 7 is 7:
            operator = tokenize_nested_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(1)


    def parse1_statement_assign__left__equal_sign(indented, left, equal_sign):
        if show is 7:
            line('%s: indented: %r; left: %r; equal_sign: %r; %s',
                 my_name(), indented, left, equal_sign, portray_string(qs()[qj():]))

        atom    = tokenize_normal_atom()
        newline = qn()

        if newline is not none:
            return AssignStatement(indented, left, equal_sign, atom, newline)

        raise_unknown_line(2)


    @share
    def parse1_statement_expression__symbol(indented, left):
        s = qs()

        if show:
            line('%s: indented: %r, left: %r; s: %r',
                 my_name(), indented, left, s[qj():])

        while 7 is 7:
            operator = tokenize_normal_operator()

            if operator.is_dot:
                #
                #<name1>
                #
                m3 = name_match(s, qj())

                if m3 is none:
                    raise_unknown_line(1)

                right = conjure_identifier(m3.group())
                #</name1>

                dot = operator
                
                if show:
                    line('%s: left: %r; dot: %s; right: %s; s: %s',
                         parse1_statement_expression__symbol.__name__, left, dot, right, portray_raw_string(s[m3.end():]))

                #
                #<postfix1-operator>
                #
                m4 = statement_postfix_operator_match1(s, m3.end())

                if m4 is none:
                    raise_unknown_line(2)

                wj(m4.end())

                right_parenthesis = m4.group('right_parenthesis')
                #</postfix1-operator>

                if right_parenthesis is not none:
                    raise_unknown_line(3)
                
                left_parenthesis = m4.group('left_parenthesis__ow')

                if left_parenthesis is not none:
                    assert m4.start('comment_newline') is -1

                    arguments = parse1_arguments__left_parenthesis(conjure_left_parenthesis(left_parenthesis))
                    newline   = qn()

                    if newline is none:
                        raise_unknown_line(4)

                    return StatementMethodCall(indented, left, dot, right, arguments, newline)
                
                raise_unknown_line(5)


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
