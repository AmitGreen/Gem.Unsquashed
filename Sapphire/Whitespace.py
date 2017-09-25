#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    if __debug__:
        cache_many = []


    comment_line_cache   = {}
    lookup_comment_line  = comment_line_cache.get
    provide_comment_line = comment_line_cache.setdefault
    store_comment_line   = comment_line_cache.__setitem__


    empty_line_cache     = {}
    lookup_empty_line    = empty_line_cache.get
    provide_empty_line   = empty_line_cache.setdefault


    class CommentLine(String):
        __slots__       = (())
        ends_in_newline = true
        line_marker     = false
        newlines        = 1


        def __repr__(t):
            return arrange('<CommentLine %s>', portray_string(t))


        def count_newlines(t):
            assert '\n' not in t

            return 1


        def display_token(t):
            if t is comment_line:
                return '<#>'

            return arrange('<# %s>', portray_string(t))


        def write(t, w):
            w('#' + t + '\n')


    class CommentLine_WithTrailingSpaces(SapphireToken):
        __slots__ = ((
            'comment',                  #   CommentLine
            'newline',                  #   EmptyLine
        ))


        ends_in_newline = true
        newlines        = 1


        def __init__(t, comment, newline):
            t.comment = comment
            t.newline = newline


        def __repr__(t):
            return arrange('<CommentLineWithTrailingSpaces %s %r>', portray_string(t.comment), t.newline)


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert ('\n' not in t.comment) and (t.newline.count_newlines() is 1)

            return 1


        def display_token(t):
            return arrange('<# %s %s>', portray_string(t.comment), portray_string(t.newline))


        def write(t, w):
            w('#' + t.comment + t.newline)


    class EmptyLine(String):
        __slots__       = (())
        ends_in_newline = true
        line_marker     = false
        newlines        = 1


        def __repr__(t):
            return arrange('<EmptyLine %s>', portray_string(t))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.newlines is 1) and (t.line_marker is false)
            assert (t.count('\n') is 1) and (t[-1] == '\n')

            return 1


        def display_token(t):
            if t is empty_line:
                return '<empty-line>'

            return arrange('<empty-line %s>', portray_string(t))


        def write(t, w):
            w(t)


    class Identation(SapphireToken):
        __slots__ = ((
            'total',                    #   Integer {> 0}
        ))


        def __init__(t, s):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s is intern_string(s)

            t.s     = intern_string(s)
            t.total = length(s)


    @export
    class TokenIndented(SapphireToken):
        display_name      = 'indented'
        is_token_indented = true


    class TokenWhitespace(SapphireToken):
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


    def conjure_identation(s):
        r = lookup_indentation_token(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_indentation_token(s, Identation(s))


    def conjure_comment_line(comment):
        r = lookup_comment_line(comment)

        if r is not none:
            return r

        r = CommentLine(comment)

        return provide_comment_line(r, r)


    def conjure_comment_line_with_trailing_spaces(comment, newline):
        assert newline != '\n'

        #
        #   NOTE:
        #       Map order is reverse here, first newline, then comment
        #
        first = lookup_comment_line(newline, absent)

        if first.__class__ is Map:
            r = first.get(comment)

            if r is not none:
                return r

            comment = conjure_comment_line(comment)
            newline = conjure_empty_line(newline)

            return first.setdefault(comment, CommentLine_WithTrailingSpaces(comment, newline))

        if first.comment == comment:
            return first
        comment = conjure_comment_line(comment)
        newline = conjure_empty_line(newline)

        r = CommentLine_WithTrailingSpaces(comment, newline)

        store_comment_line(newline, (r   if first is absent else   { first.comment : first, comment : r }))

        return r


    def conjure_empty_line(s):
        r = lookup_empty_line(s)

        if r is not none:
            return r

        r = EmptyLine(s)

        return provide_empty_line(r, r)


    comment_line = conjure_comment_line('\n')
    empty_line   = conjure_empty_line('\n')


    [
            conjure_whitespace, conjure_whitespace__ends_in_newline,
    ] = produce_conjure_action_word('whitespace', TokenWhitespace, produce_ends_in_newline = true)


    if __debug__:
        @share
        def dump_empty_line_cache():
            dump_cache('comment-line-cache', comment_line_cache)
            dump_cache('empty-line-cache',   empty_line_cache)


    share(
        'conjure_comment_line',                         conjure_comment_line,
        'conjure_comment_line_with_trailing_spaces',    conjure_comment_line_with_trailing_spaces,
        'conjure_empty_line',                           conjure_empty_line,
        'conjure_identation',                           conjure_identation,
        'conjure_whitespace',                           conjure_whitespace,
        'conjure_whitespace__ends_in_newline',          conjure_whitespace__ends_in_newline,
    )
