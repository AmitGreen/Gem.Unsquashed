#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 7


    @share
    def parse1_expression_call(j, left, left_parenthesis):
        arguments = parse1_arguments__left_parenthesis(left_parenthesis, j)

        return ExpressionCall(left, arguments)


    @share
    def parse1_arguments__left_parenthesis(left_parenthesis, j):
        s = qs()

        #
        #<atom1>
        #
        m1 = atom_match1(s, j)

        if m1 is none:
            raise_unknown_line(1)

        s1     = m1.group()
        atom   = find_atom_type(s1[0])(s1)
        #</atom1>

        if show is 7:
            line('parse1_arguments__left_parenthesis: left_parenthesis: %s; atom: %s; s: %s',
                 left_parenthesis, atom, portray_raw_string(s[m1.end():]))

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
