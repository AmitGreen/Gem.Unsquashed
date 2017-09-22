#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.OtherExpression')
def gem():
    require_gem('Sapphire.Tree')


    class TripleExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression*
            'left_operator',            #   Operator*
            'middle',                   #   Expression*
            'right_operator',           #   Operator*
            'right',                    #   Expression*
        ))


        def __init__(t, left, left_operator, middle, right_operator, right):
            t.left           = left
            t.left_operator  = left_operator
            t.middle         = middle
            t.right_operator = right_operator
            t.right          = right


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left, t.left_operator, t.middle, t.right_operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.left          .display_token(),
                           t.left_operator .display_token(),
                           t.middle        .display_token(),
                           t.right_operator.display_token(),
                           t.right         .display_token())


        def write(t, w):
            t.left          .write(w)
            t.left_operator .write(w)
            t.middle        .write(w)
            t.right_operator.write(w)
            t.right         .write(w)


    @share
    class ComprehensionForExpression(TripleExpression):
        __slots__    = (())
        display_name = 'comprehension-for'


    @share
    class TernaryExpression(TripleExpression):
        __slots__    = (())
        display_name = '?:'
