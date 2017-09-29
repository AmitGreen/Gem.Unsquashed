#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyStatement')
def gem():
    require_gem('Sapphire.BookcaseManyExpression')


    class AssignStatment_Many(BookcaseManyExpression):
        __slots__    = (())


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


    class DeleteStatement_Many(BookcaseManyExpression):
        __slots__    = (())


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
                           frill.end   .display_token())


    conjure_assign_many = produce_conjure_bookcase_many_expression('assign-*', AssignStatment_Many)
    conjure_delete_many = produce_conjure_bookcase_many_expression('delete-*', DeleteStatement_Many)


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
