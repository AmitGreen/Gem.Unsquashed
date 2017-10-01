#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DefinitionHeader')
def gem():
    require_gem('Sapphire.Tree')


    conjure_triple_frill        = Shared.conjure_triple_frill           #   due to Privileged
    produce_conjure_triple__213 = Shared.produce_conjure_triple__213    #   due to Privileged


    class DefinitionHeader(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   Indented_Keyword
            'name',                     #   String
            'parameters',               #   Parameter_0 | Parameter_1 | Parameter_Many
        ))


        is_class_or_function_header = true
        is_statement_header         = true
        is_statement                = false


        def __init__(t, frill, name, parameters):
            t.frill      = frill
            t.name       = name
            t.parameters = parameters


        def  __repr__(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.frill, t.name, t.parameters)


        def count_newlines(t):
            return t.frill.count_newlines() + t.name.count_newlines() + t.parameters.count_newlines()


        def display_token(t):
            frill = t.frill

            if 0:
                comment = frill.comment

                if comment is no_comment:
                    return arrange('<%s +%d %s %s %s>',
                                   t.display_name,
                                   frill.a      .total,
                                   frill.b      .display_token(),
                                   t.name       .display_token(),
                                   t.parameters .display_token())

            return arrange('<%s +%d %s %s %s %s %s>',
                           t.display_name,
                           frill.a      .total,
                           frill.b      .display_token(),
                           t.name       .display_token(),
                           t.parameters .display_token(),
                           frill.c      .display_token())


        def dump_token(t, newline = true):
            assert newline is true

            frill       = t.frill
            #comment     = frill.comment
            indentation = frill.a

            #if comment is not no_comment:
            #    comment.dump_token()

            partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            frill.b.dump_token()
            t.name.dump_token()
            t.parameters.dump_token()
            r = frill.c.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.indentation

            
        def write(t, w):
            frill = t.frill

            w(frill.a.s + frill.b.s + t.name.s)
            t.parameters.write(w)
            w(frill.c.s)


    DefinitionHeader.k1 = DefinitionHeader.frill
    DefinitionHeader.k2 = DefinitionHeader.name
    DefinitionHeader.k3 = DefinitionHeader.parameters


    @privileged
    def produce_conjure_definition_header(name, Meta):
        conjure_triple__312 = produce_conjure_triple__213(name, Meta)


        def conjure_definition_header(indentation, keyword, name, parameters, colon_newline):
            return conjure_triple__312(
                       conjure_triple_frill(indentation, keyword, colon_newline),
                       name,
                       parameters,
                   )


        if __debug__:
            conjure_definition_header.__name__ = intern_arrange('conjure_%s', name)

        return conjure_definition_header


    class ClassHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'class-header'


    class FunctionHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'function-header'


    conjure_class_header    = produce_conjure_definition_header('class-header',    ClassHeader)
    conjure_function_header = produce_conjure_definition_header('function-header', FunctionHeader)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
