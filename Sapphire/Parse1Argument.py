#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Argument')
def gem():
    show = 0


    @share
    def parse1_arguments__left_parenthesis(left_parenthesis, j):
        s = qs()

        if show is 7:
            line('parse1_arguments__left_parenthesis: left_parenthesis: %s; s: %s',
                 left_parenthesis, portray_raw_string(s[j:]))

        #
        #<single_quote>
        #
        m1 = single_quote_match(s, j)

        if m1 is none:
            raise_unknown_line(1)

        argument_1 = SingleQuote(m1.group())
        #</single_quote>

        #
        #<right-parenthesis>
        #
        m2 = statement_argument1_operator_match1(s, m1.end())

        if m2 is none:
            raise_unknown_line(2)

        right_parenthesis = OperatorRightParenthesis(m2.group())
        #</right-parenthesis>

        wj(m2.end())

        return Arguments_1(left_parenthesis, argument_1, right_parenthesis)
