#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    class DualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<%s+frill +%d %s %s %s %s>',
                           t.display_name,
                           frill.a.total,
                           t.a    .display_token(),
                           frill.b.display_token(),
                           t.b    .display_token(),
                           frill.c.display_token())


        @property
        def indentation(t):
            return t.frill.a


    class KeywordDualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.a.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill

            frill_a = frill.a

            return arrange('<%s+frill +%d %s %s %s %s %s>',
                           t.display_name,
                           frill_a.a.total,
                           frill_a.b.display_token(),
                           t.a      .display_token(),
                           frill.b  .display_token(),
                           t.b      .display_token(),
                           frill.c  .display_token())


        @property
        def indentation(t):
            return t.frill.a.a


    class StatementAssign_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-statement'
        frill        = conjure_triple_frill(
                           empty_indentation,
                           conjure_equal_sign(' = '),
                           empty_line_marker,
                       )


    class StatementFromImport(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'from-statement'
        frill        = conjure_triple_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('from ')),
                           conjure_keyword_import(' import '),
                           empty_line_marker,
                       )


    conjure_assign_1       = produce_conjure_bookcase_dual_expression('assign-1',       StatementAssign_1)
    conjure_from_statement = produce_conjure_bookcase_dual_expression('from-statement', StatementFromImport)


    share(
        'conjure_assign_1',         conjure_assign_1,
        'conjure_from_statement',   conjure_from_statement,
    )