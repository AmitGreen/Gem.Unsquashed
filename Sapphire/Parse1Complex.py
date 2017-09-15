#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Complex')
def gem():
    show = 0


    def parse1_condition_statement__X__m(m, conjure, MetaHeader, MetaStatement):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword_if = conjure(m.group())

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
            raise_unknown_line()

        if operator.is_colon__line_marker:
            return MetaHeader(keyword_if, condition, operator)

        if not operator.is_colon:
            raise_unknown_line()

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line()

        if not left.is_atom:
            raise_unknown_line()

        return MetaStatement(
                   keyword_if,
                   condition,
                   operator,
                   parse1_statement_expression__atom('', left),
               )


    @share
    def parse1_statement_else_colon(m):
        keyword_colon = conjure_else_colon(m.group())

        if m.end('newline') is not -1:
            return keyword_colon

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line()

        if not left.is_atom:
            raise_unknown_line()

        return ElseStatement(
                   keyword_colon,
                   parse1_statement_expression__atom('', left),
               )


    @share
    def parse1_statement_else_if(m):
        return parse1_condition_statement__X__m(m, conjure_keyword_else_if, ElseIfHeader, ElseIfStatement)


    @share
    def parse1_statement_except(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword = conjure_keyword_except(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_operator()

        if operator.is_colon__line_marker:
            return WithHeader_1(keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse1_ternary_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_operator()

        if operator_2.is_colon__line_marker:
            return ExceptHeader_2(keyword, left, operator, right, operator_2)

        raise_unknown_line()


    @share
    def parse1_statement_except_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return conjure_except_colon(m.group())


    @share
    def parse1_statement_finally_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return conjure_finally_colon(m.group())


    @share
    def parse1_statement_for(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

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
                raise_unknown_line()

            operator = tokenize_operator()

            if qn() is not none:
                raise_unknown_line()

        if not operator.is_keyword_in:
            raise_unknown_line()

        right = parse1_ternary_expression_list()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            if qn() is not none:
                raise_unknown_line()

            operator_2 = tokenize_operator()

            if qn() is not none:
                raise_unknown_line()

        if not operator_2.is_colon__line_marker:
            raise_unknown_line()

        return ForHeader(keyword_for, left, operator, right, operator_2)


    @share
    def parse1_statement_if(m):
        return parse1_condition_statement__X__m(m, conjure_keyword_if, IfHeader, IfStatement)


    @share
    def parse1_statement_try_colon(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return conjure_try_colon(m.group())


    @share
    def parse1_statement_while(m):
        return parse1_condition_statement__X__m(m, conjure_keyword_while, WhileHeader, WhileStatement)


    @share
    def parse1_statement_with(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword = conjure_keyword_with(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_operator()

        if operator.is_colon__line_marker:
            return WithHeader_1(keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse1_normal_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_operator()

        if operator_2.is_colon__line_marker:
            return WithHeader_2(keyword, left, operator, right, operator_2)

        raise_unknown_line()
