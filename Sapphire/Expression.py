#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Token')


    @share
    class Arguments_0(Object):
        __slots__ = ((
            'left_parenthesis',         #   OperatorLeftParenthesis
            'right_parenthesis',        #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<Arguments_0 %r %r>', t.left_parenthesis, t.right_parenthesis)


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


    @share
    class ExpressionBinaryBase(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        def __init__(t, left, operator, right):
            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.operator, t.right)


    @share
    class ExpressionCall(Object):
        __slot__ = ((
            'left',                         #   Expression
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, arguments):
            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<ExpressionCall %r %r>', t.left, t.arguments)


    @share
    class ExpressionComma(ExpressionBinaryBase):
        __slots__ = (())


    @share
    class ExpressionDot(ExpressionBinaryBase):
        __slots__ = (())


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
            return arrange('<%s %r %r %r %r>',
                           t.__class__.__name__, t.array, t.left_square_bracket, t.index, t.right_square_bracket)


    @share
    class ExpressionMethodCall(Object):
        __slot__ = ((
            'left',                         #   Expression
            'dot',                          #   OperatorDot
            'right',                        #   Symbol
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, dot, right, arguments):
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments


        def __repr__(t):
            return arrange('<ExpressionCall %r %r %r %r>', t.left, t.dot, t.right, t.arguments)


    @share
    class Number(Token):
        __slots__ = (())


        def __repr__(t):
            return t.s


    @share
    class SingleQuote(Token):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s>', t.s)
