#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class ExpressionStatement(BookcaseExpression):
        __slots__           = (())
        display_name        = 'expression-statement'
        frill               = conjure_dual_frill(empty_indentation, empty_line_marker)
        is_statement_header = false
        is_statement        = true


        def display_token(t):
            return arrange('<expression-statement +%d %s>',
                           t.frill.a.total,
                           t.a.display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<expression-statement+frill +%d %s %s>',
                           frill.a.total,
                           t.a    .display_token(),
                           frill.b.display_token())


        def dump_token(t, newline = true):
            frill       = t.frill
            indentation = frill.a

            partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            t.a.dump_token()
            r = frill.b.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a


    class CommentedKeywordExpressionStatement(BookcaseExpression):
        __slots__           = (())
        is_statement_header = false
        is_statement        = true


        def add_comment(t, comment):
            assert comment is not no_comment

            frill   = t.frill
            frill_a = frill.a

            assert frill_a.comment is no_comment

            return t.conjure(
                       conjure_comment_indented_token(comment, frill_a.indentation, frill_a.keyword),
                       t.a,
                       frill.b,
                   )

        def display_token(t):
            frill   = t.frill
            frill_a = frill.a
            comment = frill_a.comment

            if comment is no_comment:
                return arrange('<%s +%d %s>',
                               t.display_name,
                               frill_a.indentation.total,
                               t.a.display_token())

            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           frill_a.indentation.total,
                           comment.display_token(),
                           t.a.display_token())


        def display_token__frill(t):
            frill       = t.frill
            frill_a     = frill.a
            comment     = frill_a.comment
            indentation = frill_a.indentation

            if comment is no_comment:
                return arrange('%s<%s+frill +%d %s %s %s>',
                               indentation.s,
                               t.display_name,
                               indentation.total,
                               frill_a.keyword.display_token(),
                               t.a            .display_token(),
                               frill.b        .display_token())

            return arrange('%s<%s+frill +%d %s %s %s %s %s>',
                           indentation.s,
                           t.display_name,
                           indentation.total,
                           comment        .display_token(),
                           frill_a.keyword.display_token(),
                           t.a            .display_token(),
                           frill.b        .display_token())


        def dump_token(t, newline = true):
            assert newline is true

            frill       = t.frill
            frill_a     = frill.a
            comment     = frill_a.comment
            indentation = frill_a.indentation

            partial('%s<%s +%d', indentation.s, t.display_name, indentation.total)

            if comment is no_comment:
                partial(' ')
            else:
                line()
                frill_a.comment.dump_token()
                partial(indentation.s)

            frill.a.keyword.dump_token()
            t.a.dump_token()
            r = frill.b.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a.indentation


    class AssertStatement_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'assert-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           empty_line_marker,
                       )


    @share
    class DecoratorHeader(CommentedKeywordExpressionStatement):
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


    class DeleteStatement_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'delete-statement-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_delete('del ')),
                           empty_line_marker,
                       )


    class ElseIfHeader(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'else-if-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_else_if('elif ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class ExceptHeader_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class IfHeader(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'if-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_if('if ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class ImportStatement(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'import-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_import('import ')),
                           empty_line_marker,
                       )


    class RaiseStatement_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_raise('raise ')),
                           empty_line_marker,
                       )


    class ReturnStatement(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'return-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('return ')),
                           empty_line_marker,
                       )


    class WhileHeader(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'while-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_while('while ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class WithHeader_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           colon__empty_line_marker,
                       )

        is_statement        = false
        is_statement_header = true


    class YieldStatement_1(CommentedKeywordExpressionStatement):
        __slots__    = (())
        display_name = 'yield-statement-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_yield('yield ')),
                           empty_line_marker,
                       )


    #
    #  Derived from BookcaseExpression
    #
    conjure_expression_statement = produce_conjure_bookcase_expression('expression-statement', ExpressionStatement)


    #
    #  Derived from CommentedKeywordExpressionStatement
    #
    conjure_assert_statement_1 = produce_conjure_bookcase_expression('assert-statement-1', AssertStatement_1)
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


    DecoratorHeader.conjure = static_method(conjure_decorator_header)


    share(
        'conjure_assert_statement_1',       conjure_assert_statement_1,
        'conjure_decorator_header',         conjure_decorator_header,
        'conjure_delete_header',            conjure_delete_header,
        'conjure_else_if_header',           conjure_else_if_header,
        'conjure_except_header_1',          conjure_except_header_1,
        'conjure_expression_statement',     conjure_expression_statement,
        'conjure_if_header',                conjure_if_header,
        'conjure_import_statement',         conjure_import_statement,
        'conjure_raise_statement_1',        conjure_raise_statement_1,
        'conjure_return_statement',         conjure_return_statement,
        'conjure_while_header',             conjure_while_header,
        'conjure_with_header_1',            conjure_with_header_1,
        'conjure_yield_statement_1',        conjure_yield_statement_1,
    )
