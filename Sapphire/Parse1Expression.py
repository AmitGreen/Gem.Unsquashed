#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    require_gem('Sapphire.Core')


    lookup_operator = {
                          none : none,
                          '.' : conjure_dot,
                          '=' : OperatorEqualSign,
                      }.__getitem__


    @share
    def parse1_expression_index(left, left_square_bracket):
        atom = tokenize_nested_atom()

        while 7 is 7:
            operator = tokenize_nested_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(2)


    @share
    def parse1_statement_expression__symbol(indented, identifier):
        s = qs()

        if show:
            line('%s: indented: %r, identifier: %r; s: %r',
                 my_name(), indented, identifier, s[qj():])

        operator = tokenize_postfix_operator()

        if operator.is_arguments_0:
            newline = qn()

            if newline is not none:
                return StatementCall(indented, identifier, operator, newline)

            raise_unknown_line(2)

        if operator.is_dot:
            #
            #<name1>
            #
            m3 = name_match(s, qj())

            if m3 is none:
                raise_unknown_line(3)

            right = conjure_identifier(m3.group())
            #</name1>

            dot = operator
            
            if show:
                line('%s: identifier: %r; dot: %s; right: %s; s: %s',
                     parse1_statement_expression__symbol.__name__, identifier, dot, right, portray_raw_string(s[m3.end():]))

            #
            #<postfix1-operator>
            #
            m4 = statement_postfix_operator_match1(s, m3.end())

            if m4 is none:
                raise_unknown_line(4)

            wj(m4.end())

            right_parenthesis = m4.group('right_parenthesis')
            #</postfix1-operator>

            if right_parenthesis is not none:
                raise_unknown_line(5)
            
            left_parenthesis = m4.group('left_parenthesis')

            if left_parenthesis is not none:
                assert m4.start('comment_newline') is -1

                arguments = parse1_arguments__left_parenthesis(conjure_left_parenthesis(left_parenthesis))
                newline   = qn()

                if newline is none:
                    raise_unknown_line(6)

                return StatementMethodCall(indented, identifier, dot, right, arguments, newline)
            
            raise_unknown_line(7)

        if operator.is_left_parenthesis:
            arguments = parse1_arguments__left_parenthesis(operator)
            newline   = qn()

            if newline is not none:
                return StatementCall(indented, identifier, arguments, newline)

            raise_unknown_line(9)


        line('%s: indented: %r; identifier: %r; operator: %r', my_name(), indented, identifier, operator)

        raise_unknown_line(10)
