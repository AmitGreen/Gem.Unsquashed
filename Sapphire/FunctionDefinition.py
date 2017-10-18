#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.FunctionDefinition')
def gem():
    require_gem('Sapphire.PrefixedDualStatement')


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

        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    [
            conjure_function_definition, conjure_prefixed_function_definition,
    ] = produce_conjure_dual_twig_functions('function-definition', FunctionDefinition)


    FunctionDefinition.conjure               = static_method(conjure_function_definition)
    FunctionDefinition.conjure_prefixed_dual = static_method(conjure_prefixed_function_definition)
    FunctionDefinition.adorn                 = produce_adorn__ab('function_Definition', conjure_function_definition)

    FunctionDefinition.transform = produce_transform__a__b_with_indentation(
                                       'function_Definition',
                                       conjure_function_definition,
                                   )

    share(
        'conjure_function_definition',              conjure_function_definition,
        'conjure_prefixed_function_definition',     conjure_prefixed_function_definition,
    )
