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


    def construct_token_with_newlines(t, s, newlines, ends_in_newline):
        t.s               = s
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_token_with_python_newline_many(t, s, newlines):
        assert newlines > 1

        t.s        = s
        t.newlines = newlines
        

    def create_MetaWithNewline(Meta):
        r = Meta.MetaWithNewline = Type(
                                       arrange('%sWithNewline', Meta.__name__),
                                       ((Meta,)),
                                       {
                                           '__slots__' : ((
                                               'newlines',                 #   Integer { > 1 }
                                               'ends_in_newline',          #   Boolean
                                           )),

                                           '__init__' : construct_token_with_newlines,
                                       },
                                   )

        return r


    def create_MetaPythonNewline_Many(Meta):
        r = Meta.MetaWithNewline = Type(
                                       arrange('%s_Many', Meta.__name__),
                                       ((Meta,)),
                                       {
                                           '__slots__' : ((
                                               'newlines',                 #   Integer { > 1 }
                                           )),

                                           '__init__' : construct_token_with_python_newline_many,
                                       },
                                   )

        return r


    if __debug__:
        def raise_already_exists(name, s):
            raise_runtime_error('cache %s: attempt to insert key %s (already has value %r)',
                                name, portray_string(s), find(s))


    @privileged
    def produce_insert_and_lookup_token_functions(
            name, Meta,
            
            produce_insert              = false,
            produce_insert_with_newline = false,
            produce_lookup              = false,
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
                               ( (Meta.MetaWithNewline) or (create_MetaWithNewline(Meta)) )(s, newlines, false),
                           )



                insert.__name__ = arrange('insert_%s', name)

                append(insert)


            if produce_insert_with_newline:
                def insert_with_newline(s):
                    assert s[-1] == '\n'

                    if contains(s):
                        raise_already_exists(name, s)

                    newlines = s.count('\n')
                    s        = intern_string(s)

                    return provide(
                               s,
                               ( (Meta.MetaWithNewline) or (create_MetaWithNewline(Meta)) )(s, newlines, true),
                           )


                insert_with_newline.__name__ = arrange('insert_%s__with_newline', name)

                append(insert_with_newline)
        else:
            if produce_insert:
                def insert(s):
                    newlines = s.count('\n')
                    s        = intern_string(s)

                    if newlines is 0:
                        return provide(s, Meta(s))

                    return provide(s, (Meta or MetaWithNewline(Meta))(s, newlines, false))


                append(insert)


            if produce_insert_with_newline:
                def insert_with_newline(s):
                    s = intern_string(s)

                    return provide(s, (Meta or MetaWithNewline(Meta))(s, s.count('\n'), true))


                append(insert_with_newline)


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
                    name, Meta,

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
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        find    = cache.__getitem__


        def conjure_with_python_newline(s):
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
                       ( (Meta.MetaWithNewline) or (create_MetaPythonNewline_Many(Meta)) )(s, newlines),
                  )


        if __debug__:
            conjure_with_python_newline.__name__ = intern_arrange('conjure_%s%swith_python_newline',
                                                                  name,
                                                                  ('__'   if '_' in name else   '_'))

        return conjure_with_python_newline



    share(
        'insert_operator_map',                  insert_operator_map,
        'insert_operator__with_newline__map',   insert_operator__with_newline__map,
        'lookup_operator_map',                  lookup_operator_map,

        'insert_operator',                      insert_operator,
        'insert_operator_with_newline',         insert_operator_with_newline,
        'lookup_operator',                      lookup_operator,
    )
