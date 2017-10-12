#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.PostfixExpression')
def gem():
    require_gem('Sapphire.DualTwig')


    mutate__postfix_expression = produce__mutate__ab__priority('postfix_expression', PRIORITY_ATOM, PRIORITY_COMPREHENSION)


    class CallExpression(DualTwig):
        __slots__          = (())
        display_name       = 'call'
        is_call_expression = true


        mutate = mutate__postfix_expression


    class IndexExpression(DualTwig):
        __slots__    = (())
        display_name = 'index'

        mutate = mutate__postfix_expression


    class MethodCallExpression(DualTwig):
        __slots__    = (())
        display_name = 'method-call'

        mutate = mutate__postfix_expression


    conjure_call_expression        = produce_conjure_dual_twig('call',        CallExpression)
    conjure_index_expression       = produce_conjure_dual_twig('index',       IndexExpression)
    conjure_method_call_expression = produce_conjure_dual_twig('call-method', MethodCallExpression)


    CallExpression.conjure = static_method(conjure_call_expression)


    share(
        'conjure_call_expression',          conjure_call_expression,
        'conjure_index_expression',         conjure_index_expression,
        'conjure_method_call_expression',   conjure_method_call_expression,
    )
