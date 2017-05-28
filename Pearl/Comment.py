#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Comment')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    class CommentOperator(Token):
        display_name        = 'comment-operator'
        is_comment_operator = true


    class TokenComment(Token):
        __slots__        = (())
        is_token_comment = true


        def __repr__(t):
            return arrange('<comment %s>', t.s)


    class TokenNewline(Token):
        display_name     = 'newline'
        is_token_newline = true


    class TreeComment(Object):
        __slots__ = ((
            'comment_operator',             #   TokenComment
            'comment',                      #   String+
            'newline',                      #   TokenNewline
        ))


        def __init__(t, comment_operator, comment, newline):
            assert (comment_operator.is_comment_operator) and (comment.is_token_comment) and (newline.is_token_newline)

            t.comment_operator = comment_operator
            t.comment          = comment
            t.newline          = newline


        def __repr__(t):
            if t.comment.s is '':
                return arrange('<comment %r %r>', t.comment_operator.s, t.newline.s)

            return arrange('<comment %r %r %r>', t.comment_operator.s, t.comment.s, t.newline.s)


        def write(t, w):
            w(t.comment_operator.s + t.comment.s + t.newline.s)


    tree_comment_cache   = {}
    provide_tree_comment = tree_comment_cache.setdefault
    lookup_tree_comment  = tree_comment_cache.get
    store_tree_comment   = tree_comment_cache.__setitem__


    @export
    def conjure_tree_comment(comment_operator_s, comment_s, newline_s):
        first = lookup_tree_comment(comment_s)

        if first is none:
            comment = conjure_token_comment(comment_s)

            return provide_tree_comment(
                       comment.s,
                       TreeComment(
                           conjure_comment_operator(comment_operator_s),
                           comment,
                           conjure_token_newline(newline_s),
                       ),
                   )

        if first.__class__ is TreeComment:
            if first.comment_operator.s == comment_operator_s:
                if first.newline.s == newline_s:
                    return first

                r = TreeComment(
                        first.comment_operator,
                        first.comment,
                        conjure_token_newline(newline_s),
                    )

                store_tree_comment(
                    first.comment.s,
                    {
                        first.comment_operator.s : {
                            first.newline.s : first,
                            r.newline.s     : r,
                        },
                    },
                )

                return r

            r = TreeComment(
                    conjure_comment_operator(comment_operator_s),
                    first.comment,
                    conjure_token_newline(newline_s),
                )

            store_tree_comment(
                first.comment.s,
                {
                    first.comment_operator.s : first,
                    r.comment_operator.s     : r,
                },
            )

            return r

        second = first.get(comment_operator_s)

        if second is none:
            comment_operator = conjure_comment_operator(comment_operator_s)

            return first.setdefault(
                       comment_operator.s,
                       TreeComment(
                           comment_operator,
                           conjure_token_comment(comment_s),
                           conjure_token_newline(newline_s),
                       ),
                   )


        if second.__class__ is TreeComment:
            if second.newline.s == newline_s:
                return second

            r = TreeComment(second.comment_operator, second.comment, conjure_token_newline(newline_s))

            first[second.comment_operator.s] = {
                    second.newline.s : second,
                    r.newline.s      : r,
                }

            return r

        third = second.get(newline_s)

        if third is none:
            newline = conjure_token_newline(newline_s)

            return second.setdefault(
                       newline.s,
                       TreeComment(
                           conjure_comment_operator(comment_operator_s),
                           conjure_token_comment(comment_s),
                           newline,
                       ),
                   )

        return third


    [
            conjure_comment_operator,
    ] = produce_cache_functions(
            'Pearl.Token.comment_operator_cache', CommentOperator,

            produce_conjure_by_name = true,
        )


    [
            conjure_token_comment,
    ] = produce_cache_functions(
            'Pearl.Comment.token_comment_cache', TokenComment,

            produce_conjure_by_name = true,
        )


    [
            conjure_token_newline,
    ] = produce_cache_functions(
            'Pearl.Comment.token_newline_cache', TokenNewline,

            produce_conjure_by_name = true,
        )


    if gem_configuration.testing:
        export(
            'tree_comment_cache',   tree_comment_cache,
        )


    export(
        'conjure_token_newline',    conjure_token_newline,
    )
