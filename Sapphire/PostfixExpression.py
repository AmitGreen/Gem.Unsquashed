#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    class PostfixExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   Operator*
        ))


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.left.display_token(), t.postfix.display_token())


        def write(t, w):
            t.left   .write(w)
            t.postfix.write(w)


    @share
    class CallExpression(PostfixExpression):
        __slot__     = (())
        display_name = 'call'


    @share
    class IndexExpression(PostfixExpression):
        __slots__    = (())
        display_name = '[]'


    @share
    class MethodCallExpression(PostfixExpression):
        __slot__     = (())
        display_name = 'method-call'


    @share
    class MemberExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   DotName
        ))


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def display_token(t):
            return arrange('<member %s %s>', t.left.display_token(), t.postfix.display_token())


        def write(t, w):
            t.left.write(w)
            w(t.postfix.s)


    SapphireTrunk   .call_expression = CallExpression
    MemberExpression.call_expression = MethodCallExpression
    Token           .call_expression = CallExpression


    member_expression_cache   = {}
    lookup_member_expression  = member_expression_cache.get
    provide_member_expression = member_expression_cache.setdefault
    store_member_expression   = member_expression_cache.__setitem__


    @share
    def conjure_member_expression(left, postfix):
        first = lookup_member_expression(postfix, absent)

        if first.__class__ is Map:
            return (first.get(left)) or (first.setdefault(left, MemberExpression(left, postfix)))

        if first.left is left:
            return first

        r = MemberExpression(left, postfix)

        store_member_expression(postfix, (r   if first is absent else   { first.left : first, left : r }))

        return r


    @share
    def dump_member_expression_cache():
        dump_cache('member_expression_cache', member_expression_cache)
