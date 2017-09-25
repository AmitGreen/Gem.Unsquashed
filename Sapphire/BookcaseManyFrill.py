#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyFrill')
def gem():
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



    cache  = {}
    lookup = cache.get
    store  = cache.__setitem__


    #
    #   NOTE:
    #       The order of the keys for map lookup is: many, begin, end
    #       (instead of the more normal order: begin, many, end)
    #
    @share
    def conjure_bookcase_many_frill(begin, list, end):
        many = conjure_many_frill(list)

        first = lookup(many, absent)

        if first.__class__ is Map:
            second = first.get(begin, absent)

            if second.__class__ is Map:
                return (second.get(end)) or (second.setdefault(end, BookcaseManyFrill(begin, many, end)))

            if second.end is end:
                return second

            r = BookcaseManyFrill(begin, many, end)

            first[begin] = (r   if second is absent else   { second.end : second, end : r })

            return r

        if first.begin is begin:
            if first.end is end:
                return first

            r = BookcaseManyFrill(begin, many, end)

            store(many, { first.begin : { first.end : first, end : r } })

            return r

        r = BookcaseManyFrill(begin, many, end)

        store(many, (r   if first is absent else   { first.begin : first, begin : r }))

        return r


    @share
    def dump_bookcase_many_frill_cache():
        dump_cache('bookcase-many-frill-cache', cache)
