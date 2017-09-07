#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    class BookcaseExpression(Object):
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
    class BookcaseAtom(BookcaseExpression):
        __slots__    = (())
        display_name = 'bookcased-atom'


        is__atom__or__right_close_operator    = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    @share
    class BookcaseIdentifier(BookcaseExpression):
        __slots__    = (())
        display_name = 'bookcased-identifier'


        is__atom__or__right_close_operator    = true
        is_atom                               = true
        is_identifier                         = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    @share
    class Arguments_1(BookcaseExpression):
        __slots__    = (())
        display_name = '(1)'


    @share
    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'head-index'


        def display_token(t):
            if (t.left.s == '[') and (t.right.s == ':]'):
                return arrange('<%s [ %s :]>', t.display_name, t.middle.display_token())

            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'index'


        def display_token(t):
            if (t.left.s == '[') and (t.right.s == ']'):
                return arrange('<%s [ %s ]>', t.display_name, t.middle.display_token())

            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class PathenthesizedExpression(BookcaseExpression):
        __slots__                          = (())
        display_name                       = '()'
        is__atom__or__right_close_operator = true
        is_atom                            = true
        is_right_parenthesis               = false


        def display_token(t):
            if t.left.s == '(' and t.right.s == ')':
                return arrange('(%s)', t.middle.display_token())

            return arrange('(%s %s %s)',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class TupleExpression_1(BookcaseExpression):
        __slots__                          = (())
        display_name                       = '{,}'
        is__atom__or__right_close_operator = true
        is_atom                            = true
        is_right_parenthesis               = false


    class BookcasedDualExpression(Object):
        __slots__ = ((
            'left_operator',            #   OperatorLeftParenthesis | OperatorLeftSquareBracket
            'left',                     #   Expression*
            'middle_operator',          #   OperatorColon | OperatorComma
            'right',                    #   Expression*
            'right_operator',           #   OperatorRightParenthesis | OperatorRightSquareBracket
        ))


        def __init__(t, left_operator, left, middle_operator, right, right_operator):
            t.left_operator  = left_operator
            t.left        = left
            t.middle_operator           = middle_operator
            t.right        = right
            t.right_operator = right_operator


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__,
                           t.left_operator,
                           t.left,
                           t.middle_operator,
                           t.right,
                           t.right_operator)


        def display_token(t):
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
        display_name = '(2)'


    @share
    class RangeIndex(BookcasedDualExpression):
        __slots__    = (())
        display_name = 'range-index'


    Identifier .bookcase_meta = BookcaseIdentifier
    SingleQuote.bookcase_meta = BookcaseAtom
    Number     .bookcase_meta = BookcaseAtom
