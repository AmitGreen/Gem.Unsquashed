#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TernaryExpression')
def gem():
    require_gem('Sapphire.TripleTwig')


    append_cache                    = Shared.append_cache                       #   Due to privileged
    conjure_vw_frill                = Shared.conjure_vw_frill                   #   Due to privileged
    lookup_adjusted_meta            = Shared.lookup_adjusted_meta               #   Due to privileged
    produce_conjure_quadruple__4123 = Shared.produce_conjure_quadruple__4123    #   Due to privileged
    produce_conjure_triple          = Shared.produce_conjure_triple             #   Due to privileged
    store_adjusted_meta             = Shared.store_adjusted_meta                #   Due to privileged


    class TripleExpression(TripleTwig):
        __slots__ = (())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            frill.v.dump_token(f)
            t    .b.dump_token(f)
            frill.w.dump_token(f)
            r = t.c.dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            frill = t.frill

            t.a.write(w)
            w(frill.v.s)
            t.b.write(w)
            w(frill.w.s)
            t.c.write(w)


    @privileged
    def produce_conjure_triple_expression(
            name, Meta,

            produce_conjure_with_frill = false,
    ):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(a, b, c, frill):
            TripleExpression_WithFrill = lookup_adjusted_meta(Meta)

            if TripleExpression_WithFrill is none:
                class TripleExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, a, b, c, frill):
                        t.a     = a
                        t.b     = b
                        t.c     = c
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.frill)


                    def count_newlines(t):
                        return (
                                     t.a    .count_newlines()
                                   + t.b    .count_newlines()
                                   + t.c    .count_newlines()
                                   + t.frill.count_newlines()
                               )


                    def display_token(t):
                        frill = t.frill

                        return arrange('<%s+frill %s %s %s %s %s>',
                                       t.display_name,
                                       t.a    .display_token(),
                                       frill.v.display_token(),
                                       t.b    .display_token(),
                                       frill.w.display_token(),
                                       t.c    .display_token())


                TripleExpression_WithFrill.kq1 = TripleExpression_WithFrill.frill

                if __debug__:
                    TripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, TripleExpression_WithFrill)

            return TripleExpression_WithFrill(a, b, c, frill)


        conjure_triple    = produce_conjure_triple         (name + '__X3', Meta, cache, lookup, store)
        conjure_quadruple = produce_conjure_quadruple__4123(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w


        def conjure_triple_expression(a, frill_v, b, frill_w, c):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w):
                return conjure_triple(a, b, c)

            return conjure_quadruple(a, b, c, conjure_vw_frill(frill_v, frill_w))


        if __debug__:
            conjure_triple_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        if produce_conjure_with_frill:
            def conjure_with_frill(frill, a, b, c):
                if frill is meta_frill:
                    return conjure_triple(a, b, c)

                return conjure_quadruple(a, b, c, frill)


            if __debug__:
                conjure_with_frill.__name__ = intern_arrange('conjure_%s__with_frill', name)

            return ((
                       conjure_triple_expression,
                       conjure_with_frill,
                   ))


        return conjure_triple_expression


    class ComprehensionForExpression(TripleExpression):
        __slots__    = (())
        display_name = 'comprehension-for'
        frill        = conjure_vw_frill(W__FOR__W, W__IN__W)


    class TernaryExpression(TripleExpression):
        __slots__    = (())
        display_name = '?:'
        frill        = conjure_vw_frill(W__IF__W, W__ELSE__W)


    [
        conjure_comprehension_for, conjure_comprehension_for__with_frill,
    ] = produce_conjure_triple_expression(
            'comprehension-for',
            ComprehensionForExpression,
            
            produce_conjure_with_frill = true,
        )

    [
        conjure_ternary_expression, conjure_ternary_expression__with_frill,
    ] = produce_conjure_triple_expression(
            'ternary-expression',
            TernaryExpression,
            
            produce_conjure_with_frill = true,
        )


    TernaryExpression.mutate = produce_mutate__frill__abc__priority(
                                   'ternary-expression',
                                   conjure_ternary_expression__with_frill,
                                   PRIORITY_TERNARY,
                                   PRIORITY_BOOLEAN_OR,
                                   PRIORITY_BOOLEAN_OR,
                                   PRIORITY_TERNARY,
                              )


    share(
        'conjure_comprehension_for',    conjure_comprehension_for,
        'conjure_ternary_expression',   conjure_ternary_expression,
    )
