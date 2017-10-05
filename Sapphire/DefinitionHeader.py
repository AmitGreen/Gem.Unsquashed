#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DefinitionHeader')
def gem():
    require_gem('Sapphire.Tree')


    conjure_xy_frill            = Shared.conjure_xy_frill               #   due to privileged
    produce_conjure_triple__213 = Shared.produce_conjure_triple__213    #   due to privileged


    class DefinitionHeader(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   XY_Frill | Commented_XY_Frill
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
            frill = t.frill

            assert frill.comment is 0

            return t.conjure_with_frill(
                       conjure_commented_xy_frill(comment, frill.x, frill.y),
                       t.name,
                       t.parameters,
                   )


        def count_newlines(t):
            return t.frill.count_newlines() + t.name.count_newlines() + t.parameters.count_newlines()


        def display_token(t):
            frill          = t.frill
            comment        = frill.comment
            indented_token = frill.x

            return arrange('<%s +%d%s %s %s %s %s>',
                           t.display_name,
                           indented_token.indentation.total,
                           (''   if  comment is 0 else   ' ' + comment.display_token()),
                           indented_token.token.display_token(),
                           t.name              .display_token(),
                           t.parameters        .display_token(),
                           frill.b             .display_token())



        def dump_token(t, f, newline = true):
            assert newline is true

            frill          = t.frill
            comment        = frill.comment
            indented_token = frill.x

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, indented_token.indentation.total)
                indented_token.token.dump_token(f)
                t.name.dump_token(f)
                t.parameters.dump_token(f)
                r = frill.y.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.indent(arrange('<%s +%d', t.display_name, indented_token.indentation.total), '>'):
                comment.dump_token(f)
                indented_token.token.dump_token(f)
                t.name.dump_token(f)
                t.parameters.dump_token(f)
                frill.y.dump_token(f)


        @property
        def indentation(t):
            return t.frill.x.indentation

            
        def write(t, w):
            frill = t.frill

            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.x.s + t.name.s)
            t.parameters.write(w)
            w(frill.y.s)


    DefinitionHeader.k1 = DefinitionHeader.frill
    DefinitionHeader.k2 = DefinitionHeader.name
    DefinitionHeader.k3 = DefinitionHeader.parameters


    @privileged
    def produce_conjure_definition_header(name, Meta):
        conjure_triple__312 = produce_conjure_triple__213(name, Meta)


        def conjure_definition_header(indented_keyword, name, parameters, colon_newline):
            return conjure_triple__312(
                       conjure_xy_frill(indented_keyword, colon_newline),
                       name,
                       parameters,
                   )


        if __debug__:
            conjure_definition_header.__name__ = intern_arrange('conjure_%s', name)

        return (( conjure_definition_header, static_method(conjure_triple__312) ))


    @share
    class ClassHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'class-header'


    @share
    class FunctionHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'function-header'


    [
        conjure_class_header, ClassHeader.conjure_with_frill,
    ] = produce_conjure_definition_header(
            'class-header',
            ClassHeader,
        )

    [
        conjure_function_header, FunctionHeader.conjure_with_frill,
    ] = produce_conjure_definition_header(
            'function-header',
            FunctionHeader,
        )


    FunctionHeader.conjure = static_method(conjure_function_header)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
