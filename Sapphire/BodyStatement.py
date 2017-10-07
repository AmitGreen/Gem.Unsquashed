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


    class DecoratedDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'decorated-definition'
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


    conjure_decorated_definition = produce_conjure_dual_twig('decorated-definition', DecoratedDefinition)
    conjure_function_definition  = produce_conjure_dual_twig('function-definition',  FunctionDefinition)


    share(
        'conjure_decorated_definition',     conjure_decorated_definition,
        'conjure_function_definition',      conjure_function_definition,
    )
