#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    comment_suite_cache = {}


    class CommentSuite(TokenTuple):
        __slots__           = (())
        display_name        = 'comment-*'
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t[0].indentation


        def dump_token(t, newline = true):
            assert newline is true

            indentation = t[0].indentation

            line('%s<comment-* +%d', indentation.s, indentation.total)

            for v in t:
                partial('%s  ', indentation.s)
                v.dump_token()

            line('%s>', indentation.s)


        @property
        def s(t):
            return ''.join(v.s   for v in t)


    conjure_comment_suite = produce_conjure_tuple('comment-*', CommentSuite, comment_suite_cache)


    append_cache('comment-suite', comment_suite_cache)


    share(
        'conjure_comment_suite',    conjure_comment_suite,
    )
