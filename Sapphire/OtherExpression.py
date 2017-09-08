#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.OtherExpression')
def gem():
    @share
    class CallExpression(Object):
        __slot__ = ((
            'left',                         #   Expression
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, arguments):
            assert type(arguments) is not String

            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<CallExpression %r %r>', t.left, t.arguments)


        def display_token(t):
            return arrange('<call %s %s>', t.left.display_token(), t.arguments.display_token())


        def write(t, w):
            t.left     .write(w)
            t.arguments.write(w)


    @share
    class MemberExpression_1(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   OperatorDot
            'right',                    #   Identifier
        ))


        def __init__(t, left, operator, right):
            assert (type(left) is not String) and (operator.is_dot) and (right.is_identifier)

            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<MemberExpression_1 %r %r %r>', t.left, t.operator, t.right)


        def display_token(t):
            return arrange('<. %s %s %s>',
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.left.write(w)
            w(t.operator.s + t.right.s)


    @share
    class MethodCall_1(Object):
        __slot__ = ((
            'left',                     #   Expression
            'dot',                      #   OperatorDot
            'right',                    #   Identifier
            'arguments',                #   Arguments*
        ))


        def __init__(t, left, dot, right, arguments):
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments


        def __repr__(t):
            return arrange('<MethodCall_1 %r %r %r %r>', t.left, t.dot, t.right, t.arguments)
