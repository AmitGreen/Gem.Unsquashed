#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConjureNewline')
def gem():
    insert_operator_map                = {}
    insert_operator__with_newline__map = {}
    lookup_operator_map                = {}


    insert_operator              = insert_operator_map               .__getitem__
    insert_operator_with_newline = insert_operator__with_newline__map.__getitem__
    lookup_operator              = lookup_operator_map               .__getitem__

    def construct_token_with_newlines(t, s, newlines, ends_in_newline, ends_in_python_newline):
        t.s                      = s
        t.newlines               = newlines
        t.ends_in_newline        = ends_in_newline
        t.ends_in_python_newline = ends_in_python_newline
        

    def create_MetaWithNewline(Meta):
        r = Meta.MetaWithNewline = Type(
                                       arrange('%sWithNewline', Meta.__name__),
                                       ((Meta,)),
                                       {
                                           '__slots__' : ((
                                               'newlines',                 #   Integer
                                               'ends_in_newline',          #   Boolean
                                               'ends_in_python_newline',   #   Boolean
                                           )),

                                           '__init__' : construct_token_with_newlines,
                                       },
                                   )

        return r


    @privileged
    def produce_insert_and_lookup_token_functions(
            k, name, Meta,
            
            produce_insert                     = false,
            produce_insert_with_newline        = false,
            produce_insert_with_python_newline = false,
            produce_lookup                     = false,
    ):
        r      = []
        append = r.append

        cache   = {}
        provide = cache.setdefault
        find    = cache.__getitem__


        if __debug__:
            contains = cache.__contains__


            def raise_already_exists(s):
                raise_runtime_error('cache %s: attempt to insert key %s (already has value %r)',
                                    name, portray_string(s), find(s))


            if produce_insert:
                def insert(s):
                    assert s[-1] != '\n'

                    if contains(s):
                        raise_already_exists(s)

                    newlines = s.count('\n')
                    s        = intern_string(s)

                    if newlines is 0:
                        return provide(s, Meta(s))

                    return provide(
                               s,
                               ( (Meta.MetaWithNewline) or (create_MetaWithNewline(Meta)) )(s, newlines, false, false),
                           )



                insert.__name__ = arrange('insert_%s', name)

                append(insert)


            if produce_insert_with_newline:
                def insert_with_newline(s):
                    assert s[-1] == '\n'

                    if contains(s):
                        raise_already_exists(s)

                    newlines = s.count('\n')
                    s        = intern_string(s)

                    return provide(
                               s,
                               ( (Meta.MetaWithNewline) or (create_MetaWithNewline(Meta)) )(s, newlines, true, false),
                           )


                insert_with_newline.__name__ = arrange('insert_%s__with_newline', name)

                append(insert_with_newline)


            if produce_insert_with_python_newline:
                def insert_with_python_newline(s):
                    assert s[-1] == '\n'

                    if contains(s):
                        raise_already_exists(s)

                    newlines = s.count('\n')
                    s        = intern_string(s)

                    return provide(
                               s,
                               ( (Meta.MetaWithNewline) or (create_MetaWithNewline(Meta)) )(s, newlines, false, true),
                           )


                insert_with_python_newline.__name__ = arrange('insert_%s__with_python_newline', name)

                append(insert_with_python_newline)
        else:
            if produce_insert:
                def insert(s):
                    newlines = s.count('\n')
                    s        = intern_string(s)

                    if newlines is 0:
                        return provide(s, Meta(s))

                    return provide(s, (Meta or MetaWithNewline(Meta))(s, newlines, False, False))


                append(insert)


            if produce_insert_with_newline:
                def insert_with_newline(s):
                    s = intern_string(s)

                    return provide(s, (Meta or MetaWithNewline(Meta))(s, s.count('\n'), True, False))


                append(insert_with_newline)


            if produce_insert_with_python_newline:
                def insert_with_python_newline(s):
                    s = intern_string(s)

                    return provide(s, (Meta or MetaWithNewline(Meta))(s, s.count('\n'), True, True))


                append(insert_with_python_newline)


        if produce_lookup:
            append(cache.get)


        return r


    @share
    def produce_operator_insert_and_lookup_maps(many):
        store_insert              = insert_operator_map               .__setitem__
        store_insert_with_newline = insert_operator__with_newline__map.__setitem__
        store_lookup              = lookup_operator_map               .__setitem__


        for [k, name, Meta] in many:
            [
                    insert, insert_with_newline, lookup
            ] = produce_insert_and_lookup_token_functions(
                    k, name, Meta,

                    produce_insert              = true,
                    produce_insert_with_newline = true,
                    produce_lookup              = true
                )

            store_insert             (k, insert)
            store_insert_with_newline(k, insert_with_newline)
            store_lookup             (k, lookup)



    @share
    @privileged
    def produce_conjure_operator(k, name):
        lookup = lookup_operator(k)
        insert = insert_operator(k)


        def conjure_operator(s):
            return (lookup(s)) or (insert(s))


        if __debug__:
            conjure_operator.__name__ = intern_arrange('conjure_%s', name)


        return conjure_operator


    @share
    @privileged
    def produce_conjure_operator_with_newline(k, name):
        lookup              = lookup_operator(k)
        insert_with_newline = insert_operator_with_newline(k)


        def conjure_operator(s):
            return (lookup(s)) or (insert_with_newline(s))


        if __debug__:
            conjure_operator.__name__ = intern_arrange('conjure_%s%swith_newline',
                                                       name,
                                                       ('__'   if '_' in name else   '_'))


        return conjure_operator


    @share
    @privileged
    def produce_conjure_operator_with_python_newline(k, name, Meta):
        [
                insert_with_python_newline, lookup,
        ] = produce_insert_and_lookup_token_functions(
                k, name, Meta,

                produce_insert_with_newline = true,
                produce_lookup              = true
            )


        def conjure_operator(s):
            return (lookup(s)) or (insert_with_python_newline(s))


        if __debug__:
            conjure_operator.__name__ = intern_arrange('conjure_%s%swith_python_newline',
                                                       name,
                                                       ('__'   if '_' in name else   '_'))


        return conjure_operator



    share(
        'insert_operator_map',                  insert_operator_map,
        'insert_operator__with_newline__map',   insert_operator__with_newline__map,
        'lookup_operator_map',                  lookup_operator_map,

        'insert_operator',                      insert_operator,
        'insert_operator_with_newline',         insert_operator_with_newline,
        'lookup_operator',                      lookup_operator,
    )
