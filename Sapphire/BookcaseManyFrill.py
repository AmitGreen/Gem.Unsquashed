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


        def remove_comments(t):
            begin = t.begin
            many  = t.many
            end   = t.end

            begin__2 = begin.remove_comments()
            many__2  = many.remove_comments()
            end__2   = end.remove_comments()

            if (begin is begin__2) and (many is many__2) and (end is end__2):
                return t

            return conjure_bookcase_many_frill__213(begin__2, many__2, end__2)


        def transform(t, mutate):
            begin = t.begin
            many  = t.many
            end   = t.end

            begin__2 = begin.transform(mutate)
            many__2  = many .transform(mutate)
            end__2   = end  .transform(mutate)

            if (begin is begin__2) and (many is many__2) and (end is end__2):
                return t

            return conjure_bookcase_many_frill__213(begin__2, many__2, end__2)


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
