#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    postfix_cache  = {}
    lookup_postfix = postfix_cache.get
    store_postfix  = postfix_cache.__setitem__


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


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            t.a.write(w)
            t.b.write(w)


    @privileged
    def produce_conjure_postfix_expression(name, Meta):
        #
        #   NOTE:
        #       Reversed from normal: uses 'b' as the first map index & 'a' as the second map index.
        #
        def conjure_postfix_expression(a, b):
            first = lookup_postfix(b, absent)

            if first.__class__ is Map:
                return (first.get(a)) or (first.setdefault(a, Meta(a, b)))

            if first.a is a:
                return first

            r = Meta(a, b)

            store_postfix(b, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_postfix_expression.__name__ = intern_arrange('conjure_%s', name)

        return conjure_postfix_expression


    class CallExpression(PostfixExpression):
        __slot__     = (())
        display_name = 'call'


    class IndexExpression(PostfixExpression):
        __slots__    = (())
        display_name = 'index'


    class MethodCallExpression(PostfixExpression):
        __slot__     = (())
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
