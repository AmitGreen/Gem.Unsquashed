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
        display_name     = 'comment'
        is_token_comment = true


    class TokenCommentNewline(Token):
        __slots__        = (())
        display_name     = 'comment-newline'
        is_token_comment = true
        is_token_newline = true


    class TokenNewline(Token):
        display_name     = 'newline'
        is_token_newline = true


        def display_token(t):
            return portray_raw_string(t.s)


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
            return arrange('<comment %r %r %r>', t.comment_operator.s, t.comment.s, t.newline.s)


        def write(t, w):
            w(t.comment_operator.s + t.comment.s + t.newline.s)


    [
            conjure_comment_operator,
    ] = produce_cache_functions('comment_operator', CommentOperator, produce_conjure_by_name = true)


    [
            conjure_comment_newline,
    ] = produce_cache_functions(
            'comment_operator_newline', TokenCommentNewline,
            
            produce_conjure_by_name = true,
        )


    [
            conjure_token_comment,
    ] = produce_cache_functions('token_comment', TokenComment, produce_conjure_by_name = true)


    [
            conjure_token_newline,
    ] = produce_cache_functions('token_newline', TokenNewline, produce_conjure_by_name = true)


    share(
        'conjure_comment_operator',     conjure_comment_operator,
        'conjure_token_comment',        conjure_token_comment,
    )


    export(
        'conjure_comment_newline',     conjure_comment_newline,
        'conjure_token_newline',       conjure_token_newline,
    )
