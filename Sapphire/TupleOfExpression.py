#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TupleOfExpression')
def gem():
    cache   = {}
    provide = cache.setdefault


    class TupleOfExpression(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def count_newlines(t):
            total = 0

            for v in t:
                total += v.count_newlines()

            return total


        def display_token(t):
            return arrange('<many-expression %s>', ' '.join(v.display_token()   for v in t))


    @share
    def tuple_of_many_expression(many):
        r = TupleOfExpression(many)

        return provide(r, r)


    if __debug__:
        @share
        def dump_tuple_of_expression_cache():
            dump_cache('tuple-of-expression', cache)
