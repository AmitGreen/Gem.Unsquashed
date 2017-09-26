#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDual')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.TripleFrill')


    conjure_triple_frill         = Shared.conjure_triple_frill              #   Due to privileged
    produce_dual_cache_functions = Shared.produce_dual_cache_functions      #   Due to privileged


    if __debug__:
        cache_many = []


    COMMA_SPACE = conjure_comma               (', ')
    LP          = conjure_left_parenthesis    ('(')
    LSB         = conjure_left_square_bracket ('[')
    RP          = conjure_right_parenthesis   (')')
    RSB         = conjure_right_square_bracket(']')


    class BookcaseDualExpression(SapphireTrunk):
        __slots__ = ((
            'a',                    #   Expression+
            'b',                    #   Expression+
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.a.write(w)
            w(frill.b.s)
            t.b.write(w)
            w(frill.c.s)


    @share
    def conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill):
        BookcaseDualExpression_WithFrill = lookup_adjusted_meta(Meta)

        if BookcaseDualExpression_WithFrill is none:
            class BookcaseDualExpression_WithFrill(Meta):
                __slots__ = ((
                    'frill',                #   TripleFrill
                ))


                def __init__(t, a, b, frill):
                    t.a     = a
                    t.b     = b
                    t.frill = frill


                def __repr__(t):
                    return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.frill)


                def count_newlines(t):
                    return t.a.count_newlines() + t.b.count_newlines() + t.frill.count_newlines()


                def display_token(t):
                    frill = t.frill

                    return arrange('<%s+frill %s %s %s %s %s>',
                                   t.display_name,
                                   frill.a.display_token(),
                                   t.a    .display_token(),
                                   frill.b.display_token(),
                                   t.b    .display_token(),
                                   frill.c.display_token())


            if __debug__:
                BookcaseDualExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

            store_adjusted_meta(Meta, BookcaseDualExpression_WithFrill)

        return BookcaseDualExpression_WithFrill(a, b, frill)


    @privileged
    def produce_conjure_bookcase_dual_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b
        meta_frill_c = Meta.frill.c

        conjure_dual = produce_dual_cache_functions(name + '__X__dual', Meta, cache)


        def conjure_bookcase_dual_expression(frill_a, a, frill_b, b, frill_c):
            if (frill_a is meta_frill_a) and (frill_b is meta_frill_b) and (frill_c is meta_frill_c):
                return conjure_dual(a, b)

            frill = conjure_triple_frill(frill_a, frill_b, frill_c)

            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    return (
                                  second.get(b)
                               or second.setdefault(b, conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill))
                           )

                if second.b is b:
                    return second

                r = conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    return first

                r = conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_bookcase_dual_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_bookcase_dual_expression


    class Arguments_2(BookcaseDualExpression):
        __slots__    = (())
        display_name = '(2)'
        frill        = conjure_triple_frill(LP, COMMA_SPACE, RP)


    class ListExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        display_name                   = '[2]'
        frill                          = conjure_triple_frill(LSB, COMMA_SPACE, RSB)
        is__atom__or__special_operator = true
        is_atom                        = true


    class RangeIndex(BookcaseDualExpression):
        __slots__    = (())
        display_name = 'range-index'
        frill        = conjure_triple_frill(LSB, conjure_colon(' : '), RSB)


    class TupleExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        display_name                   = '{,2}'
        frill                          = conjure_triple_frill(LP, COMMA_SPACE, RP)
        is__atom__or__special_operator = true
        is_atom                        = true


    conjure_arguments_2        = produce_conjure_bookcase_dual_expression('arguments-2',        Arguments_2)
    conjure_list_expression_2  = produce_conjure_bookcase_dual_expression('list-expression-2',  ListExpression_2)
    conjure_range_index        = produce_conjure_bookcase_dual_expression('range-index',        RangeIndex)
    conjure_tuple_expression_2 = produce_conjure_bookcase_dual_expression('tuple-expression-2', TupleExpression_2)


    if __debug__:
        @share
        def dump_bookcase_dual_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_arguments_2',          conjure_arguments_2,
        'conjure_list_expression_2',    conjure_list_expression_2,
        'conjure_range_index',          conjure_range_index,
        'conjure_tuple_expression_2',   conjure_tuple_expression_2,
    )
