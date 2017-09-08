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


    @share
    class TernaryExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'if_operator',              #   KeywordIf
            'middle',                   #   Expression
            'else_operator',            #   KeywordElse
            'right',                    #   Expression
        ))


        def __init__(t, left, if_operator, middle, else_operator, right):
            t.left          = left
            t.if_operator   = if_operator
            t.middle        = middle
            t.else_operator = else_operator
            t.right         = right


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left, t.if_operator, t.middle, t.else_operator, t.right)


        def display_token(t):
            return arrange('<?: %s %s %s %s %s>',
                           t.left         .display_token(),
                           t.if_operator  .display_token(),
                           t.middle       .display_token(),
                           t.else_operator.display_token(),
                           t.right        .display_token())


        def write(t, w):
            t.left         .write(w)
            t.if_operator  .write(w)
            t.middle       .write(w)
            t.else_operator.write(w)
            t.right        .write(w)


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
