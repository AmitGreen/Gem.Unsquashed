#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.DualTwig')


    class CallExpression(DualTwig):
        __slots__    = (())
        display_name = 'call'


    class IndexExpression(DualTwig):
        __slots__    = (())
        display_name = 'index'


    class MethodCallExpression(DualTwig):
        __slots__    = (())
        display_name = 'method-call'


    produce_call_expression        = produce_conjure_dual_twig('call',        CallExpression)
    produce_index_expression       = produce_conjure_dual_twig('index',       IndexExpression)
    produce_method_call_expression = produce_conjure_dual_twig('call-method', MethodCallExpression)


    share(
        'produce_call_expression',          produce_call_expression,
        'produce_index_expression',         produce_index_expression,
        'produce_method_call_expression',   produce_method_call_expression,
    )
