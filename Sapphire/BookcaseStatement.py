#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class KeywordExpressionStatement_1(BookcaseExpression):
        __slots__ = (())


        def display_token(t):
            frill = t.frill

            return arrange('<%s +%d %s>',
                           t.display_name,
                           frill.a.a.total,
                           t.a.display_token())


        def display_token__frill(t):
            frill   = t.frill
            frill_a = frill.a

            return arrange('<%s+frill +%d %s %s %s>',
                           t.display_name,
                           frill_a.a.total,
                           frill.a.b.display_token(),
                           t.a    .display_token(),
                           frill.b.display_token())


        @property
        def indentation(t):
            return t.frill.a.a


    class DecoratorHeader(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = '@-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_at_sign('@')),
                           empty_line_marker,
                       )


    class ReturnStatement(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'return-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('return ')),
                           empty_line_marker,
                       )


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


    conjure_decorator_header   = produce_conjure_bookcase_expression     ('decorator-header', DecoratorHeader)
    conjure_from_statement     = produce_conjure_bookcase_dual_expression('from-statement',   StatementFromImport)
    conjure_return_statement_1 = produce_conjure_bookcase_expression     ('return-statement', ReturnStatement)


    share(
        'conjure_decorator_header',     conjure_decorator_header,
        'conjure_from_statement',       conjure_from_statement,
        'conjure_return_statement_1',   conjure_return_statement_1,
    )
