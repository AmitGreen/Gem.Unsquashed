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


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<%s+frill +%d %s %s %s %s>',
                           t.display_name,
                           frill.a.total,
                           t.a    .display_token(),
                           frill.b.display_token(),
                           t.b    .display_token(),
                           frill.c.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            indentation = frill.a

            f.partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            t.a.dump_token(f)
            frill.b.dump_token(f)
            t.b.dump_token(f)
            r = frill.c.dump_token(f, false)

            if (r) and (newline):
                f.line('>')
                return false

            f.partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a


    class AssignStatement_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-1'
        frill        = conjure_triple_frill(
                           empty_indentation,
                           conjure_equal_sign(' = '),
                           empty_line_marker,
                       )


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_triple_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           empty_line_marker,
                       )


    conjure_assign_1         = produce_conjure_bookcase_dual_expression('assign-1',         AssignStatement_1)
    conjure_modify_statement = produce_conjure_bookcase_dual_expression('modify-statement', ModifyStatement)


    share(
        'conjure_assign_1',             conjure_assign_1,
        'conjure_modify_statement',     conjure_modify_statement,
    )
