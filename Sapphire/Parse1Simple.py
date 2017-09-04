#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Simple')
def gem():
    show = 7


    @share
    def parse1_statement_pass(m):
        if m.end('newline') is -1:
            raise_unknown_line(1)

        return StatementPass(m.group())


    @share
    def parse1_statement_return(m):
        if m.end('newline') is not -1:
            return keyword_return

        keyword_return = conjure_keyword_return(m.group())

        j = m.end()

        wi(j)
        wj(j)

        atom = tokenize_atom()

        newline = qn()

        if newline is not none:
            return StatementReturnExpression(keyword_return, atom, newline)

        operator = tokenize_operator()

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

            expression = parse1_call_expression__left__operator(atom, operator)
            newline    = qn()

            if newline is none:
                raise_unknown_line(3)
            
            return StatementReturnExpression(keyword_return, expression, newline)

        raise_unknown_line(3)
