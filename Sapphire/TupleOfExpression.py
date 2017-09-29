#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TupleOfExpression')
def gem():
    require_gem('Sapphire.TokenTuple')


    tuple_of_expression_cache = {}


    class TupleOfExpression(TokenTuple):
        __slots__    = (())
        display_name = 'expression-*'


    conjure_tuple_of_many_expression = produce_conjure_tuple(
                                           'many-expression',
                                           TupleOfExpression,
                                           tuple_of_expression_cache,
                                       )


    append_cache('tuple-of-expression', tuple_of_expression_cache)


    share(
        'conjure_tuple_of_many_expression',     conjure_tuple_of_many_expression,
    )
