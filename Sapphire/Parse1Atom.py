#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Atom')
def gem():
    show = 0


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
            left     = parse1_atom()
            operator = tokenize_operator()

            while 7 is 7:
                if operator.is_right_parenthesis:
                    return PathenthesizedExpression(token, left, operator)

                if operator.is_compare_operator:
                    left     = parse1_compare_expression(left, operator)
                    operator = qk()

                    wk(none)
                    continue

                raise_unknown_line(2)

        raise_unknown_line(3)


    @share
    def parse1_atom():
        token = tokenize_atom()

        if token.is_atom:
            return token

        if token.is_left_parenthesis:
            left     = parse1_atom()
            operator = tokenize_operator()

            while not operator.is_comma:
                if operator.is_right_parenthesis:
                    return PathenthesizedExpression(token, left, operator)

                if operator.is_compare_operator:
                    left     = parse1_compare_expression(left, operator)
                    operator = qk()

                    wk(none)
                    continue

                raise_unknown_line(2)

            token_2 = tokenize__comma__first_atom()

            if token_2.is_right_parenthesis:
                return Tuple_1(token, left, Comma_RightParenthesis(operator, token_2))

            raise_unknown_line(3)

        raise_unknown_line(4)
