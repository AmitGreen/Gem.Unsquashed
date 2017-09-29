#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    postfix_cache = {}


    produce_conjure_dual = Shared.produce_conjure_dual      #   Due to privileged


    class PostfixExpression(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression+
            'b',                        #   Expression+
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            t.a.write(w)
            t.b.write(w)


    PostfixExpression.k1 = PostfixExpression.a
    #PostfixExpression.k2 = PostfixExpression.b


    produce_conjure_postfix_expression = produce_conjure_dual__21


    class CallExpression(PostfixExpression):
        __slots__    = (())
        display_name = 'call'


    class IndexExpression(PostfixExpression):
        __slots__    = (())
        display_name = 'index'


    class MethodCallExpression(PostfixExpression):
        __slots__    = (())
        display_name = 'method-call'


    produce_call_expression        = produce_conjure_postfix_expression('call',        CallExpression)
    produce_index_expression       = produce_conjure_postfix_expression('index',       IndexExpression)
    produce_method_call_expression = produce_conjure_postfix_expression('call-method', MethodCallExpression)


    append_cache('postfix', postfix_cache)


    share(
        'produce_call_expression',          produce_call_expression,
        'produce_index_expression',         produce_index_expression,
        'produce_method_call_expression',   produce_method_call_expression,
    )
