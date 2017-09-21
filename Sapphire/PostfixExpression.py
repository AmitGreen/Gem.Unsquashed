#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    class PostfixExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
        ))


        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false
        is_statement                          = false


        def __init__(t, left, operator):
            t.left     = left
            t.operator = operator


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.operator)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.left    .display_token(),
                           t.operator.display_token())


        display_full_token = display_token


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)


    @share
    class IndexExpression(PostfixExpression):
        __slots__    = (())
        display_name = '[]'
