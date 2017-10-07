#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualStatement')
def gem():
    require_gem('Sapphire.HeaderBodyStatement')


    class DualStatement(DualTwig):
        __slots__           = (())
        display_name        = 'dual-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    class ElseFragment(DualTwig):
        __slots__           = (())
        display_name        = 'else-fragment'
        is_else_header      = false
        is_statement_header = false
        is_statement        = false

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    conjure_dual_statement = produce_conjure_dual_twig('dual-statement', DualStatement)
    conjure_else_fragment  = produce_conjure_dual_twig('else-fragment',  ElseFragment)


    share(
        'conjure_dual_statement',   conjure_dual_statement,
        'conjure_else_fragment',    conjure_else_fragment,
    )
