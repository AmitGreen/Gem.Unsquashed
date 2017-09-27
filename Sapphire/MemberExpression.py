#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.PostfixExpression')


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


        def count_newlines(t):
            return t.left.count_newlines() + t.postfix.count_newlines()


        def display_token(t):
            return arrange('<member %s %s>', t.left.display_token(), t.postfix.display_token())


        def write(t, w):
            t.left.write(w)
            w(t.postfix.s)


    #MemberExpression.k1 = MemberExpression.left
    MemberExpression.k2 = MemberExpression.postfix


    static_produce_call_expression = static_method(produce_call_expression)


    MemberExpression.call_expression = static_method(produce_method_call_expression)
    SapphireToken   .call_expression = static_produce_call_expression
    SapphireTrunk   .call_expression = static_produce_call_expression


    member_expression_cache = {}


    conjure_member_expression = produce_dual_cache('member-expession', MemberExpression, member_expression_cache)


    @share
    def dump_member_expression_cache():
        dump_cache('member_expression_cache', member_expression_cache)


    share(
        'conjure_member_expression',    conjure_member_expression,
    )
