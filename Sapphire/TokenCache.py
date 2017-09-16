#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TokenCache')
def gem():
    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       argument_token_cache        - '()' that is used as function arguments.
    #
    #       indentation_token_cache     - White space at beginning of a line that is considered indentation.
    #
    #       join_token_cache            - Whitespace that is used to concatanate strings; Example:
    #
    #                                           "hi"  'there'
    #
    #                                     The two spaces between the two strings are considered an "invisible" join
    #                                     token & are stored in join_token_cache.
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
    argument_token_cache    = {}
    indentation_token_cache = {}
    join_token_cache        = {}
    line_marker_token_cache = {}
    normal_token_cache      = {}
    parameter_token_cache   = {}

    lookup_argument_token    = argument_token_cache   .get
    lookup_indentation_token = indentation_token_cache.get
    lookup_join_token        = join_token_cache       .get
    lookup_line_marker_token = line_marker_token_cache.get
    lookup_normal_token      = normal_token_cache     .get
    lookup_parameter_token   = parameter_token_cache  .get
    lookup_argument_token    = argument_token_cache   .get

    provide_indentation_token = indentation_token_cache.setdefault
    provide_join_token        = join_token_cache       .setdefault
    provide_line_marker_token = line_marker_token_cache.setdefault
    provide_normal_token      = normal_token_cache     .setdefault
    provide_parameter_token   = parameter_token_cache  .setdefault


    if __debug__:
        @share
        def dump_line_markers():
            for k in sorted_list(v.s   for v in view_values(line_marker_token_cache)):
                line('%r', line_marker_token_cache[k])


    share(
        'lookup_argument_token',        lookup_argument_token,
        'lookup_indentation_token',     lookup_indentation_token,
        'lookup_join_token',            lookup_join_token,
        'lookup_line_marker_token',     lookup_line_marker_token,
        'lookup_normal_token',          lookup_normal_token,
        'lookup_parameter_token',       lookup_parameter_token,
        'lookup_argument_token',        lookup_argument_token,
        'provide_indentation_token',    provide_indentation_token,
        'provide_join_token',           provide_join_token,
        'provide_line_marker_token',    provide_line_marker_token,
        'provide_normal_token',         provide_normal_token,
        'provide_parameter_token',      provide_parameter_token,
    )
