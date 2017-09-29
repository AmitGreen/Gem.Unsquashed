#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class ExpressionStatement(BookcaseExpression):
        __slots__ = (())
        frill     = conjure_dual_frill(empty_indentation, empty_line_marker)


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


        @property
        def indentation(t):
            return t.frill.a


    class KeywordExpressionStatement(BookcaseExpression):
        __slots__ = (())


        def display_token(t):
            return arrange('<%s +%d %s>',
                           t.display_name,
                           t.frill.a.a.total,
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


    class AssertStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'assert-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           empty_line_marker,
                       )


    class DecoratorHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = '@-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_at_sign('@')),
                           empty_line_marker,
                       )


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
                           conjure_colon__line_marker(':\n'),
                       )


    class ExceptHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           conjure_colon__line_marker(':\n'),
                       )


    class IfHeader(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'if-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_if('if ')),
                           conjure_colon__line_marker(':\n'),
                       )


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
                           conjure_colon__line_marker(':\n'),
                       )


    class WithHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           conjure_colon__line_marker(':\n'),
                       )


    class YieldStatement_1(KeywordExpressionStatement):
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
    #  Derived from KeywordExpressionStatement
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
