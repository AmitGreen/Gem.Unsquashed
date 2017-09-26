#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    postfix_cache = {}


    produce_dual_cache = Shared.produce_dual_cache              #   Due to privileged


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


    PostfixExpression.kd1 = PostfixExpression.b         #   Reverse order on purpose
    PostfixExpression.kd2 = PostfixExpression.a         #   Reverse order on purpose


    @privileged
    def produce_conjure_postfix_expression(name, Meta):
        def create_postfix_expression(b, a):            #   Reverse order on purpose
            return Meta(a, b)


        conjure_dual = produce_dual_cache(name + '__X2', create_postfix_expression, postfix_cache)


        def conjure_postfix_expression(a, b):
            return conjure_dual(b, a)                   #   Reverse order on purpose


        if __debug__:
            create_postfix_expression .__name__ = arrange('create_%s', name)
            conjure_postfix_expression.__name__ = arrange('conjure_%s', name)


        return conjure_postfix_expression


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


    if __debug__:
        @share
        def dump_postfix_expression_cache():
            dump_cache('postfix-cache', postfix_cache)


    share(
        'produce_call_expression',          produce_call_expression,
        'produce_index_expression',         produce_index_expression,
        'produce_method_call_expression',   produce_method_call_expression,
    )
