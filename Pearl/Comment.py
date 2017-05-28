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


    @share
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


    share(
        'conjure_comment_operator',     conjure_comment_operator,
        'conjure_token_comment',        conjure_token_comment,
    )


    export(
        'conjure_token_newline',    conjure_token_newline,
    )
