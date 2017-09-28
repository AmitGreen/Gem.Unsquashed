#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class KeywordExpressionStatement_1(BookcaseExpression):
        __slots__ = (())


        def display_token(t):
            frill = t.frill

            return arrange('<+%d %s %s %s %s>',
                           frill.a.a.total,
                           t.display_name,
                           frill.a.b.display_token(),
                           t.a.display_token(),
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


    class ReturnStatement_1(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'return-statement-1'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_return('return')),
                           empty_line_marker,
                       )


    conjure_decorator_header   = produce_conjure_bookcase_expression('decorator-header', DecoratorHeader)
    conjure_return_statement_1 = produce_conjure_bookcase_expression('return-1',         ReturnStatement_1)


    share(
        'conjure_decorator_header',     conjure_decorator_header,
        'conjure_return_statement_1',   conjure_return_statement_1,
    )
