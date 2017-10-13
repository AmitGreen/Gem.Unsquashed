#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseDualStatement')
def gem():
    require_gem('Sapphire.BookcaseDualExpression')


    class DualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return t.conjure_with_frill(
                       conjure_commented_vwx_frill(comment, frill.v, frill.w, frill.x),
                       t.a,
                       t.b,
                   )


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.v.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s+frill +%d%s %s %s %s %s>',
                           t.display_name,
                           frill.v.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a    .display_token(),
                           frill.w.display_token(),
                           t.b    .display_token(),
                           frill.x.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)

                t        .a.dump_token(f)
                frill    .w.dump_token(f)
                t        .b.dump_token(f)
                r = frill.x.dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d ', t.display_name, frill.v.total), '>'):
                comment.dump_token(f)
                t.a.dump_token(f)
                frill.w.dump_token(f)
                t.b.dump_token(f)
                frill.x.dump_token(f)

            return false



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
            t.b.write(w)
            w(frill.x.s)


    class AssignStatement_1(DualExpressionStatement):
        __slots__        = (())
        display_name     = 'assign-1'
        frill            = conjure_vwx_frill(empty_indentation, W__ASSIGN__W, LINE_MARKER)
        find_require_gem = find_require_gem__0
        transform        = produce_transform__frill_ab_with_priority('assign-1', PRIORITY_TERNARY_LIST, PRIORITY_YIELD)


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_vwx_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


    [
            conjure_assign_1, AssignStatement_1.conjure_plain, AssignStatement_1.conjure_with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'assign-1',
            AssignStatement_1,

            produce_conjure_plain      = true,
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
