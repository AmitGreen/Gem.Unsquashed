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


        display_name = 'bookcase-*-frill'


        __init__       = construct__123
        count_newlines = count_newlines__123
        __repr__       = portray__123
        display_token  = display_token__123


    BookcaseManyFrill.a = BookcaseManyFrill.begin
    BookcaseManyFrill.b = BookcaseManyFrill.many
    BookcaseManyFrill.c = BookcaseManyFrill.end

    BookcaseManyFrill.k1 = BookcaseManyFrill.begin
    BookcaseManyFrill.k2 = BookcaseManyFrill.many
    BookcaseManyFrill.k3 = BookcaseManyFrill.end


    conjure_bookcase_many_frill__213 = produce_conjure_triple__213(
                                           'bookcase_many_frill__213',
                                           BookcaseManyFrill,
                                           bookcase_many_frill_cache,
                                       )

    BookcaseManyFrill.transform = produce_transform__abc('bookcase_many_frill', conjure_bookcase_many_frill__213)

    append_cache('bookcase-*-frill', bookcase_many_frill_cache)


    @share
    def conjure_bookcase_many_frill(begin, list, end):
        return conjure_bookcase_many_frill__213(begin, conjure_many_frill(list), end)
