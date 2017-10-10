#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.QuadrupleStatement')
def gem():
    class QuadrupleStatement(QuadrupleTwig):
        __slots__                  = (())
        display_name               = 'quadruple-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
                t.a.dump_token(f)
                t.b.dump_token(f)
                t.c.dump_token(f)
                t.d.dump_token(f)


        def find_require_gem(t, e):
            t.a.find_require_gem(e)
            t.b.find_require_gem(e)
            t.c.find_require_gem(e)
            t.d.find_require_gem(e)


        indentation = indentation__a_indentation


    conjure_quadruple_statement = produce_conjure_quadruple_twig('quadruple-statement', QuadrupleStatement)


    share(
        'conjure_quadruple_statement',  conjure_quadruple_statement,
    )
