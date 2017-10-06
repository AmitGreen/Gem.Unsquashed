#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    suite_cache   = {}
    provide_suite = suite_cache.setdefault


    def dump_token__no_impression(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s', t.display_name), '>'):
            for v in t:
                v.dump_token(f)


    class SuiteBase(TokenTuple):
        __slots__           = (())
        is_statement        = true
        is_statement_header = false


    class CommentSuite(SuiteBase):
        __slots__   =  (())
        indendation = none


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<comment-* +%d', t[0].impression.total), '>'):
                for v in t:
                    v.dump_token(f)


    class EmptyLineSuite(SuiteBase):
        __slots__    = (())
        display_name = 'empty-line-*'
        indendation  = none


        dump_token = dump_token__no_impression


    class MixedSuite(SuiteBase):
        __slots__    = (())
        display_name = 'mixed-*'
        indendation  = none


        dump_token = dump_token__no_impression


    class StatementSuite(SuiteBase):
        __slots__ = (())


        def dump_token(t, f, newline = true):
            assert newline is true

            indendation = (t[0].indentation) or (t[1].indendation)

            with f.indent(arrange('<statement-* ++%d', indentation.total), '>'):
                for v in t:
                    v.dump_token(f)


        if __debug__:
            @property
            def indentation(t):
                indendation = (t[0].indentation) or (t[1].indendation)

                assert indendation is not none

                return indendation
        else:
            @property
            def indentation(t):
                return (t[0].indentation) or (t[1].indendation)


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
