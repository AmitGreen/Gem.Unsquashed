#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TokenCache')
def gem():
    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       arguments_0_token_cache     - '()' that is used as function arguments.
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
    arguments_0_token_cache = {}
    indentation_token_cache = {}
    join_token_cache        = {}
    line_marker_token_cache = {}
    normal_token_cache      = {}
    parameter_token_cache   = {}

    lookup_arguments_0_token = arguments_0_token_cache.get
    lookup_indentation_token = indentation_token_cache.get
    lookup_join_token        = join_token_cache       .get
    lookup_line_marker       = line_marker_token_cache.get
    lookup_normal_token      = normal_token_cache     .get
    lookup_parameter_token   = parameter_token_cache  .get

    provide_arguments_0_token = arguments_0_token_cache.setdefault
    provide_indentation_token = indentation_token_cache.setdefault
    provide_join_token        = join_token_cache       .setdefault
    provide_line_marker_token = line_marker_token_cache.setdefault
    provide_normal_token      = normal_token_cache     .setdefault
    provide_parameter_token   = parameter_token_cache  .setdefault


    if __debug__:
        def dump_cache(cache):
            for k in sorted_list(v.s   for v in view_values(cache)):
                line('%s:', portray_string(k))
                line('  %r', cache[k])


        @share
        def dump_token_caches():
            line('===  Arguments_0  ===')
            dump_cache(arguments_0_token_cache)

            line()
            line('===  Line_Marker  ===')
            dump_cache(line_marker_token_cache)


    share(
        'lookup_arguments_0_token',     lookup_arguments_0_token,
        'lookup_indentation_token',     lookup_indentation_token,
        'lookup_join_token',            lookup_join_token,
        'lookup_line_marker',           lookup_line_marker,
        'lookup_normal_token',          lookup_normal_token,
        'lookup_parameter_token',       lookup_parameter_token,
        'provide_arguments_0_token',    provide_arguments_0_token,
        'provide_indentation_token',    provide_indentation_token,
        'provide_join_token',           provide_join_token,
        'provide_line_marker_token',    provide_line_marker_token,
        'provide_normal_token',         provide_normal_token,
        'provide_parameter_token',      provide_parameter_token,
    )
