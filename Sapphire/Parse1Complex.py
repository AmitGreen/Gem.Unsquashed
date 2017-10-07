#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Complex')
def gem():
    require_gem('Sapphire.UnaryStatement')


    show = 0


    def parse1_condition_statement__X__m(m, conjure_indented_keyword, evoke_header, conjure_body_statement):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_else_if(m.end('indented'), j)

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
            return evoke_header(indented_keyword, condition, operator)

        if not operator.is_colon:
            raise_unknown_line()

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line()

        if not left.is_atom:
            raise_unknown_line()

        return conjure_body_statement(
                   evoke_header(indented_keyword, condition, operator),
                   parse1_statement_expression__atom('', left),
               )


    @share
    def parse1_statement_else_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__else__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        j = m.end()

        keyword = evoke_indented_else_colon(m.end('indented'), m.start('colon'), j)

        wi(j)
        wj(j)

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line()

        if not left.is_atom:
            raise_unknown_line()

        return conjure_else_statement(keyword, parse1_statement_expression__atom('', left))


    @share
    def parse1_statement_else_if(m):
        return parse1_condition_statement__X__m(
                   m,
                   conjure_keyword_else_if,
                   conjure_else_if_header,
                   conjure_else_if_statement
               )


    @share
    def parse1_statement_except(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_except(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_operator()

        if operator.is_colon__line_marker:
            return conjure_except_header_1(indented_keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse1_ternary_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_operator()

        if operator_2.is_colon__line_marker:
            return conjure_except_header_2(indented_keyword, left, operator, right, operator_2)

        raise_unknown_line()


    @share
    def parse1_statement_except_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__except__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse1_statement_finally_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__finally__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse1_statement_for(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_for(m.end('indented'), j)

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

        return conjure_for_header(indented_keyword, left, operator, right, operator_2)


    @share
    def parse1_statement_if(m):
        return parse1_condition_statement__X__m(m, evoke_indented_if, conjure_if_header, conjure_if_statement)


    @share
    def parse1_statement_try_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__try__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse1_statement_while(m):
        return parse1_condition_statement__X__m(m, evoke_indented_while, conjure_while_header, conjure_while_statement)


    @share
    def parse1_statement_with(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_with(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_operator()

        if operator.is_colon__line_marker:
            return conjure_with_header_1(indented_keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse1_normal_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_operator()

        if operator_2.is_colon__line_marker:
            return conjure_with_header_2(indented_keyword, left, operator, right, operator_2)

        raise_unknown_line()
