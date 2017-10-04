#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    require_gem('Sapphire.BookcaseDualExpression')


    class DualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        is_statement_header = false
        is_statement        = true


        def add_comment(t, comment):
            assert comment is not no_comment

            frill = t.frill

            assert frill.comment is no_comment

            return t.conjure_triple(
                       t.a,
                       t.b,
                       conjure_commented_dual_expression_statement_frill(
                           comment,
                           frill.indentation,
                           frill.assign_operator,
                           frill.line_marker,
                       ),
                   )


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.indentation.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s+frill +%d%s %s %s %s %s>',
                           t.display_name,
                           frill.indentation.total,
                           (''   if comment is no_comment else   ' ' + comment.display_token()),
                           t.a                  .display_token(),
                           frill.assign_operator.display_token(),
                           t.b                  .display_token(),
                           frill.line_marker    .display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment     = frill.comment
            indentation = frill.indentation

            if comment is no_comment:
                f.partial('<%s +%d ', t.display_name, indentation.total)
                t.a.dump_token(f)
                frill.assign_operator.dump_token(f)
                t.b.dump_token(f)
                r = frill.line_marker.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.indent(arrange('<%s +%d ', t.display_name, frill.indentation.total), '>'):
                comment.dump_token(f)
                t.a.dump_token(f)
                frill.assign_operator.dump_token(f)
                t.b.dump_token(f)
                frill.line_marker.dump_token(f)

            return false


        @property
        def indentation(t):
            return t.frill.indentation


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not no_comment:
                comment.write(w)

            w(frill.indentation.s)
            t.a.write(w)
            w(frill.assign_operator.s)
            t.b.write(w)
            w(frill.line_marker.s)


    class AssignStatement_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-1'
        frill        = conjure_dual_expression_statement_frill(
                           empty_indentation,
                           conjure_equal_sign(' = '),
                           empty_line_marker,
                       )


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_dual_expression_statement_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           empty_line_marker,
                       )


    [
            conjure_assign_1, AssignStatement_1.conjure_triple,
    ] = produce_conjure_bookcase_dual_expression(
            'assign-1',
            AssignStatement_1,

            conjure_triple_frill   = conjure_dual_expression_statement_frill,
            produce_conjure_triple = true,
        )

    [
            conjure_modify_statement, ModifyStatement.conjure_triple,
    ] = produce_conjure_bookcase_dual_expression(
            'modify-statement',
            ModifyStatement,

            conjure_triple_frill   = conjure_dual_expression_statement_frill,
            produce_conjure_triple = true,
        )


    share(
        'conjure_assign_1',             conjure_assign_1,
        'conjure_modify_statement',     conjure_modify_statement,
    )
