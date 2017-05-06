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

        line('indented: %r, symbol: %r; s: %r', indented, symbol, s[index:])

        return create_UnknownLine(parse1_statement_expression__symbol, 1)
