#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    @share
    def parse1_compare_expression(left, compare_operator):
        right    = tokenize_atom()
        operator = tokenize_operator()

        if operator.is_right_parenthesis:
            assert qk() is none

            wk(operator)

            return compare_operator.compare_expression_meta(left, compare_operator, right)

        raise_unknown_line(2)


    @share
    def parse1_or_expression(left, or_operator):
        if show is 7:
            my_line('%r, %r, %s', left, or_operator, portray_string(qs()[qj():]))

        right    = parse1_atom()
        operator = tokenize_operator()

        if show is 7:
            my_line('%r, %r, %r, %r, %s',
                    left, or_operator, right, operator, portray_string(qs()[qj():]))

        if (operator.is_right_parenthesis) or (operator.is_colon_newline):
            assert qk() is none

            wk(operator)

            return OrExpression(left, or_operator, right)

        raise_unknown_line(2)


    @share
    def parse1_expression_index(left, left_square_bracket):
        atom = tokenize_atom()

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(1)


