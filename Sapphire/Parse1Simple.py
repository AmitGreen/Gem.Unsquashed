#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Simple')
def gem():
    show = 7


    @share
    def parse1_statement_delete(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword = conjure_keyword_delete(m.group())

        j = m.end()

        wi(j)
        wj(j)

        right = parse1_normal_expression_list()

        if qk() is not none:
            raise_unknown_line(2)

        newline = qn()

        if newline is none:
            raise_unknown_line(3)

        return DeleteExpression(keyword, right, newline)


    @share
    def parse1_statement_pass(m):
        if m.end('newline') is -1:
            raise_unknown_line(1)

        return StatementPass(m.group())


    @share
    def parse1_statement_return(m):
        keyword = conjure_keyword_return(m.group())

        if m.end('newline') is not -1:
            return keyword

        j = m.end()

        wi(j)
        wj(j)

        right = parse1_normal_expression_list()

        if qk() is not none:
            raise_unknown_line(2)

        newline = qn()

        if newline is none:
            raise_unknown_line(3)

        return ReturnExpression(keyword, right, newline)
