#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TupleOfExpression')
def gem():
    tuple_of_expression_cache = {}


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


    conjure_tuple_of_many_expression = produce_conjure_tuple(
                                           'many-expression',
                                           TupleOfExpression,
                                           tuple_of_expression_cache,
                                       )


    append_cache('tuple-of-expression', tuple_of_expression_cache)


    share(
        'conjure_tuple_of_many_expression',     conjure_tuple_of_many_expression,
    )
