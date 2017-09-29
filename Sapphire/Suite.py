#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    comment_suite_cache = {}


    class CommentSuite(TokenTuple):
        __slots__ = (())


    conjure_comment_suite = produce_conjure_tuple('comment-*', CommentSuite, comment_suite_cache)


    append_cache('comment-suite', comment_suite_cache)


    share(
        'conjure_comment_suite',    conjure_comment_suite,
    )
