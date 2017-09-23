#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Tree')


    lookup_adjusted_meta = Shared.lookup_adjusted_meta
    store_adjusted_meta  = Shared.store_adjusted_meta


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


    class BinaryExpression_New(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Expression
            'b',                        #   Expression
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def write(t, w):
            t.a.write(w)
            w(t.frill.s)
            t.b.write(w)


    @privileged
    def conjure_BinaryExpression_WithFrill(Meta, a, frill, b):
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
                               portray_frill_with_braces   if Meta.__repr__.im_func is portray_with_braces else
                               portray_frill
                           )


                display_token = (
                                    display_token__frill_with_braces
                                        if Meta.display_token.im_func is display_token__with_braces else
                                            display_token__frill
                                )


            if __debug__:
                BinaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

            store_adjusted_meta(Meta, BinaryExpression_WithFrill)

        return BinaryExpression_WithFrill(a, frill, b)


    @privileged
    def produce_conjure_binary_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__

        meta_frill = Meta.frill


        def conjure_binary_expression(a, frill, b):
            if frill is meta_frill:
                first = lookup(a, absent)

                if first.__class__ is Map:
                    return (first.get(b)) or (first.setdefault(b, Meta(a, b)))

                if first.b is b:
                    return first

                r = Meta(a, b)

                store(a, (r   if first is absent else   { first.b : first, b : r }))

                return r

            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    return (
                                  second.get(b)
                               or second.setdefault(b, conjure_BinaryExpression_WithFrill(Meta, a, frill, b))
                           )

                if second.b is b:
                    return second

                r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    return first

                r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_binary_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_binary_expression


    class AddExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = 'add'
        frill        = conjure_action_word('+', ' + ')


    class AndExpression_1(BinaryExpression_New):
        __slots__    = (())
        display_name = 'and-1'
        frill        = conjure_action_word('and', ' and ')


    class CommaExpression_1(BinaryExpression_New):
        __slots__    = (())
        display_name = ','
        frill        = conjure_comma(', ')


    class ComprehensionIfExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = 'comprehension-if'
        frill        = conjure_keyword_if(' if ')


    class CompareContainsExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = 'in'
        frill        = conjure_keyword_in(' in ')


    class CompareEqualExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = '=='
        frill        = conjure_action_word('==', ' == ')


    class CompareDifferentExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = 'is-not'
        frill        = conjure_is_not(conjure_keyword_is(' is '), conjure_keyword_not('not '))


    del Shared.conjure_is_not


    class CompareExcludeExpression(BinaryExpression_New):
        __slots__    = (())
        display_name = 'not-in'
        frill        = conjure_not_in(conjure_keyword_is(' not '), conjure_keyword_not('in '))


    del Shared.conjure_not_in


    class CompareGreaterThanExpression(BinaryExpression_New):
        __slots__     = (())
        display_name  = '>'
        frill = conjure_action_word('>', ' > ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces



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

    class BinaryExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        def __init__(t, left, operator, right):
            assert type(left)  is not String
            assert type(right) is not String

            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)
            t.right   .write(w)


    @share
    class CompareGreaterThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>='


    @share
    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'


    @share
    class CompareNotEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '!='


    @share
    class DivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '/'


    @share
    class IntegerDivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '//'


    @share
    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'


    @share
    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'


    @share
    class LessThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<'


    @share
    class LessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='


    @share
    class LogicalAndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '&'


    @share
    class LogicalOrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '|'


    @share
    class MapElement(BinaryExpression):
        __slots__      = (())
        display_name   = ':'
        is_right_brace = false


    @share
    class MemberExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '.'
        is_statement = false


    @share
    class ModulusExpression(BinaryExpression):
        __slots__    = (())
        display_name = '%'


    @share
    class MultiplyExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '*'


    @share
    class OrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'or'


    @share
    class PowerExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'power'


    @share
    class SubtractExpression(BinaryExpression):
        __slots__    = (())
        display_name = '-'


    Is_Not                    .expression_meta = static_method(conjure_compare_different)
    KeywordIn                 .expression_meta = static_method(conjure_compare_contains)
    KeywordIs                 .expression_meta = CompareIdentityExpression
    Not_In                    .expression_meta = static_method(conjure_compare_exclude)
    OperatorCompareEqual      .expression_meta = static_method(conjure_compare_equal)
    OperatorCompareNotEqual   .expression_meta = CompareNotEqualExpression
    OperatorDivide            .expression_meta = DivideExpression
    OperatorGreaterThan       .expression_meta = static_method(conjure_compare_greater_than)
    OperatorGreaterThanOrEqual.expression_meta = CompareGreaterThanOrEqualExpression
    OperatorIntegerDivide     .expression_meta = IntegerDivideExpression
    OperatorLessThan          .expression_meta = LessThanExpression
    OperatorLessThanOrEqual   .expression_meta = LessThanOrEqualExpression
    OperatorMinusSign         .expression_meta = SubtractExpression
    OperatorPercentSign       .expression_meta = ModulusExpression
    OperatorPlusSign          .expression_meta = static_method(conjure_add_expression)
    OperatorStarSign          .expression_meta = MultiplyExpression_1


    if __debug__:
        @share
        def dump_binary_expression_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_and_expression_1',     conjure_and_expression_1,
        'conjure_comma_expression_1',   conjure_comma_expression_1,
        'conjure_comprehension_if',     conjure_comprehension_if,
    )
