#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    class BookcaseExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Operator+
            'middle',                   #   Expression+
            'right',                    #   Operator+
        ))


        def __init__(t, left, middle, right):
            t.left   = left
            t.middle = middle
            t.right  = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.middle, t.right)


        def display_token(t):
            if (t.left.s == t.a_name) and (t.right.s == t.b_name):
                return arrange('<%s %s %s %s>', t.display_name, t.a_name, t.middle.display_token(), t.b_name)

            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


        def write(t, w):
            w(t.left.s)
            t.middle.write(w)
            t.right .write(w)


    @share
    class Arguments_1(BookcaseExpression):
        __slots__    = (())
        a_name       = '('
        b_name       = ')'
        display_name = '(1)'


    @share
    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ':]'
        display_name = 'head-index'


    @share
    class ListExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '['
        b_name                         = ']'
        display_name                   = '[1]'
        is__atom__or__special_operator = true
        is_atom                        = true



    @share
    class MapExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '{'
        b_name                         = '}'
        display_name                   = '{1}'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ']'
        display_name = 'index'


    @share
    class ParenthesizedExpression(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ')'
        display_name                   = '()'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class TailIndex(BookcaseExpression):
        __slots__    = (())
        a_name       = '[:'
        b_name       = ']'
        display_name = 'tail-index'


    @share
    class TupleExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ')'
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class BookcasedDualExpression(Object):
        __slots__ = ((
            'left_operator',            #   Operator*
            'left',                     #   Expression*
            'middle_operator',          #   Operator*
            'right',                    #   Expression*
            'right_operator',           #   Operator*
        ))


        is_right_parenthesis    = false
        is_right_square_bracket = false


        def __init__(t, left_operator, left, middle_operator, right, right_operator):
            t.left_operator   = left_operator
            t.left            = left
            t.middle_operator = middle_operator
            t.right           = right
            t.right_operator  = right_operator


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left_operator, t.left, t.middle_operator, t.right, t.right_operator)


        def display_token(t):
            if (
                    t.left_operator  .s == t.a_name
                and t.middle_operator.s == t.b_name
                and t.right_operator .s == t.c_name
            ):
                b_name = t.b_name

                if ' ' in b_name:
                    b_name = '<' + b_name + '>',

                return arrange('<%s %s %s %s %s %s>',
                               t.display_name,
                               t.a_name,
                               t.left .display_token(),
                               b_name,
                               t.right.display_token(),
                               t.c_name)

            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.left_operator  .display_token(),
                           t.left           .display_token(),
                           t.middle_operator.display_token(),
                           t.right          .display_token(),
                           t.right_operator .display_token())


        def write(t, w):
            t.left_operator  .write(w)
            t.left           .write(w)
            t.middle_operator.write(w)
            t.right          .write(w)
            t.right_operator .write(w)


    @share
    class Arguments_2(BookcasedDualExpression):
        __slots__    = (())
        a_name       = '('
        b_name       = ', '
        c_name       = ')'
        display_name = '(2)'


    @share
    class ListExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        a_name                         = '['
        b_name                         = ', '
        c_name                         = ']'
        display_name                   = '[2]'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class RangeIndex(BookcasedDualExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ':'
        c_name       = ']'
        display_name = 'range-index'


    @share
    class TupleExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ', '
        c_name                         = ')'
        display_name                   = '{,2}'
        is__atom__or__special_operator = true
        is_atom                        = true
