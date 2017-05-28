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


    from Gem import create_DelayedFileOutput, create_StringOutput, produce_cache_functions, stop_iteration
    from Gem import read_text_from_path
    from Pearl import conjure_token_newline, construct__comment, construct__indented_comment, create_UnknownLine
    from Pearl import display__comment, display__indented_comment
    from Pearl import EmptyLine, IndentedPoundSignCommentLine
    from Pearl import PoundSignCommentLine, qj, qk, qs, Token, TokenIndented
    from Pearl import slots__comment, slots__indented_comment
    from Pearl import wj, wk, write__comment, write__indented_comment, z_initialize


    share(
        #
        #   Classes
        #   
        'EmptyLine',                        EmptyLine,
        'IndentedPoundSignCommentLine',     IndentedPoundSignCommentLine,
        'PoundSignCommentLine',             PoundSignCommentLine,
        'Token',                            Token,
        'TokenIndented',                    TokenIndented,


        #
        #   Functions
        #
        'conjure_token_newline',        conjure_token_newline,
        'construct__comment',           construct__comment,
        'construct__indented_comment',  construct__indented_comment,
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'create_UnknownLine',           create_UnknownLine,
        'display__comment',             display__comment,
        'display__indented_comment',    display__indented_comment,
#       'produce_cache_functions',      produce_cache_functions,
        'qj',                           qj,
        'qk',                           qk,
        'qs',                           qs,
        'read_text_from_path',          read_text_from_path,
        'wj',                           wj,
        'wk',                           wk,
        'write__comment',               write__comment,
        'write__indented_comment',      write__indented_comment,
        'z_initialize',                 z_initialize,


        #
        #   Values
        #
        'slots__comment',               slots__comment,
        'slots__indented_comment,',     slots__indented_comment,
        'stop_iteration',               stop_iteration,
    )
