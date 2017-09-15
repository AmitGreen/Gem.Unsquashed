#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConjureNewline')
def gem():
    require_gem('Sapphire.CreateMeta')


    create_Meta_WithNewlines = Shared.create_Meta_WithNewlines      #   Due to 'privileged'
    create_Meta_Many         = Shared.create_Meta_Many              #   Due to 'privileged'
    lookup_adjusted_meta     = Shared.lookup_adjusted_meta          #   Due to 'privileged'


    action_word__cache                 = {}
    action_word__Meta__cache           = {}
    action_word__python_newline__cache = {}

    find_action_word__Meta              = action_word__Meta__cache                .__getitem__
    lookup_action_word                  = action_word__cache                      .get
    lookup_action_word__python_newline  = action_word__python_newline__cache      .get
    provide_action_word                 = action_word__cache                      .setdefault
    provide_action_word__python_newline = action_word__python_newline__cache      .setdefault


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

        Meta     = find_action_word__Meta(full)
        newlines = s.count('\n')

        return provide_action_word(
                   s,
                   (
                       provide_action_word(s, Meta(s))
                           if newlines is 0 else
                               (
                                      lookup_adjusted_meta(Meta)
                                   or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                                )(s, newlines, false)
                   ),
               )


    @share
    def conjure_action_word__ends_in_newline(full, s):
        assert s[-1] == '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta = find_action_word__Meta(full)

        return provide_action_word(
                   s,
                   (
                         lookup_adjusted_meta(Meta)
                      or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                   )(s, s.count('\n'), true)
               )


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

            return provide_action_word(
                       s,
                       (
                           Meta(s)
                               if newlines is 0 else
                                   (
                                         lookup_adjusted_meta(Meta)
                                      or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                                   )(s, newlines, false)
                       ),
                   )


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

            return provide_action_word(
                       s,
                       (
                             lookup_adjusted_meta(Meta)
                          or create_Meta_WithNewlines(Meta, construct_token__with_newlines)
                       )(s, s.count('\n'), true)
                   )


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
                return provide_action_word__python_newline(s, Meta(s))

            return provide_action_word__python_newline(
                       s,
                       (
                             lookup_adjusted_meta(Meta)
                          or create_Meta_Many(Meta, construct_token__python_newline__many)
                       )(s, s.count('\n'))
                   )


        if __debug__:
            conjure_action_word__python_newline.__name__ = intern_arrange('conjure_%s__python_newline', name)

        return conjure_action_word__python_newline
