#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.LineMarker')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.TokenCache')


    conjure_ActionWord_LineMarker_Many = Shared.conjure_ActionWord_LineMarker_Many  #   Due to privileged
    lookup_line_marker                 = Shared.lookup_line_marker                  #   Due to privileged
    provide_line_marker                = Shared.provide_line_marker                 #   Due to privileged


    def construct_token__line_marker__many(t, s, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)

        t.s        = s
        t.newlines = newlines


    class LineMarker(SapphireToken):
        display_name                            = 'line-marker'
        ends_in_newline                         = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_comprehension_expression      = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_multiply_expression           = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        is_line_marker                          = true
        line_marker                             = true
        newlines                                = 1


        def __init__(t, s):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (s.count('\n') == 1) and (s[-1] == '\n')

            t.s = s


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.s.count('\n') == 1) and (t.s[-1] == '\n')

            return 1


        def display_token(t):
            return arrange('<line-marker %s>', portray_string(t.s))


        def dump_token(t, newline = true):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.s.count('\n') == 1) and (t.s[-1] == '\n')

            partial('{%s}', portray_string(t.s)[1:-1])

            if newline:
                line()
                return false

            return true


    @share
    def conjure_line_marker(s):
        r = lookup_line_marker(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_line_marker(s, LineMarker(s))


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
                                   conjure_ActionWord_LineMarker_Many(
                                       Meta, construct_token__line_marker__many,
                                   )(s, s.count('\n'))
                       ),
                   )


        if __debug__:
            conjure_action_word__line_marker.__name__ = intern_arrange('conjure_%s__line_marker', name)

        return conjure_action_word__line_marker


    empty_line_marker = conjure_line_marker('\n')


    share(
        'empty_line_marker',    empty_line_marker,
    )
