#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DefinitionHeader')
def gem():
    require_gem('Sapphire.Tree')


    conjure_dual_frill          = Shared.conjure_dual_frill             #   due to privileged
    produce_conjure_triple__213 = Shared.produce_conjure_triple__213    #   due to privileged


    class DefinitionHeader(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   DualFrill
            'name',                     #   String
            'parameters',               #   Parameter_0 | Parameter_1 | Parameter_Many
        ))


        is_class_decorator_or_function_header = true
        is_statement_header                   = true
        is_statement                          = false


        def __init__(t, frill, name, parameters):
            t.frill      = frill
            t.name       = name
            t.parameters = parameters


        def  __repr__(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.frill, t.name, t.parameters)


        def add_comment(t, comment):
            assert comment is not no_comment

            frill   = t.frill
            frill_a = frill.a

            assert frill_a.comment is no_comment

            return t.conjure(
                       conjure_comment_indented_token(comment, frill_a.indentation, frill_a.keyword),
                       t.name,
                       t.parameters,
                       frill.b,
                   )


        def count_newlines(t):
            return t.frill.count_newlines() + t.name.count_newlines() + t.parameters.count_newlines()


        def display_token(t):
            frill   = t.frill
            frill_a = frill.a
            comment = frill_a.comment

            if comment is no_comment:
                return arrange('<%s +%d %s %s %s %s>',
                               t.display_name,
                               frill_a.indentation.total,
                               frill_a.keyword    .display_token(),
                               t.name             .display_token(),
                               t.parameters       .display_token(),
                               frill.b            .display_token())

            return arrange('<%s +%d %s %s %s %s %s>',
                           t.display_name,
                           frill_a.indentation.total,
                           comment            .display_token(),
                           frill_a.keyword    .display_token(),
                           t.name             .display_token(),
                           t.parameters       .display_token(),
                           frill.b            .display_token())



        def dump_token(t, newline = true):
            assert newline is true

            frill       = t.frill
            frill_a     = frill.a
            comment     = frill_a.comment
            indentation = frill_a.indentation

            if comment is not no_comment:
                comment.dump_token()

            partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            frill_a.keyword.dump_token()
            t.name.dump_token()
            t.parameters.dump_token()
            r = frill.b.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a.indentation

            
        def write(t, w):
            frill = t.frill

            w(frill.a.s + t.name.s)
            t.parameters.write(w)
            w(frill.b.s)


    DefinitionHeader.k1 = DefinitionHeader.frill
    DefinitionHeader.k2 = DefinitionHeader.name
    DefinitionHeader.k3 = DefinitionHeader.parameters


    @privileged
    def produce_conjure_definition_header(name, Meta):
        conjure_triple__312 = produce_conjure_triple__213(name, Meta)


        def conjure_definition_header(indented_keyword, name, parameters, colon_newline):
            return conjure_triple__312(
                       conjure_dual_frill(indented_keyword, colon_newline),
                       name,
                       parameters,
                   )


        if __debug__:
            conjure_definition_header.__name__ = intern_arrange('conjure_%s', name)

        return conjure_definition_header


    @share
    class ClassHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'class-header'


    @share
    class FunctionHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'function-header'


    conjure_class_header    = produce_conjure_definition_header('class-header',    ClassHeader)
    conjure_function_header = produce_conjure_definition_header('function-header', FunctionHeader)


    FunctionHeader.conjure = static_method(conjure_function_header)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
