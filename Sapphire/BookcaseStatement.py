#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class DecoratorHeader(BookcaseExpression):
        __slots__    = (())
        display_name = '@-header'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_at_sign('@')),
                           empty_line_marker,
                       )


        @property
        def indentation(t):
            my_line('%r', t.frill.a.a)

            return t.frill.a.a


    conjure_decorator_header = produce_conjure_bookcase_expression('decorator-header', DecoratorHeader)


    share(
        'conjure_decorator_header',     conjure_decorator_header,
    )
