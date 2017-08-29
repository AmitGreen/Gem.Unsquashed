#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Simple')
def gem():
    show = 7


    @share
    def parse1_statement_assert(m):
        keyword = conjure_keyword_assert(m.group())

        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return AssertStatement_1(keyword, left, newline)

        wk(none)

        if not operator.is_comma:
            raise_unknown_line()

        right = parse1_ternary_expression()

        operator_2 = qk()

        if operator_2 is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return AssertStatement_2(keyword, left, operator, right, newline)

        raise_unknown_line()


    @share
    def parse1_statement_delete(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword = conjure_keyword_delete(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_normal_expression()

        operator = qk()

        if operator is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return DeleteStatement_1(keyword, left, newline)

        wk(none)

        if not operator.is_comma:
            raise_unknown_line()

        many = [left, operator]

        while 7 is 7:
            many.append(parse1_normal_expression())

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is none:
                    raise_unknown_line()

                return DeleteStatement_Many(keyword, Tuple(many), newline)

            wk(none)

            if not operator.is_comma:
                raise_unknown_line()

            many.append(operator)


    @share
    def parse1_statement_pass(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return StatementPass(m.group())


    @share
    def parse1_statement_raise(m):
        keyword = conjure_keyword_raise(m.group())

        if m.end('newline') is not -1:
            return keyword

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_ternary_expression()

        operator = qk()

        if operator is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return RaiseStatement_1(keyword, left, newline)

        wk(none)

        if not operator.is_comma:
            raise_unknown_line()

        middle = parse1_ternary_expression()

        operator_2 = qk()

        if operator_2 is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return RaiseStatement_2(keyword, left, operator, middle, newline)

        wk(none)

        if not operator_2.is_comma:
            raise_unknown_line()

        right = parse1_ternary_expression()

        if qk() is none:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return RaiseStatement_3(keyword, left, operator, middle, operator_2, right, newline)

        raise_unknown_line()



    @share
    def parse1_statement_return(m):
        keyword = conjure_keyword_return(m.group())

        if m.end('newline') is not -1:
            return keyword

        j = m.end()

        wi(j)
        wj(j)

        right = parse1_ternary_expression_list()

        if qk() is not none:
            #my_line('qk: %r; full: %s', qk(), portray_string(qs()))
            raise_unknown_line()

        newline = qn()

        if newline is none:
            raise_unknown_line()

        return ReturnStatement_1(keyword, right, newline)


    @share
    def parse1_statement_yield(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        keyword = conjure_keyword_yield(m.group())

        j = m.end()

        wi(j)
        wj(j)

        left = parse1_ternary_expression_list()

        if qk() is not none:
            raise_unknown_line()

        newline = qn()

        if newline is none:
            raise_unknown_line()

        return YieldStatement(keyword, left, newline)
