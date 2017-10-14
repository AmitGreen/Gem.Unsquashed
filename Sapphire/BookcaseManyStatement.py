#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyStatement')
def gem():
    require_gem('Sapphire.BookcaseManyExpression')


    def write__comment_many(t, w):
        begin = t.frill.begin

        begin.v.write(w)
        w(begin.w.s)
        write__X__many_end(t, w)


    class AssignStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = 'assign-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def add_comment(t, comment):
            frill = t.frill

            return conjure_comment_assign_many(conjure_vw_frill(comment, frill.begin), t.many, frill.many, frill.end)


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<assign-* +%d %s %s %s>',
                           begin.total,
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<assign-* +%d ', frill.begin.total)

            dump_token__X__many(t, f)

            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        find_require_gem = find_require_gem__0


        @property
        def indentation(t):
            return t.frill.begin


        def transform(t, vary):
            frill    = t.frill
            many     = t.many
            iterator = iterate(many)

            frill__2 = frill.transform(vary)

            i            = 0
            i_maximum_m1 = length(many) - 1
            priority     = PRIORITY_TERNARY_LIST

            for v in iterator:
                v__2 = v.mutate(vary, priority)

                if v is not v__2:
                    break

                i += 1

                if i == i_maximum_m1:
                    priority = PRIORITY_YIELD
            else:
                if frill is frill__2:
                    return t

                return conjure_assign_many__with_frill(frill__2, many)

            many__2 = (
                          []          if i is 0 else
                          [many[0]]   if i is 1 else
                          List(many[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.mutate(vary, priority))

                i += 1

                if i == i_maximum_m1:
                    priority = PRIORITY_YIELD

            return conjure_assign_many__with_frill(frill__2, conjure_tuple_of_many_expression(many__2))


    class Comment_AssignStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = '#assign-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<#assign-* +%d %s %s %s %s>',
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


        find_require_gem = find_require_gem__0


        @property
        def indentation(t):
            return t.frill.begin.w


        write = write__comment_many


    class Comment_DeleteStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = '#delete-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        @property
        def indentation(t):
            return t.frill.begin.w.a


        def display_token(t):
            frill          = t.frill
            begin          = frill.begin
            comment        = begin.v
            indented_token = begin.w

            return arrange('<#delete-* +%d %s %s %s %s %s>',
                           indented_token.a.total,
                           indented_token.b.display_token(),
                           comment         .display_token(),
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end .display_token())


        def dump_token(t, f, newline = true):
            frill          = t.frill
            begin          = frill.begin
            comment        = begin.v
            indented_token = begin.w

            with f.indent(arrange('<#delete-* +%d ', indented_token.a.total), '>'):
                comment.dump_token(f)
                indented_token.b.dump_token(f)
                dump_token__X__many(t, f)
                frill.end.dump_token(f)


        find_require_gem = find_require_gem__0
        write            = write__comment_many


    class DeleteStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = 'delete-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def add_comment(t, comment):
            frill = t.frill

            return conjure_comment_delete_many(conjure_vw_frill(comment, frill.begin), t.many, frill.many, frill.end)


        @property
        def indentation(t):
            return t.frill.begin.a


        def display_token(t):
            frill          = t.frill
            indented_token = frill.begin

            return arrange('<delete-* +%d%s %s %s %s %s>',
                           indented_token.a   .total,
                           indented_token.b   .display_token(),
                           ' '.join(v         .display_token()   for v in t.many),
                           frill         .many.display_token(),
                           frill         .end .display_token())


        def dump_token(t, f, newline = true):
            frill          = t.frill
            indented_token = frill.begin

            f.partial('<delete-* +%d ', indented_token.a.total)
            indented_token.b.dump_token(f)

            dump_token__X__many(t, f)

            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        find_require_gem = find_require_gem__0


        def transform(t, vary):
            frill    = t.frill
            many     = t.many
            iterator = iterate(many)

            frill__2 = frill.transform(vary)

            i = 0

            for v in iterator:
                v__2 = v.mutate(vary, PRIORITY_NORMAL)

                if v is not v__2:
                    break

                i += 1
            else:
                if frill is frill__2:
                    return t

                return conjure_delete_many__with_frill(frill__2, many)

            many__2 = (
                          []          if i is 0 else
                          [many[0]]   if i is 1 else
                          List(many[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.mutate(vary, PRIORITY_NORMAL))

            return conjure_delete_many__with_frill(frill__2, conjure_tuple_of_many_expression(many__2))


    [
        conjure_assign_many, conjure_assign_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'assign-*',
            AssignStatement_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_comment_assign_many, Comment_AssignStatement_Many.conjure_dual,
    ] = produce_conjure_bookcase_many_expression('#assign-*', Comment_AssignStatement_Many)

    [
        conjure_comment_delete_many, Comment_DeleteStatement_Many.conjure_dual,
    ] = produce_conjure_bookcase_many_expression('#delete-*', Comment_DeleteStatement_Many)

    [
        conjure_delete_many, conjure_delete_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'delete-*',
            DeleteStatement_Many,

            produce_conjure_with_frill = 1,
        )


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
