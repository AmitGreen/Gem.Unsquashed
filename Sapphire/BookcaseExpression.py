#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseExpression')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.DualFrill')
    require_gem('Sapphire.Elemental')


    conjure_dual_frill                  = Shared.conjure_dual_frill                     #   Due to privileged
    create_BookcaseExpression_WithFrill = Shared.create_BookcaseExpression_WithFrill    #   Due to privileged
    lookup_adjusted_meta                = Shared.lookup_adjusted_meta                   #   Due to privileged
    provide_adjusted_meta               = Shared.provide_adjusted_meta                  #   Due to privileged


    LP  = conjure_left_parenthesis    ('(')
    LSB = conjure_left_square_bracket ('[')
    RP  = conjure_right_parenthesis   (')')
    RSB = conjure_right_square_bracket(']')

    LP_RP   = conjure_dual_frill(LP,  RP)
    LSB_RSB = conjure_dual_frill(LSB, RSB)


    class BookcaseExpression(SapphireTrunk):
        __slots__ = ((
            'middle',                   #   Expression+
        ))


        def __init__(t, middle):
            t.middle = middle


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.middle)


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.middle.display_token())


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.middle.write(w)
            w(frill.b.s)


    class Arguments_1(BookcaseExpression):
        __slots__    = (())
        display_name = '(1)'
        frill        = LP_RP


    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'head-index'
        frill        = conjure_dual_frill(LSB, conjure__colon__right_square_bracket(conjure_colon(':'), RSB))


    class ListExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '[1]'
        frill                          = LSB_RSB
        is__atom__or__special_operator = true
        is_atom                        = true


    class MapExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '{1}'
        frill                          = conjure_dual_frill(conjure_left_brace ('{'), conjure_right_brace('}'))
        is__atom__or__special_operator = true
        is_atom                        = true


    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'index'
        frill        = LSB_RSB


    class ParenthesizedExpression(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '()'
        frill                          = LP_RP
        is__atom__or__special_operator = true
        is_atom                        = true


    class TailIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'tail-index'
        frill        = conjure_dual_frill(conjure__left_square_bracket__colon(LSB, conjure_colon(':')), RSB)


    class TupleExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '{,}'
        frill                          = conjure_dual_frill(LP, conjure__comma__right_parenthesis(conjure_comma(','), RP))
        is__atom__or__special_operator = true
        is_atom                        = true


    @privileged
    def produce_conjure_bookcase_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__

        frill_a = Meta.frill.a
        frill_b = Meta.frill.b


        def conjure_bookcase_expression(a, middle, b):
            if (a is frill_a) and (b is frill_b):
                return (lookup(middle)) or (provide(middle, Meta(middle)))

            frill = conjure_dual_frill(a, b)

            assert frill.a is a
            assert frill.b is b

            first = lookup(frill, absent)

            if first.__class__ is Map:
                return (
                              first.get(middle)
                           or first.setdefault(
                                  middle,
                                  (
                                         lookup_adjusted_meta(Meta)
                                      or create_BookcaseExpression_WithFrill(Meta)
                                  )(middle, frill),
                              )
                       )

            if first.middle is middle:
                return first

            r = ((lookup_adjusted_meta(Meta)) or (create_BookcaseExpression_WithFrill(Meta)))(middle, frill)

            store(frill, (r   if first is absent else   { first.middle : first, middle : r }))

            return r


        if not __debug__:
            return ((conjure_bookcase_expression, none))


        conjure_bookcase_expression.__name__ = intern_arrange('conjure_%s', name)


        def dump_bookcase_expression_cache():
            line('===  %s_cache   ===', name)

            for [k, v] in iterate_items_sorted_by_key(cache):
                line('%s:', k.display_token())

                if v.__class__ is Map:
                    for [k2, w2] in view_items(v):
                        line('  %s:', k2.display_token())
                        line('    %s', w2.display_token())

                    continue

                line('  %s', v.display_token())


        return ((conjure_bookcase_expression, dump_bookcase_expression_cache))


    [conjure_arguments_1, dump_arguments_1_cache] = produce_conjure_bookcase_expression('arguments-1', Arguments_1)
    [conjure_head_index,  dump_head_index_cache]  = produce_conjure_bookcase_expression('head-index',  HeadIndex)

    [
        conjure_list_expression_1, dump_list_expression_1_cache,
    ] = produce_conjure_bookcase_expression('list-expression-1', ListExpression_1)

    [
        conjure_map_expression_1, dump_map_expression_1_cache,
    ] = produce_conjure_bookcase_expression('map-expression-1', MapExpression_1)

    [conjure_normal_index, dump_normal_index_cache] = produce_conjure_bookcase_expression('normal-index', NormalIndex)

    [
        conjure_parenthesized_expression, dump_parenthesized_expression_cache,
    ] = produce_conjure_bookcase_expression('parenthesized-expression', ParenthesizedExpression)

    [conjure_tail_index, dump_tail_index_cache] = produce_conjure_bookcase_expression('tail-index', TailIndex)

    [
        conjure_tuple_expression_1, dump_tuple_expression_1_cache,
    ] = produce_conjure_bookcase_expression('tuple-expression-1', TupleExpression_1)


    share(
        'conjure_arguments_1',                  conjure_arguments_1,
        'conjure_head_index',                   conjure_head_index,
        'conjure_list_expression_1',            conjure_list_expression_1,
        'conjure_map_expression_1',             conjure_map_expression_1,
        'conjure_normal_index',                 conjure_normal_index,
        'conjure_parenthesized_expression',     conjure_parenthesized_expression,
        'conjure_tail_index',                   conjure_tail_index,
        'conjure_tuple_expression_1',           conjure_tuple_expression_1,
    )


    if __debug__:
        share(
            'dump_arguments_1_cache',               dump_arguments_1_cache,
            'dump_head_index_cache',                dump_head_index_cache,
            'dump_list_expression_1_cache',         dump_list_expression_1_cache,
            'dump_map_expression_1_cache',          dump_map_expression_1_cache,
            'dump_normal_index_cache',              dump_normal_index_cache,
            'dump_parenthesized_expression_cache',  dump_parenthesized_expression_cache,
            'dump_tail_index_cache',                dump_tail_index_cache,
            'dump_tuple_expression_1_cache',        dump_tuple_expression_1_cache,
        )
