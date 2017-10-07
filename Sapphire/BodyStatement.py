#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BodyStatement')
def gem():
    require_gem('Sapphire.DualTwig')


    def dump_token__body_statement(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
            t.a.dump_token(f)
            t.b.dump_token(f)

        return false


    @property
    def indentation__body_statement(t):
        return t.a.indentation


    class ClassDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'class-definition'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    class DecoratedDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'decorated-definition'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    class ElseIfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'else-if-statement'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement




    class FunctionDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'function-definition'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    class IfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'if-statement'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    class WhileStatement(DualTwig):
        __slots__           = (())
        display_name        = 'while-statement'
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__body_statement
        indentation = indentation__body_statement


    conjure_class_definition     = produce_conjure_dual_twig('class-definition',     ClassDefinition)
    conjure_decorated_definition = produce_conjure_dual_twig('decorated-definition', DecoratedDefinition)
    conjure_else_if_statement    = produce_conjure_dual_twig('else-if-statement',    ElseIfStatement)
    conjure_function_definition  = produce_conjure_dual_twig('function-definition',  FunctionDefinition)
    conjure_if_statement         = produce_conjure_dual_twig('if-statement',         IfStatement)
    conjure_while_statement      = produce_conjure_dual_twig('while-statement',      WhileStatement)


    share(
        'conjure_class_definition',         conjure_class_definition,
        'conjure_decorated_definition',     conjure_decorated_definition,
        'conjure_else_if_statement',        conjure_else_if_statement,
        'conjure_function_definition',      conjure_function_definition,
        'conjure_if_statement',             conjure_if_statement,
        'conjure_while_statement',          conjure_while_statement,
    )
