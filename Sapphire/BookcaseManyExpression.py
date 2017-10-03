#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BookcaseManyExpression')
def gem():
    require_gem('Sapphire.BookcaseManyFrill')
    require_gem('Sapphire.TupleOfExpression')

    append_cache                     = Shared.append_cache                      #   Due to privileged
    conjure_bookcase_many_frill      = Shared.conjure_bookcase_many_frill       #   Due to privileged
    produce_conjure_dual             = Shared.produce_conjure_dual              #   Due to privileged
    conjure_tuple_of_many_expression = Shared.conjure_tuple_of_many_expression  #   Due to privileged


    @share
    class BookcaseManyExpression(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   BookcaseManyFrill
            'many',                     #   TupleOfExpression+
        ))


        def __init__(t, frill, many):
            t.frill = frill
            t.many  = many


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, t.frill, ' '.join(portray(v)   for v in t.many))


        def count_newlines(t):
            return t.many.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.frill.display_token(),
                           ' '.join(v.display_token()   for v in t.many))


        def dump_token(t, f, newline = true):
            frill = t.frill
            many  = t.many

            frill_many = frill.many

            frill_estimate = frill_many.frill_estimate

            f.partial('<%s ', t.display_name)
            frill.begin.dump_token(f)

            if frill_estimate is 1:
                assert length(many) is 2

                many[0].dump_token(f)
                frill_many.dump_token(f)
                many[1].dump_token(f)
            elif frill_estimate is 2:
                assert length(many) is 3

                many[0].dump_token(f)
                frill_many.a.dump_token(f)
                many[1].dump_token(f)
                frill_many.b.dump_token(f)
                many[2].dump_token(f)
            elif frill_estimate is 3:
                assert length(many) is 4

                many[0].dump_token(f)
                frill_many.a.dump_token(f)
                many[1].dump_token(f)
                frill_many.b.dump_token(f)
                many[2].dump_token(f)
                frill_many.c.dump_token(f)
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
                frill.many.d.dump_token(f)
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


        def write(t, w):
            frill = t.frill
            many  = t.many

            frill_many = frill.many

            frill_estimate = frill_many.frill_estimate

            w(frill.begin.s)

            if frill_estimate is 1:
                assert length(many) is 2

                many[0].write(w)
                w(frill_many.s)
                many[1].write(w)
                w(frill.end.s)
                return

            if frill_estimate is 2:
                assert length(many) is 3

                many[0].write(w)
                w(frill_many.a.s)
                many[1].write(w)
                w(frill_many.b.s)
                many[2].write(w)
                w(frill.end.s)
                return

            if frill_estimate is 3:
                assert length(many) is 4

                many[0].write(w)
                w(frill_many.a.s)
                many[1].write(w)
                w(frill_many.b.s)
                many[2].write(w)
                w(frill_many.c.s)
                many[3].write(w)
                w(frill.end.s)
                return

            if frill_estimate is 4:
                assert length(many) is 5

                many[0].write(w)
                w(frill_many.a.s)
                many[1].write(w)
                w(frill_many.b.s)
                many[2].write(w)
                w(frill_many.c.s)
                many[3].write(w)
                w(frill.many.d.s)
                many[4].write(w)
                w(frill.end.s)
                return

            iterator         = iterate(many)
            write_frill_many = next_method(frill_many.iterate_write(w))

            next_method(iterator)().write(w)

            for v in iterator:
                write_frill_many()
                v.write(w)

            w(frill.end.s)


    #BookcaseManyExpression.k1 = BookcaseManyExpression.frill
    BookcaseManyExpression.k2 = BookcaseManyExpression.many


    @share
    @privileged
    def produce_conjure_bookcase_many_expression(name, Meta):
        cache = {}

        conjure_dual = produce_conjure_dual(name + '__X2', Meta, cache)


        def conjure_bookcase_many_expression(begin, many, frill_many, end):
            return conjure_dual(
                       conjure_bookcase_many_frill(begin, frill_many, end),
                       conjure_tuple_of_many_expression(many),
                   )


        if __debug__:
            conjure_bookcase_many_expression.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        return conjure_bookcase_many_expression


    class Arguments_Many(BookcaseManyExpression):
        __slots__    = (())
        display_name = 'arguments-*'


    class ListExpression_Many(BookcaseManyExpression):
        __slots__                      = (())
        display_name                   = '[*]'
        is__atom__or__special_operator = true
        is_atom                        = true


    class MapExpression_Many(BookcaseManyExpression):
        __slots__                      = (())
        display_name                   = '{:*:}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class ParameterColon_Many(BookcaseManyExpression):
        __slots__    = (())
        display_name = '(*):'


    class TupleExpression_Many(BookcaseManyExpression):
        __slots__                      = (())
        display_name                   = '{,*,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    conjure_arguments_many        = produce_conjure_bookcase_many_expression('arguments-*',        Arguments_Many)
    conjure_list_expression_many  = produce_conjure_bookcase_many_expression('list-expression-*',  ListExpression_Many)
    conjure_map_expression_many   = produce_conjure_bookcase_many_expression('map-expression-*',   MapExpression_Many)
    conjure_parameter_colon_many  = produce_conjure_bookcase_many_expression('parameter-colon-*',  ParameterColon_Many)
    conjure_tuple_expression_many = produce_conjure_bookcase_many_expression('tuple-expression-*', TupleExpression_Many)


    share(
        'conjure_arguments_many',           conjure_arguments_many,
        'conjure_list_expression_many',     conjure_list_expression_many,
        'conjure_map_expression_many',      conjure_map_expression_many,
        'conjure_parameter_colon_many',     conjure_parameter_colon_many,
        'conjure_tuple_expression_many',    conjure_tuple_expression_many,
    )
