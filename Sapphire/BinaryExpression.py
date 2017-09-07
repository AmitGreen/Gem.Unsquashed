#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    class BinaryExpression(Object):
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


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)
            t.right   .write(w)


    @share
    class AddExpression(BinaryExpression):
        __slots__    = (())
        display_name = '+'


    @share
    class CompareEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '=='


    @share
    class CommaExpression(BinaryExpression):
        __slots__    = (())
        display_name = ','


    @share
    class LessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='


    @share
    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'


    @share
    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'


    @share
    class OrExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'or'


    OperatorCompareEqual   .compare_expression_meta = CompareEqualExpression
    OperatorLessThanOrEqual.compare_expression_meta = LessThanOrEqualExpression