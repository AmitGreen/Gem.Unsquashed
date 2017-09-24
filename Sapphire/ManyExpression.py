#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ManyExpression')
def gem():
    cache   = {}
    provide = cache.setdefault


    class ManyExpression(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def display_token(t):
            return arrange('<many-expression %s>', ' '.join(v.display_token()   for v in t))


    @share
    def conjure_many_expression(many):
        r = ManyExpression(many)

        return provide(r, r)


    if __debug__:
        @share
        def dump_many_expression_cache():
            dump_cache('many-expression', cache)
