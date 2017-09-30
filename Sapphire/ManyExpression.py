#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyExpression')
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


        def dump_token(t, newline = true):
            frill = t.frill
            many  = t.many

            frill_estimate = frill.frill_estimate

            partial('<%s ', t.display_name)

            if frill_estimate is 1:
                assert length(many) is 2

                many[0].dump_token()
                frill.dump_token()
                r = many[1].dump_token(false)
            elif frill_estimate is 2:
                assert length(many) is 3

                many[0].dump_token()
                frill.a.dump_token()
                many[1].dump_token()
                frill.b.dump_token()
                r = many[2].dump_token(false)
            elif frill_estimate is 3:
                assert length(many) is 4

                many[0].dump_token()
                frill.a.dump_token()
                many[1].dump_token()
                frill.b.dump_token()
                many[2].dump_token()
                frill.c.dump_token()
                r = many[3].dump_token(false)
            elif frill_estimate is 4:
                assert length(many) is 5

                many[0].dump_token()
                frill.a.dump_token()
                many[1].dump_token()
                frill.b.dump_token()
                many[2].dump_token()
                frill.c.dump_token()
                many[3].dump_token()
                frill.many.dump_token()
                r = many[4].dump_token(false)
            else:
                iterator   = iterate(many)
                next_frill = next_method(iterate(frill))

                many[0].dump_token()

                for v in many[1:-1]:
                    next_frill().dump_token()
                    v.dump_token()

                next_frill().dump_token()
                r = many[-1].dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


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
                w(frill.a.s)
                many[1].write(w)
                w(frill.b.s)
                many[2].write(w)
                return

            if frill_estimate is 3:
                assert length(many) is 4

                many[0].write(w)
                w(frill.a.s)
                many[1].write(w)
                w(frill.b.s)
                many[2].write(w)
                w(frill.c.s)
                many[3].write(w)
                return

            if frill_estimate is 4:
                assert length(many) is 5

                many[0].write(w)
                w(frill.a.s)
                many[1].write(w)
                w(frill.b.s)
                many[2].write(w)
                w(frill.c.s)
                many[3].write(w)
                w(frill.d.s)
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
    def produce_conjure_many_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        conjure_dual = produce_conjure_dual(name + '__X2', Meta, cache)


        def conjure_many_expression(list, frill_list):
            return conjure_dual(conjure_many_frill(frill_list), conjure_tuple_of_many_expression(list))


        if __debug__:
            conjure_many_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

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
    conjure_comma_expression_many      = produce_conjure_many_expression('comma-*',      CommaExpression_Many)
    conjure_compare_expression_many    = produce_conjure_many_expression('compare-*',    CompareExpression_Many)
    conjure_logical_or_expression_many = produce_conjure_many_expression('logical-or-*', LogicalOrExpression_Many)
    conjure_multiply_expression_many   = produce_conjure_many_expression('multiply-*',   MultiplyExpression_Many)
    conjure_or_expression_many         = produce_conjure_many_expression('or-*',         OrExpression_Many)


    share(
        'conjure_and_expression_many',          conjure_and_expression_many,
        'conjure_arithmetic_expression_many',   conjure_arithmetic_expression_many,
        'conjure_comma_expression_many',        conjure_comma_expression_many,
        'conjure_compare_expression_many',      conjure_compare_expression_many,
        'conjure_logical_or_expression_many',   conjure_logical_or_expression_many,
        'conjure_multiply_expression_many',     conjure_multiply_expression_many,
        'conjure_or_expression_many',           conjure_or_expression_many,
    )
