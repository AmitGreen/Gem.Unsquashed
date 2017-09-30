#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    comment_suite_cache = {}


    class CommentSuite(TokenTuple):
        __slots__    = (())
        display_name = 'comment-*'


        def dump_token(t, newline = true):
            assert newline is true

            indentation = t[0].indentation

            line('%s<comment-* +%d', indentation.s, indentation.total)

            for v in t:
                line('%*s%s', indentation.total + 2, '', v.display_token())

            line('>')


    conjure_comment_suite = produce_conjure_tuple('comment-*', CommentSuite, comment_suite_cache)


    append_cache('comment-suite', comment_suite_cache)


    share(
        'conjure_comment_suite',    conjure_comment_suite,
    )
