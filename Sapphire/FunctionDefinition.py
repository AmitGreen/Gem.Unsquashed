#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.FunctionDefinition')
def gem():
    class FunctionDefinition(DualTwig):
        __slots__                  = (())
        display_name               = 'function-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_function_definition     = true
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#function-definition'


        if 0:
            def adorn(t, art, decorated = false):
                if art.phase_function:
                    art.add_function_definition(t)
                    return t

                a = t.a
                b = t.b

                child_art = create_function_symbol_table(art)

                a__2 = a.adorn(child_art)
                b__2 = b#.adorn(child_art)

                if (a is a__2) and (b is b__2):
                    return t

                prefix = t.prefix

                if prefix is 0:
                    return conjure_function_definition(a__2, b__2)

                return conjure_prefixed_function_definition(prefix, a__2, b__2)


        def scan_variables(t, art):
            t.a.scan_variables(art)


        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    [
            conjure_function_definition, conjure_prefixed_function_definition,
    ] = produce_conjure_dual_twig_functions('function-definition', FunctionDefinition)


    FunctionDefinition.conjure               = static_method(conjure_function_definition)
    FunctionDefinition.conjure_prefixed_dual = static_method(conjure_prefixed_function_definition)

    FunctionDefinition.transform = produce_transform__a__b_with_indentation(
                                       'function_Definition',
                                       conjure_function_definition,
                                   )

    share(
        'conjure_function_definition',              conjure_function_definition,
        'conjure_prefixed_function_definition',     conjure_prefixed_function_definition,
    )
