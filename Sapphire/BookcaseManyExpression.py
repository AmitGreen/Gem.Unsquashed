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
    def dump_token__X__many(t, f):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

        if frill_estimate is 1:
            assert length(many) is 2

            many   [0].dump_token(f)
            frill_many.dump_token(f)
            many   [1].dump_token(f)

            return

        if frill_estimate is 2:
            assert length(many) is 3

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)

            return

        if frill_estimate is 3:
            assert length(many) is 4

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)
            frill_many.x .dump_token(f)
            many      [3].dump_token(f)

            return

        if frill_estimate is 4:
            assert length(many) is 5

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)
            frill_many.x .dump_token(f)
            many      [3].dump_token(f)
            frill.many.y .dump_token(f)
            many      [4].dump_token(f)

            return

        iterator   = iterate(many)
        next_frill = next_method(iterate(frill_many))

        next_method(iterator)().dump_token(f)

        for v in iterator:
            next_frill().dump_token(f)
            v           .dump_token(f)


    @export
    def write__X__many_end(t, w):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

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
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill.end.s)
            return

        if frill_estimate is 3:
            assert length(many) is 4

            many[0].write(w)
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill_many.x.s)
            many[3].write(w)
            w(frill.end.s)
            return

        if frill_estimate is 4:
            assert length(many) is 5

            many[0].write(w)
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill_many.x.s)
            many[3].write(w)
            w(frill.many.y.s)
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

            f.partial('<%s ', t.display_name)
            frill.begin.dump_token(f)
            dump_token__X__many(t, f)
            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        def transform(t, vary):
            frill    = t.frill
            many     = t.many
            iterator = iterate(many)

            frill_2 = frill.transform(vary)

            i = 0

            for v in iterator:
                v__2 = v.transform(vary)

                if v is not v__2:
                    break

                i += 1
            else:
                if frill is frill_2:
                    return t

                return t.conjure_dual(frill__2, many)

            many__2 = (
                          []          if i is 0 else
                          [many[0]]   if i is 1 else
                          List(many[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.transform(vary))

            return t.conjure_dual(frill_2, conjure_tuple_of_many_expression(many__2))


        def write(t, w):
            w(t.frill.begin.s)

            write__X__many_end(t, w)


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

        return ((
                   conjure_bookcase_many_expression,
                   static_method(conjure_dual),
               ))


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


    class Parameter_Many(BookcaseManyExpression):
        __slots__    = (())
        display_name = 'parameter-(*)'


        def parameter_1_named(t, name):
            return 0


    class TupleExpression_Many(BookcaseManyExpression):
        __slots__                      = (())
        display_name                   = '{,*,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    [
        conjure_arguments_many, Arguments_Many.conjure_dual
    ] = produce_conjure_bookcase_many_expression('arguments-*', Arguments_Many)

    [
        conjure_list_expression_many, ListExpression_Many.conjure_dual,
    ] = produce_conjure_bookcase_many_expression('list-expression-*', ListExpression_Many)

    [
        conjure_map_expression_many, MapExpression_Many.conjure_dual
    ] = produce_conjure_bookcase_many_expression('map-expression-*', MapExpression_Many)

    [
        conjure_parameter_many, Parameter_Many.conjure_dual
    ] = produce_conjure_bookcase_many_expression('parameter-*', Parameter_Many)

    [
        conjure_tuple_expression_many, TupleExpression_Many.conjure_dual
    ] = produce_conjure_bookcase_many_expression('tuple-expression-*', TupleExpression_Many)


    share(
        'conjure_arguments_many',           conjure_arguments_many,
        'conjure_list_expression_many',     conjure_list_expression_many,
        'conjure_map_expression_many',      conjure_map_expression_many,
        'conjure_parameter_many',           conjure_parameter_many,
        'conjure_tuple_expression_many',    conjure_tuple_expression_many,
    )
