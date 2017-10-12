#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualExpression')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.TripleFrill')


    append_cache           = Shared.append_cache                #   due to privileged
    conjure_vwx_frill      = Shared.conjure_vwx_frill           #   due to privileged
    lookup_adjusted_meta   = Shared.lookup_adjusted_meta        #   due to privileged
    produce_conjure_dual   = Shared.produce_conjure_dual        #   due to privileged
    produce_conjure_triple = Shared.produce_conjure_triple      #   due to privileged
    store_adjusted_meta    = Shared.store_adjusted_meta         #   due to privileged
    transform__frill_ab    = Shared.transform__frill_ab         #   due to privileged


    @share
    class BookcaseDualExpression(DualTwig):
        k3 = none


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines() + t.frill.count_newlines()


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            r = frill.x.dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)
 
 
    BookcaseDualExpression.k1 = BookcaseDualExpression.a
    BookcaseDualExpression.k2 = BookcaseDualExpression.b


    @share
    @privileged
    def produce_conjure_bookcase_dual_expression(
            name,
            Meta,

            produce_conjure_plain      = false,
            produce_conjure_with_frill = false,
    ):
        assert type(produce_conjure_plain)      is Boolean
        assert type(produce_conjure_with_frill) is Boolean

        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(frill, a, b):
            BookcaseDualExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseDualExpression_WithFrill is none:
                class BookcaseDualExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   TripleFrill
                    ))


                    def __init__(t, frill, a, b):
                        t.frill = frill
                        t.a     = a
                        t.b     = b


                    def __repr__(t):
                        return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.a, t.b)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            return arrange('<%s+frill %s %s %s %s %s>',
                                           t.display_name,
                                           frill.v.display_token(),
                                           t.a    .display_token(),
                                           frill.w.display_token(),
                                           t.b    .display_token(),
                                           frill.x.display_token())


                #BookcaseDualExpression_WithFrill.k1 = BookcaseDualExpression_WithFrill.frill
                BookcaseDualExpression_WithFrill.k2 = BookcaseDualExpression_WithFrill.a
                BookcaseDualExpression_WithFrill.k3 = BookcaseDualExpression_WithFrill.b


                write = attribute(Meta, 'write__frill', none)


                if write is not none:
                    BookcaseDualExpression_WithFrill.write = write


                BookcaseDualExpression_WithFrill.k3 = BookcaseDualExpression_WithFrill.frill


                if __debug__:
                    BookcaseDualExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseDualExpression_WithFrill)

            return BookcaseDualExpression_WithFrill(frill, a, b)


        conjure_dual              = produce_conjure_dual  (name, Meta,                   cache, lookup, store)
        conjure_triple_with_frill = produce_conjure_triple(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill_v = Meta.frill.v
        meta_frill_w = Meta.frill.w
        meta_frill_x = Meta.frill.x


        def conjure_bookcase_dual_expression(frill_v, a, frill_w, b, frill_x):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w) and (frill_x is meta_frill_x):
                return conjure_dual(a, b)

            return conjure_triple_with_frill(conjure_vwx_frill(frill_v, frill_w, frill_x), a, b)


        if __debug__:
            conjure_bookcase_dual_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        if produce_conjure_with_frill:
            def conjure_with_frill(frill, a, b):
                if frill is meta_frill:
                    return conjure(a, b)

                return conjure_triple_with_frill(conjure_vwx_frill(frill_v, frill_w, frill_x), a, b)


            if __debug__:
                conjure_with_frill.__name__ = intern_arrange('conjure_%s__with_frill', name)


            if produce_conjure_plain:
                return ((
                           conjure_bookcase_dual_expression,
                           static_method(conjure_dual),
                           static_method(conjure_triple_with_frill),
                       ))

            return ((
                       conjure_bookcase_dual_expression,
                       static_method(conjure_triple_with_frill),
                   ))

        if produce_conjure_plain:
            return ((
                       conjure_bookcase_dual_expression,
                       static_method(conjure_dual),
                   ))



        return conjure_bookcase_dual_expression


    class Arguments_2(BookcaseDualExpression):
        __slots__    = (())
        display_name = '(2)'
        frill        = conjure_vwx_frill(LP, COMMA__W, RP)

        mutate = produce_mutate__frill__ab__priority(
                     'arguments_2',
                     PRIORITY_COMPREHENSION,
                     PRIORITY_COMPREHENSION,
                     PRIORITY_COMPREHENSION,
                 )


    class ListExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        display_name                   = '[2]'
        frill                          = conjure_vwx_frill(LSB, COMMA__W, RSB)
        is__atom__or__special_operator = true
        is_atom                        = true


    class RangeIndex(BookcaseDualExpression):
        __slots__    = (())
        display_name = 'range-index'
        frill        = conjure_vwx_frill(LSB, conjure_colon(' : '), RSB)


    class TupleExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        display_name                   = '{,2}'
        frill                          = conjure_vwx_frill(LP, COMMA__W, RP)
        is__atom__or__special_operator = true
        is_atom                        = true


    [
        conjure_arguments_2, Arguments_2.conjure_plain,
    ] = produce_conjure_bookcase_dual_expression(
                'arguments-2',
                Arguments_2,
                
                produce_conjure_plain = true,
        )

    conjure_list_expression_2  = produce_conjure_bookcase_dual_expression('list-expression-2',  ListExpression_2)
    conjure_range_index        = produce_conjure_bookcase_dual_expression('range-index',        RangeIndex)
    conjure_tuple_expression_2 = produce_conjure_bookcase_dual_expression('tuple-expression-2', TupleExpression_2)


    share(
        'conjure_arguments_2',          conjure_arguments_2,
        'conjure_list_expression_2',    conjure_list_expression_2,
        'conjure_range_index',          conjure_range_index,
        'conjure_tuple_expression_2',   conjure_tuple_expression_2,
    )
