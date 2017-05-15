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
    require_gem('Pearl.Line')
    require_gem('Pearl.Token')
    require_gem('Pearl.Tokenizer')


    from Gem import create_DelayedFileOutput, create_StringOutput, produce_cache_functions, stop_iteration
    from Gem import read_text_from_path
    from Pearl import create_UnknownLine, EmptyLine, PoundSignComment, IndentedPoundSignComment
    from Pearl import qj, qk, qs, Token, TokenIndented, TokenNewline
    from Pearl import wj, wk, z_initialize


    share(
        #
        #   Classes
        #   
        'EmptyLine',                    EmptyLine,
        'IndentedPoundSignComment',     IndentedPoundSignComment,
        'PoundSignComment',             PoundSignComment,
        'Token',                        Token,
        'TokenIndented',                TokenIndented,
        'TokenNewline',                 TokenNewline,


        #
        #   Imported functions
        #
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
