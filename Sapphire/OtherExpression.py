#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.OtherExpression')
def gem():
    @share
    class Arguments_2(Object):
        __slots__ = ((
            'left_parenthesis',         #   OperatorLeftParenthesis
            'argument_0',               #   Expression*
            'comma_0',                  #   OperatorComma
            'argument_1',               #   Expression*
            'right_parenthesis',        #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, argument_0, comma_0, argument_1, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.argument_0        = argument_0
            t.comma_0           = comma_0
            t.argument_1        = argument_1
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<Arguments_2 %r %r %r %r %r>',
                           t.left_parenthesis,
                           t.argument_0,
                           t.comma_0,
                           t.argument_1,
                           t.right_parenthesis)


        def display_token(t):
            return arrange('<(2) %s %s %s %s %s>',
                           t.left_parenthesis .display_token(),
                           t.argument_0       .display_token(),
                           t.comma_0          .display_token(),
                           t.argument_1       .display_token(),
                           t.right_parenthesis.display_token())


        def write(t, w):
            t.left_parenthesis .write(w)
            t.argument_0       .write(w)
            t.comma_0          .write(w)
            t.argument_1       .write(w)
            t.right_parenthesis.write(w)


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


    @share
    class TupleExpression_2(Object):
        __slots__ = ((
            'left',                     #   OperatorLeftParenthesis
            'middle_1',                 #   Expression+
            'comma_1',                  #   OperatorComma
            'middle_2',                 #   Expression+
            'right',                    #   OperatorRightParenthesis | Comma_RightParenthesis
        ))


        is__atom__or__right_close_operator = true
        is_atom                            = true
        is_right_parenthesis               = false


        def __init__(t, left, middle_1, comma_1, middle_2, right):
            t.left     = left
            t.middle_1 = middle_1
            t.comma_1  = comma_1
            t.middle_2 = middle_2
            t.right    = right


        def __repr__(t):
            return arrange('<TupleExpression_2 %r %r %r %r %r>', t.left, t.middle_1, t.comma_1, t.middle_2, t.right)


        def display_token(t):
            if t.left.s == '(' and t.right.s == ')':
                return arrange('({,2} %s %s %s)',
                               t.middle_1.display_token(),
                               t.comma_1 .display_token(),
                               t.middle_2.display_token())

            return arrange('({,2} %s %s %s %s %s)',
                           t.left    .display_full_token(),
                           t.middle_1.display_token(),
                           t.comma_1 .display_token(),
                           t.middle_2.display_token(),
                           t.right   .display_full_token())


        def write(t, w):
            w(t.left.s)
            t.middle_1.write(w)
            t.comma_1 .write(w)
            t.middle_2.write(w)
            t.right   .write(w)
