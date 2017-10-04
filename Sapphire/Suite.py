#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    suite_cache   = {}
    provide_suite = suite_cache.setdefault


    class SuiteBase(TokenTuple):
        __slots__           = (())
        is_statement        = true
        is_statement_header = false


        @property
        def indentation(t):
            return t[0].indentation


        def dump_token(t, f, newline = true):
            assert newline is true

            indentation = t[0].indentation

            with f.indent(prefix = indentation.total):
                with f.indent(arrange('%s +%d', t.display_name, indentation.total), '>'):
                    for v in t:
                        v.dump_token(f)


        @property
        def s(t):
            return ''.join(v.s   for v in t)


    class CommentSuite(SuiteBase):
        __slots__    = (())
        display_name = 'comment-*'


    class EmptyLineSuite(SuiteBase):
        __slots__    = (())
        display_name = 'empty-line-*'


    class MixedSuite(SuiteBase):
        __slots__    = (())
        display_name = 'mixed-*'

    class StatementSuite(SuiteBase):
        __slots__    = (())
        display_name = 'statement-*'


    conjure_comment_suite    = produce_conjure_tuple('comment-*',    CommentSuite,    suite_cache, provide_suite)
    conjure_empty_line_suite = produce_conjure_tuple('empty-line-*', EmptyLineSuite,  suite_cache, provide_suite)
    conjure_mixed_suite      = produce_conjure_tuple('mixed-*',      MixedSuite,      suite_cache, provide_suite)
    conjure_statement_suite  = produce_conjure_tuple('statement-*',  StatementSuite,  suite_cache, provide_suite)


    append_cache('suite', suite_cache)


    share(
        'conjure_comment_suite',        conjure_comment_suite,
        'conjure_empty_line_suite',     conjure_empty_line_suite,
        'conjure_mixed_suite',          conjure_mixed_suite,
        'conjure_statement_suite',      conjure_statement_suite,
    )
