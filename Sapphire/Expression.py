#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Elemental')


    @share
    class Arguments_0(Object):
        __slots__ = ((
            'left_parenthesis',         #   OperatorLeftParenthesis
            'right_parenthesis',        #   OperatorRightParenthesis
        ))


        is_arguments_0 = true


        def __init__(t, left_parenthesis, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<Arguments_0 %r %r>', t.left_parenthesis, t.right_parenthesis)


        def write(t, w):
            w(t.left_parenthesis.s + t.right_parenthesis.s)


    @share
    class Arguments_1(Object):
        __slots__ = ((
            'left_parenthesis',         #   OperatorLeftParenthesis
            'argument_0',               #   Expression*
            'right_parenthesis',        #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, argument_0, right_parenthesis):
            assert left_parenthesis .is_left_parenthesis
            assert right_parenthesis.is_right_parenthesis

            t.left_parenthesis  = left_parenthesis
            t.argument_0        = argument_0
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<Arguments_1 %r %r %r>', t.left_parenthesis, t.argument_0, t.right_parenthesis)


        def display_token(t):
            return arrange('<Arguments_1 %s %s %s>',
                           t.left_parenthesis .display_token(),
                           t.argument_0       .display_token(),
                           t.right_parenthesis.display_token())


        def write(t, w):
            t.left_parenthesis .write(w)
            t.argument_0       .write(w)
            t.right_parenthesis.write(w)


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
            return arrange('<Arguments_2 %s %s %s %s %s>',
                           t.left_parenthesis.display_token(),
                           t.argument_0.display_token(),
                           t.comma_0.display_token(),
                           t.argument_1.display_token(),
                           t.right_parenthesis.display_token)


        def write(t, w):
            t.left_parenthesis .write(w)
            t.argument_0       .write(w)
            t.comma_0          .write(w)
            t.argument_1       .write(w)
            t.right_parenthesis.write(w)


    @share
    class ExpressionBinaryBase(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        def __init__(t, left, operator, right):
            assert type(left)  is not String
            assert type(right) is not String

            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.operator, t.right)


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)
            t.right   .write(w)


    @share
    class ExpressionComma(ExpressionBinaryBase):
        __slots__ = (())


    @share
    class ExpressionCall(Object):
        __slot__ = ((
            'left',                         #   Expression
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, arguments):
            assert type(arguments) is not String

            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<f() %r %r>', t.left, t.arguments)


        def display_token(t):
            return arrange('<f() %s %s>', t.left.display_token(), t.arguments.display_token())


        def write(t, w):
            t.left     .write(w)
            t.arguments.write(w)


    @share
    class ExpressionDot(Object):
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
            return arrange('<. %r %r %r>', t.left, t.operator, t.right)


        def write(t, w):
            t.left.write(w)
            w(t.operator.s + t.right.s)


    @share
    class ExpressionIndex_1(Object):
        __slots__ = ((
            'array',                    #   Expression
            'left_square_bracket',      #   LeftSquareBracket
            'index',                    #   Expression
            'right_square_bracket',     #   RightSquareBracket
        ))


        def __init__(t, array, left_square_bracket, index, right_square_bracket):
            t.array                = array
            t.left_square_bracket  = left_square_bracket
            t.index                = index
            t.right_square_bracket = right_square_bracket


        def __repr__(t):
            return arrange('<[] %r %r %r %r>',
                           t.array, t.left_square_bracket, t.index, t.right_square_bracket)


        def display_token(t):
            return arrange('<[] %s %s %s %s>',
                           t.array               .display_token(),
                           t.left_square_bracket .display_token(),
                           t.index               .display_token(),
                           t.right_square_bracket.display_token())


        def write(t, w):
            t.array               .write(w)
            t.left_square_bracket .write(w)
            t.index               .write(w)
            t.right_square_bracket.write(w)


    @share
    class ExpressionMethodCall(Object):
        __slot__ = ((
            'left',                         #   Expression
            'dot',                          #   OperatorDot
            'right',                        #   Identifier
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, dot, right, arguments):
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments


        def __repr__(t):
            return arrange('<ExpressionCall %r %r %r %r>', t.left, t.dot, t.right, t.arguments)
