#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.OtherExpression')
def gem():
    @share
    class MethodCall_1(Object):
        __slot__ = ((
            'left',                     #   Expression
            'dot',                      #   OperatorDot
            'right',                    #   Identifier
            'arguments',                #   Arguments*
        ))


        is_statement = false


        def __init__(t, left, dot, right, arguments):
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments


        def __repr__(t):
            return arrange('<MethodCall_1 %r %r %r %r>', t.left, t.dot, t.right, t.arguments)


        def display_token(t):
            return arrange('<method-call-1 %s %s %s %s>',
                           t.left     .display_token(),
                           t.dot      .display_token(),
                           t.right    .display_token(),
                           t.arguments.display_token())


        def write(t, w):
            t.left     .write(w)
            t.dot      .write(w)
            t.right    .write(w)
            t.arguments.write(w)


    @export
    class MethodCall_2(Object):
        __slots__ = ((
            'left',                     #   Expression*
            'left_operator',            #   Operator*
            'middle',                   #   Expression*
            'right_operator',           #   Operator*
            'right',                    #   Expression*
            'arguments',                #   Expression*
        ))


        is_statement = false


        def __init__(t, left, left_operator, middle, right_operator, right, arguments):
            t.left           = left
            t.left_operator  = left_operator
            t.middle         = middle
            t.right_operator = right_operator
            t.right          = right
            t.arguments      = arguments


        def __repr__(t):
            return arrange('<MethodCall_2 %r %r %r %r %r %r>',
                           t.left,
                           t.left_operator,
                           t.middle,
                           t.right_operator,
                           t.right,
                           t.arguments)


        def display_token(t):
            return arrange('<method-call-2 %s %s %s %s %s %s>',
                           t.left          .display_token(),
                           t.left_operator .display_token(),
                           t.middle        .display_token(),
                           t.right_operator.display_token(),
                           t.right         .display_token(),
                           t.arguments     .display_token())


        def write(t, w):
            t.left          .write(w)
            t.left_operator .write(w)
            t.middle        .write(w)
            t.right_operator.write(w)
            t.right         .write(w)
            t.arguments     .write(w)


    @export
    class MethodCall_3(Object):
        __slots__ = ((
            'first',                    #   Expression*
            'first_operator',           #   Operator*
            'second',                   #   Expression*
            'second_operator',          #   Operator*
            'third',                    #   Expression*
            'third_operator',           #   Operator*
            'fourth',                   #   Expression*
            'arguments',                #   Expression*
        ))


        is_statement = false


        def __init__(t, first, first_operator, second, second_operator, third, third_operator, fourth, arguments):
            t.first           = first
            t.first_operator  = first_operator
            t.second          = second
            t.second_operator = second_operator
            t.third           = third
            t.third_operator  = third_operator
            t.fourth          = fourth
            t.arguments       = arguments


        def __repr__(t):
            return arrange('<MethodCall_3 %r %r %r %r %r %r %r %r>',
                           t.first,  t.first_operator,
                           t.second, t.second_operator,
                           t.third,  t.third_operator,
                           t.fourth,
                           t.arguments)


        def display_token(t):
            return arrange('<method-call-3 %s %s %s %s %s %s %s %s>',
                           t.first          .display_token(),
                           t.first_operator .display_token(),
                           t.second         .display_token(),
                           t.second_operator.display_token(),
                           t.third          .display_token(),
                           t.third_operator .display_token(),
                           t.fourth         .display_token(),
                           t.arguments)


        def write(t, w):
            t.first          .write(w)
            t.first_operator .write(w)
            t.second         .write(w)
            t.second_operator.write(w)
            t.third          .write(w)
            t.third_operator .write(w)
            t.fourth         .write(w)
            t.arguments      .write(w)


    class TripleExpression(Object):
        __slots__ = ((
            'left',                     #   Expression*
            'left_operator',            #   Operator*
            'middle',                   #   Expression*
            'right_operator',           #   Operator*
            'right',                    #   Expression*
        ))


        def __init__(t, left, left_operator, middle, right_operator, right):
            t.left           = left
            t.left_operator  = left_operator
            t.middle         = middle
            t.right_operator = right_operator
            t.right          = right


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left, t.left_operator, t.middle, t.right_operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.left          .display_token(),
                           t.left_operator .display_token(),
                           t.middle        .display_token(),
                           t.right_operator.display_token(),
                           t.right         .display_token())


        display_full_token = display_token


        def write(t, w):
            t.left          .write(w)
            t.left_operator .write(w)
            t.middle        .write(w)
            t.right_operator.write(w)
            t.right         .write(w)


    @share
    class ComprehensionForExpression(TripleExpression):
        __slots__    = (())
        display_name = 'comprehension-for'


    @share
    class TernaryExpression(TripleExpression):
        __slots__    = (())
        display_name = '?:'
