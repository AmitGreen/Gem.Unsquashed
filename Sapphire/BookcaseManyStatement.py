#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyStatement')
def gem():
    require_gem('Sapphire.BookcaseManyExpression')


    def dump_token__X__many(t, newline = true):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

        if frill_estimate is 1:
            assert length(many) is 2

            many[0].dump_token()
            frill_many.dump_token()
            many[1].dump_token()
        elif frill_estimate is 2:
            assert length(many) is 3

            many[0].dump_token()
            frill_many.a.dump_token()
            many[1].dump_token()
            frill_many.b.dump_token()
            many[2].dump_token()
        elif frill_estimate is 3:
            assert length(many) is 4

            many[0].dump_token()
            frill_many.a.dump_token()
            many[1].dump_token()
            frill_many.b.dump_token()
            many[2].dump_token()
            frill_many.c.dump_token()
            many[3].dump_token()
        elif frill_estimate is 4:
            assert length(many) is 5

            many[0].dump_token()
            frill_many.a.dump_token()
            many[1].dump_token()
            frill_many.b.dump_token()
            many[2].dump_token()
            frill_many.c.dump_token()
            many[3].dump_token()
            frill.many.dump_token()
            many[4].dump_token()
        else:
            iterator   = iterate(many)
            next_frill = next_method(iterate(frill_many))

            next_method(iterator)().dump_token()

            for v in iterator:
                next_frill().dump_token()
                v.dump_token()

        r = frill.end.dump_token(false)

        if (r) and (newline):
            line('>')
            return false

        partial('>')
        return r


    class AssignStatment_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = 'assign-*'
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


        def dump_token(t, newline = true):
            indentation = t.frill.begin

            partial('%s<assign-* +%d ', indentation.s, indentation.total)

            return dump_token__X__many(t, newline)


    class DeleteStatement_Many(BookcaseManyExpression):
        __slots__           = (())
        display_name        = 'delete-*'
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t.frill.begin.a


        def display_token(t):
            frill = t.frill

            frill_begin = frill.begin

            return arrange('<delete-* +%d %s %s %s %s>',
                           frill_begin.a.total,
                           frill_begin.b.display_token(),
                           ' '.join(v   .display_token()   for v in t.many),
                           frill.many   .display_token(),
                           frill.end    .display_token())


        def dump_token(t, newline = true):
            frill_begin = t.frill.begin
            indentation = frill_begin.a

            partial('%s<delete-* +%d ', indentation.s, indentation.total)
            frill_begin.b.dump_token()

            return dump_token__X__many(t, newline)


    conjure_assign_many = produce_conjure_bookcase_many_expression('assign-*', AssignStatment_Many)
    conjure_delete_many = produce_conjure_bookcase_many_expression('delete-*', DeleteStatement_Many)


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
