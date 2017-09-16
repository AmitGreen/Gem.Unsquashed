#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.LineMarker')
def gem():
    require_gem('Sapphire.CreateMeta')


    create_ActionWord_LineMarker_Many = Shared.create_ActionWord_LineMarker_Many    #   Due to 'privileged'


    line_marker_cache = {}                          #   Map { String : ActionWord_LineMarker_* | LineMarker }

    lookup_line_marker  = line_marker_cache.get
    provide_line_marker = line_marker_cache.setdefault


    def construct_token__line_marker__many(t, s, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)

        t.s        = s
        t.newlines = newlines


    class LineMarker(Token):
        display_name    = 'line-marker'
        ends_in_newline = true
        line_marker     = true
        newlines        = 1


        def __init__(t, s):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (s.count('\n') == 1) and (s[-1] == '\n')

            t.s = s


    @share
    def conjure_line_marker(s):
        r = lookup_line_marker(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_line_marker(s, LineMarker(s))


    if __debug__:
        @share
        def dump_line_markers():
            for k in sorted_list(v.s   for v in view_values(line_marker_cache)):
                line('%r', line_marker_cache[k])


    @share
    @privileged
    def produce_conjure_action_word__line_marker(name, Meta):
        def conjure_action_word__line_marker(s):
            assert s[-1] == '\n'

            r = lookup_line_marker(s)

            if r is not none:
                return r

            s = intern_string(s)

            newlines = s.count('\n')

            return provide_line_marker(
                       s,
                       (
                           Meta(s)
                               if newlines is 1 else
                                   (
                                         lookup_adjusted_meta(Meta)
                                      or create_ActionWord_LineMarker_Many(Meta, construct_token__line_marker__many)
                                   )(s, s.count('\n'))
                       ),
                   )


        if __debug__:
            conjure_action_word__line_marker.__name__ = intern_arrange('conjure_%s__line_marker', name)

        return conjure_action_word__line_marker
