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


    class ImportStatement(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'import-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_import('import ')),
                           empty_line_marker,
                       )


    class ReturnStatement(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'return-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(conjure_indentation('    '), conjure_keyword_return('return ')),
                           empty_line_marker,
                       )


    class WhileHeader(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'while-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_return('while ')),
                           empty_line_marker,
                       )


    conjure_decorator_header = produce_conjure_bookcase_expression('decorator-header', DecoratorHeader)
    conjure_import_statement = produce_conjure_bookcase_expression('import-statement', ImportStatement)
    conjure_return_statement = produce_conjure_bookcase_expression('return-statement', ReturnStatement)
    conjure_while_header     = produce_conjure_bookcase_expression('while-header',     WhileHeader)


    share(
        'conjure_decorator_header',     conjure_decorator_header,
        'conjure_import_statement',     conjure_import_statement,
        'conjure_return_statement',     conjure_return_statement,
        'conjure_while_header',         conjure_while_header,
    )
