#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')
    require_gem('Pearl.Comment')
    require_gem('Pearl.Token')
    require_gem('Pearl.Tokenizer')


    from Gem import create_DelayedFileOutput, create_StringOutput, produce_cache_functions, stop_iteration
    from Gem import read_text_from_path
    from Pearl import conjure_token_newline, create_UnknownLine, qj, qk, qs, Token, wj, wk, z_initialize


    share(
        #
        #   Classes
        #
        'Token',                        Token,


        #
        #   Imported functions
        #
        'conjure_token_newline',        conjure_token_newline,
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'create_UnknownLine',           create_UnknownLine,
        'produce_cache_functions',      produce_cache_functions,
        'qj',                           qj,
        'qk',                           qk,
        'qs',                           qs,
        'read_text_from_path',          read_text_from_path,
        'wj',                           wj,
        'wk',                           wk,
        'z_initialize',                 z_initialize,

        #
        #   Values
        #
        'stop_iteration',               stop_iteration,
        'tuple_of_2_nones',             ((none, none)),
        'tuple_of_3_nones',             ((none, none, none)),
    )
