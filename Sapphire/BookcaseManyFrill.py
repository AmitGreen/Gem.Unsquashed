#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyFrill')
def gem():
    require_gem('Sapphire.ManyExpression')


    bookcase_many_frill_cache = {}


    #
    #   NOTE:
    #       This is pretty similiar to 'TripleFrill', but the code is clearer with making
    #       this is a seperate class and using .begin, .many & .end for the members
    #       (instead of .a, .b, & .c as in TripleFrill)
    #
    class BookcaseManyFrill(Object):
        __slots__ = ((
            'begin',                    #   SapphireToken+
            'many',                     #   ManyFrill
            'end',                      #   SapphireToken+
        ))


        def __init__(t, begin, many, end):
            t.begin = begin
            t.many  = many
            t.end   = end


        def count_newlines(t):
            return t.begin.count_newlines() + t.many.count_newlines() + t.end.count_newlines()


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.begin, t.many, t.end)


        def display_token(t):
            return arrange('<bookcase-many-frill %s %s %s>',
                           t.begin.display_token(), t.many.display_token(), t.end.display_token())


    BookcaseManyFrill.k1 = BookcaseManyFrill.begin
    BookcaseManyFrill.k2 = BookcaseManyFrill.many
    BookcaseManyFrill.k3 = BookcaseManyFrill.end


    conjure_bookcase_many_frill__213 = produce_conjure_triple__213(
                                           'bookcase_many_frill__213',
                                           BookcaseManyFrill,
                                           bookcase_many_frill_cache,
                                       )


    append_cache('bookcase-*-frill', bookcase_many_frill_cache)


    @share
    def conjure_bookcase_many_frill(begin, list, end):
        return conjure_bookcase_many_frill__213(begin, conjure_many_frill(list), end)
