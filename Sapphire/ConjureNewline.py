#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConjureNewline')
def gem():
    require_gem('Sapphire.CreateMeta')


    new = 7
    old = 7


    create_Meta_WithNewlines = Shared.create_Meta_WithNewlines      #   Due to 'privileged'
    create_Meta_Many         = Shared.create_Meta_Many              #   Due to 'privileged'


    if new:
        action_word__cache                      = {}
        action_word__Meta__cache                = {}
        action_word__with_newlines__Meta__cache = {}

        find_action_word__Meta                   = action_word__Meta__cache               .__getitem__
        lookup_action_word                       = action_word__cache                     .get
        lookup_action_word__with_newlines__Meta  = action_word__with_newlines__Meta__cache.get
        provide_action_word                      = action_word__cache                     .setdefault
        provide_action_word__with_newlines__Meta = action_word__with_newlines__Meta__cache.setdefault


    if old:
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


    if new:
        @share
        def conjure_action_word(full, s):
            assert s[-1] != '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            newlines = s.count('\n')
            s        = intern_string(s)

            if newlines is 0:
                return provide_action_word(s, find_action_word__Meta(full)(s))

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(full)

            if Meta_WithNewlines is none:
                full = intern_string(full)

                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        full,
                                        create_Meta_WithNewlines(
                                            find_action_word__Meta(full),
                                            construct_token__with_newlines,
                                        ),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, newlines, false))


        @share
        def conjure_action_word__ends_in_newline(full, s):
            assert s[-1] == '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(full)

            if Meta_WithNewlines is none:
                full = intern_string(full)

                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        full,
                                        create_Meta_WithNewlines(
                                            find_action_word__Meta(full),
                                            construct_token__with_newlines,
                                        ),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, s.count('\n'), true))


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
        if old:
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


        if new:
            provide_action_word__Meta = action_word__Meta__cache.setdefault

            for [k, name, Meta] in many:
                provide_action_word__Meta(k, Meta)

            assert length(many) == length(action_word__Meta__cache)


    @share
    @privileged
    def produce_conjure_action_word(k, name):
        k    = intern_string(k)
        Meta = find_action_word__Meta(k)

        def conjure_action_word(s):
            assert s[-1] != '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            newlines = s.count('\n')
            s        = intern_string(s)

            if newlines is 0:
                return provide_action_word(s, Meta(s))

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(k)

            if Meta_WithNewlines is none:
                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        k,
                                        create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, newlines, false))


        if __debug__:
            conjure_action_word.__name__ = intern_arrange('conjure_%s', name)

        return conjure_action_word


    @share
    @privileged
    def produce_conjure_action_word__ends_in_newline(k, name):
        k    = intern_string(k)
        Meta = find_action_word__Meta(k)

        def conjure_action_word__ends_in_newline(s):
            assert s[-1] == '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(k)

            if Meta_WithNewlines is none:
                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        k,
                                        create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, s.count('\n'), true))


        if __debug__:
            conjure_action_word__ends_in_newline.__name__ = intern_arrange('conjure_%s__ends_in_newline', name)

        return conjure_action_word__ends_in_newline


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
