#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Tree')


    @share
    class BaseExpression_Many(SapphireTrunk):
        __slots__ = ((
            'many',                     #   Tuple of *
        ))


        def __init__(t, many):
            t.many = many


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, ' '.join(portray(v)   for v in t.many))


        def display_token(t):
            many = t.many

            return arrange('{%s %s %s %s}',
                           t.display_name,
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


        def write(t, w):
            for v in t.many:
                v.write(w)


    @share
    class ArithmeticExpression_Many(BaseExpression_Many):
        __slots__    = (())
        display_name = 'arithmetic-*'


    @share
    class CommaExpression_Many(BaseExpression_Many):
        __slots__    = (())
        display_name = ',-*'


    @share
    class CompareExpression_Many(BaseExpression_Many):
        __slots__ = (())


        def __repr__(t):
            return arrange('{%s %r}', t.__class__.__name__, ' '.join(portray(v)   for v in t.many))


        def display_token(t):
            many = t.many

            return arrange('{compare-* %s %s %s}',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class LogicalOrExpression_Many(BaseExpression_Many):
        __slots__    = (())
        display_name = '|-*'


    @share
    class MultiplyExpression_Many(BaseExpression_Many):
        __slots__    = (())
        display_name = 'multiply-*'


    @share
    class OrExpression_Many(BaseExpression_Many):
        __slots__    = (())
        display_name = 'or-*'
