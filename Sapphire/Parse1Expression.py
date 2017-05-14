#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    require_gem('Sapphire.Core')


    show = 7


    @share
    def parse1_statement_expression__symbol(indented, symbol, index):
        s = qs()

        if show:
            line('indented: %r, symbol: %r; s: %r', indented, symbol, s[index:])

        #
        #<postfix1-operator>
        #
        m2 = statement1_expression_operator(s, index)

        if m2 is none:
            return create_UnknownLine(parse1_statement_expression__symbol, 1)

        right_parenthesis__start = m2.start('right_parenthesis')
        #</postfix1-operator>

        if right_parenthesis__start is not -1:
            if m2.start('comment_newline') is not -1:
                return StatementCall(
                           indented,
                           symbol,
                           Arguments_0(
                               OperatorLeftParenthesis(s[index:right_parenthesis__start]),
                               OperatorRightParenthesis(m2.group('right_parenthesis')),
                           ),
                           TokenNewline(s[m2.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(parse1_statement_expression__symbol, 2)

        if m2.start('equal_sign') is not -1:
            operator_equal_sign = OperatorEqualSign(m2.group())

            #
            #<atom1>
            #
            m3 = atom1_match(s, m2.end())

            if m3 is none:
                return create_UnknownLine(parse1_statement_expression__symbol, 1)

            s3     = m3.group()
            atom   = find_atom_type(s3[0])(s3)
            m3_end = m3.end()
            #</atom1>

            line('indented: %r; symbol: %r; operator_equal_sign: %r; atom: %r', indented, symbol, operator_equal_sign, atom)

            return create_UnknownLine(parse1_statement_expression__symbol, 3)

        return create_UnknownLine(parse1_statement_expression__symbol, 4)

        #left_parenthesis = m2.group()
        line('indented: %r, symbol: %r; s: %r; left_parenthesis: %r', indented, symbol, s[index:], left_parenthesis)
