#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    require_gem('Sapphire.BookcaseDualExpression')


    class DualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        is_else_header      = false
        is_statement_header = false
        is_statement        = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return t.conjure_with_frill(
                       t.a,
                       t.b,
                       conjure_commented_xyz_frill(comment, frill.x, frill.y, frill.z),
                   )


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.x.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s+frill +%d%s %s %s %s %s>',
                           t.display_name,
                           frill.x.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a    .display_token(),
                           frill.y.display_token(),
                           t.b    .display_token(),
                           frill.z.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.x.total)
                t.a.dump_token(f)
                frill.y.dump_token(f)
                t.b.dump_token(f)
                r = frill.z.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.indent(arrange('<%s +%d ', t.display_name, frill.x.total), '>'):
                comment.dump_token(f)
                t.a.dump_token(f)
                frill.y.dump_token(f)
                t.b.dump_token(f)
                frill.z.dump_token(f)

            return false


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
            t.b.write(w)
            w(frill.z.s)


    class AssignStatement_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-1'
        frill        = conjure_xyz_frill(
                           empty_indentation,
                           conjure_equal_sign(' = '),
                           empty_line_marker,
                       )


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_xyz_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           empty_line_marker,
                       )


    [
            conjure_assign_1, AssignStatement_1.conjure_with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'assign-1',
            AssignStatement_1,

            produce_conjure_with_frill = true,
        )

    [
            conjure_modify_statement, ModifyStatement.conjure_with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'modify-statement',
            ModifyStatement,

            produce_conjure_with_frill = true,
        )


    share(
        'conjure_assign_1',             conjure_assign_1,
        'conjure_modify_statement',     conjure_modify_statement,
    )
