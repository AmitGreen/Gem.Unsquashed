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
            return arrange('<expression-statement +%d %s>', t.frill.a.total, t.a.display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<expression-statement+frill +%d %s %s>',
                           frill.a.total,
                           t.a    .display_token(),
                           frill.b.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s +%d ', t.display_name, frill.a.total)
            t.a.dump_token(f)
            r = frill.b.dump_token(f, false)

            if (r) and (newline):
                f.line('>')
                return false

            f.partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a


    conjure_expression_statement = produce_conjure_bookcase_expression('expression-statement', ExpressionStatement)


    share(
        'conjure_expression_statement',     conjure_expression_statement,
    )
