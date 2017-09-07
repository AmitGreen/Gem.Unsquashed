#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Complex')
def gem():
    show = 0


    @share
    def parse1_statement_except_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line(1)

        return conjure_except_colon(m.group())


    @share
    def parse1_statement_for(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_for = conjure_keyword_for(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_normal_expression_list()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            if qn() is not none:
                raise_unknown_line(2)

            operator = tokenize_operator()

            if qn() is not none:
                raise_unknown_line(3)

        if not operator.is_keyword_in:
            raise_unknown_line(4)

        right = parse1_ternary_expression_list()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            if qn() is not none:
                raise_unknown_line(5)

            operator_2 = tokenize_operator()

            if qn() is not none:
                raise_unknown_line(6)

        if not operator_2.is_colon_newline:
            raise_unknown_line(7)

        return ForHeader(keyword_for, left, operator, right, operator_2)


    @share
    def parse1_statement_if(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_if = conjure_keyword_if(m.group())

        j = m.end()

        wi(j)
        wj(j)

        condition = parse1_ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_operator()

        if qn() is not none:
            raise_unknown_line(3)
            
        if operator.is_colon_newline:
            return IfHeader(keyword_if, condition, operator)

        if not operator.is_colon:
            raise_unknown_line(4)

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line(5)

        if not left.is_atom:
            raise_unknown_line(7)

        return IfStatement(
                   keyword_if,
                   condition,
                   operator,
                   parse1_statement_expression__symbol('', left),
               )


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

        j = m.end()

        wi(j)
        wj(j)

        left = tokenize_atom()

        if qn() is not none:
            raise_unknown_line(2)

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_arguments_0:
                left = CallExpression(left, operator)
                continue

            if operator.is_keyword_as:
                break

            raise_unknown_line(3)

        right      = tokenize_atom()
        operator_2 = tokenize_operator()

        if operator_2.is_colon_newline:
            return WithHeader(keyword_with, left, operator, right, operator_2)

        raise_unknown_line(4)
