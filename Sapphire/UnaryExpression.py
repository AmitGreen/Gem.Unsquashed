#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    class UnaryExpression(Object):
        __slots__ = ((
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        is_right_square_bracket = false


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
    class PrefixAtom(UnaryExpression):
        __slots__                             = (())
        display_name                          = 'prefixed-atom'
        is__atom__or__right_close_operator    = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    @share
    class PrefixIdentifier(UnaryExpression):
        __slots__                             = (())
        display_name                          = 'prefixed-identifier'
        is__atom__or__right_close_operator    = true
        is_atom                               = true
        is_identifier                         = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    Identifier .prefix_meta = PrefixIdentifier
    DoubleQuote.prefix_meta = PrefixAtom
    SingleQuote.prefix_meta = PrefixAtom
    Number     .prefix_meta = PrefixAtom
