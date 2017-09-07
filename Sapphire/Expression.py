#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


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


    class UnaryExpression(Object):
        __slots__ = ((
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


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
        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    @share
    class PrefixIdentifier(UnaryExpression):
        __slots__                             = (())
        display_name                          = 'prefixed-identifier'
        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is_identifier                         = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    Identifier .prefix_meta = PrefixIdentifier
    SingleQuote.prefix_meta = PrefixAtom
    Number     .prefix_meta = PrefixAtom
