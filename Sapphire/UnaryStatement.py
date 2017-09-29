#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.UnaryStatement')
def gem():
    class ElseStatement(UnaryExpression):
        __slots__    = (())
        display_name = 'else-statement'
        frill        = conjure_indented_else_colon(
                           empty_indentation,
                           conjure_keyword_else('else'),
                           conjure_colon(': '),
                       )


        def display_token__frill(t):
            frill = t.frill

            return arrange('<else-statement+frill +%d %s %s %s>',
                           frill.a.total,
                           frill.b.display_token(),
                           frill.c.display_token(),
                           t.a.display_token())


        @property
        def indentation(t):
            return t.frill.a


    del Shared.conjure_indented_else_colon


    conjure_else_statement = produce_conjure_unary_expression('else-statement', ElseStatement)


    share(
        'conjure_else_statement',   conjure_else_statement,
    )
