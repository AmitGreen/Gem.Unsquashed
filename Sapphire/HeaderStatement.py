#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.HeaderStatement')
def gem():
    require_gem('Sapphire.Tree')


    class HeaderStatement(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   Indented_Keyword
            'name',                     #   String
            'parameters_colon',         #   Parameter_0 | Parameter_1 | Parameter_Colon_Many
        ))


        is_class_or_function_header = true
        is_statement_header         = true
        is_statement                = false


        def __init__(t, frill, name, parameters_colon):
            t.frill            = frill
            t.name             = name
            t.parameters_colon = parameters_colon


        def  __repr__(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.frill, t.name, t.parameters_colon)


        def count_newlines(t):
            return t.frill.count_newlines() + t.name.count_newlines() + t.parameters_colon.count_newlines()


        def display_token(t):
            frill = t.frill

            comment = frill.comment

            if comment is no_comment:
                return arrange('<%s +%d %s %s %s>',
                               t.display_name,
                               frill.indentation.total,
                               frill.keyword     .display_token(),
                               t.name            .display_token(),
                               t.parameters_colon.display_token())

            return arrange('<%s +%d %s %s %s %s>',
                           t.display_name,
                           frill.indentation.total,
                           frill.comment     .display_token(),
                           frill.keyword     .display_token(),
                           t.name            .display_token(),
                           t.parameters_colon.display_token())


        def dump_token(t, newline = true):
            assert newline is true

            frill       = t.frill
            comment     = frill.comment
            indentation = frill.indentation

            if comment is not no_comment:
                comment.dump_token()

            partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            frill.keyword.dump_token()
            t.name.dump_token()
            r = t.parameters_colon.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.indentation

            
        def write(t, w):
            w(t.frill.s + t.name.s)
            t.parameters_colon.write(w)


    HeaderStatement.k1 = HeaderStatement.frill
    HeaderStatement.k2 = HeaderStatement.name
    HeaderStatement.k3 = HeaderStatement.parameters_colon


    class ClassHeader(HeaderStatement):
        __slots__    = (())
        display_name = 'class-header'


    class FunctionHeader(HeaderStatement):
        __slots__    = (())
        display_name = 'function-header'


    conjure_class_header    = produce_conjure_triple__312('class-header',    ClassHeader)
    conjure_function_header = produce_conjure_triple__312('function-header', FunctionHeader)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
