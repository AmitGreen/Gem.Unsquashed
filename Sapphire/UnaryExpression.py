#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Tree')


    if __debug__:
        cache_many = []


    class UnaryExpression_New(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression
        ))


        is_colon       = false
        is_right_brace = false


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def write(t, w):
            w(t.frill.s)
            t.a.write(w)


    def conjure_UnaryExpression_WithFrill(Meta, frill, a):
        UnaryExpression_WithFrill = lookup_adjusted_meta(Meta)

        if UnaryExpression_WithFrill is none:
            class UnaryExpression_WithFrill(Meta):
                __slots__ = ((
                    'frill',                #   Operator*
                ))


                def __init__(t, frill, a):
                    t.frill = frill
                    t.a     = a


                def __repr__(t):
                    return arrange('<%s %r %r>', t.__class__.__name__, t.frill, t.a)


                def display_token(t):
                    return arrange('<%s+frill %s %s>', t.display_name, t.frill.display_token(), t.a.display_token())


            if __debug__:
                UnaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

            store_adjusted_meta(Meta, UnaryExpression_WithFrill)

        return UnaryExpression_WithFrill(frill, a)


    @privileged
    def produce_conjure_unary_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__

        meta_frill = Meta.frill


        def conjure_unary_expression(frill, a):
            if frill is meta_frill:
                return (lookup(a)) or (provide(a, Meta(a)))

            first = lookup(frill, absent)

            if first.__class__ is Map:
                return (
                              first.get(a)
                           or first.setdefault(a, conjure_UnaryExpression_WithFrill(Meta, frill, a))
                       )

            if first.a is a:
                return first

            r = conjure_UnaryExpression_WithFrill(Meta, frill, a)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_unary_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_unary_expression


    class NegativeExpression(UnaryExpression_New):
        __slots__    = (())
        display_name = '-'
        frill        = conjure_action_word('-', '-')


    class NotExpression(UnaryExpression_New):
        __slots__    = (())
        display_name = 'not'
        frill        = conjure_keyword_not('not ')


    class StarArgument(UnaryExpression_New):
        __slots__    = (())
        display_name = '*-argument'
        frill        = conjure_star_sign('*')


    conjure_negative_expression = produce_conjure_unary_expression('negative',   NegativeExpression)
    conjure_not_expression      = produce_conjure_unary_expression('not',        NotExpression)
    conjure_star_argument       = produce_conjure_unary_expression('*-argument', StarArgument)


    class UnaryExpression(SapphireTrunk):
        __slots__ = ((
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        is_colon                              = false
        is_right_brace                        = false
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false


        def __init__(t, operator, right):
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.operator.write(w)
            t.right   .write(w)


    @share
    class StarArgument(UnaryExpression):
        __slots__    = (())
        display_name = '*-argument'


    @share
    class StarParameter(UnaryExpression):
        __slots__    = (())
        display_name = '*-parameter'
        is_atom      = true


    @share
    class TwosComplementExpression(UnaryExpression):
        __slots__    = (())
        display_name = '~'


    if __debug__:
        @share
        def dump_unary_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_negative_expression',  conjure_negative_expression,
        'conjure_not_expression',       conjure_not_expression,
        'conjure_star_argument',        conjure_star_argument,
    )
