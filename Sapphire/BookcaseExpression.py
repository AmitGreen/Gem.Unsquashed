#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseExpression')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.DualFrill')
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Tree')
    require_gem('Sapphire.TripleToken')


    append_cache             = Shared.append_cache                  #   Due to privileged
    conjure_vw_frill         = Shared.conjure_vw_frill              #   Due to privileged
    lookup_adjusted_meta     = Shared.lookup_adjusted_meta          #   Due to privileged
    produce_conjure_dual__21 = Shared.produce_conjure_dual__21      #   Due to privileged
    store_adjusted_meta      = Shared.store_adjusted_meta           #   Due to privileged


    LSB = conjure_left_square_bracket ('[')
    RSB = conjure_right_square_bracket(']')

    LP_RP   = conjure_vw_frill(LP,  RP)
    LSB_RSB = conjure_vw_frill(LSB, RSB)


    @share
    class BookcaseExpression(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression+
        ))


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def count_newlines(t):
            return t.a.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            r = frill.w.dump_token(f, false)

            return f.token_result(r, newline)


        remove_comments = remove_comments__a__plain


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


    BookcaseExpression.k1 = BookcaseExpression.a


    @share
    @privileged
    def produce_conjure_bookcase_expression(
            name, Meta,

            produce_conjure_with_frill = 0,
    ):
        assert 0 <= produce_conjure_with_frill <= 2

        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        def conjure_BookcaseExpression_WithFrill(a, frill):
            BookcaseExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseExpression_WithFrill is none:
                class BookcaseExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, a, frill):
                        t.a     = a
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            return arrange('<%s+frill %s %s %s>',
                                           t.display_name,
                                           frill.v.display_token(),
                                           t.a    .display_token(),
                                           frill.w.display_token())


                    remove_comments = attribute(Meta, 'remove_comments__frill', none)

                    if remove_comments is none:
                        def remove_comments(t):
                            return t.conjure_plain(t.a.remove_comments())


                write = attribute(Meta, 'write__frill', none)

                if write is not none:
                    BookcaseExpression_WithFrill.write = write


                #BookcaseExpression_WithFrill.k2 = BookcaseExpression_WithFrill.frill


                if __debug__:
                    BookcaseExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseExpression_WithFrill)

            return BookcaseExpression_WithFrill(a, frill)


        conjure_dual__with_frill = produce_conjure_dual__21(
                                       name + '__X2',
                                       conjure_BookcaseExpression_WithFrill,
                                       cache,
                                       lookup,
                                       store,
                                   )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w


        def conjure_bookcase_expression(frill_v, a, frill_w):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w):
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__with_frill(a, conjure_vw_frill(frill_v, frill_w))


        if __debug__:
            conjure_bookcase_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)


        if produce_conjure_with_frill:
            def conjure_with_frill(frill, a):
                if frill is meta_frill:
                    return (lookup(a)) or (provide(a, Meta(a)))

                return conjure_dual__with_frill(a, frill)


            if __debug__:
                conjure_with_frill.__name__ = intern_arrange('conjure_%s__with_frill', name)


            return ((
                       conjure_bookcase_expression,
                       (
                           conjure_dual__with_frill   if produce_conjure_with_frill is 1 else
                           static_method(conjure_with_frill)
                       ),
                   ))


        return conjure_bookcase_expression


    class Arguments_1(BookcaseExpression):
        __slots__      = (())
        display_name   = 'arguments-(1)'
        frill          = LP_RP
        is_arguments_1 = true


        def remove_comments(t):
            a = t.a

            a__2 = a.remove_comments()

            if (t.frill is LP_RP) and (a is a__2):
                return t

            return conjure_arguments_1(LP, a__2, RP)


        def transform(t, mutate):
            assert mutate.remove_comments

            return t.remove_comments()


    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'head-index'
        frill        = conjure_vw_frill(LSB, conjure__colon__right_square_bracket(COLON, RSB))


    class ListExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '[1]'
        frill                          = LSB_RSB
        is__atom__or__special_operator = true
        is_atom                        = true


    class MapExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '{:1:}'
        frill                          = conjure_vw_frill(conjure_left_brace ('{'), conjure_right_brace('}'))
        is__atom__or__special_operator = true
        is_atom                        = true


    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'normal-index'
        frill        = LSB_RSB


    class Parameters_1(BookcaseExpression):
        __slots__       = (())
        display_name    = 'parameters-(1)'
        frill           = LP_RP
        is_parameters_1 =  true


        def parameter_1_named(t, name):
            return t.a.s == name


        def remove_comments(t):
            a = t.a

            a__2 = a.remove_comments()

            if (t.frill is LP_RP) and (a is a__2):
                return t

            return conjure_parameters_1(LP, a__2, RP)


    class ParenthesizedExpression(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '()'
        frill                          = LP_RP
        is__atom__or__special_operator = true
        is_atom                        = true


    class TailIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'tail-index'
        frill        = conjure_vw_frill(conjure__left_square_bracket__colon(LSB, COLON), RSB)


    class TupleExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '{,}'
        frill                          = conjure_vw_frill(LP, conjure_comma__right_parenthesis(conjure_comma(','), RP))
        is__atom__or__special_operator = true
        is_atom                        = true


    conjure_arguments_1       = produce_conjure_bookcase_expression('arguments-1',       Arguments_1)
    conjure_head_index        = produce_conjure_bookcase_expression('head-index',        HeadIndex)
    conjure_list_expression_1 = produce_conjure_bookcase_expression('list-expression-1', ListExpression_1)
    conjure_map_expression_1  = produce_conjure_bookcase_expression('map-expression-1',  MapExpression_1)
    conjure_normal_index      = produce_conjure_bookcase_expression('normal-index',      NormalIndex)
    conjure_parameters_1      = produce_conjure_bookcase_expression('parameters-1',      Parameters_1)

    conjure_parenthesized_expression = produce_conjure_bookcase_expression(
                                           'parenthesized-expression',
                                           ParenthesizedExpression,
                                       )

    conjure_tail_index         = produce_conjure_bookcase_expression('tail-index',         TailIndex)
    conjure_tuple_expression_1 = produce_conjure_bookcase_expression('tuple-expression-1', TupleExpression_1)


    share(
        'conjure_arguments_1',                      conjure_arguments_1,
        'conjure_head_index',                       conjure_head_index,
        'conjure_list_expression_1',                conjure_list_expression_1,
        'conjure_map_expression_1',                 conjure_map_expression_1,
        'conjure_normal_index',                     conjure_normal_index,
        'conjure_parameters_1',                     conjure_parameters_1,
        'conjure_parenthesized_expression',         conjure_parenthesized_expression,
        'conjure_tail_index',                       conjure_tail_index,
        'conjure_tuple_expression_1',               conjure_tuple_expression_1,
    )
