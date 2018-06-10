#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Sapphire.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.DumpCache')
    require_gem('Gem.Exception')
    require_gem('Gem.GeneratedConjureQuadruple')
    require_gem('Gem.Herd')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')
    require_gem('Pearl.ActionWord')
    require_gem('Pearl.Atom')
    require_gem('Pearl.ClassOrder')
    require_gem('Pearl.CreateMeta')
    require_gem('Pearl.Elemental')
    require_gem('Pearl.Method')
    require_gem('Pearl.Nub')
    require_gem('Pearl.Tokenizer')


    from Gem import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Gem import empty_herd, path_join, print_cache, print_exception_chain
    from Gem import produce_conjure_dual, produce_conjure_dual__21
    from Gem import produce_conjure_single, produce_conjure_triple
    from Gem import produce_conjure_triple__312, produce_conjure_tuple
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_quadruple__4123
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import program_exit, read_text_from_path, return_self, slice_all, StringOutput
    from Pearl import CLASS_ORDER__NORMAL_TOKEN, CLASS_ORDER__PYTHON_END, CLASS_ORDER__PYTHON_START
    from Pearl import conjure_action_word, conjure_action_word__ends_in_newline, conjure_keyword_import, conjure_nub
    from Pearl import conjure_ActionWord_WithNewlines
    from Pearl import initialize_action_word__Meta, is_name__0, KeywordAndOperatorBase
    from Pearl import KeywordImport
    from Pearl import la, lookup_adjusted_meta, lookup_normal_token, order__s
    from Pearl import parse_context, PearlToken, produce_conjure_action_word, provide_normal_token
    from Pearl import qd, qi, qj, qk, ql, qn, qs, static_conjure_nub, store_adjusted_meta
    from Pearl import raise_unknown_line, wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize


    share(
        #
        #   Imported types (Gem)
        #
        'StringOutput',     StringOutput,

        #
        #   Imported types (Pearl)
        #
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'KeywordImport',            KeywordImport,
        'PearlToken',               PearlToken,

        #
        #   Imported functions (Gem)
        #
        'create_cache',                         create_cache,
        'create_DelayedFileOutput',             create_DelayedFileOutput,
        'create_SimpleStringOutput',            create_SimpleStringOutput,
        'create_StringOutput',                  create_StringOutput,
        'path_join',                            path_join,
        'print_cache',                          print_cache,
        'print_exception_chain',                print_exception_chain,
        'produce_conjure_dual__21',             produce_conjure_dual__21,
        'produce_conjure_dual',                 produce_conjure_dual,
        'produce_conjure_single',               produce_conjure_single,
        'produce_conjure_triple__312',          produce_conjure_triple__312,
        'produce_conjure_triple',               produce_conjure_triple,
        'produce_conjure_tuple',                produce_conjure_tuple,
        'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_quadruple__4123',      produce_conjure_quadruple__4123,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'program_exit',                         program_exit,
        'read_text_from_path',                  read_text_from_path,
        'return_self',                          return_self,


        #
        #   Imported functions (Pearl)
        #
        'conjure_action_word',                      conjure_action_word,
        'conjure_action_word__ends_in_newline',     conjure_action_word__ends_in_newline,
        'conjure_ActionWord_WithNewlines',          conjure_ActionWord_WithNewlines,
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_nub',                              conjure_nub,
        'initialize_action_word__Meta',             initialize_action_word__Meta,
        'is_name__0',                               is_name__0,
        'la',                                       la,
        'lookup_adjusted_meta',                     lookup_adjusted_meta,
        'lookup_normal_token',                      lookup_normal_token,
        'order__s',                                 order__s,
        'produce_conjure_action_word',              produce_conjure_action_word,
        'provide_normal_token',                     provide_normal_token,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
        'static_conjure_nub',                       static_conjure_nub,
        'store_adjusted_meta',                      store_adjusted_meta,
        'wd0',                                      wd0,
        'wd1',                                      wd1,
        'wd',                                       wd,
        'wi',                                       wi,
        'wj',                                       wj,
        'wk',                                       wk,
        'wn',                                       wn,
        'ws',                                       ws,
        'z_initialize',                             z_initialize,


        #
        #   Values (Gem)
        #
        'empty_herd',           empty_herd,
        'slice_all',            slice_all,
        'tuple_of_2_nones',     ((none, none)),


        #
        #   Values (Pearl)
        #
        'CLASS_ORDER__NORMAL_TOKEN',                CLASS_ORDER__NORMAL_TOKEN,
        'CLASS_ORDER__PYTHON_END',                  CLASS_ORDER__PYTHON_END,
        'CLASS_ORDER__PYTHON_START',                CLASS_ORDER__PYTHON_START,
        'parse_context',                            parse_context,
    )
