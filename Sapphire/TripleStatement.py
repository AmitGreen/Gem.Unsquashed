#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleStatement')
def gem():
    class TripleStatement(TripleTwig):
        __slots__           = (())
        display_name        = 'triple-statement'
        is_any_else         = false
        is_else_header      = false
        is_statement_header = false
        is_statement        = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
                t.a.dump_token(f)
                t.b.dump_token(f)
                t.c.dump_token(f)


        indentation = indentation__a_indentation


    conjure_triple_statement = produce_conjure_triple_twig('triple-statement', TripleStatement)


    share(
        'conjure_triple_statement',     conjure_triple_statement,
    )