#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseTriple')
def gem():
    require_gem('Sapphire.QuadrupleFrill')
    require_gem('Sapphire.TripleTwig')


    append_cache                    = Shared.append_cache                       #   Due to privileged
    conjure_vwxy_frill              = Shared.conjure_vwxy_frill                 #   Due to privileged
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
                       + t.frill.count_newlines()
                   )


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            frill    .x.dump_token(f)
            t        .c.dump_token(f)
            r = frill.y.dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)
            t.c.write(w)
            w(frill.y.s)
 
 
    @share
    @privileged
    def produce_conjure_bookcase_triple_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(frill, a, b, c):
            BookcaseTripleExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseTripleExpression_WithFrill is none:
                class BookcaseTripleExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   QuadrupleFrill
                    ))


                    def __init__(t, frill, a, b, c):
                        t.frill = frill
                        t.a     = a
                        t.b     = b
                        t.c     = c


                    def __repr__(t):
                        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            frill_v = frill.v

                            return arrange('<%s+frill %+d %s %s %s %s %s %s %s>',
                                           t.display_name,
                                           frill_v.a.total,
                                           frill_v.b.display_token(),
                                           t      .a.display_token(),
                                           frill  .w.display_token(),
                                           t      .b.display_token(),
                                           frill  .x.display_token(),
                                           t      .c.display_token(),
                                           frill  .y.display_token())


                BookcaseTripleExpression_WithFrill.k4 = BookcaseTripleExpression_WithFrill.frill


                if __debug__:
                    BookcaseTripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseTripleExpression_WithFrill)

            return BookcaseTripleExpression_WithFrill(frill, a, b, c)


        conjure_triple    = produce_conjure_triple         (name, Meta,                   cache, lookup, store)
        conjure_quadruple = produce_conjure_quadruple__4123(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill_v = Meta.frill.v
        meta_frill_w = Meta.frill.w
        meta_frill_x = Meta.frill.x
        meta_frill_y = Meta.frill.y


        def conjure_bookcase_triple(frill_v, a, frill_w, b, frill_x, c, frill_y):
            if (
                       frill_v is meta_frill_v
                   and frill_w is meta_frill_w
                   and frill_x is meta_frill_x
                   and frill_y is meta_frill_y
            ):
                return conjure_triple(a, b, c)

            return conjure_quadruple(conjure_vwxy_frill(frill_v, frill_w, frill_x, frill_y), a, b, c)


        if __debug__:
            conjure_bookcase_triple.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        return conjure_bookcase_triple


    class RaiseStatement_3(BookcaseTripleExpression):
        __slots__    = (())
        display_name = 'raise-statement-3'
        frill        = conjure_vwxy_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           COMMA__W,
                           COMMA__W,
                           LINE_MARKER,
                       )

        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        @property
        def indentation(t):
            return t.frill.v.a


    conjure_raise_statement_3 = produce_conjure_bookcase_triple_expression('raise-statement-3', RaiseStatement_3)


    share(
        'conjure_raise_statement_3',    conjure_raise_statement_3,
    )
