#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseTriple')
def gem():
    require_gem('Sapphire.QuadrupleFrill')
    require_gem('Sapphire.TripleTwig')


    append_cache                    = Shared.append_cache                       #   Due to privileged
    conjure_quadruple_frill         = Shared.conjure_quadruple_frill            #   Due to privileged
    lookup_adjusted_meta            = Shared.lookup_adjusted_meta               #   Due to privileged
    produce_conjure_triple          = Shared.produce_conjure_triple             #   Due to privileged
    produce_conjure_quadruple__4123 = Shared.produce_conjure_quadruple__4123    #   Due to privileged
    store_adjusted_meta             = Shared.store_adjusted_meta                #   Due to privileged


    @share
    class BookcaseTripleExpression(TripleTwig):
        __slots__ = (())
        k4        = none


        def count_newlines(t):
            return (
                         t.a    .count_newlines()
                       + t.b    .count_newlines()
                       + t.c    .count_newlines()
                       + t.d    .count_newlines()
                       + t.frill.count_newlines()
                   )


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)
            frill.a.dump_token(f)
            t.a.dump_token(f)
            frill.b.dump_token(f)
            t.b.dump_token(f)
            frill.c.dump_token(f)
            t.c.dump_token(f)
            r = frill.d.dump_token(f, false)

            if (r) and (newline):
                f.line('>')
                return false

            f.partial('>')
            return r


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.a.write(w)
            w(frill.b.s)
            t.b.write(w)
            w(frill.c.s)
            t.c.write(w)
            w(frill.d.s)
 
 
    @share
    @privileged
    def produce_conjure_bookcase_triple_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(a, b, c, frill):
            BookcaseTripleExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseTripleExpression_WithFrill is none:
                class BookcaseTripleExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   QuadrupleFrill
                    ))


                    def __init__(t, a, b, c, frill):
                        t.a     = a
                        t.b     = b
                        t.c     = c
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            frill_a = frill.a

                            return arrange('<%s+frill %+d %s %s %s %s %s %s %s>',
                                           t.display_name,
                                           frill_a.a.total,
                                           frill_a.b.display_token(),
                                           t.a      .display_token(),
                                           frill.b  .display_token(),
                                           t.b      .display_token(),
                                           frill.c  .display_token(),
                                           t.c      .display_token(),
                                           frill.d  .display_token())


                BookcaseTripleExpression_WithFrill.k4 = BookcaseTripleExpression_WithFrill.frill


                if __debug__:
                    BookcaseTripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseTripleExpression_WithFrill)

            return BookcaseTripleExpression_WithFrill(a, b, c, frill)


        conjure_triple    = produce_conjure_triple         (name, Meta,                   cache, lookup, store)
        conjure_quadruple = produce_conjure_quadruple__4123(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b
        meta_frill_c = Meta.frill.c
        meta_frill_d = Meta.frill.d


        def conjure_bookcase_triple(frill_a, a, frill_b, b, frill_c, c, frill_d):
            if (
                       frill_a is meta_frill_a
                   and frill_b is meta_frill_b
                   and frill_c is meta_frill_c
                   and frill_d is meta_frill_d
            ):
                return conjure_triple(a, b, c)

            return conjure_quadruple(a, b, c, conjure_quadruple_frill(frill_a, frill_b, frill_c, frill_d))


        if __debug__:
            conjure_bookcase_triple.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        return conjure_bookcase_triple


    class RaiseStatement_3(BookcaseTripleExpression):
        __slots__    = (())
        display_name = 'raise-statement-3'
        frill        = conjure_quadruple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           conjure_comma(', '),
                           conjure_comma(', '),
                           empty_line_marker,
                       )

        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t.frill.a.a


    conjure_raise_statement_3 = produce_conjure_bookcase_triple_expression('raise-statement-3', RaiseStatement_3)


    share(
        'conjure_raise_statement_3',    conjure_raise_statement_3,
    )
