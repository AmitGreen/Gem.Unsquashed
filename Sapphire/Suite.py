#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    suite_cache   = {}
    provide_suite = suite_cache.setdefault


    def find_require_gem__many(t, e):
        for v in t:
            v.find_require_gem(e)


    def dump_token__no_impression(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s', t.display_name), '>'):
            for v in t:
                v.dump_token(f)


    def dump_token__many(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s +%d', t.display_name, t[0].indentation.total), '>'):
            for v in t:
                v.dump_token(f)


    @property
    def indentation__index_0(t):
        return t[0].indentation


    class CommentSuite(TokenTuple):
        __slots__                  = (())
        indentation                = none
        is_any_else                = false
        is_any_except_or_finally   = false
        is_comment_suite           = true
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<comment-* +%d', t[0].impression.total), '>'):
                for v in t:
                    v.dump_token(f)


        @property
        def impression(t):
            return t[0].impression


    class EmptyLineSuite(TokenTuple):
        __slots__                  = (())
        display_name               = 'empty-line-*'
        impression                 = 0
        indentation                = none
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_empty_line_suite        = true
        is_statement_header        = false
        is_statement               = true

        dump_token       = dump_token__no_impression
        find_require_gem = find_require_gem__0


    class IfStatement_Many(TokenTuple):
        __slots__                  = (())
        display_name               = 'if-statement-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true

        dump_token       = dump_token__many
        find_require_gem = find_require_gem__many
        indentation      = indentation__index_0


    class MixedSuite(TokenTuple):
        __slots__                  = (())
        display_name               = 'mixed-*'
        indentation                = none
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true

        dump_token       = dump_token__no_impression
        find_require_gem = find_require_gem__0


    class StatementSuite(TokenTuple):
        __slots__                  = (())
        display_name               = 'statement-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        is_statement_suite         = true


        def dump_token(t, f, newline = true):
            assert newline is true

            indentation = (t[0].indentation) or (t[1].indentation)

            assert indentation is not none

            with f.indent(arrange('<statement-* ++%d', indentation.total), '>'):
                for v in t:
                    v.dump_token(f)


        find_require_gem = find_require_gem__many


        if __debug__:
            @property
            def indentation(t):
                indentation = (t[0].indentation) or (t[1].indentation)

                assert indentation is not none

                return indentation
        else:
            @property
            def indentation(t):
                return (t[0].indentation) or (t[1].indentation)


    class TryStatement_Many(TokenTuple):
        __slots__                  = (())
        display_name               = 'try-statement-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true

        dump_token       = dump_token__many
        find_require_gem = find_require_gem__many
        indentation      = indentation__index_0


    conjure_comment_suite     = produce_conjure_tuple('comment-*',      CommentSuite,     suite_cache, provide_suite)
    conjure_empty_line_suite  = produce_conjure_tuple('empty-line-*',   EmptyLineSuite,   suite_cache, provide_suite)
    conjure_if_statement_many = produce_conjure_tuple('if-statement-*', IfStatement_Many, suite_cache, provide_suite)
    conjure_mixed_suite       = produce_conjure_tuple('mixed-*',        MixedSuite,       suite_cache, provide_suite)
    conjure_statement_suite   = produce_conjure_tuple('statement-*',    StatementSuite,   suite_cache, provide_suite)

    conjure_try_statement_many = produce_conjure_tuple(
                                     'try-statement-*',
                                     TryStatement_Many,
                                     suite_cache,
                                     provide_suite,
                                 )


    append_cache('suite', suite_cache)


    share(
        'conjure_comment_suite',        conjure_comment_suite,
        'conjure_empty_line_suite',     conjure_empty_line_suite,
        'conjure_if_statement_many',    conjure_if_statement_many,
        'conjure_mixed_suite',          conjure_mixed_suite,
        'conjure_statement_suite',      conjure_statement_suite,
        'conjure_try_statement_many',   conjure_try_statement_many,
    )
