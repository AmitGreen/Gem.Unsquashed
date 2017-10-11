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

            indented_keyword = frill.v

            return arrange('<%s+frill +%d %s %s %s %s %s>',
                           t.display_name,
                           indented_keyword.a.total,
                           indented_keyword.b.display_token(),
                           t               .a.display_token(),
                           frill           .w.display_token(),
                           t               .b.display_token(),
                           frill           .x.display_token())


        def dump_token(t, f, newline = true):
            frill            = t.frill
            indented_keyword = frill.v

            f.partial('<%s +%d ', t.display_name, indented_keyword.a.total)

            indented_keyword.b.dump_token(f)
            t               .a.dump_token(f)
            frill           .w.dump_token(f)
            t               .b.dump_token(f)
            r = frill       .x.dump_token(f, false)

            return f.token_result(r, newline)


        def remove_comments(t):
            frill               = t.frill
            indented_keyword    = frill.v
            a                   = t.a
            b                   = t.b
            uncommented_keyword = t.uncommented_keyword
            uncommented_middle  = t.uncommented_middle
            uncommented_ending  = t.uncommented_ending

            indented_keyword__2 = (
                                      indented_keyword   if indented_keyword.token is uncommented_keyword else
                                      conjure_indented_keyword(indented_keyword.indentation, uncommented_keyword)
                                  )

            a__2 = a.remove_comments()
            b__2 = b.remove_comments()

            if (
                    indented_keyword is indented_keyword__2
                and a                is a__2
                and frill.w          is uncommented_middle
                and b                is b__2
                and frill.x          is uncommented_ending
            ):
                return t

            return t.conjure(indented_keyword__2, a__2, uncommented_middle, b__2, uncommented_ending)


        remove_comments__frill = remove_comments


        @property
        def indentation(t):
            return t.frill.v.a


    class AssertStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'assert-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           conjure_comma(', '),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


    @share
    class ExceptHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           conjure_keyword_as(' as '),
                           COLON__LINE_MARKER,
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

        uncommented_keyword = conjure_keyword_for('for ')
        uncommented_middle  = conjure_keyword_in(' in ')
        uncommented_ending  = COLON__LINE_MARKER
        frill               = conjure_vwx_frill(
                                  conjure_indented_token(empty_indentation, uncommented_keyword),
                                  uncommented_middle,
                                  uncommented_ending
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
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


    class RaiseStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           conjure_comma(', '),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


    @share
    class WithHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-2'

        uncommented_keyword = conjure_keyword_with('with ')
        uncommented_middle  = conjure_keyword_as(' as ')
        uncommented_ending  = COLON__LINE_MARKER
        frill               = conjure_vwx_frill(
                                  conjure_indented_token(empty_indentation, uncommented_keyword),
                                  uncommented_middle,
                                  uncommented_ending,
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


    ForHeader.conjure = static_method(conjure_for_header)


    share(
        'conjure_assert_statement_2',   conjure_assert_statement_2,
        'conjure_except_header_2',      conjure_except_header_2,
        'conjure_for_header',           conjure_for_header,
        'conjure_from_statement',       conjure_from_statement,
        'conjure_raise_statement_2',    conjure_raise_statement_2,
        'conjure_with_header_2',        conjure_with_header_2,
    )
