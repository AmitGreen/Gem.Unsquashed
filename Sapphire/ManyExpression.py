#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyExpression')
def gem():
    require_gem('Sapphire.ManyFrill')
    require_gem('Sapphire.TupleOfExpression')


    conjure_many_frill       = Shared.conjure_many_frill                #   Due to privileged
    tuple_of_many_expression = Shared.tuple_of_many_expression          #   Due to privileged


    if __debug__:
        cache_many = []


    class ManyExpression(SapphireTrunk):
        __slots__ = ((
            'many',                     #   TupleOfExpression+
            'frill',                    #   BookcaseManyFrill
        ))


        def __init__(t, many, frill):
            t.many  = many
            t.frill = frill


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, ' '.join(portray(v)   for v in t.many), t.frill)


        def count_newlines(t):
            return t.many.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           ' '.join(v.display_token()   for v in t.many),
                           t.frill.display_token())


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

            iterator    = iterate(many)
            write_frill = next_method(frill.iterate_write(w))

            next_method(iterator)().write(w)

            for v in iterator:
                write_frill()
                v.write(w)


    @privileged
    def produce_conjure_many_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        #
        #   NOTE:
        #       Reversed from normal: uses 'frill' as the first map index & 'many' as the second map index.
        #
        def conjure_many_expression(list, frill_list):
            many  = tuple_of_many_expression(list)
            frill = conjure_many_frill(frill_list)

            first = lookup(frill, absent)

            if first.__class__ is Map:
                return (first.get(many)) or (first.setdefault(many, Meta(many, frill)))

            if first.many is many:
                return first

            r = Meta(many, frill)

            store(frill, (r   if first is absent else   { first.many : first, many : r }))

            return r


        if __debug__:
            conjure_many_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

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


    conjure_and_expression_many        = produce_conjure_many_expression('and-many',        AndExpression_Many)
    conjure_arithmetic_expression_many = produce_conjure_many_expression('arithmetic-many', ArithmeticExpression_Many)
    conjure_comma_expression_many      = produce_conjure_many_expression('comma-many',      CommaExpression_Many)
    conjure_compare_expression_many    = produce_conjure_many_expression('compare-many',    CompareExpression_Many)
    conjure_logical_or_expression_many = produce_conjure_many_expression('logical_or-many', LogicalOrExpression_Many)
    conjure_multiply_expression_many   = produce_conjure_many_expression('multiply-many',   MultiplyExpression_Many)
    conjure_or_expression_many         = produce_conjure_many_expression('or-many',         OrExpression_Many)


    if __debug__:
        @share
        def dump_many_expression_cache_many():
            for [name, cache] in cache_many[-1:]:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_and_expression_many',          conjure_and_expression_many,
        'conjure_arithmetic_expression_many',   conjure_arithmetic_expression_many,
        'conjure_comma_expression_many',        conjure_comma_expression_many,
        'conjure_compare_expression_many',      conjure_compare_expression_many,
        'conjure_logical_or_expression_many',   conjure_logical_or_expression_many,
        'conjure_multiply_expression_many',     conjure_multiply_expression_many,
        'conjure_or_expression_many',           conjure_or_expression_many,
    )
