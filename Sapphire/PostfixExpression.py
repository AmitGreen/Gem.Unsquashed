#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.PostfixExpression')
def gem():
    require_gem('Sapphire.DualTwig')


    class CallExpression(DualTwig):
        __slots__          = (())
        display_name       = 'call'
        is_call_expression = true

        remove_comments = remove_comments__ab


    class IndexExpression(DualTwig):
        __slots__    = (())
        display_name = 'index'

        remove_comments = remove_comments__ab


    class MethodCallExpression(DualTwig):
        __slots__    = (())
        display_name = 'method-call'


    conjure_call_expression        = produce_conjure_dual_twig('call',        CallExpression)
    conjure_index_expression       = produce_conjure_dual_twig('index',       IndexExpression)
    conjure_method_call_expression = produce_conjure_dual_twig('call-method', MethodCallExpression)


    CallExpression.conjure = static_method(conjure_call_expression)


    share(
        'conjure_call_expression',          conjure_call_expression,
        'conjure_index_expression',         conjure_index_expression,
        'conjure_method_call_expression',   conjure_method_call_expression,
    )
