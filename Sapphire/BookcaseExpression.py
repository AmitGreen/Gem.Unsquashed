#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.DualFrill')
    require_gem('Sapphire.Elemental')


    conjure_dual_frill                  = Shared.conjure_dual_frill                     #   Due to privileged
    create_BookcaseExpression_WithFrill = Shared.create_BookcaseExpression_WithFrill    #   Due to privileged
    lookup_adjusted_meta                = Shared.lookup_adjusted_meta                   #   Due to privileged
    provide_adjusted_meta               = Shared.provide_adjusted_meta                  #   Due to privileged


    class BookcaseExpression_New(SapphireTrunk):
        __slots__ = ((
            'middle',                   #   Expression+
        ))


        def __init__(t, middle):
            t.middle = middle


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.middle)


        def display_token(t):
            frill = t.frill

            return arrange('<%s %s %s %s>', t.display_name, frill.a, t.middle.display_token(), frill.b)


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.middle.write(w)
            w(frill.b.s)


    class Arguments_1(BookcaseExpression_New):
        __slots__    = (())
        frill        = conjure_dual_frill(conjure_left_parenthesis('('), conjure_right_parenthesis(')'))
        display_name = '(1)'


    class HeadIndex(BookcaseExpression_New):
        __slots__    = (())
        frill        = conjure_dual_frill(
                           conjure_left_square_bracket('['),
                           conjure__colon__right_square_bracket(conjure_colon(':'), conjure_right_square_bracket(']')),
                       )
        display_name = 'head-index'


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
                line('%s:', k)

                if v.__class__ is Map:
                    for [k2, w2] in view_items(v):
                        line('  %s:', k2)
                        line('    %s', w2)

                    continue

                line('  %s', v)


        return ((conjure_bookcase_expression, dump_bookcase_expression_cache))


    [conjure_arguments_1, dump_arguments_1_cache] = produce_conjure_bookcase_expression('arguments-1', Arguments_1)
    [conjure_head_index,  dump_head_index_cache]  = produce_conjure_bookcase_expression('head-index',  HeadIndex)


    class BookcaseExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Operator+
            'middle',                   #   Expression+
            'right',                    #   Operator+
        ))


        def __init__(t, left, middle, right):
            t.left   = left
            t.middle = middle
            t.right  = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.middle, t.right)


        def display_token(t):
            if (t.left.s == t.a_name) and (t.right.s == t.b_name):
                return arrange('<%s %s %s %s>', t.display_name, t.a_name, t.middle.display_token(), t.b_name)

            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


        def write(t, w):
            w(t.left.s)
            t.middle.write(w)
            t.right .write(w)


    @share
    class ListExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '['
        b_name                         = ']'
        display_name                   = '[1]'
        is__atom__or__special_operator = true
        is_atom                        = true



    @share
    class MapExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '{'
        b_name                         = '}'
        display_name                   = '{1}'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ']'
        display_name = 'index'


    @share
    class ParenthesizedExpression(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ')'
        display_name                   = '()'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class TailIndex(BookcaseExpression):
        __slots__    = (())
        a_name       = '[:'
        b_name       = ']'
        display_name = 'tail-index'


    @share
    class TupleExpression_1(BookcaseExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ')'
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class BookcasedDualExpression(Object):
        __slots__ = ((
            'left_operator',            #   Operator*
            'left',                     #   Expression*
            'middle_operator',          #   Operator*
            'right',                    #   Expression*
            'right_operator',           #   Operator*
        ))


        is_right_parenthesis    = false
        is_right_square_bracket = false


        def __init__(t, left_operator, left, middle_operator, right, right_operator):
            t.left_operator   = left_operator
            t.left            = left
            t.middle_operator = middle_operator
            t.right           = right
            t.right_operator  = right_operator


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left_operator, t.left, t.middle_operator, t.right, t.right_operator)


        def display_token(t):
            if (
                    t.left_operator  .s == t.a_name
                and t.middle_operator.s == t.b_name
                and t.right_operator .s == t.c_name
            ):
                b_name = t.b_name

                if ' ' in b_name:
                    b_name = '<' + b_name + '>'

                return arrange('<%s %s %s %s %s %s>',
                               t.display_name,
                               t.a_name,
                               t.left .display_token(),
                               b_name,
                               t.right.display_token(),
                               t.c_name)

            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.left_operator  .display_token(),
                           t.left           .display_token(),
                           t.middle_operator.display_token(),
                           t.right          .display_token(),
                           t.right_operator .display_token())


        def write(t, w):
            t.left_operator  .write(w)
            t.left           .write(w)
            t.middle_operator.write(w)
            t.right          .write(w)
            t.right_operator .write(w)


    @share
    class Arguments_2(BookcasedDualExpression):
        __slots__    = (())
        a_name       = '('
        b_name       = ', '
        c_name       = ')'
        display_name = '(2)'


    @share
    class ListExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        a_name                         = '['
        b_name                         = ', '
        c_name                         = ']'
        display_name                   = '[2]'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class RangeIndex(BookcasedDualExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ':'
        c_name       = ']'
        display_name = 'range-index'


    @share
    class TupleExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ', '
        c_name                         = ')'
        display_name                   = '{,2}'
        is__atom__or__special_operator = true
        is_atom                        = true


    share(
        'conjure_arguments_1',  conjure_arguments_1,
        'conjure_head_index',   conjure_head_index,
    )


    if __debug__:
        share(
            'dump_arguments_1_cache',   dump_arguments_1_cache,
            'dump_head_index_cache',    dump_head_index_cache,
        )
