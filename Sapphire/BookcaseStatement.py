#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class ExpressionStatement(BookcaseExpression):
        __slots__           = (())
        display_name        = 'expression-statement'
        frill               = conjure_xy_frill(empty_indentation, empty_line_marker)
        is_else_header      = false
        is_statement_header = false
        is_statement        = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return conjure_expression_statement__with_frill(
                       t.a,
                       conjure_commented_xy_frill(comment, frill.x, frill.y),
                   )


        def display_token(t):
            return arrange('<expression-statement +%d %s>', t.frill.x.total, t.a.display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<expression-statement+frill +%d %s %s>',
                           frill.x.total,
                           t.a    .display_token(),
                           frill.y.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.x.total)
                t.a.dump_token(f)
                r = frill.y.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.indent(arrange('<%s +%d', t.display_name, frill.x.total), '>'):
                comment.dump_token(f)
                t.a    .dump_token(f)
                frill.y.dump_token(f)


        @property
        def indentation(t):
            return t.frill.x


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.x.s)
            t.a.write(w)
            w(frill.y.s)


    [
        conjure_expression_statement, conjure_expression_statement__with_frill,
    ] = produce_conjure_bookcase_expression(
            'expression-statement',
            ExpressionStatement,
                                         
            produce_conjure_with_frill = 1,
        )


    share(
        'conjure_expression_statement',     conjure_expression_statement,
    )
