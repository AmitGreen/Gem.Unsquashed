#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Quartz.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')
    require_gem('Pearl.Comment')
    require_gem('Pearl.Line')
    require_gem('Pearl.Token')
    require_gem('Pearl.Tokenizer')


    from Gem import create_DelayedFileOutput, create_StringOutput, produce_cache_functions, read_text_from_path
    from Gem import stop_iteration
    from Pearl import conjure_token_newline, conjure_tree_comment, create_UnknownLine, EmptyLine
    from Pearl import qj, qk, qs, Token, TokenIndented, wj, wk, z_initialize


    share(
        #
        #   Classes
        #   
        'EmptyLine',                        EmptyLine,
        'Token',                            Token,
        'TokenIndented',                    TokenIndented,


        #
        #   Functions
        #
        'conjure_token_newline',        conjure_token_newline,
        'conjure_tree_comment',         conjure_tree_comment,
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'create_UnknownLine',           create_UnknownLine,
#       'produce_cache_functions',      produce_cache_functions,
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
    )
