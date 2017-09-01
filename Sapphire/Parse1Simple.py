#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Simple')
def gem():
    show = 7


    @share
    def parse1_statement_pass(m1):
        if m1.end('newline') is -1:
            raise_unknown_line(1)

        return StatementPass(m1.group())


    @share
    def parse1_statement_return(m1):
        if m1.end('newline') is not -1:
            return StatementReturn(m1.group())

        keyword_return = KeywordReturn(m1.group())
        s              = qs()

        wj(m1.end())

        #
        #<normal-atom>
        #
        atom = tokenize_normal_atom()
        #</normal-atom>

        newline = qn()

        if newline is not none:
            return StatementReturnExpression(keyword_return, atom, newline)

        #
        #<postfix-operator>
        #
        operator = tokenize_postfix_operator()
        #</postfix-operator>

        if operator.is_arguments_0:
            newline = qn()

            if newline is not none:
                return StatementReturnExpression(
                           keyword_return,
                           ExpressionCall(atom, operator),
                           newline,
                       )

            raise_unknown_line(1)

        if operator.is_left_parenthesis:
            if qn() is not none:
                raise_unknown_line(2)

            expression = parse1_expression_call(atom, operator)
            newline    = qn()

            if newline is none:
                raise_unknown_line(3)
            
            return StatementReturnExpression(keyword_return, expression, newline)

        raise_unknown_line(3)
