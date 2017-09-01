#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Complex')
def gem():
    show = 7


    @share
    def parse1_statement_except_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line(1)

        return conjure_except_colon(m.group())


    @share
    def parse1_statement_if(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_if = conjure_keyword_if(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_normal_atom()

        if qn() is not none:
            raise_unknown_line(2)
            
        operator = tokenize_normal_operator()

        if operator.is_colon_newline:
            return IfHeader(keyword_if, left, operator)

        line('%s: %r %r %r', my_name(), keyword_if, left, operator)
        raise_unknown_line(3)


    @share
    def parse1_statement_try_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line(1)

        return conjure_try_colon(m.group())


    @share
    def parse1_statement_with(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_with = conjure_keyword_with(m.group())

        wj(m.end())

        left = tokenize_normal_atom()

        if qn() is not none:
            raise_unknown_line(2)

        while 7 is 7:
            operator = tokenize_normal_operator()

            if operator.is_arguments_0:
                left = ExpressionCall(left, operator)
                continue

            if operator.is_keyword_as:
                break

            raise_unknown_line(3)

        right      = tokenize_normal_atom()
        operator_2 = tokenize_normal_operator()

        if operator_2.is_colon_newline:
            return WithHeader(keyword_with, left, operator, right, operator_2)

        raise_unknown_line(4)
