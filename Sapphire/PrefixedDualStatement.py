#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.PrefixedDualStatement')
def gem():
    require_gem('Sapphire.DualStatement')


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
    conjure_else_fragment        = produce_conjure_dual_twig('else-fragment',        ElseFragment)
    conjure_else_if_statement    = produce_conjure_dual_twig('else-if-statement',    ElseIfStatement)
    conjure_function_definition  = produce_conjure_dual_twig('function-definition',  FunctionDefinition)
    conjure_if_statement         = produce_conjure_dual_twig('if-statement',         IfStatement)
    conjure_while_statement      = produce_conjure_dual_twig('while-statement',      WhileStatement)


    share(
        'conjure_class_definition',         conjure_class_definition,
        'conjure_decorated_definition',     conjure_decorated_definition,
        'conjure_else_fragment',            conjure_else_fragment,
        'conjure_else_if_statement',        conjure_else_if_statement,
        'conjure_function_definition',      conjure_function_definition,
        'conjure_if_statement',             conjure_if_statement,
        'conjure_while_statement',          conjure_while_statement,
    )
