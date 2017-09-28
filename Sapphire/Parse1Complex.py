#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Complex')
def gem():
    show = 0


    def parse1_condition_statement__X__m(m, conjure, MetaHeader, MetaStatement):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword = conjure(m.group())

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
            return MetaHeader(keyword, condition, operator)

        if not operator.is_colon:
            raise_unknown_line()

        left = parse1_atom()

        if qn() is not none:
            raise_unknown_line()

        if not left.is_atom:
            raise_unknown_line()

        return MetaStatement(
                   keyword,
                   condition,
                   operator,
                   parse1_statement_expression__atom('', left),
               )


    def parse1_condition_statement__X__m2(m, conjure_indented_keyword, evoke_header, MetaStatement):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = conjure_indented_keyword(m.end('indented'), j)

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

        return MetaStatement(
                   indented_keyword,
                   condition,
                   operator,
                   parse1_statement_expression__atom('', left),
               )


    @share
    def parse1_statement_else_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__else__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        keyword_colon = conjure_else_colon(m.group())

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
            return conjure__finally__colon__line_marker(m.group())

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
        return parse1_condition_statement__X__m2(m, evoke_indented_if, conjure_if_header, IfStatement)


    @share
    def parse1_statement_try_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__try__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse1_statement_while(m):
        return parse1_condition_statement__X__m2(m, evoke_indented_while, conjure_while_header, WhileStatement)


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
