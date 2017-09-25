#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    require_gem('Sapphire.Indentation')


    if __debug__:
        cache_many = []


    comment_line_cache   = {}
    lookup_comment_line  = comment_line_cache.get
    provide_comment_line = comment_line_cache.setdefault
    store_comment_line   = comment_line_cache.__setitem__


    class CommentLine(String):
        __slots__       = (())
        ends_in_newline = true
        indented        = empty_indentation
        line_marker     = false
        newlines        = 1


        def __repr__(t):
            return arrange('<CommentLine %s>', portray_string(t))


        def count_newlines(t):
            assert '\n' not in t

            return 1


        def display_token(t):
            if t is empty_comment_line:
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
        indented        = empty_indentation
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


    class IndentedCommentLine(SapphireToken):
        __slots__ = ((
            'indented',                 #   Indentation
            'comment',                  #   CommentLine
        ))


        ends_in_newline = true
        newlines        = 1


        def __init__(t, indented, comment):
            t.indented = indented
            t.comment  = comment


        def __repr__(t):
            return arrange('<IndentedCommentLine %s %r>', portray_string(t.indented), portray_string(t.comment))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert (t.indented.count_newlines() is 0) and ('\n' not in t.comment)

            return 1


        def display_token(t):
            return arrange('<#+%d %s>', t.indented.total, portray_string(t.comment))


        def write(t, w):
            w(t.indented.s + '#' + t.comment + '\n')


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

        if indentation_end is 0:
            comment = s[1           : comment_end]
            newline = s[comment_end :            ]

            if newline == '\n':
                return provide_comment_line(s, conjure_comment_line(comment))

            return provide_comment_line(
                       s,
                       CommentLine_WithTrailingSpaces(conjure_comment_line(comment), conjure_empty_line(newline)),
                   )



        indentation = s[                    : indentation_end]
        comment     = s[indentation_end + 1 : comment_end    ]
        newline     = s[comment_end         :                ]

        if newline != '\n':
            raise_unknown_line()

        return provide_comment_line(
                   s,
                   IndentedCommentLine(conjure_indentation(indentation), conjure_comment_line(comment)),
               )


    empty_comment_line = conjure_comment_line('')


    if __debug__:
        @share
        def dump_comment_line_cache():
            dump_cache('comment-line-cache', comment_line_cache)


    share(
        'conjure_any_comment_line', conjure_any_comment_line,
    )
