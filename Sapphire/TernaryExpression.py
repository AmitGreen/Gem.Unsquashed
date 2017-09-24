#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TernaryExpression')
def gem():
    require_gem('Sapphire.Tree')


    conjure_dual_frill   = Shared.conjure_dual_frill            #   Due to privileged
    lookup_adjusted_meta = Shared.lookup_adjusted_meta          #   Due to privileged
    store_adjusted_meta  = Shared.store_adjusted_meta           #   Due to privileged


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


    @share
    def conjure_TripleExpression_WithFrill(Meta, a, b, c, frill):
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


            if __debug__:
                TripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

            store_adjusted_meta(Meta, TripleExpression_WithFrill)

        return TripleExpression_WithFrill(a, b, c, frill)


    @privileged
    def produce_conjure_triple_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b


        def conjure_triple_expression(a, frill_a, b, frill_b, c):
            if (frill_a is meta_frill_a) and (frill_b is meta_frill_b):
                first = lookup(a, absent)

                if first.__class__ is Map:
                    second = first.get(b, absent)

                    if second.__class__ is Map:
                        return (
                                      second.get(c)
                                   or second.setdefault(c, Meta(a, b, c))
                               )

                    if second.c is c:
                        return second

                    r = Meta(a, b, c)

                    first[b] = (r   if second is absent else   { second.c : second, c : r })

                    return r

                if first.b is b:
                    if first.c is c:
                        return first

                    r = Meta(a, b, c)

                    store(a, { b : { first.c : first, c : r } })

                    return r

                r = Meta(a, b, c)

                store(a, (r   if first is absent else   { first.a : first, a : r }))

                return r

            frill = conjure_dual_frill(frill_a, frill_b)

            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    third = first.get(b, absent)

                    if third.__class__ is Map:
                        return (
                                      third.get(c)
                                   or third.setdefault(c, conjure_TripleExpression_WithFrill(Meta, a, b, c, frill))
                               )

                    if third.c is c:
                        return third

                    r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

                    second[b] = (r   if third is absent else   { third.c : third, c : r })

                    return r

                if second.b is b:
                    if second.c is c:
                        return second

                    r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

                    first[a] = { b : { second.c : second, c : r } }

                    return r

                r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    if first.c is c:
                        return first

                    r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

                    store(frill, { a : { b : { first.c : first, c : r } } })

                    return r

                r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_TripleExpression_WithFrill(Meta, a, b, c, frill)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


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
