#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Tree')


    lookup_adjusted_meta        = Shared.lookup_adjusted_meta           #   Due to privileged
    produce_conjure_dual        = Shared.produce_conjure_dual           #   Due to privileged
    produce_conjure_triple__312 = Shared.produce_conjure_triple__312    #   Due to privileged
    store_adjusted_meta         = Shared.store_adjusted_meta            #   Due to privileged


    if __debug__:
        cache_many = []


    def portray_frill(t):
        return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.frill, t.b)


    def portray_frill_with_braces(t):
        return arrange('{%s+frill %r %r %r}', t.__class__.__name__, t.a, t.frill, t.b)


    def portray_with_braces(t):
        return arrange('{%s %r %r}', t.__class__.__name__, t.a, t.b)


    def display_token__frill(t):
        return arrange('<%s+frill %s %s %s>',
                       t.display_name,
                       t.a    .display_token(),
                       t.frill.display_token(),
                       t.b    .display_token())

    def display_token__frill_with_braces(t):
        return arrange('{%s+frill %s %s %s}',
                       t.display_name,
                       t.a    .display_token(),
                       t.frill.display_token(),
                       t.b    .display_token())


    def display_token__with_braces(t):
        return arrange('{%s %s %s}', t.display_name, t.a.display_token(), t.b.display_token())


    class BinaryExpression(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression
            'b',                        #   Expression
        ))


        k3  = none


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            t.a.write(w)
            w(t.frill.s)
            t.b.write(w)


    BinaryExpression.k1 = BinaryExpression.a
    BinaryExpression.k2 = BinaryExpression.b


    @privileged
    def produce_conjure_binary_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_BinaryExpression_WithFrill(a, b, frill):
            BinaryExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BinaryExpression_WithFrill is none:
                class BinaryExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   Operator*
                    ))


                    def __init__(t, a, frill, b):
                        t.a     = a
                        t.frill = frill
                        t.b     = b


                    __repr__ = (
                                   portray_frill_with_braces
                                       if method_is_function(Meta.__repr__, portray_with_braces) else
                                           portray_frill
                               )


                    def count_newlines(t):
                        return t.a.count_newlines() + t.b.count_newlines() + t.frill.count_newlines()


                    display_token = (
                                        display_token__frill_with_braces
                                            if method_is_function(Meta.display_token, display_token__with_braces) else
                                                display_token__frill
                                    )


                BinaryExpression_WithFrill.k3  = BinaryExpression_WithFrill.frill


                if __debug__:
                    BinaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BinaryExpression_WithFrill)

            return BinaryExpression_WithFrill(a, frill, b)


        conjure_dual   = produce_conjure_dual       (name, Meta,                               cache, lookup, store)
        conjure_triple = produce_conjure_triple__312(name, conjure_BinaryExpression_WithFrill, cache, lookup, store)

        meta_frill = Meta.frill


        def conjure_binary_expression(a, frill, b):
            if frill is meta_frill:
                return conjure_dual(a, b)

            return conjure_triple(a, b, frill)


        if __debug__:
            conjure_binary_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_binary_expression


    class AddExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'add'
        frill        = conjure_action_word('+', ' + ')


    class AndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'and-1'
        frill        = conjure_action_word('and', ' and ')


    class CommaExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = ','
        frill        = conjure_comma(', ')


    class ComprehensionIfExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'comprehension-if'
        frill        = conjure_keyword_if(' if ')


    class CompareContainsExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'in'
        frill        = conjure_keyword_in(' in ')


    class CompareEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '=='
        frill        = conjure_action_word('==', ' == ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class CompareDifferentExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is-not'
        frill        = conjure_is_not(conjure_keyword_is(' is '), conjure_keyword_not('not '))


    del Shared.conjure_is_not


    class CompareExcludeExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'not-in'
        frill        = conjure_not_in(conjure_keyword_is(' not '), conjure_keyword_not('in '))


    del Shared.conjure_not_in


    class CompareGreaterThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>'
        frill        = conjure_action_word('>', ' > ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class CompareGreaterThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>='
        frill        = conjure_action_word('>=', ' >= ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'
        frill        = conjure_keyword_is(' is ')


    class CompareLessThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<'
        frill        = conjure_action_word('<', ' < ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class CompareLessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='
        frill        = conjure_action_word('<=', ' <= ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class CompareNotEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '!='
        frill        = conjure_action_word('!=', ' != ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class DivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '/'
        frill        = conjure_action_word('/', ' / ') 

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class IntegerDivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '//'
        frill        = conjure_action_word('//', ' // ') 

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'
        frill        = conjure_action_word('=', ' = ')


    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'
        frill        = conjure_action_word('=', ' = ')


    class LogicalAndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '&'
        frill        = conjure_action_word('&', ' & ')


    class LogicalOrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '|'
        frill        = conjure_action_word('|', ' | ')


    class MapElement(BinaryExpression):
        __slots__    = (())
        display_name = ':'
        frill        = conjure_action_word(':', ' : ')


    class ModuleAsFragment(BinaryExpression):
        __slots__      = (())
        display_name   = 'as-fragment'
        frill          = conjure_action_word('as', ' as ')


    class ModulusExpression(BinaryExpression):
        __slots__    = (())
        display_name = '%'
        frill        = conjure_action_word('%', ' % ')


    class MultiplyExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '*'
        frill        = conjure_action_word('*', ' * ')


    class OrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'or'
        frill        = conjure_action_word('or', ' or ')


    class PowerExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'power'
        frill        = conjure_action_word('**', ' ** ')


    class SubtractExpression(BinaryExpression):
        __slots__    = (())
        display_name = '-'
        frill        = conjure_action_word('-', ' - ')


    conjure_add_expression     = produce_conjure_binary_expression('add',               AddExpression)
    conjure_and_expression_1   = produce_conjure_binary_expression('and-1',             AndExpression_1)
    conjure_comma_expression_1 = produce_conjure_binary_expression('comma-1',           CommaExpression_1)
    conjure_comprehension_if   = produce_conjure_binary_expression('comprehension-if',  ComprehensionIfExpression)
    conjure_compare_contains   = produce_conjure_binary_expression('compare-contains',  CompareContainsExpression)
    conjure_compare_equal      = produce_conjure_binary_expression('compare-equal',     CompareEqualExpression)
    conjure_compare_different  = produce_conjure_binary_expression('compare-different', CompareDifferentExpression)
    conjure_compare_exclude    = produce_conjure_binary_expression('compare-exclude',   CompareExcludeExpression)

    conjure_compare_greater_than = produce_conjure_binary_expression(
                                       'compare-greater-than',
                                       CompareGreaterThanExpression,
                                   )

    conjure_compare_greater_than_or_equal = produce_conjure_binary_expression(
                                                'compare-greater-than-or-equal',
                                                CompareGreaterThanOrEqualExpression,
                                            )

    conjure_compare_identity  = produce_conjure_binary_expression('compare-identity',  CompareIdentityExpression)
    conjure_compare_less_than = produce_conjure_binary_expression('compare-less-than', CompareLessThanExpression)

    conjure_compare_less_than_or_equal = produce_conjure_binary_expression(
                                             'compare-less-than-or-equal',
                                             CompareLessThanOrEqualExpression,
                                        )

    conjure_compare_not_equal         = produce_conjure_binary_expression('compare-not-equal',  CompareNotEqualExpression)
    conjure_divide_expression         = produce_conjure_binary_expression('divide',             DivideExpression)
    conjure_integer_divide_expression = produce_conjure_binary_expression('integer-divide',     IntegerDivideExpression)
    conjure_keyword_argument          = produce_conjure_binary_expression('keyword-argument',   KeywordArgument)
    conjure_keyword_parameter         = produce_conjure_binary_expression('keyword-parameter',  KeywordParameter)
    conjure_logical_and_expression    = produce_conjure_binary_expression('logical-and-1',      LogicalAndExpression_1)
    conjure_logical_or_expression     = produce_conjure_binary_expression('logical-or-1',       LogicalOrExpression_1)
    conjure_map_element               = produce_conjure_binary_expression('map-element',        MapElement)
    conjure_module_as_fragment        = produce_conjure_binary_expression('module-as-fragment', ModuleAsFragment)
    conjure_modulus_expression        = produce_conjure_binary_expression('modulus',            ModulusExpression)
    conjure_multiple_expression_1     = produce_conjure_binary_expression('multiply-1',         MultiplyExpression_1)
    conjure_or_expression_1           = produce_conjure_binary_expression('or-1',               OrExpression_1)
    conjure_power_expression          = produce_conjure_binary_expression('power',              PowerExpression)
    conjure_subtract_expression       = produce_conjure_binary_expression('subtract',           SubtractExpression)


    Is_Not                    .expression_meta = static_method(conjure_compare_different)
    KeywordIn                 .expression_meta = static_method(conjure_compare_contains)
    KeywordIs                 .expression_meta = static_method(conjure_compare_identity)
    Not_In                    .expression_meta = static_method(conjure_compare_exclude)
    OperatorCompareEqual      .expression_meta = static_method(conjure_compare_equal)
    OperatorCompareNotEqual   .expression_meta = static_method(conjure_compare_not_equal)
    OperatorDivide            .expression_meta = static_method(conjure_divide_expression)
    OperatorGreaterThan       .expression_meta = static_method(conjure_compare_greater_than)
    OperatorGreaterThanOrEqual.expression_meta = static_method(conjure_compare_greater_than_or_equal)
    OperatorIntegerDivide     .expression_meta = static_method(conjure_integer_divide_expression)
    OperatorLessThan          .expression_meta = static_method(conjure_compare_less_than)
    OperatorLessThanOrEqual   .expression_meta = static_method(conjure_compare_less_than_or_equal)
    OperatorMinusSign         .expression_meta = static_method(conjure_subtract_expression)
    OperatorPercentSign       .expression_meta = static_method(conjure_modulus_expression)
    OperatorPlusSign          .expression_meta = static_method(conjure_add_expression)
    OperatorStarSign          .expression_meta = static_method(conjure_multiple_expression_1)


    if __debug__:
        @share
        def dump_binary_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s-cache', name), cache)


    share(
        'conjure_and_expression_1',         conjure_and_expression_1,
        'conjure_comma_expression_1',       conjure_comma_expression_1,
        'conjure_comprehension_if',         conjure_comprehension_if,
        'conjure_keyword_argument',         conjure_keyword_argument,
        'conjure_keyword_parameter',        conjure_keyword_parameter,
        'conjure_logical_and_expression',   conjure_logical_and_expression,
        'conjure_logical_or_expression',    conjure_logical_or_expression,
        'conjure_map_element',              conjure_map_element,
        'conjure_module_as_fragment',       conjure_module_as_fragment,
        'conjure_modulus_expression',       conjure_modulus_expression,
        'conjure_or_expression_1',          conjure_or_expression_1,
        'conjure_power_expression',         conjure_power_expression,
    )
