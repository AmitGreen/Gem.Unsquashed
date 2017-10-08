#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyStatement')
def gem():
    require_gem('Sapphire.BookcaseManyExpression')


    def dump_token__X__many(t, f, newline = true):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

        if frill_estimate is 1:
            assert length(many) is 2

            many[0].dump_token(f)
            frill_many.dump_token(f)
            many[1].dump_token(f)

        elif frill_estimate is 2:
            assert length(many) is 3

            many[0].dump_token(f)
            frill_many.v.dump_token(f)
            many[1].dump_token(f)
            frill_many.w.dump_token(f)
            many[2].dump_token(f)

        elif frill_estimate is 3:
            assert length(many) is 4

            many[0].dump_token(f)
            frill_many.v.dump_token(f)
            many[1].dump_token(f)
            frill_many.w.dump_token(f)
            many[2].dump_token(f)
            frill_many.x.dump_token(f)
            many[3].dump_token(f)

        elif frill_estimate is 4:
            assert length(many) is 5

            many[0].dump_token(f)
            frill_many.a.dump_token(f)
            many[1].dump_token(f)
            frill_many.b.dump_token(f)
            many[2].dump_token(f)
            frill_many.c.dump_token(f)
            many[3].dump_token(f)
            frill.many.dump_token(f)
            many[4].dump_token(f)

        else:
            iterator   = iterate(many)
            next_frill = next_method(iterate(frill_many))

            next_method(iterator)().dump_token(f)

            for v in iterator:
                next_frill().dump_token(f)
                v.dump_token(f)

        r = frill.end.dump_token(f, false)

        if (r) and (newline):
            f.line('>')
            return false

        f.partial('>')
        return r


    class AssignStatment_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = 'assign-*'
        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t.frill.begin


        def display_token(t):
            frill = t.frill

            return arrange('<assign-* +%d %s %s %s>',
                           frill.begin.total,
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end.display_token())


        def dump_token(t, f, newline = true):
            f.partial('<assign-* +%d ', t.frill.begin.total)

            return dump_token__X__many(t, f, newline)


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


    conjure_assign_many = produce_conjure_bookcase_many_expression('assign-*', AssignStatment_Many)
    conjure_delete_many = produce_conjure_bookcase_many_expression('delete-*', DeleteStatement_Many)


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
