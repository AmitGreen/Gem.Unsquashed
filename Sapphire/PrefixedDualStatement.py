#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.PrefixedDualStatement')
def gem():
    require_gem('Sapphire.DualStatement')


    lookup_adjusted_meta        = Shared.lookup_adjusted_meta           #   Due to 'privileged'
    produce_conjure_dual_twig   = Shared.produce_conjure_dual_twig      #   Due to privileged
    produce_conjure_triple__312 = Shared.produce_conjure_triple__312    #   Due to privileged
    store_adjusted_meta         = Shared.store_adjusted_meta            #   Due to 'privileged'


    prefixed_dual_twig_cache  = {}
    lookup_prefixed_dual_twig = prefixed_dual_twig_cache.get
    store_prefixed_dual_twig  = prefixed_dual_twig_cache.__setitem__


    class ClassDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'class-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class DecoratedDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'decorated-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class ElseFragment(DualTwig):
        __slots__           = (())
        display_name        = 'else-fragment'
        is_else_header      = false
        is_statement_header = false
        is_statement        = false

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class ElseIfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'else-if-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class FunctionDefinition(DualTwig):
        __slots__           = (())
        display_name        = 'function-definition'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class IfStatement(DualTwig):
        __slots__           = (())
        display_name        = 'if-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


    class WhileStatement(DualTwig):
        __slots__           = (())
        display_name        = 'while-statement'
        is_else_header      = false
        is_statement_header = false
        is_statement        = true

        dump_token  = dump_token__ab
        indentation = indentation__a_indentation


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
                                       t.display_name.display_token(),
                                       t.prefix      .display_token(),
                                       t.a           .display_token(),
                                       t.b           .display_token())


                    def dump_token(t, f, newline = true):
                        assert newline is true

                        with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
                            t.prefix.dump_token(f)
                            t.a.dump_token(f)
                            t.b.dump_token(f)

                                        
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
            conjure_else_if_statement, conjure_prefixed_else_if_statement,
    ] = produce_conjure_dual_twig_functions('else-if-statement', ElseIfStatement)

    [
            conjure_function_definition, conjure_prefixed_function_definition,
    ] = produce_conjure_dual_twig_functions('function-definition', FunctionDefinition)

    [
            conjure_if_statement, conjure_prefixed_if_statement,
    ] = produce_conjure_dual_twig_functions('if-statement', IfStatement)

    [
            conjure_while_statement, conjure_prefixed_while_statement,
    ] = produce_conjure_dual_twig_functions('while-statement', WhileStatement)


    append_cache('#dual-twig', prefixed_dual_twig_cache)


    share(
        'conjure_class_definition',                 conjure_class_definition,
        'conjure_decorated_definition',             conjure_decorated_definition,
        'conjure_else_fragment',                    conjure_else_fragment,
        'conjure_else_if_statement',                conjure_else_if_statement,
        'conjure_function_definition',              conjure_function_definition,
        'conjure_if_statement',                     conjure_if_statement,
        'conjure_while_statement',                  conjure_while_statement,

        'conjure_prefixed_class_definition',        conjure_prefixed_class_definition,
        'conjure_prefixed_decorated_definition',    conjure_prefixed_decorated_definition,
        'conjure_prefixed_else_fragment',           conjure_prefixed_else_fragment,
        'conjure_prefixed_else_if_statement',       conjure_prefixed_else_if_statement,
        'conjure_prefixed_function_definition',     conjure_prefixed_function_definition,
        'conjure_prefixed_if_statement',            conjure_prefixed_if_statement,
        'conjure_prefixed_while_statement',         conjure_prefixed_while_statement,
    )
