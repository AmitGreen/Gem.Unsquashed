#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TernaryExpression')
def gem():
    require_gem('Sapphire.Tree')


    conjure_dual_frill              = Shared.conjure_dual_frill                 #   Due to privileged
    lookup_adjusted_meta            = Shared.lookup_adjusted_meta               #   Due to privileged
    produce_conjure_quadruple__4123 = Shared.produce_conjure_quadruple__4123    #   Due to privileged
    produce_triple_cache            = Shared.produce_triple_cache               #   Due to privileged
    store_adjusted_meta             = Shared.store_adjusted_meta                #   Due to privileged


    if __debug__:
        cache_many = []


    class TripleExpression(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression*
            'b',                        #   Expression*
            'c',                        #   Expression*
        ))


        def __init__(t, a, b, c):
            t.a = a
            t.b = b
            t.c = c


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.c)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines() + t.c.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.a.display_token(),
                           t.b.display_token(),
                           t.c.display_token())


        def write(t, w):
            frill = t.frill

            t.a.write(w)
            w(frill.a.s)
            t.b.write(w)
            w(frill.b.s)
            t.c.write(w)


    TripleExpression.kq2 = TripleExpression.a
    TripleExpression.kq3 = TripleExpression.b
    TripleExpression.kq4 = TripleExpression.c

    TripleExpression.k1 = TripleExpression.a
    TripleExpression.k2 = TripleExpression.b
    TripleExpression.k3 = TripleExpression.c


    @privileged
    def produce_conjure_triple_expression(name, Meta):
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
                                       frill.a.display_token(),
                                       t.b    .display_token(),
                                       frill.b.display_token(),
                                       t.c    .display_token())


                TripleExpression_WithFrill.kq1 = TripleExpression_WithFrill.frill

                if __debug__:
                    TripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, TripleExpression_WithFrill)

            return TripleExpression_WithFrill(a, b, c, frill)


        conjure_triple    = produce_triple_cache           (name + '__X3', Meta, cache, lookup, store)
        conjure_quadruple = produce_conjure_quadruple__4123(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b


        def conjure_triple_expression(a, frill_a, b, frill_b, c):
            if (frill_a is meta_frill_a) and (frill_b is meta_frill_b):
                return conjure_triple(a, b, c)

            return conjure_quadruple(a, b, c, conjure_dual_frill(frill_a, frill_b))


        if __debug__:
            conjure_triple_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_triple_expression


    class ComprehensionForExpression(TripleExpression):
        __slots__    = (())
        display_name = 'comprehension-for'
        frill        = conjure_dual_frill(conjure_keyword_for(' for '), conjure_keyword_in(' in '))


    class TernaryExpression(TripleExpression):
        __slots__    = (())
        display_name = '?:'
        frill        = conjure_dual_frill(conjure_keyword_if(' if '), conjure_action_word('else', ' else '))


    conjure_comprehension_for  = produce_conjure_triple_expression('comprehension-for',  ComprehensionForExpression)
    conjure_ternary_expression = produce_conjure_triple_expression('ternary-expression', TernaryExpression)


    if __debug__:
        @share
        def dump_ternary_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s-cache', name), cache)


    share(
        'conjure_comprehension_for',    conjure_comprehension_for,
        'conjure_ternary_expression',   conjure_ternary_expression,
    )
