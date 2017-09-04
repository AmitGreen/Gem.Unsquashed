#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Atom')
def gem():
    show = 0


    def parse1__parenthesized_expression__left_parenthesis(left_parenthesis):
        left     = parse1_atom()
        operator = tokenize_operator()

        while not operator.is_comma:
            if operator.is_right_parenthesis:
                return PathenthesizedExpression(left_parenthesis, left, operator)

            if operator.is_compare_operator:
                left     = parse1_compare_expression__left__operator(left, operator)
                operator = qk()

                wk(none)
                continue

            raise_unknown_line(1)

        token_2 = tokenize__comma__first_atom()

        if token_2.is_right_parenthesis:
            return Tuple_1(left_parenthesis, left, Comma_RightParenthesis(operator, token_2))

        raise_unknown_line(2)


    @share
    def parse1__argument__first_atom():
        #
        #<different-from: parse1_atom>
        #
        token = tokenize__argument__first_atom()

        if token.is__atom__or__right_parenthesis:
            return token
        #</different-from>

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        raise_unknown_line(1)


    @share
    def parse1_atom():
        token = tokenize_atom()

        if token.is_atom:
            return token

        if token.is_left_parenthesis:
            return parse1__parenthesized_expression__left_parenthesis(token)

        raise_unknown_line(1)
