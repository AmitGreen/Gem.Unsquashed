#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TokenCache')
def gem():
    require_gem('Sapphire.Cache')


    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       arguments_0_token_cache     - '()' that is used as function arguments.
    #
    #       comment_line_cache          - COmment lines (See Sapphire/Whitespace.py)
    #
    #       empty_line_cache            - Empty lines (See Sapphire/Whitespace.py)
    #
    #       indentation_cache           - White space at beginning of a line that is considered indentation.
    #                                     (Also used for dual token Indentation_Token)
    #
    #       join_token_cache            - Whitespace that is used to concatanate strings; Example:
    #
    #                                           "hi"  'there'
    #
    #                                     The two spaces between the two strings are considered an "invisible" join
    #                                     token & are stored in join_token_cache (or 'will be stored', when this
    #                                     feature is implemented)
    #
    #       line_marker_token_cache     - Line markers.  The last '\n is a significant line-maker.
    #
    #                                     Any other '\n' in the strings here is considered whitespace.
    #
    #       normal_token_cache          - Normal tokens.  Any '\n' in the strinss here is considered whitespace.
    #
    #                                     This includes '()' when used as a tuple {where as '()' when used as
    #                                     function arguments or function parameters appears in different caches}.
    #
    #                                     Normal whitespace also appears in this cache (for example whitespace
    #                                     before an atom on a continuation line).
    #   
    #       parameter_token_cache       - '()' that is used as function parameters.
    #
    arguments_0_token_cache = {}
    indentation_cache       = {}
    join_token_cache        = {}
    line_marker_token_cache = {}
    normal_token_cache      = {}
    parameter_token_cache   = {}

    lookup_arguments_0_token = arguments_0_token_cache.get
    lookup_indentation       = indentation_cache      .get
    lookup_join_token        = join_token_cache       .get
    lookup_line_marker       = line_marker_token_cache.get
    lookup_normal_token      = normal_token_cache     .get
    lookup_parameter_token   = parameter_token_cache  .get

    provide_arguments_0_token = arguments_0_token_cache.setdefault
    provide_indentation       = indentation_cache      .setdefault
    provide_join_token        = join_token_cache       .setdefault
    provide_line_marker       = line_marker_token_cache.setdefault
    provide_normal_token      = normal_token_cache     .setdefault
    provide_parameter_token   = parameter_token_cache  .setdefault


    append_cache('arguments-0-token', arguments_0_token_cache)
    append_cache('indentation',       indentation_cache)
    append_cache('join-token',        join_token_cache)
    append_cache('line-marker-token', line_marker_token_cache)
    append_cache('normal-token',      normal_token_cache)
    append_cache('parameter-token',   parameter_token_cache)


    share(
        'lookup_arguments_0_token',     lookup_arguments_0_token,
        'lookup_join_token',            lookup_join_token,
        'lookup_line_marker',           lookup_line_marker,
        'lookup_normal_token',          lookup_normal_token,
        'lookup_parameter_token',       lookup_parameter_token,
        'lookup_indentation',           lookup_indentation,

        'provide_arguments_0_token',    provide_arguments_0_token,
        'provide_join_token',           provide_join_token,
        'provide_line_marker',          provide_line_marker,
        'provide_normal_token',         provide_normal_token,
        'provide_parameter_token',      provide_parameter_token,
        'provide_indentation',          provide_indentation,
    )
