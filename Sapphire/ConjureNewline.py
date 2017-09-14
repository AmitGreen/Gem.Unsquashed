#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConjureNewline')
def gem():
    require_gem('Sapphire.CreateMeta')


    create_Meta_WithNewlines = Shared.create_Meta_WithNewlines      #   Due to 'privileged'
    create_Meta_Many         = Shared.create_Meta_Many              #   Due to 'privileged'


    insert_operator_map                 = {}
    insert_operator__with_newlines__map = {}
    lookup_operator_map                 = {}


    find_insert_operator                = insert_operator_map                .__getitem__
    find_insert_operator__with_newlines = insert_operator__with_newlines__map.__getitem__
    find_lookup_operator                = lookup_operator_map                .__getitem__


    def construct_token__with_newlines(t, s, newlines, ends_in_newline):
        t.s               = s
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_token__python_newline__many(t, s, newlines):
        assert newlines > 1

        t.s        = s
        t.newlines = newlines


    if __debug__:
        def raise_already_exists(name, s):
            raise_runtime_error('cache %s: attempt to insert key %s (already has value %r)',
                                name, portray_string(s), find(s))


    @privileged
    def produce_insert_and_lookup_token_functions(
            name, Meta,

            produce_insert               = false,
            produce_insert_with_newlines = false,
            produce_lookup               = false,
    ):
        r      = []
        append = r.append

        cache   = {}
        provide = cache.setdefault
        find    = cache.__getitem__


        if __debug__:
            contains = cache.__contains__


            if produce_insert:
                def insert(s):
                    assert s[-1] != '\n'

                    if contains(s):
                        raise_already_exists(name, s)

                    newlines = s.count('\n')
                    s        = intern_string(s)

                    if newlines is 0:
                        return provide(s, Meta(s))

                    return provide(
                               s,
                               (
                                     Meta.Meta_WithNewlines
                                  or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                               )(s, newlines, false),
                           )


                insert.__name__ = arrange('insert_%s', name)

                append(insert)


            if produce_insert_with_newlines:
                def insert_with_newlines(s):
                    assert s[-1] == '\n'

                    if contains(s):
                        raise_already_exists(name, s)

                    s = intern_string(s)

                    return provide(
                               s,
                               (
                                     Meta.Meta_WithNewlines
                                  or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                               )(s, s.count('\n'), true),
                           )


                insert_with_newlines.__name__ = arrange('insert_%s__with_newlines', name)

                append(insert_with_newlines)
        else:
            if produce_insert:
                def insert(s):
                    newlines = s.count('\n')
                    s        = intern_string(s)

                    if newlines is 0:
                        return provide(s, Meta(s))

                    return provide(
                               s,
                               (
                                     Meta.Meta_WithNewlines
                                  or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                               )(s, newlines, false),
                           )


                append(insert)


            if produce_insert_with_newlines:
                def insert_with_newlines(s):
                    s = intern_string(s)

                    return provide(
                               s,
                               (
                                     Meta.Meta_WithNewlines
                                  or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                               )(s, s.count('\n'), true),
                           )


                append(insert_with_newlines)


        if produce_lookup:
            append(cache.get)


        return r


    @share
    def produce_operator_insert_and_lookup_maps(many):
        store_insert                = insert_operator_map                .__setitem__
        store_insert__with_newlines = insert_operator__with_newlines__map.__setitem__
        store_lookup                = lookup_operator_map                .__setitem__


        for [k, name, Meta] in many:
            [
                    insert, insert_with_newlines, lookup
            ] = produce_insert_and_lookup_token_functions(
                    name, Meta,

                    produce_insert               = true,
                    produce_insert_with_newlines = true,
                    produce_lookup               = true
                )

            store_insert               (k, insert)
            store_insert__with_newlines(k, insert_with_newlines)
            store_lookup               (k, lookup)



    @share
    @privileged
    def produce_conjure_operator(k, name):
        lookup = find_lookup_operator(k)
        insert = find_insert_operator(k)


        def conjure_operator(s):
            return (lookup(s)) or (insert(s))


        if __debug__:
            conjure_operator.__name__ = intern_arrange('conjure_%s', name)

        return conjure_operator


    @share
    @privileged
    def produce_conjure_operator__with_newlines(k, name):
        lookup               = find_lookup_operator(k)
        insert_with_newlines = find_insert_operator__with_newlines(k)


        def conjure_operator__with_newlines(s):
            return (lookup(s)) or (insert_with_newlines(s))


        if __debug__:
            conjure_operator__with_newlines.__name__ = intern_arrange('conjure_%s__swith_newlines', name)

        return conjure_operator__with_newlines


    @share
    @privileged
    def produce_conjure_operator__python_newline(k, name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        find    = cache.__getitem__


        def conjure_token__python_newline(s):
            r = lookup(s)

            if r is not none:
                return r

            assert s[-1] == '\n'

            newlines = s.count('\n')
            s        = intern_string(s)

            if newlines is 1:
                return Meta(s)

            return provide(
                       s,
                       (
                             Meta.Meta_Many
                          or create_Meta_Many(Meta, construct_token__python_newline__many)
                       )(s, s.count('\n'), true),
                   )


        if __debug__:
            conjure_token__python_newline.__name__ = intern_arrange('conjure_%s__python_newline', name)

        return conjure_token__python_newline



    share(
        'find_insert_operator',                 find_insert_operator,
        'find_insert_operator__with_newlines',  find_insert_operator__with_newlines,
        'find_lookup_operator',                 find_lookup_operator,
        'insert_operator_map',                  insert_operator_map,
        'lookup_operator_map',                  lookup_operator_map,
    )
