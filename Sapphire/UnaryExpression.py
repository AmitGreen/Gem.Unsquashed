#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Tree')


    class UnaryExpression(SapphireTrunk):
        __slots__ = ((
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        is_colon                              = false
        is_right_brace                        = false
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false


        def __init__(t, operator, right):
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.operator.display_token(),
                           t.right   .display_token())


        display_full_token = display_token


        def write(t, w):
            t.operator.write(w)
            t.right   .write(w)


    @share
    class NegativeExpression(UnaryExpression):
        __slots__    = (())
        display_name = '-'


    @share
    class NotExpression(UnaryExpression):
        __slots__    = (())
        display_name = 'not'


    @share
    class StarArgument(UnaryExpression):
        __slots__    = (())
        display_name = '*-argument'


    @share
    class StarParameter(UnaryExpression):
        __slots__    = (())
        display_name = '*-parameter'
        is_atom      = true


    @share
    class TwosComplementExpression(UnaryExpression):
        __slots__    = (())
        display_name = '~'

