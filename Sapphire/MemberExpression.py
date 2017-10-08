#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.PostfixExpression')


    member_expression_cache = {}


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


        def dump_token(t, f, newline = true):
            f.partial('<member ')

            t    .left   .dump_token(f)
            r = t.postfix.dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            t.left.write(w)
            w(t.postfix.s)


    #MemberExpression.k1 = MemberExpression.left
    MemberExpression.k2 = MemberExpression.postfix


    static_produce_call_expression = static_method(produce_call_expression)


    MemberExpression.call_expression = static_method(produce_method_call_expression)
    SapphireToken   .call_expression = static_produce_call_expression
    SapphireTrunk   .call_expression = static_produce_call_expression


    conjure_member_expression = produce_conjure_dual('member-expession', MemberExpression, member_expression_cache)


    append_cache('member-expression', member_expression_cache)


    share(
        'conjure_member_expression',    conjure_member_expression,
    )
