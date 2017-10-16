#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.PrefixedDualStatement')
def gem():
    require_gem('Sapphire.DualStatement')
    require_gem('Sapphire.DumpToken')


    dump_token                  = Shared.dump_token                     #   due to privileged
    lookup_adjusted_meta        = Shared.lookup_adjusted_meta           #   due to privileged
    produce_conjure_dual_twig   = Shared.produce_conjure_dual_twig      #   due to privileged
    produce_conjure_triple__312 = Shared.produce_conjure_triple__312    #   due to privileged
    store_adjusted_meta         = Shared.store_adjusted_meta            #   due to privileged


    prefixed_dual_twig_cache  = {}
    lookup_prefixed_dual_twig = prefixed_dual_twig_cache.get
    store_prefixed_dual_twig  = prefixed_dual_twig_cache.__setitem__


    def find_require_gem__b(t, e):
        t.b.find_require_gem(e)


    @privileged
    def produce_transform__a__b_with_indentation(name, conjure):
        def transform(t, vary):
            a = t.a
            b = t.b

            a__2 = a.transform(vary)

            if 'clique':
                previous = vary.push_indentation()

                b__2 = b.transform(vary)

                vary.pop_indentation(previous)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)

        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    def transform__prefix__ab(t, vary):
        prefix = t.prefix
        a      = t.a
        b      = t.b

        prefix__2 = prefix.transform(vary)
        a__2      = a     .transform(vary)
        b__2      = b     .transform(vary)

        if (prefix is prefix__2) and (a is a__2) and (b is b__2):
            return t

        if prefix__2 is 0:
            return t.conjure(a__2, b__2)

        return t.conjure_prefixed_dual(prefix__2, a__2, b__2)


    def transform__prefix__a__b_with_indentation(t, vary):
        prefix = t.prefix
        a      = t.a
        b      = t.b

        prefix__2 = prefix.transform(vary)
        a__2      = a     .transform(vary)

        if 'clique':
            previous = vary.push_indentation()

            b__2 = b.transform(vary)

            vary.pop_indentation(previous)

        if (prefix is prefix__2) and (a is a__2) and (b is b__2):
            return t

        if prefix__2 is 0:
            return t.conjure(a__2, b__2)

        return t.conjure_prefixed_dual(prefix__2, a__2, b__2)


    class ClassDefinition(DualTwig):
        __slots__                  = (())
        display_name               = 'class-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#class-definition'

        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    class DecoratedDefinition(DualTwig):
        __slots__                  = (())
        display_name               = 'decorated-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_decorated_definition    = true
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#decorated-definition'

        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class ElseFragment(DualTwig):
        __slots__                  = (())
        display_name               = 'else-fragment'
        is_any_else                = true
        is_any_except_or_finally   = false
        is_else_fragment           = true
        is_else_header_or_fragment = true
        is_statement               = false
        is_statement_header        = false
        prefix                     = 0
        prefixed_display_name      = 'prefixed-else-fragment'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class ElseIfFragment(DualTwig):
        __slots__                  = (())
        display_name               = 'else-if-fragment'
        is_any_else                = true
        is_any_except_or_finally   = false
        is_else_fragment           = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = 'prefixed-else-if-fragment'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class ExceptFragment(DualTwig):
        __slots__                  = (())
        display_name               = 'except-fragment'
        is_any_else                = false
        is_any_except_or_finally   = true
        is_else_header_or_fragment = false
        is_finally_fragment        = false
        is_statement               = false
        is_statement_header        = false
        prefix                     = 0
        prefixed_display_name      = 'prefixed-except-fragment'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class FinallyFragment(DualTwig):
        __slots__                  = (())
        display_name               = 'finally-fragment'
        is_any_else                = false
        is_any_except_or_finally   = true
        is_else_header_or_fragment = false
        is_finally_fragment        = true
        is_statement               = false
        is_statement_header        = false
        prefix                     = 0
        prefixed_display_name      = 'prefixed-finally-fragment'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    class ForStatement(DualTwig):
        __slots__                  = (())
        display_name               = 'for-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#for-statement'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    class FunctionDefinition(DualTwig):
        __slots__                  = (())
        display_name               = 'function-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_function_definition     = true
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#function-definition'

        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class IfStatement(DualTwig):
        __slots__                  = (())
        display_name               = 'if-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = true
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#if-statement'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @share
    class TryStatement(DualTwig):
        __slots__                    = (())
        display_name                 = 'try-statement'
        is_any_except_or_finally     = false
        is_finaly_header_or_fragment = false
        is_statement_header          = true
        is_statement                 = true
        prefix                     = 0
        prefixed_display_name        = '#try-statement'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    class WhileStatement(DualTwig):
        __slots__                  = (())
        display_name               = 'while-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#while-statement'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    class WithStatement(DualTwig):
        __slots__                  = (())
        display_name               = 'with-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#with-statement'
        split_comment              = 0

        add_comment      = 0
        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__b
        indentation      = indentation__a_indentation


    @privileged
    def produce_conjure_dual_twig_functions(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_PrefixedDualTwig(prefix, a, b):
            PrefixedDualTwig = lookup_adjusted_meta(Meta)

            if PrefixedDualTwig is none:
                class PrefixedDualTwig(Meta):
                    __slots__ = ((
                        'prefix',                #   Comment* | EmptyLine | CommentSuite | EmptyLineSuite | MixedSuite
                    ))


                    def __init__(t, prefix, a, b):
                        t.prefix = prefix
                        t.a      = a
                        t.b      = b


                    def __repr__(t):
                        return arrange('<%s %r %r %r>', t.__class__.__name__, t.prefix, t.a, t.b)


                    def count_newlines(t):
                        return t.prefix.count_newlines() + t.a.count_newlines() + t.b.count_newlines()


                    def display_token(t):
                        return arrange('<%s %r %r %r>',
                                       t.prefixed_display_name,
                                       t.prefix.display_token(),
                                       t.a     .display_token(),
                                       t.b     .display_token())


                    def dump_token(t, f, newline = true):
                        assert newline is true

                        with f.indent(arrange('<%s +%d', t.prefixed_display_name, t.a.indentation.total), '>'):
                            t.prefix.dump_token(f)
                            t.a.dump_token(f)
                            t.b.dump_token(f)


                    transform = (
                                    transform__prefix__ab   if Meta is DecoratedDefinition else
                                    transform__prefix__a__b_with_indentation
                                )


                    def write(t, w):
                        t.prefix.write(w)
                        t.a     .write(w)
                        t.b     .write(w)


                PrefixedDualTwig.k3 = PrefixedDualTwig.prefix

                if __debug__:
                    PrefixedDualTwig.__name__ = intern_arrange('Prefixed%s', Meta.__name__)

                store_adjusted_meta(Meta, PrefixedDualTwig)

            return PrefixedDualTwig(prefix, a, b)


        return ((
                   produce_conjure_dual_twig(name, Meta),
                   produce_conjure_triple__312(
                       name,
                       conjure_PrefixedDualTwig,
                       prefixed_dual_twig_cache,
                       lookup_prefixed_dual_twig,
                       store_prefixed_dual_twig,
                  ),
               ))


    [
            conjure_class_definition, conjure_prefixed_class_definition,
    ] = produce_conjure_dual_twig_functions('class-definition',ClassDefinition)

    [
            conjure_decorated_definition, conjure_prefixed_decorated_definition,
    ] = produce_conjure_dual_twig_functions('decorated-definition', DecoratedDefinition)

    [
            conjure_else_fragment, conjure_prefixed_else_fragment,
    ] = produce_conjure_dual_twig_functions('else-fragment', ElseFragment)

    [
            conjure_else_if_fragment, conjure_prefixed_else_if_fragment,
    ] = produce_conjure_dual_twig_functions('else-if-statement', ElseIfFragment)

    [
            conjure_except_fragment, conjure_prefixed_except_fragment,
    ] = produce_conjure_dual_twig_functions('except-fragment', ExceptFragment)

    [
            conjure_finally_fragment, conjure_prefixed_finally_fragment,
    ] = produce_conjure_dual_twig_functions('finally-fragment', FinallyFragment)

    [
            conjure_for_statement, conjure_prefixed_for_statement,
    ] = produce_conjure_dual_twig_functions('for-statement', ForStatement)

    [
            conjure_function_definition, conjure_prefixed_function_definition,
    ] = produce_conjure_dual_twig_functions('function-definition', FunctionDefinition)

    [
            conjure_if_statement, conjure_prefixed_if_statement,
    ] = produce_conjure_dual_twig_functions('if-statement', IfStatement)

    [
            conjure_try_statement, conjure_prefixed_try_statement,
    ] = produce_conjure_dual_twig_functions('try-statement', TryStatement)

    [
            conjure_while_statement, conjure_prefixed_while_statement,
    ] = produce_conjure_dual_twig_functions('while-statement', WhileStatement)

    [
            conjure_with_statement, conjure_prefixed_with_statement,
    ] = produce_conjure_dual_twig_functions('with-statement', WithStatement)


    DecoratedDefinition.conjure = static_method(conjure_decorated_definition)
    ElseFragment       .conjure = static_method(conjure_else_fragment)
    ExceptFragment     .conjure = static_method(conjure_except_fragment)
    ForStatement       .conjure = static_method(conjure_for_statement)
    FunctionDefinition .conjure = static_method(conjure_function_definition)
    IfStatement        .conjure = static_method(conjure_if_statement)
    TryStatement       .conjure = static_method(conjure_try_statement)
    WithStatement      .conjure = static_method(conjure_with_statement)

    ExceptFragment     .conjure_prefixed_dual = static_method(conjure_prefixed_except_fragment)
    DecoratedDefinition.conjure_prefixed_dual = static_method(conjure_prefixed_decorated_definition)
    FunctionDefinition .conjure_prefixed_dual = static_method(conjure_prefixed_function_definition)



    #
    #   .transform
    #
    ClassDefinition.transform = produce_transform__a__b_with_indentation('class_definition', conjure_class_definition)

    DecoratedDefinition.transform = produce_transform__ab('decorated-definition', conjure_decorated_definition)

    ElseFragment   .transform = produce_transform__a__b_with_indentation('else_fragment',    conjure_else_fragment)
    ElseIfFragment .transform = produce_transform__a__b_with_indentation('else_if_fragment', conjure_else_if_fragment)
    ExceptFragment .transform = produce_transform__a__b_with_indentation('except_fragment',  conjure_except_fragment)
    FinallyFragment.transform = produce_transform__a__b_with_indentation('finally_fragment', conjure_finally_fragment)
    ForStatement   .transform = produce_transform__a__b_with_indentation('for_statement',    conjure_for_statement)

    FunctionDefinition.transform = produce_transform__a__b_with_indentation(
                                       'function_Definition',
                                       conjure_function_definition,
                                   )

    IfStatement   .transform = produce_transform__a__b_with_indentation('if_statement',    conjure_if_statement)
    TryStatement  .transform = produce_transform__a__b_with_indentation('try_statement',   conjure_try_statement)
    WhileStatement.transform = produce_transform__a__b_with_indentation('while_statement', conjure_while_statement)
    WithStatement .transform = produce_transform__a__b_with_indentation('with_statement',  conjure_with_statement)


    append_cache('#dual-twig', prefixed_dual_twig_cache)


    share(
        'conjure_class_definition',                 conjure_class_definition,
        'conjure_decorated_definition',             conjure_decorated_definition,
        'conjure_for_statement',                    conjure_for_statement,
        'conjure_else_fragment',                    conjure_else_fragment,
        'conjure_else_if_fragment',                 conjure_else_if_fragment,
        'conjure_except_fragment',                  conjure_except_fragment,
        'conjure_finally_fragment',                 conjure_finally_fragment,
        'conjure_function_definition',              conjure_function_definition,
        'conjure_if_statement',                     conjure_if_statement,
        'conjure_try_statement',                    conjure_try_statement,
        'conjure_while_statement',                  conjure_while_statement,
        'conjure_with_statement',                   conjure_with_statement,

        'conjure_prefixed_class_definition',        conjure_prefixed_class_definition,
        'conjure_prefixed_decorated_definition',    conjure_prefixed_decorated_definition,
        'conjure_prefixed_else_fragment',           conjure_prefixed_else_fragment,
        'conjure_prefixed_else_if_fragment',        conjure_prefixed_else_if_fragment,
        'conjure_prefixed_except_fragment',         conjure_prefixed_except_fragment,
        'conjure_prefixed_finally_fragment',        conjure_prefixed_finally_fragment,
        'conjure_prefixed_for_statement',           conjure_prefixed_for_statement,
        'conjure_prefixed_function_definition',     conjure_prefixed_function_definition,
        'conjure_prefixed_if_statement',            conjure_prefixed_if_statement,
        'conjure_prefixed_try_statement',           conjure_prefixed_try_statement,
        'conjure_prefixed_while_statement',         conjure_prefixed_while_statement,
        'conjure_prefixed_with_statement',          conjure_prefixed_with_statement,
    )
