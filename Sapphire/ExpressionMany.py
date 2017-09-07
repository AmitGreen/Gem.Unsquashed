#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    @share
    class BaseExpression_Many(Object):
        __slots__ = ((
            'many',                     #   Tuple of *
        ))


        def __init__(t, many):
            t.many = many


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, ' '.join(portray(v)   for v in t.many))


        def write(t, w):
            for v in t.many:
                v.write(w)


    @share
    class Arguments_Many(BaseExpression_Many):
        __slots__ = (())


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == ')'):
                return arrange('(%s)', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('(%s %s %s)',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class CompareExpression_Many(BaseExpression_Many):
        __slots__ = (())

        def __repr__(t):
            return arrange('{%s %r}', t.__class__.__name__, ' '.join(portray(v)   for v in t.many))

        def display_token(t):
            many = t.many

            return arrange('{%s %s %s}',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class ParameterColon_Many(BaseExpression_Many):
        __slots__ = (())


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == '):'):
                return arrange('<(): %s>', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('<(): %s %s %s>',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class TupleExpression_Many(BaseExpression_Many):
        __slots__ = (())


        is__atom__or__right_parenthesis = true
        is_atom                         = true
        is_right_parenthesis            = false


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == ')'):
                return arrange('({,*} %s)', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('({,*} %s %s %s)',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())
