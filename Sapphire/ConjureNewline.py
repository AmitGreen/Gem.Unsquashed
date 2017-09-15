#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConjureNewline')
def gem():
    require_gem('Sapphire.CreateMeta')


    create_Meta_WithNewlines = Shared.create_Meta_WithNewlines      #   Due to 'privileged'
    create_Meta_Many         = Shared.create_Meta_Many              #   Due to 'privileged'


    action_word__cache                       = {}
    action_word__Meta__cache                 = {}
    action_word__python_newline__cache       = {}

    action_word__python_newline__Meta__cache = {}
    action_word__with_newlines__Meta__cache  = action_word__python_newline__Meta__cache

    find_action_word__Meta                    = action_word__Meta__cache                .__getitem__
    lookup_action_word                        = action_word__cache                      .get
    lookup_action_word__python_newline        = action_word__python_newline__cache      .get
    lookup_action_word__python_newline__Meta  = action_word__python_newline__Meta__cache.get
    lookup_action_word__with_newlines__Meta   = action_word__with_newlines__Meta__cache .get
    provide_action_word                       = action_word__cache                      .setdefault
    provide_action_word__python_newline       = action_word__python_newline__cache      .setdefault
    provide_action_word__python_newline__Meta = action_word__python_newline__Meta__cache.setdefault
    provide_action_word__with_newlines__Meta  = action_word__with_newlines__Meta__cache .setdefault


    def construct_token__with_newlines(t, s, newlines, ends_in_newline):
        t.s               = s
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_token__python_newline__many(t, s, newlines):
        assert newlines > 1

        t.s        = s
        t.newlines = newlines


    @share
    def conjure_action_word(full, s):
        assert s[-1] != '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        newlines = s.count('\n')

        if newlines is 0:
            return provide_action_word(s, find_action_word__Meta(full)(s))

        Meta_WithNewlines = lookup_action_word__with_newlines__Meta(full)

        if Meta_WithNewlines is none:
            Meta = find_action_word__Meta(full)

            Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                    Meta,
                                    create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                )

        return provide_action_word(s, Meta_WithNewlines(s, newlines, false))


    @share
    def conjure_action_word__ends_in_newline(full, s):
        assert s[-1] == '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta_WithNewlines = lookup_action_word__with_newlines__Meta(full)

        if Meta_WithNewlines is none:
            Meta = find_action_word__Meta(full)

            Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                    Meta,
                                    create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                )

        return provide_action_word(s, Meta_WithNewlines(s, s.count('\n'), true))


    @share
    def initialize_action_word__Meta(many):
        provide_action_word__Meta = action_word__Meta__cache.setdefault

        for [k, Meta] in many:
            provide_action_word__Meta(k, Meta)

        assert length(many) == length(action_word__Meta__cache)


    @share
    @privileged
    def produce_conjure_action_word(name, Meta):
        def conjure_action_word(s):
            assert s[-1] != '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            newlines = s.count('\n')

            if newlines is 0:
                return provide_action_word(s, Meta(s))

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(Meta)

            if Meta_WithNewlines is none:
                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        Meta,
                                        create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, newlines, false))


        if __debug__:
            conjure_action_word.__name__ = intern_arrange('conjure_%s', name)

        return conjure_action_word


    @share
    @privileged
    def produce_conjure_action_word__ends_in_newline(name, Meta):
        def conjure_action_word__ends_in_newline(s):
            assert s[-1] == '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            Meta_WithNewlines = lookup_action_word__with_newlines__Meta(Meta)

            if Meta_WithNewlines is none:
                Meta_WithNewlines = provide_action_word__with_newlines__Meta(
                                        Meta,
                                        create_Meta_WithNewlines(Meta, construct_token__with_newlines),
                                    )

            return provide_action_word(s, Meta_WithNewlines(s, s.count('\n'), true))


        if __debug__:
            conjure_action_word__ends_in_newline.__name__ = intern_arrange('conjure_%s__ends_in_newline', name)

        return conjure_action_word__ends_in_newline


    @share
    @privileged
    def produce_conjure_action_word__python_newline(name, Meta):
        def conjure_action_word__python_newline(s):
            assert s[-1] == '\n'

            r = lookup_action_word__python_newline(s)

            if r is not none:
                return r

            s = intern_string(s)

            newlines = s.count('\n')

            if newlines is 1:
                return Meta(s)

            Meta_Many = lookup_action_word__python_newline__Meta(Meta)

            if Meta_Many is none:
                Meta_Many = provide_action_word__python_newline__Meta(
                                Meta,
                                create_Meta_Many(Meta, construct_token__python_newline__many),
                            )

            return provide_action_word__python_newline(s, Meta_Many(s, s.count('\n')))


        if __debug__:
            conjure_action_word__python_newline.__name__ = intern_arrange('conjure_%s__python_newline', name)

        return conjure_action_word__python_newline


    @share
    def dump_newline_meta_cache():
        for k in iterate_values_sorted_by_key({ k.__name__ : k   for k in action_word__python_newline__Meta__cache }):
            line('%30s : %s', k.__name__, action_word__python_newline__Meta__cache[k].__name__)
