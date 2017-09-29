#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    require_gem('Sapphire.BookcaseDualExpression')


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


    class AssertStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'assert-2'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           conjure_comma(', '),
                           empty_line_marker,
                       )


    class AssignStatement_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-1'
        frill        = conjure_triple_frill(
                           empty_indentation,
                           conjure_equal_sign(' = '),
                           empty_line_marker,
                       )


    class ExceptHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-2'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           conjure_keyword_as(' as '),
                           conjure_colon__line_marker(':\n'),
                       )


    class ForHeader(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'for-header'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_for('for ')),
                           conjure_keyword_in(' in '),
                           conjure_colon__line_marker(':\n'),
                       )


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_triple_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           empty_line_marker,
                       )


    class StatementFromImport(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'from-statement'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_from('from ')),
                           conjure_keyword_import(' import '),
                           empty_line_marker,
                       )


    class RaiseStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement-2'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           conjure_comma(', '),
                           empty_line_marker,
                       )


    class WithHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-2'
        frill        = conjure_triple_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           conjure_keyword_as(' as '),
                           conjure_colon__line_marker(':\n'),
                       )


    conjure_assert_statement_2 = produce_conjure_bookcase_dual_expression('assert-statement-2', AssertStatement_2)
    conjure_assign_1           = produce_conjure_bookcase_dual_expression('assign-1',           AssignStatement_1)
    conjure_except_header_2    = produce_conjure_bookcase_dual_expression('assign-1',           ExceptHeader_2)
    conjure_for_header         = produce_conjure_bookcase_dual_expression('for-header',         ForHeader)
    conjure_from_statement     = produce_conjure_bookcase_dual_expression('from-statement',     StatementFromImport)
    conjure_modify_statement   = produce_conjure_bookcase_dual_expression('modify-statement',   ModifyStatement)
    conjure_raise_statement_2  = produce_conjure_bookcase_dual_expression('raise-statement-2',  RaiseStatement_2)
    conjure_with_header_2      = produce_conjure_bookcase_dual_expression('with-header-2',      WithHeader_2)


    share(
        'conjure_assert_statement_2',   conjure_assert_statement_2,
        'conjure_assign_1',             conjure_assign_1,
        'conjure_except_header_2',      conjure_except_header_2,
        'conjure_for_header',           conjure_for_header,
        'conjure_from_statement',       conjure_from_statement,
        'conjure_modify_statement',     conjure_modify_statement,
        'conjure_raise_statement_2',    conjure_raise_statement_2,
        'conjure_with_header_2',        conjure_with_header_2,
    )
