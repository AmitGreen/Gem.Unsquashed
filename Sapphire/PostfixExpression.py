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


        def remove_comments(t):
            a = t.a
            b = t.b

            a__2 = a.remove_comments()
            b__2 = b.remove_comments()

            if (a is a__2) and (b is b__2):
                return t

            return t.conjure(a__2, b__2)


    class IndexExpression(DualTwig):
        __slots__    = (())
        display_name = 'index'


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
