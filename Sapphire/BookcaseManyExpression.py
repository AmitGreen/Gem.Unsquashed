#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyExpression')
def gem():
    require_gem('Sapphire.BookcaseManyFrill')
    require_gem('Sapphire.ManyExpression')


    conjure_bookcase_many_frill = Shared.conjure_bookcase_many_frill    #   Due to privileged
    conjure_many_expression     = Shared.conjure_many_expression        #   Due to privileged


    if __debug__:
        cache_many = []


    class BookcaseManyExpression(SapphireTrunk):
        __slots__ = ((
            'many',                     #   Tuple of Expression+
            'frill',                    #   ManyFrill
        ))


        def __init__(t, many, frill):
            t.many  = many
            t.frill = frill


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, ' '.join(portray(v)   for v in t.many), t.frill)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           ' '.join(v.display_token()   for v in t.many),
                           t.frill.display_token())


        def write(t, w):
            frill = t.frill
            many  = t.many

            frill_many = frill.many

            w(frill.begin.s)

            if frill_many.frill_estimate is 2:
                many[0].write(w)
                w(frill_many.a.s)
                many[1].write(w)
                w(frill_many.b.s)
                many[2].write(w)
            elif frill_many.frill_estimate is 3:
                many[0].write(w)
                w(frill_many.a.s)
                many[1].write(w)
                w(frill_many.b.s)
                many[2].write(w)
                w(frill_many.c.s)
                many[3].write(w)
            else:
                iterator         = iterate(many)
                write_frill_many = next_method(frill_many.iterate_write(w))

                next_method(iterator)().write(w)

                for v in iterator:
                    write_frill_many()
                    v.write(w)

            w(frill.end.s)


    @privileged
    def produce_conjure_bookcase_many_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        #
        #   NOTE:
        #       Reversed from normal: uses 'frill' as the first map index & 'many' as the second map index.
        #
        def conjure_bookcase_many_expression(begin, list, frill_list, end):
            many  = conjure_many_expression(list)
            frill = conjure_bookcase_many_frill(begin, frill_list, end)

            first = lookup(frill, absent)

            if first.__class__ is Map:
                return (first.get(many)) or (first.setdefault(many, Meta(many, frill)))

            if first.many is many:
                return first

            r = Meta(many, frill)

            store(frill, (r   if first is absent else   { first.many : first, many : r }))

            return r


        if __debug__:
            conjure_bookcase_many_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_bookcase_many_expression


    class Arguments_Many(BookcaseManyExpression):
        __slots__    = (())
        display_name = 'arguments-many'


    conjure_arguments_many = produce_conjure_bookcase_many_expression('arguments-many', Arguments_Many)


    if __debug__:
        @share
        def dump_bookcase_many_cache_many():
            for [name, cache] in cache_many:
                dump_cache(arrange('%s_cache', name), cache)


    share(
        'conjure_arguments_many',   conjure_arguments_many,
    )
