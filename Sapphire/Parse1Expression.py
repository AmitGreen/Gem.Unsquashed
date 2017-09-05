#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    #
    #   1.  Index
    #
    @share
    def parse1_index_expression__left__operator(left, left_square_bracket):
        atom = tokenize_atom()

        while 7 is 7:
            operator = tokenize_operator()

            if operator.is_right_square_bracket:
                return ExpressionIndex_1(left, left_square_bracket, atom, operator)

            raise_unknown_line(1)


    #
    #   2.  Power
    #

    #
    #   3.  Factor
    #

    #
    #   4.  Multiply
    #

    #
    #   5.  Arithmetic
    #

    #
    #   6.  Shift
    #

    #
    #   7.  Logical-And
    #

    #
    #   8.  Logical-Exclusive-Or
    #

    #
    #   9.  Expression (Logical-Inclusive-Or)
    #
    if 0:
        @share
        def parse1_expression():
            left = tokenize_atom()
            operator = tokenize_operator()

            if operator.is_end_of_expression:
                wk(operator)

                return left

            return parse1_expression__left__operator(left, operator)




    #
    #   10.  compare
    #
    @share
    def parse1_compare_expression__left__operator(left, compare_operator):
        right    = tokenize_atom()
        operator = tokenize_operator()

        if operator.is_right_parenthesis:
            assert qk() is none

            wk(operator)

            return compare_operator.compare_expression_meta(left, compare_operator, right)

        raise_unknown_line(2)


    #
    #   11. Not
    #
    @share
    def parse1_not_expression__operator(not_operator):
        if show is 7:
            my_line('%s, %s', not_operator, portray_raw_string(qs()[qj(): ]))

        right = parse1_atom()

        operator = qk()

        if operator is not none:
            if qn() is not none:
                raise_unknown_line(1)

            if operator.is_end_of_not_expression:
                return NotExpression(not_operator, right)

            wk(none)
        else:
            newline = qn()

            if qn() is not none:
                return NotExpression(not_operator, right)

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line(2)

            if operator.is_end_of_not_expression:
                wk(operator)
                return NotExpression(not_operator, right)

        my_line('right: %s, operator: %s', right, operator)
        raise_unknown_line(3)


    #
    #   12. Boolean-And
    #

    #
    #   13. Boolean-Or
    #
    @share
    def parse1_or_expression__left__operator(left, or_operator):
        if show is 7:
            my_line('%r, %r, %s', left, or_operator, portray_string(qs()[qj():]))

        right = parse1_atom()

        if qk() is not qn() is not none:
            raise_unknown_line(1)

        operator = tokenize_operator()

        if qk() is not qn() is not none:
            raise_unknown_line(2)

        while not operator.is_end_of_expression:
            if operator.is_or_operator:
                left        = OrExpression(left, or_operator, right)
                or_operator = operator

                if qn() is not none:
                    raise_unknown_line(3)

                right = parse1_atom()

                operator = qk()

                if operator is none:
                    operator = tokenize_operator()

                    if qk() is not none:
                        my_line('qk: %r, qn: %r', qk(), qn())
                        raise_unknown_line(4)
                else:
                    wk(none)

                continue

            my_line('left: %r; or_operator: %r; right: %r; operator: %r; s: %s',
                    left, or_operator, right, operator, portray_string(qs()[qj():]))

            raise_unknown_line(5)

        if qk() is not none:
            my_line('qk: %r, qn: %r', qk(), qn())
            raise_unknown_line(6)

        wk(operator)

        return OrExpression(left, or_operator, right)


    @share
    def parse1_any_or_expression__left__operator(left, operator):
        if operator.is_or_operator:
            left = parse1_or_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left__operator(left, operator)

            operator = qk()

            if operator.is_end_of_expression:
                return left

            wk(none)

        my_line('left: %s; operator: %s; s: %s',
                left, operator, portray_string(qs()[qj():]))

        raise_unknown_line(1)


#
#   14. Lambda
#
