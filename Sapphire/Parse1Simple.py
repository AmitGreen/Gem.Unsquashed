#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Simple')
def gem():
    show = 7


    @share
    def parse1_statement_return(m1):
        if m1.end('newline') is not -1:
            return StatementReturn(m1.group())

        keyword_return = KeywordReturn(m1.group())
        s              = qs()

        wj(m1.end())

        #
        #<atom>
        #
        atom = tokenize_normal_atom()
        #</atom>

        newline = qn()

        if newline is not none:
            return StatementReturnExpression(keyword_return, atom, newline)

        #
        #<postfix>
        #
        m3 = statement_postfix_match1(s, qj())

        if m3 is none:
            raise_unknown_line(2)

        wj(m3.end())

        left_parenthesis__end = m3.end('left_parenthesis__ow')
        #</postfix>

        if left_parenthesis__end is -1:
            return StatementReturnExpression(keyword_return, atom, conjure_token_newline(m3.group()))

        left_parenthesis  = OperatorLeftParenthesis(s[qi() : left_parenthesis__end])
        right_parenthesis = m3.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = conjure_right_parenthesis(right_parenthesis)

            if m3.end('comment_newline') is not -1:
                return StatementReturnExpression(
                           keyword_return,
                           ExpressionCall(atom, Arguments_0(left_parenthesis, right_parenthesis)),
                           conjure_token_newline(s[m3.end('right_parenthesis'):]),
                       )

            raise_unknown_line(3)

        expression = parse1_expression_call(atom, left_parenthesis)

        return StatementReturnExpression(keyword_return, expression, qn())
