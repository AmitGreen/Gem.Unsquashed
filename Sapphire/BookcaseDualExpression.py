#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDual')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.TripleFrill')


    conjure_triple_frill                     = Shared.conjure_triple_frill                      #   Due to privileged
    conjure_BookcaseDualExpression_WithFrill = Shared.conjure_BookcaseDualExpression_WithFrill  #   Due to privileged
    lookup_adjusted_meta                     = Shared.lookup_adjusted_meta                      #   Due to privileged


    if __debug__:
        cache_many = []


    LP          = conjure_left_parenthesis ('(')
    COMMA_SPACE = conjure_comma            (', ')
    RP          = conjure_right_parenthesis(')')


    class BookcaseDualExpression_New(SapphireTrunk):
        __slots__ = ((
            'a',                    #   Expression+
            'b',                    #   Expression+
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.a.write(w)
            w(frill.b.s)
            t.b.write(w)
            w(frill.b.s)


    class Arguments_2(BookcaseDualExpression_New):
        __slots__    = (())
        display_name = '(2)'
        frill        = conjure_triple_frill(LP, COMMA_SPACE, RP)


    class BookcaseDualExpression(Object):
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


    @privileged
    def produce_conjure_bookcase_dual_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b
        meta_frill_c = Meta.frill.c


        def conjure_bookcase_dual_expression(frill_a, a, frill_b, b, frill_c):
            if (frill_a is meta_frill_a) and (frill_b is meta_frill_b) and (frill_c is meta_frill_c):
                first = lookup(a, absent)

                if first.__class__ is Map:
                    return (first.get(b)) or (first.setdefault(b, BookcaseDualExpression_New(a, b)))

                if first.b is b:
                    return first

                r = BookcaseDualExpression_New(a, b)

                store(a, (r   if first is absent else   { first.b : first, b : r }))

                return r

            frill = conjure_triple_frill(frill_a, frill_b, frill_c)

            assert frill.a is frill_a
            assert frill.b is frill_b
            assert frill.c is frill_c

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

                second[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    return first

                r = conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_BookcaseDualExpression_WithFrill(Meta, a, b, frill)

            store(frill, (r   if first is absent else   { first.a : first, left : r }))

            return r


        if not __debug__:
            conjure_bookcase_dual_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_bookcase_dual_expression


    @share
    class Arguments_2(BookcaseDualExpression):
        __slots__    = (())
        a_name       = '('
        b_name       = ', '
        c_name       = ')'
        display_name = '(2)'


    @share
    class ListExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        a_name                         = '['
        b_name                         = ', '
        c_name                         = ']'
        display_name                   = '[2]'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class RangeIndex(BookcaseDualExpression):
        __slots__    = (())
        a_name       = '['
        b_name       = ':'
        c_name       = ']'
        display_name = 'range-index'


    @share
    class TupleExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        a_name                         = '('
        b_name                         = ', '
        c_name                         = ')'
        display_name                   = '{,2}'
        is__atom__or__special_operator = true
        is_atom                        = true
