#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BinaryExpression')
def gem():
    require_gem('Sapphire.Cache')
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.DualTwig')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Priority')
    require_gem('Sapphire.Tree')


    append_cache                = Shared.append_cache                   #   Due to privileged
    lookup_adjusted_meta        = Shared.lookup_adjusted_meta           #   Due to privileged
    produce_conjure_dual        = Shared.produce_conjure_dual           #   Due to privileged
    produce_conjure_triple__312 = Shared.produce_conjure_triple__312    #   Due to privileged
    store_adjusted_meta         = Shared.store_adjusted_meta            #   Due to privileged


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


    class BinaryExpression(DualTwig):
        __slots__ = (())


        k3 = none


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            frill  .dump_token(f)
            r = t.b.dump_token(f)

            return f.token_result(r, newline)


        def write(t, w):
            t.a.write(w)
            w(t.frill.s)
            t.b.write(w)


    @privileged
    def produce_conjure_binary_expression(
            name,
            Meta,

            produce_conjure_with_frill = false,
    ):
        assert (type(produce_conjure_with_frill) is Boolean) or (produce_conjure_with_frill is 1)

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
                        return t.a.count_newlines() + t.frill.count_newlines() + t.b.count_newlines()


                    display_token = (
                                        display_token__frill_with_braces
                                            if method_is_function(Meta.display_token, display_token__with_braces) else
                                                display_token__frill
                                    )


                BinaryExpression_WithFrill.k3 = BinaryExpression_WithFrill.frill


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

            append_cache(name, cache)


        if produce_conjure_with_frill:
            def conjure_binary_expression__with_frill(frill, a, b):
                if frill is meta_frill:
                    return conjure_dual(a, b)

                return conjure_triple(a, b, frill)

            if __debug__:
                conjure_binary_expression__with_frill.__name__ = intern_arrange('conjure_%s__with_frill', name)

            if produce_conjure_with_frill is 1:
                return ((
                           conjure_binary_expression,
                           conjure_binary_expression__with_frill,
                       ))

            return ((
                       conjure_binary_expression,
                       static_method(conjure_binary_expression__with_frill),
                   ))


        return conjure_binary_expression


    class AddExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'add'
        frill        = conjure_action_word('+', ' + ')


    class AndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'and-1'
        frill        = conjure_action_word('and', ' and ')


    class AsFragment(BinaryExpression):
        __slots__      = (())
        display_name   = 'as-fragment'
        frill          = conjure_action_word('as', ' as ')


    class CommaExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = ','
        frill        = COMMA__W


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

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareDifferentExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is-not'
        frill        = conjure_is_not(W__IS__W, NOT__W)


    del Shared.conjure_is_not


    class CompareExcludeExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'not-in'
        frill        = conjure_not_in(W__NOT__W, conjure_keyword_in('in '))


    del Shared.conjure_not_in


    class CompareGreaterThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>'
        frill        = conjure_action_word('>', ' > ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareGreaterThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>='
        frill        = conjure_action_word('>=', ' >= ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'
        frill        = conjure_keyword_is(' is ')


    class CompareLessThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<'
        frill        = conjure_action_word('<', ' < ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareLessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='
        frill        = conjure_action_word('<=', ' <= ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareNotEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '!='
        frill        = conjure_action_word('!=', ' != ')

        __repr__      = portray_with_braces
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
        frill        = W__ASSIGN__W


    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'
        frill        = W__ASSIGN__W


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
        frill        = W__COLON__W


    class ModulusExpression(BinaryExpression):
        __slots__    = (())
        display_name = '%'
        frill        = W__PERCENT_SIGN__W


    class MultiplyExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '*'
        frill        = W__STAR_SIGN__W


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


    [
        conjure_add_expression, conjure_add_expression__with_frill,
    ] = produce_conjure_binary_expression(
            'add',
            AddExpression,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_and_expression_1, conjure_and_expression_1__with_frill,
    ] = produce_conjure_binary_expression(
            'and-1',
            AndExpression_1,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_as_fragment, conjure_as_fragment__with_frill,
    ] = produce_conjure_binary_expression(
            'as-fragment',
            AsFragment,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_comma_expression_1, conjure_comma_expression_1__with_frill,
    ] = produce_conjure_binary_expression(
            'comma-1',
            CommaExpression_1,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_comprehension_if, conjure_comprehension_if__with_frill,
    ] = produce_conjure_binary_expression(
            'comprehension-if',
            ComprehensionIfExpression,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_compare_contains, conjure_compare_contains__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-contains',
            CompareContainsExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_equal, conjure_compare_equal__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-equal',
            CompareEqualExpression,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_compare_different, conjure_compare_different__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-different',
            CompareDifferentExpression,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_compare_exclude, conjure_compare_exclude__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-exclude',
            CompareExcludeExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_greater_than, conjure_compare_greater_than__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-greater-than',
            CompareGreaterThanExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_greater_than_or_equal, conjure_compare_greater_than_or_equal__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-greater-than-or-equal',
            CompareGreaterThanOrEqualExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_identity, conjure_compare_identity__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-identity',
            CompareIdentityExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_less_than, conjure_compare_less_than__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-less-than',
            CompareLessThanExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_less_than_or_equal, conjure_compare_less_than_or_equal__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-less-than-or-equal',
            CompareLessThanOrEqualExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_compare_not_equal, conjure_compare_not_equal__with_frill,
    ] = produce_conjure_binary_expression(
            'compare-not-equal',
            CompareNotEqualExpression,

            produce_conjure_with_frill = 1,
        )

    conjure_divide_expression         = produce_conjure_binary_expression('divide',             DivideExpression)
    conjure_integer_divide_expression = produce_conjure_binary_expression('integer-divide',     IntegerDivideExpression)

    [
        conjure_keyword_argument, conjure_keyword_argument__with_frill,
    ] = produce_conjure_binary_expression(
            'keyword-argument',
            KeywordArgument,

            produce_conjure_with_frill = 1,
        )


    conjure_keyword_parameter = produce_conjure_binary_expression('keyword-parameter', KeywordParameter)

    [
        conjure_logical_and_expression, conjure_logical_and_expression__with_frill,
    ] = produce_conjure_binary_expression(
            'logical-and-1',
            LogicalAndExpression_1,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_logical_or_expression, conjure_logical_or_expression__with_frill,
    ] = produce_conjure_binary_expression(
            'logical-or-1',
            LogicalOrExpression_1,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_map_element, conjure_map_element__with_frill,
    ] = produce_conjure_binary_expression(
            'map-element',
            MapElement,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_modulus_expression, conjure_modulus_expression__with_frill,
    ] = produce_conjure_binary_expression(
            'modulus',
            ModulusExpression,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_multiple_expression_1, conjure_multiple_expression_1__with_frill,
    ] = produce_conjure_binary_expression(
            'multiply-1',
            MultiplyExpression_1,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_or_expression_1, conjure_or_expression_1__with_frill,
    ] = produce_conjure_binary_expression(
            'or-1',
            OrExpression_1,

            produce_conjure_with_frill = 1,
        )

    conjure_power_expression          = produce_conjure_binary_expression('power',              PowerExpression)


    [
        conjure_subtract_expression, conjure_subtract_expression__with_frill,
    ] = produce_conjure_binary_expression(
            'subtract',
            SubtractExpression,

            produce_conjure_with_frill = 1,
        )


    #
    #   .mutate
    #
    AddExpression.mutate = produce_mutate__frill__ab_with_priority(
                               'add-expression',
                               PRIORITY_ARITHMETIC,
                               PRIORITY_MULTIPLY,
                               conjure_add_expression__with_frill,
                           )

    AndExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                 'and-expression-1',
                                 PRIORITY_BOOLEAN_AND,
                                 PRIORITY_NOT,
                                 conjure_and_expression_1__with_frill,
                             )

    AsFragment.mutate = produce_mutate__frill__ab_with_priority(
                            'as_fragment',
                            PRIORITY_TERNARY,
                            PRIORITY_NORMAL,
                            conjure_as_fragment__with_frill,
                        )


    CommaExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                   'comma_expression_1',
                                   PRIORITY_TERNARY,
                                   PRIORITY_TERNARY,
                                   conjure_comma_expression_1__with_frill,
                               )

    CompareContainsExpression.mutate = produce_mutate__frill__ab_with_priority(
                                           'compare_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_contains__with_frill,
                                       )

    CompareEqualExpression.mutate = produce_mutate__frill__ab_with_priority(
                                        'compare_equal_expression',
                                        PRIORITY_COMPARE,
                                        PRIORITY_NORMAL,
                                        conjure_compare_equal__with_frill,
                                    )

    CompareDifferentExpression.mutate = produce_mutate__frill__ab_with_priority(
                                            'compare_different_expression',
                                            PRIORITY_COMPARE,
                                            PRIORITY_NORMAL,
                                            conjure_compare_different__with_frill,
                                        )

    CompareExcludeExpression.mutate = produce_mutate__frill__ab_with_priority(
                                          'compare_exclude_expression',
                                          PRIORITY_COMPARE,
                                          PRIORITY_NORMAL,
                                          conjure_compare_exclude__with_frill,
                                      )

    CompareGreaterThanExpression.mutate = produce_mutate__frill__ab_with_priority(
                                              'compare_greater_than_expression',
                                              PRIORITY_COMPARE,
                                              PRIORITY_NORMAL,
                                              conjure_compare_greater_than__with_frill,
                                          )

    CompareGreaterThanOrEqualExpression.mutate = produce_mutate__frill__ab_with_priority(
                                                     'compare_greater_than_or_equal_expression',
                                                     PRIORITY_COMPARE,
                                                     PRIORITY_NORMAL,
                                                     conjure_compare_greater_than_or_equal__with_frill,
                                                 )

    CompareIdentityExpression.mutate = produce_mutate__frill__ab_with_priority(
                                           'compare_identity_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_identity__with_frill,
                                       )

    CompareLessThanExpression.mutate = produce_mutate__frill__ab_with_priority(
                                           'compare_less_than_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_less_than__with_frill,
                                       )

    CompareLessThanOrEqualExpression.mutate = produce_mutate__frill__ab_with_priority(
                                                  'compare_less_than_or_equal_expression',
                                                  PRIORITY_COMPARE,
                                                  PRIORITY_NORMAL,
                                                  conjure_compare_less_than_or_equal__with_frill,
                                              )

    CompareNotEqualExpression.mutate = produce_mutate__frill__ab_with_priority(
                                           'compare_not_equal_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_not_equal__with_frill,
                                       )

    ComprehensionIfExpression.mutate = produce_mutate__frill__ab_with_priority(
                                           'comprehension_if_expression',
                                           PRIORITY_TERNARY,
                                           PRIORITY_LAMBDA,
                                           conjure_comprehension_if__with_frill,
                                       )

    KeywordArgument.mutate = produce_mutate__frill__ab_with_priority(
                                 'keyword-argument',
                                 PRIORITY_POSTFIX,
                                 PRIORITY_TERNARY,
                                 conjure_keyword_argument__with_frill,
                             )

    LogicalAndExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                        'logical_and_expression_1',
                                        PRIORITY_LOGICAL_AND,
                                        PRIORITY_SHIFT,
                                        conjure_logical_and_expression__with_frill,
                                    )

    LogicalOrExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                       'logical_or_expression_1',
                                       PRIORITY_NORMAL,
                                       PRIORITY_LOGICAL_EXCLUSIVE_OR,
                                       conjure_logical_or_expression__with_frill,
                                   )

    MapElement.mutate = produce_mutate__frill__ab__priority(
                            'map_element',
                            PRIORITY_MAP_ELEMENT,
                            PRIORITY_TERNARY,
                            PRIORITY_TERNARY,
                            conjure_map_element__with_frill
                        )

    ModulusExpression.mutate = produce_mutate__frill__ab_with_priority(
                                        'modulus_expression',
                                        PRIORITY_MULTIPLY,
                                        PRIORITY_UNARY,
                                        conjure_modulus_expression__with_frill,
                                    )

    MultiplyExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                      'multiply_expression_1',
                                      PRIORITY_MULTIPLY,
                                      PRIORITY_UNARY,
                                      conjure_multiple_expression_1__with_frill,
                                  )

    OrExpression_1.mutate = produce_mutate__frill__ab_with_priority(
                                'or_expression_1',
                                PRIORITY_BOOLEAN_OR,
                                PRIORITY_BOOLEAN_AND,
                                conjure_or_expression_1__with_frill,
                            )

    SubtractExpression.mutate = produce_mutate__frill__ab_with_priority(
                                    'subtract_expression',
                                    PRIORITY_ARITHMETIC,
                                    PRIORITY_MULTIPLY,
                                    conjure_subtract_expression__with_frill,
                                )

    #
    #   .transform
    #
    KeywordParameter.transform = produce_transform__frill__ab_with_priority(
                                     'keyword_parameter',
                                     PRIORITY_ATOM,
                                     PRIORITY_TERNARY,
                                     conjure_keyword_argument__with_frill,
                                 )


    #
    #   .expression_meta
    #
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


    share(
        'conjure_and_expression_1',         conjure_and_expression_1,
        'conjure_comma_expression_1',       conjure_comma_expression_1,
        'conjure_comprehension_if',         conjure_comprehension_if,
        'conjure_keyword_argument',         conjure_keyword_argument,
        'conjure_keyword_parameter',        conjure_keyword_parameter,
        'conjure_logical_and_expression',   conjure_logical_and_expression,
        'conjure_logical_or_expression',    conjure_logical_or_expression,
        'conjure_map_element',              conjure_map_element,
        'conjure_as_fragment',              conjure_as_fragment,
        'conjure_modulus_expression',       conjure_modulus_expression,
        'conjure_or_expression_1',          conjure_or_expression_1,
        'conjure_power_expression',         conjure_power_expression,
    )
