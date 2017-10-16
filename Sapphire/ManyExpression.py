#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ManyExpression')
def gem():
    require_gem('Sapphire.ManyFrill')
    require_gem('Sapphire.TupleOfExpression')


    append_cache                     = Shared.append_cache                      #   Due to privileged
    conjure_many_frill               = Shared.conjure_many_frill                #   Due to privileged
    conjure_tuple_of_many_expression = Shared.conjure_tuple_of_many_expression  #   Due to privileged
    produce_conjure_dual             = Shared.produce_conjure_dual              #   Due to privileged


    if __debug__:
        cache_many = []


    class ManyExpression(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   BookcaseManyFrill
            'many',                     #   TupleOfExpression+
        ))


        def __init__(t, frill, many):
            t.frill = frill
            t.many  = many


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, t.frill, ' '.join(portray(v)   for v in t.many))


        def count_newlines(t):
            return t.many.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.frill.display_token(),
                           ' '.join(v.display_token()   for v in t.many))


        def dump_token(t, f, newline = true):
            frill = t.frill
            many  = t.many

            frill_estimate = frill.frill_estimate

            f.partial('<%s ', t.display_name)

            if frill_estimate is 1:
                assert length(many) is 2

                many    [0].dump_token(f)
                frill      .dump_token(f)
                r = many[1].dump_token(f, false)

            elif frill_estimate is 2:
                assert length(many) is 3

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                r = many[2].dump_token(f, false)

            elif frill_estimate is 3:
                assert length(many) is 4

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                many    [2].dump_token(f)
                frill   .x .dump_token(f)
                r = many[3].dump_token(f, false)

            elif frill_estimate is 4:
                assert length(many) is 5

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                many    [2].dump_token(f)
                frill   .x .dump_token(f)
                many    [3].dump_token(f)
                frill   .y .dump_token(f)
                r = many[4].dump_token(f, false)

            else:
                iterator   = iterate(many)
                next_frill = next_method(iterate(frill))

                many[0].dump_token(f)

                for v in many[1:-1]:
                    next_frill().dump_token(f)
                    v           .dump_token(f)

                next_frill().dump_token(f)
                r = many[-1].dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            many  = t.many
            frill = t.frill

            frill_estimate = frill.frill_estimate

            if frill_estimate is 1:
                assert length(many) is 2

                many[0].write(w)
                w(frill.s)
                many[1].write(w)
                return

            if frill_estimate is 2:
                assert length(many) is 3

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                return

            if frill_estimate is 3:
                assert length(many) is 4

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                w(frill.x.s)
                many[3].write(w)
                return

            if frill_estimate is 4:
                assert length(many) is 5

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                w(frill.x.s)
                many[3].write(w)
                w(frill.y.s)
                many[4].write(w)
                return

            iterator    = iterate(many)
            write_frill = next_method(frill.iterate_write(w))

            next_method(iterator)().write(w)

            for v in iterator:
                write_frill()
                v.write(w)


    #ManyExpression.k1 = ManyExpression.frill
    ManyExpression.k2 = ManyExpression.many


    @privileged
    def produce_conjure_many_expression(
            name, Meta,

            produce_conjure_with_frill = 0,
    ):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        conjure_dual = produce_conjure_dual(name + '__X2', Meta, cache)


        def conjure_many_expression(list, frill_list):
            return conjure_dual(conjure_many_frill(frill_list), conjure_tuple_of_many_expression(list))


        if __debug__:
            conjure_many_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        if produce_conjure_with_frill:
            if __debug__:
                conjure_dual.__name__ = intern_arrange('conjure_%s__with_frill', name)

            return ((
                       conjure_many_expression,
                       conjure_dual,
                   ))

        return conjure_many_expression


    class AndExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'and-*'


    class ArithmeticExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'arithmetic-*'


    class CommaExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = ',-*'


    class CompareExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'compare-*'


    class LogicalOrExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = '|-*'


    class MultiplyExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'multiply-*'


    class OrExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'or-*'


    conjure_and_expression_many        = produce_conjure_many_expression('and-*',        AndExpression_Many)
    conjure_arithmetic_expression_many = produce_conjure_many_expression('arithmetic-*', ArithmeticExpression_Many)

    [
        conjure_comma_expression_many, conjure_comma_expression_many__with_frill,
    ] = produce_conjure_many_expression(
            'comma-*',
            CommaExpression_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_expression_many, conjure_compare_expression_many__with_frill,
    ] = produce_conjure_many_expression(
            'compare-*',
            CompareExpression_Many,

            produce_conjure_with_frill = 1,
        )

    conjure_logical_or_expression_many = produce_conjure_many_expression('logical-or-*', LogicalOrExpression_Many)
    conjure_multiply_expression_many   = produce_conjure_many_expression('multiply-*',   MultiplyExpression_Many)
    conjure_or_expression_many         = produce_conjure_many_expression('or-*',         OrExpression_Many)


    #
    #   .mutate
    #
    CommaExpression_Many.mutate = produce_mutate__frill__many(
                                      'comma_expression_many',
                                      PRIORITY_TERNARY,
                                      PRIORITY_TERNARY,
                                      PRIORITY_TERNARY,
                                      conjure_comma_expression_many__with_frill,
                                  )

    CompareExpression_Many.mutate = produce_mutate__frill__many(
                                        'compare_expression_many',
                                        PRIORITY_COMPARE,
                                        PRIORITY_COMPARE,
                                        PRIORITY_NORMAL,
                                        conjure_compare_expression_many__with_frill,
                                    )

    share(
        'conjure_and_expression_many',          conjure_and_expression_many,
        'conjure_arithmetic_expression_many',   conjure_arithmetic_expression_many,
        'conjure_comma_expression_many',        conjure_comma_expression_many,
        'conjure_compare_expression_many',      conjure_compare_expression_many,
        'conjure_logical_or_expression_many',   conjure_logical_or_expression_many,
        'conjure_multiply_expression_many',     conjure_multiply_expression_many,
        'conjure_or_expression_many',           conjure_or_expression_many,
    )
