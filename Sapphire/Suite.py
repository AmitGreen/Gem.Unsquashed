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


        def dump_token(t, f, newline = true):
            assert newline is true

            indentation = t[0].indentation

            with f.indent(prefix = indentation.total):
                with f.indent(arrange('<comment-* +%d', indentation.total), '>'):
                    for v in t:
                        v.dump_token(f)


        @property
        def s(t):
            return ''.join(v.s   for v in t)


    conjure_comment_suite = produce_conjure_tuple('comment-*', CommentSuite, comment_suite_cache)


    append_cache('comment-suite', comment_suite_cache)


    share(
        'conjure_comment_suite',    conjure_comment_suite,
    )
