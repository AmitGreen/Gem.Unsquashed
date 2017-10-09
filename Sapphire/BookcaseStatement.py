#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseStatement')
def gem():
    class ExpressionStatement(BookcaseExpression):
        __slots__                  = (())
        display_name               = 'expression-statement'
        frill                      = conjure_vw_frill(empty_indentation, empty_line_marker)
        is_any_else                = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return conjure_expression_statement__with_frill(
                       t.a,
                       conjure_commented_vw_frill(comment, frill.v, frill.w),
                   )


        def display_token(t):
            return arrange('<expression-statement +%d %s>', t.frill.v.total, t.a.display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<expression-statement+frill +%d %s %s>',
                           frill.v.total,
                           t.a    .display_token(),
                           frill.w.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)
                t.a        .dump_token(f)
                r = frill.w.dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d', t.display_name, frill.v.total), '>'):
                comment.dump_token(f)
                t.a    .dump_token(f)
                frill.w.dump_token(f)


        @property
        def indentation(t):
            return t.frill.v


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


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
