#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualStatement')
def gem():
    def dump_token__ab(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
            t.a.dump_token(f)
            t.b.dump_token(f)

        return false


    @property
    def indentation__a_indentation(t):
        return t.a.indentation


    class ClassDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'class-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class DecoratedDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'decorated-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class DualStatement(DualTwig):
        __slots__           = (())
        display_name        = 'dual-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class ElseFragment(DualTwig):
        __slots__           = (())
        display_name        = 'else-fragment'
        is_else_header      = false
        is_statement_header = false
        is_statement        = false

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class ElseIfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'else-if-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class FunctionDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'function-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class IfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'if-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class WhileStatement(DualTwig):
        __slots__           = (())
        display_name        = 'while-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    conjure_class_definition     = produce_conjure_dual_twig('class-definition',     ClassDefinition)
    conjure_decorated_definition = produce_conjure_dual_twig('decorated-definition', DecoratedDefinition)
    conjure_dual_statement       = produce_conjure_dual_twig('dual-statement',       DualStatement)
    conjure_else_fragment        = produce_conjure_dual_twig('else-fragment',        ElseFragment)
    conjure_else_if_statement    = produce_conjure_dual_twig('else-if-statement',    ElseIfStatement)
    conjure_function_definition  = produce_conjure_dual_twig('function-definition',  FunctionDefinition)
    conjure_if_statement         = produce_conjure_dual_twig('if-statement',         IfStatement)
    conjure_while_statement      = produce_conjure_dual_twig('while-statement',      WhileStatement)


    share(
        'conjure_class_definition',         conjure_class_definition,
        'conjure_decorated_definition',     conjure_decorated_definition,
        'conjure_dual_statement',           conjure_dual_statement,
        'conjure_else_fragment',            conjure_else_fragment,
        'conjure_else_if_statement',        conjure_else_if_statement,
        'conjure_function_definition',      conjure_function_definition,
        'conjure_if_statement',             conjure_if_statement,
        'conjure_while_statement',          conjure_while_statement,
    )
