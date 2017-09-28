#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    class StatementFromImport(BookcaseDualExpression):
        __slots__    = (())
        display_name = 'from-statement'
        frill        = conjure_triple_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('from ')),
                           conjure_keyword_import(' import '),
                           empty_line_marker,
                       )


        def display_token(t):
            return arrange('<from-statement +%d %s %s>',
                           t.frill.a.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill
            frill_a = frill.a

            return arrange('<from-statement+frill +%d %s %s %s %s %s>',
                           frill_a.a.total,
                           frill_a.b.display_token(),
                           t.a      .display_token(),
                           frill.b  .display_token(),
                           t.b      .display_token(),
                           frill.c  .display_token())


        @property
        def indentation(t):
            return t.frill.a.a


    conjure_from_statement = produce_conjure_bookcase_dual_expression('from-statement', StatementFromImport)


    share(
        'conjure_from_statement',   conjure_from_statement,
    )
