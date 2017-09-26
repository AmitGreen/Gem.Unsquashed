#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyFrill')
def gem():
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


    BookcaseManyFrill.kt1 = BookcaseManyFrill.many          #   First (instead of second) on purpose
    BookcaseManyFrill.kt2 = BookcaseManyFrill.begin         #   Second (instead of first) on purpose
    BookcaseManyFrill.kt3 = BookcaseManyFrill.end


    def create_bookcase_many_frill(many, begin, end):       #   First & Second parameters flipped on purpose
        return BookcaseManyFrill(begin, many, end)


    conjure_bookcase_many_frill__X3 = produce_triple_cache(
                                          'bookcase_many_frill__X3',
                                          create_bookcase_many_frill,
                                          bookcase_many_frill_cache,
                                      )


    @share
    def conjure_bookcase_many_frill(begin, list, end):
        return conjure_bookcase_many_frill__X3(conjure_many_frill(list), begin, end)


    @share
    def dump_bookcase_many_frill_cache():
        dump_cache('bookcase-many-frill-cache', cache)
