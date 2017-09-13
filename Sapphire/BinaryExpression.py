#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.DualToken')
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
    class CommaExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = ','


    @share
    class ComprehensionIfExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'comprehension-if'


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
    class CompareGreaterThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>'


    @share
    class CompareGreaterThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>='


    @share
    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'


    @share
    class CompareNotEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '!='


    @share
    class DivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '/'


    @share
    class IntegerDivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '//'


    @share
    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'


    @share
    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'


    @share
    class LessThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<'


    @share
    class LessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='


    @share
    class LogicalAndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '&'


    @share
    class LogicalOrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '|'


    @share
    class MapElement(BinaryExpression):
        __slots__      = (())
        display_name   = ':'
        is_right_brace = false


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
    class MultiplyExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '*'


    @share
    class OrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'or'


    @share
    class PowerExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'power'


    @share
    class SubtractExpression(BinaryExpression):
        __slots__    = (())
        display_name = '-'


    IsNot                     .expression_meta = CompareDifferentExpression
    KeywordIn                 .expression_meta = CompareContainsExpression
    KeywordIs                 .expression_meta = CompareIdentityExpression
    NotIn                     .expression_meta = CompareExcludeExpression
    OperatorCompareEqual      .expression_meta = CompareEqualExpression
    OperatorCompareNotEqual   .expression_meta = CompareNotEqualExpression
    OperatorDivide            .expression_meta = DivideExpression
    OperatorGreaterThan       .expression_meta = CompareGreaterThanExpression
    OperatorGreaterThanOrEqual.expression_meta = CompareGreaterThanOrEqualExpression
    OperatorIntegerDivide     .expression_meta = IntegerDivideExpression
    OperatorLessThan          .expression_meta = LessThanExpression
    OperatorLessThanOrEqual   .expression_meta = LessThanOrEqualExpression
    OperatorMinusSign         .expression_meta = SubtractExpression
    OperatorPercentSign       .expression_meta = ModulusExpression
    OperatorPlusSign          .expression_meta = AddExpression
    OperatorStarSign          .expression_meta = MultiplyExpression_1
