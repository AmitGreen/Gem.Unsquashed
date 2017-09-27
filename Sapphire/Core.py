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
    require_gem('Gem.System')
    require_gem('Gem.Traceback')
    require_gem('Pearl.Tokenizer')


    from Gem import create_DelayedFileOutput, create_StringOutput, print_exception_chain, produce_conjure_by_name
    from Gem import produce_dual_cache, produce_dual_cache__12A, produce_dual_cache__21, produce_quadruple_cache, produce_triple_cache
    from Gem import program_exit, read_text_from_path
    from Pearl import la, parse_context, qd, qi, qj, qk, ql, qn, qs, raise_unknown_line
    from Pearl import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'la',                           la,
        'print_exception_chain',        print_exception_chain,
        'produce_conjure_by_name',      produce_conjure_by_name,
        'produce_dual_cache__12A',      produce_dual_cache__12A,
        'produce_dual_cache__21',       produce_dual_cache__21,
        'produce_dual_cache',           produce_dual_cache,
        'produce_quadruple_cache',      produce_quadruple_cache,
        'produce_triple_cache',         produce_triple_cache,
        'program_exit',                 program_exit,
        'qd',                           qd,
        'qi',                           qi,
        'qj',                           qj,
        'qk',                           qk,
        'ql',                           ql,
        'qn',                           qn,
        'qs',                           qs,
        'raise_unknown_line',           raise_unknown_line,
        'read_text_from_path',          read_text_from_path,
        'wd0',                          wd0,
        'wd1',                          wd1,
        'wd',                           wd,
        'wi',                           wi,
        'wj',                           wj,
        'wk',                           wk,
        'wn',                           wn,
        'ws',                           ws,
        'z_initialize',                 z_initialize,


        #
        #   Values
        #
        'parse_context',        parse_context,
        'tuple_of_2_nones',     ((none, none)),
    )
