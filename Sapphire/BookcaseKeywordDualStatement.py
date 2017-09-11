#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseKeywordDualStatement')
def gem():
    require_gem('Sapphire.BookcaseDualExpression')


    class KeywordDualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.v.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill

            frill_v = frill.v

            return arrange('<%s+frill +%d %s %s %s %s %s>',
                           t.display_name,
                           frill_v.a.total,
                           frill_v.b.display_token(),
                           t.a      .display_token(),
                           frill.w  .display_token(),
                           t.b      .display_token(),
                           frill.x  .display_token())


        def dump_token(t, f, newline = true):
            frill   = t.frill
            frill_v = frill.v

            f.partial('<%s +%d ', t.display_name, frill_v.a.total)

            frill_v  .b.dump_token(f)
            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            r = frill.x.dump_token(f, false)

            return f.token_result(r, newline)


        @property
        def indentation(t):
            return t.frill.v.a


    class AssertStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'assert-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           conjure_comma(', '),
                           empty_line_marker,
                       )

        find_require_gem = find_require_gem__0


    @share
    class ExceptHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           conjure_keyword_as(' as '),
                           colon__empty_line_marker,
                       )

        is_any_except_or_finally = true
        is_statement             = false
        is_statement_header      = true
        split_comment            = 0

        add_comment = 0


    @share
    class ForHeader(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'for-header'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_for('for ')),
                           conjure_keyword_in(' in '),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 1

        add_comment = 0


    class StatementFromImport(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'from-statement'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_from('from ')),
                           conjure_keyword_import(' import '),
                           empty_line_marker,
                       )

        find_require_gem = find_require_gem__0


    class RaiseStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           conjure_comma(', '),
                           empty_line_marker,
                       )

        find_require_gem = find_require_gem__0


    @share
    class WithHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           conjure_keyword_as(' as '),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 1

        add_comment = 0


    conjure_assert_statement_2 = produce_conjure_bookcase_dual_expression('assert-statement-2', AssertStatement_2)
    conjure_except_header_2    = produce_conjure_bookcase_dual_expression('except-header2',     ExceptHeader_2)
    conjure_for_header         = produce_conjure_bookcase_dual_expression('for-header',         ForHeader)
    conjure_from_statement     = produce_conjure_bookcase_dual_expression('from-statement',     StatementFromImport)
    conjure_raise_statement_2  = produce_conjure_bookcase_dual_expression('raise-statement-2',  RaiseStatement_2)
    conjure_with_header_2      = produce_conjure_bookcase_dual_expression('with-header-2',      WithHeader_2)


    share(
        'conjure_assert_statement_2',   conjure_assert_statement_2,
        'conjure_except_header_2',      conjure_except_header_2,
        'conjure_for_header',           conjure_for_header,
        'conjure_from_statement',       conjure_from_statement,
        'conjure_raise_statement_2',    conjure_raise_statement_2,
        'conjure_with_header_2',        conjure_with_header_2,
    )
