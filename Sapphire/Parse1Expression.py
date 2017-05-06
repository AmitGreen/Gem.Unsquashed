#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    require_gem('Sapphire.Tokenizer')


    @share
    def parse1_statement_expression__symbol(m1, symbol):
        indented = m1.group('indented')
        index    = m1.end()
        s        = qs()

        #
        #<postfix1-operator>
        #
        m2 = postfix_operator1_match(s, index)

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

        return create_UnknownLine(parse1_statement_expression__symbol, 3)

        #left_parenthesis = m2.group()
        #line('indented: %r, symbol: %r; s: %r; left_parenthesis: %r', indented, symbol, s[index:], left_parenthesis)
