#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyStatement')
def gem():
    require_gem('Sapphire.BookcaseManyExpression')


    class AssignStatment_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = 'assign-*'
        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        def add_comment(t, comment):
            frill = t.frill

            my_line('frill.many: %r', frill.many)

            return conjure_comment_assign_many(conjure_vw_frill(comment, frill.begin), t.many, frill.many, frill.end)


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<%s +%d %s %s %s>',
                           t.display_name,
                           begin.total,
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s +%d ', t.display_name, frill.begin.total)

            dump_token__X__many(t, f)

            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        @property
        def indentation(t):
            return t.frill.begin


    class Comment_AssignStatment_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = '#assign-*'
        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<%s +%d %s %s %s %s>',
                           t.display_name,
                           begin.w.total,
                           begin.v   .display_token(),
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end .display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill
            begin = frill.begin

            with f.indent(arrange('<#assign-* +%d ', begin.w.total), '>'):
                begin.v.dump_token(f)
                dump_token__X__many(t, f)
                frill.end.dump_token(f)


        @property
        def indentation(t):
            return t.frill.begin.w


        def write(t, w):
            begin = t.frill.begin

            begin.v.write(w)
            w(begin.w.s)
            write__X__many_end(t, w)



    class DeleteStatement_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = 'delete-*'
        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t.frill.begin.a


        def display_token(t):
            frill = t.frill

            frill_begin = frill.begin

            return arrange('<delete-* +%d %s %s %s %s>',
                           frill_begin.v.total,
                           frill_begin.w.display_token(),
                           ' '.join(v   .display_token()   for v in t.many),
                           frill.many   .display_token(),
                           frill.end    .display_token())


        def dump_token(t, f, newline = true):
            frill_begin = t.frill.begin

            f.partial('<delete-* +%d ', frill_begin.a.total)
            frill_begin.b.dump_token(f)

            return dump_token__X__many(t, f, newline)


    conjure_assign_many         = produce_conjure_bookcase_many_expression('assign-*',  AssignStatment_Many)
    conjure_comment_assign_many = produce_conjure_bookcase_many_expression('#assign-*', Comment_AssignStatment_Many)
    conjure_delete_many         = produce_conjure_bookcase_many_expression('delete-*',  DeleteStatement_Many)


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
