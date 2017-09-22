#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    class PostfixExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   Operator*
        ))


        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false
        is_statement                          = false


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.left.display_token(), t.postfix.display_token())


        display_full_token = display_token


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
    class SimpleMemberExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   DotName
        ))


        is_statement = false


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.left.display_token(), t.postfix.display_token())


        display_full_token = display_token


        def write(t, w):
            t.left.write(w)
            w(t.postfix.s)


    simple_member_expression_cache   = {}
    lookup_simple_member_expression  = simple_member_expression_cache.get
    provide_simple_member_expression = simple_member_expression_cache.setdefault
    store_simple_member_expression   = simple_member_expression_cache.__setitem__


    @share
    def conjure_simple_member_expression(left, postfix):
        first = lookup_simple_member_expression(postfix)

        if first is none:
            return provide_simple_member_expression(postfix, SimpleMemberExpression(left, postfix))

        if first.__class__ is Map:
            return (first.get(left)) or (first.setdefault(left, SimpleMemberExpression(left, postfix)))

        if first.left is left:
            return first

        r = SimpleMemberExpression(left, postfix)

        store_simple_member_expression(postfix, { first.left : first, left : r })

        return r


    @share
    def dump_simple_member_expression_cache():
        line('===  simple_member_expression_cache  ===')

        for [k, v] in iterate_items_sorted_by_key(simple_member_expression_cache):
            if v.__class__ is Map:
                line('%s:', k)

                for [k2, w2] in view_items(v):
                    line('  %s: %s', k2, w2)

                continue

            line('%s: %s', k, v)
