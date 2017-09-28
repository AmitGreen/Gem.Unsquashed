#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Tree')


    lookup_adjusted_meta     = Shared.lookup_adjusted_meta          #   Due to privileged
    produce_conjure_dual__21 = Shared.produce_conjure_dual__21      #   Due to privileged
    store_adjusted_meta      = Shared.store_adjusted_meta           #   Due to privileged


    if __debug__:
        cache_many = []


    class UnaryExpression(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression
        ))


        is_colon       = false
        is_right_brace = false


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def count_newlines(t):
            return t.a.count_newlines()


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def write(t, w):
            w(t.frill.s)
            t.a.write(w)


    UnaryExpression.k1 = UnaryExpression.a


    @privileged
    def produce_conjure_unary_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        def conjure_UnaryExpression_WithFrill(a, frill):
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


                    def count_newlines(t):
                        return t.a.count_newlines() + t.frill.count_newlines()


                    def display_token(t):
                        return arrange('<%s+frill %s %s>', t.display_name, t.frill.display_token(), t.a.display_token())


                #UnaryExpression_WithFrill.k2 = UnaryExpression_WithFrill.frill


                if __debug__:
                    UnaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, UnaryExpression_WithFrill)

            return UnaryExpression_WithFrill(frill, a)



        conjure_dual__21 = produce_conjure_dual__21(
                               name + '__X2',
                               conjure_UnaryExpression_WithFrill,
                               cache,
                               lookup,
                               store,
                           )

        meta_frill = Meta.frill


        def conjure_unary_expression(frill, a):
            if frill is meta_frill:
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__21(a, frill)


        if __debug__:
            conjure_unary_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_unary_expression


    class NegativeExpression(UnaryExpression):
        __slots__    = (())
        display_name = '-'
        frill        = conjure_action_word('-', '-')


    class NotExpression(UnaryExpression):
        __slots__    = (())
        display_name = 'not'
        frill        = conjure_keyword_not('not ')


    class StarArgument(UnaryExpression):
        __slots__    = (())
        display_name = '*-argument'
        frill        = conjure_star_sign('*')


    class StarParameter(UnaryExpression):
        __slots__    = (())
        display_name = '*-parameter'
        frill        = conjure_star_sign('*')
        is_atom      = true


    class TwosComplementExpression(UnaryExpression):
        __slots__    = (())
        display_name = '~'
        frill        = conjure_action_word('~', '~')


    conjure_negative_expression = produce_conjure_unary_expression('negative',        NegativeExpression)
    conjure_not_expression      = produce_conjure_unary_expression('not',             NotExpression)
    conjure_star_argument       = produce_conjure_unary_expression('*-argument',      StarArgument)
    conjure_star_parameter      = produce_conjure_unary_expression('*-parameter',     StarParameter)
    conjure_twos_complement     = produce_conjure_unary_expression('twos-complement', TwosComplementExpression)


    if __debug__:
        @share
        def dump_unary_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_negative_expression',  conjure_negative_expression,
        'conjure_not_expression',       conjure_not_expression,
        'conjure_star_argument',        conjure_star_argument,
        'conjure_star_parameter',       conjure_star_parameter,
        'conjure_twos_complement',      conjure_twos_complement,
    )
