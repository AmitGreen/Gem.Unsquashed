#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseKeywordStatement')
def gem():
    class KeywordExpressionStatement(BookcaseExpression):
        __slots__           = (())
        is_statement_header = false
        is_statement        = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return t.conjure_with_frill(
                       t.a,
                       conjure_commented__indented_keyword__x__frill(comment, frill.indented_keyword, frill.x),
                   )


        def display_token(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s +%d%s %s>',
                           t.display_name,
                           frill.indented_keyword.indentation.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a.display_token())


        def display_token__frill(t):
            frill            = t.frill
            comment          = frill.comment
            indented_keyword = frill.indented_keyword

            return arrange('<%s+frill +%d%s %s %s %s>',
                           t.display_name,
                           indented_keyword.indentation.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           indented_keyword.keyword.display_token(),
                           t.a                     .display_token(),
                           frill.x                 .display_token())


        def dump_token(t, f, newline = true):
            assert newline is true

            frill            = t.frill
            comment          = frill.comment
            indented_keyword = frill.indented_keyword

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, indented_keyword.indentation.total)

                indented_keyword.keyword.dump_token(f)
                t.a.dump_token(f)
                r = frill.x.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.indent(arrange('<%s +%d ', t.display_name, indented_keyword.indentation.total), '>'):
                comment.dump_token(f)
                indented_keyword.keyword.dump_token(f)
                t.a.dump_token(f)
                frill.x.dump_token(f, false)

            return false


        @property
        def indentation(t):
            return t.frill.indented_keyword.indentation


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.indented_keyword.s)
            t.a.write(w)
            w(frill.x.s)


    class AssertStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'assert-1'
        frill        = conjure__indented_keyword__x__frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           empty_line_marker,
                       )


    @share
    class DecoratorHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = '@-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_at_sign('@')),
                           empty_line_marker,
                       )

        is_class_decorator_or_function_header = true
        is_decorator_header                   = true
        is_statement                          = false
        is_statement_header                   = true


    class DeleteStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'delete-statement-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_delete('del ')),
                           empty_line_marker,
                       )


    class ElseIfHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'else-if-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_else_if('elif ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class ExceptHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class IfHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'if-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_if('if ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class ImportStatement(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'import-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_import('import ')),
                           empty_line_marker,
                       )


    class RaiseStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_raise('raise ')),
                           empty_line_marker,
                       )


    class ReturnStatement(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'return-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('return ')),
                           empty_line_marker,
                       )


    class WhileHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'while-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_while('while ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class WithHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class YieldStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'yield-statement-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_yield('yield ')),
                           empty_line_marker,
                       )


    [
        conjure_assert_statement_1, AssertStatement_1.conjure_with_frill,
    ] = produce_conjure_bookcase_expression(
            'assert-statement-1',
            AssertStatement_1,

            conjure_dual_frill         = conjure__indented_keyword__x__frill,
            produce_conjure_with_frill = true,
        )


    conjure_decorator_header   = produce_conjure_bookcase_expression('decorator-header',   DecoratorHeader)
    conjure_delete_header      = produce_conjure_bookcase_expression('delete-header',      DeleteStatement_1)
    conjure_else_if_header     = produce_conjure_bookcase_expression('else-if-header',     ElseIfHeader)
    conjure_except_header_1    = produce_conjure_bookcase_expression('except-header-1',    ExceptHeader_1)
    conjure_if_header          = produce_conjure_bookcase_expression('if-header',          IfHeader)
    conjure_import_statement   = produce_conjure_bookcase_expression('import-statement',   ImportStatement)
    conjure_raise_statement_1  = produce_conjure_bookcase_expression('raise-statement-1',  RaiseStatement_1)
    conjure_return_statement   = produce_conjure_bookcase_expression('return-statement',   ReturnStatement)
    conjure_while_header       = produce_conjure_bookcase_expression('while-header',       WhileHeader)
    conjure_with_header_1      = produce_conjure_bookcase_expression('with-header-1',      WithHeader_1)
    conjure_yield_statement_1  = produce_conjure_bookcase_expression('yield-statement-1',  YieldStatement_1)


    share(
        'conjure_assert_statement_1',       conjure_assert_statement_1,
        'conjure_decorator_header',         conjure_decorator_header,
        'conjure_delete_header',            conjure_delete_header,
        'conjure_else_if_header',           conjure_else_if_header,
        'conjure_except_header_1',          conjure_except_header_1,
        'conjure_if_header',                conjure_if_header,
        'conjure_import_statement',         conjure_import_statement,
        'conjure_raise_statement_1',        conjure_raise_statement_1,
        'conjure_return_statement',         conjure_return_statement,
        'conjure_while_header',             conjure_while_header,
        'conjure_with_header_1',            conjure_with_header_1,
        'conjure_yield_statement_1',        conjure_yield_statement_1,
    )
