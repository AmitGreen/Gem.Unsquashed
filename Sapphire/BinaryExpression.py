#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.JoinedToken')


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


        display_full_token = display_token


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)
            t.right   .write(w)


    @share
    class AddExpression(BinaryExpression):
        __slots__    = (())
        display_name = '+'


    @share
    class AndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'and'


    @share
    class CompareContainsExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'in'


    @share
    class CompareEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '=='


    @share
    class CompareDifferentExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is-not'


    @share
    class CompareExcludeExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'not-in'


    @share
    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'


    @share
    class CommaExpression(BinaryExpression):
        __slots__    = (())
        display_name = ','


    @share
    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'


    @share
    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'


    @share
    class LessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='


    @share
    class MemberExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '.'
        is_statement = false


    @share
    class ModulusExpression(BinaryExpression):
        __slots__    = (())
        display_name = '%'


    @share
    class OrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'or'


    IsNot                  .expression_meta = CompareDifferentExpression
    NotIn                  .expression_meta = CompareExcludeExpression
    KeywordIn              .expression_meta = CompareContainsExpression
    KeywordIs              .expression_meta = CompareIdentityExpression
    OperatorCompareEqual   .expression_meta = CompareEqualExpression
    OperatorLessThanOrEqual.expression_meta = LessThanOrEqualExpression
    OperatorPercentSign    .expression_meta = ModulusExpression
    OperatorPlusSign       .expression_meta = AddExpression
