#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualStatement')
def gem():
    @share
    def dump_token__ab(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
            t.a.dump_token(f)
            t.b.dump_token(f)


    @property
    def indentation__a_indentation(t):
        return t.a.indentation


    class DualStatement(DualTwig):
        __slots__           = (())
        display_name        = 'dual-statement'
        is_any_else         = false
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class CommentedStatement(DualTwig):
        __slots__           = (())
        display_name        = '#statement'
        is_any_else         = false
        is_else_header      = false
        is_statement_header = false
        is_statement        = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<%s +%d', t.display_name, t.b.indentation.total), '>'):
                t.a.dump_token(f)
                t.b.dump_token(f)


        @property
        def indentation(t):
            return t.b.indentation


    conjure_commented_statement = produce_conjure_dual_twig('#statement',     CommentedStatement)
    conjure_dual_statement      = produce_conjure_dual_twig('dual-statement', DualStatement)


    share(
        'conjure_commented_statement',  conjure_commented_statement,
        'conjure_dual_statement',       conjure_dual_statement,
        'indentation__a_indentation',   indentation__a_indentation,
    )
