#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    require_gem('Sapphire.Indentation')


    comment_line_cache   = {}
    lookup_comment_line  = comment_line_cache.get
    provide_comment_line = comment_line_cache.setdefault
    store_comment_line   = comment_line_cache.__setitem__


    def dump_token__comment(t, f, newline = true):
        f.partial(t.display_token())

        if newline:
            f.line()
            return false

        return true


    class CommentLine(String):
        __slots__                  = (())
        ends_in_newline            = true
        indentation                = empty_indentation
        is_comment_line            = true
        is_comment__or__empty_line = true
        is_empty_line              = false
        is_end_of_data             = false
        is_statement               = false
        is_statement_header        = false
        line_marker                = false
        newlines                   = 1


        def __repr__(t):
            return arrange('<CommentLine %s>', portray_string(t))


        def count_newlines(t):
            assert '\n' not in t

            return 1


        def display_token(t):
            if t is empty_comment_line:
                return '<#>'

            return arrange('<# %s>', portray_string(t))


        dump_token = dump_token__comment


        @property
        def s(t):
            return '#' + t + '\n'


        def write(t, w):
            w('#' + t + '\n')


    class CommentLine_WithTrailer(SapphireToken):
        __slots__ = ((
            'comment',                  #   CommentLine
            'newline',                  #   EmptyLine
        ))


        ends_in_newline            = true
        indentation                = empty_indentation
        is_comment_line            = true
        is_comment__or__empty_line = true
        is_empty_line              = false
        is_end_of_data             = false
        is_statement               = false
        is_statement_header        = false
        newlines                   = 1


        def __init__(t, s, comment, newline):
            t.s       = s
            t.comment = comment
            t.newline = newline


        def __repr__(t):
            return arrange('<CommentLineWithTrailer %s %r>', portray_string(t.comment), t.newline)


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert ('\n' not in t.comment) and (t.newline.count_newlines() is 1)

            return 1


        def display_token(t):
            return arrange('<# %s %s>', portray_string(t.comment), portray_string(t.newline))


        dump_token = dump_token__comment


    class IndentedCommentLine(SapphireToken):
        __slots__ = ((
            'indentation',              #   Indentation
            'comment',                  #   CommentLine
        ))


        ends_in_newline            = true
        is_comment_line            = true
        is_comment__or__empty_line = true
        is_empty_line              = false
        is_end_of_data             = false
        is_statement               = false
        is_statement_header        = false
        newlines                   = 1


        def __init__(t, s, indentation, comment):
            t.s           = s
            t.indentation = indentation
            t.comment     = comment


        def __repr__(t):
            return arrange('<IndentedCommentLine +%d %r>', t.indentation.total, portray_string(t.comment))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert (t.indentation.count_newlines() is 0) and ('\n' not in t.comment)

            return 1


        def display_token(t):
            return arrange('<# +%d %s>', t.indentation.total, portray_string(t.comment))


        dump_token = dump_token__comment


    class IndentedCommentLine_WithTrailer(SapphireToken):
        __slots__ = ((
            'indentation',              #   Indentation
            'comment',                  #   CommentLine
            'newline',                  #   EmptyLine
        ))


        ends_in_newline            = true
        is_comment_line            = true
        is_comment__or__empty_line = true
        is_empty_line              = false
        is_statement               = false
        is_statement_header        = false
        newlines                   = 1


        def __init__(t, s, indentation, comment, newline):
            t.s           = s
            t.indentation = indentation
            t.comment     = comment
            t.newline     = newline


        def __repr__(t):
            return arrange('<IndentedCommentLine_WithTrailer +%d %s %s>',
                           t.indentation.total, portray_string(t.comment), portray_string(t.newline))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert (t.indentation.count_newlines() is 0) and ('\n' not in t.comment)
            assert t.newline.count_newlines() is 1

            return 1


        def display_token(t):
            return arrange('<# +%d %s %s>', t.indentation.total, portray_string(t.comment), portray_string(t.newline))


        dump_token = dump_token__comment



    class NoComment(SapphireToken):
        __slots__ = (())


        @static_method
        def __repr__():
            return '<no-comment>'


        display_token = __repr__


        def dump_token(t, newline = true):
            line('<no-comment>')


    def conjure_comment_line(comment):
        r = lookup_comment_line(comment)

        if r is not none:
            return r

        r = CommentLine(comment)

        return provide_comment_line(r, r)


    def conjure_any_comment_line(indentation_end, comment_end):
        r = lookup_comment_line(qs())

        if r is not none:
            return r

        s = intern_string(qs())

        comment = conjure_comment_line(s[indentation_end + 1 : comment_end])
        newline =                      s[comment_end         :            ]

        if indentation_end is 0:
            if newline == '\n':
                return provide_comment_line(s, comment)

            return provide_comment_line(s, CommentLine_WithTrailer(s, comment, conjure_empty_line(newline)))

        indentation = conjure_indentation(s[ : indentation_end])

        if newline == '\n':
            return provide_comment_line(s, IndentedCommentLine(s, indentation, comment))

        return provide_comment_line(
                   s,
                   IndentedCommentLine_WithTrailer(s, indentation, comment, conjure_empty_line(newline)),
               )


    empty_comment_line = conjure_comment_line('')
    no_comment         = NoComment('')


    append_cache('comment-line', comment_line_cache)


    share(
        'conjure_any_comment_line',     conjure_any_comment_line,
        'no_comment',                   no_comment,
    )
