#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')
    require_gem('Pearl.Tokenizer')


    from Gem import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Gem import dump_caches, path_join, print_exception_chain
    from Gem import produce_conjure_dual, produce_conjure_dual__21, produce_conjure_quadruple__4123
    from Gem import produce_conjure_single, produce_conjure_triple, produce_conjure_triple__213
    from Gem import produce_conjure_triple__312, produce_conjure_tuple, produce_conjure_unique_dual
    from Gem import program_exit, read_text_from_path, return_self, slice_all, StringOutput
    from Pearl import la, parse_context, qd, qi, qj, qk, ql, qn, qs, raise_unknown_line
    from Pearl import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize


    share(
        #
        #   Imported types
        #
        'StringOutput',                     StringOutput,

        #
        #   Imported functions
        #
        'create_cache',                     create_cache,
        'create_DelayedFileOutput',         create_DelayedFileOutput,
        'create_SimpleStringOutput',        create_SimpleStringOutput,
        'create_StringOutput',              create_StringOutput,
        'dump_caches',                      dump_caches,
        'la',                               la,
        'path_join',                        path_join,
        'print_exception_chain',            print_exception_chain,
        'produce_conjure_dual__21',         produce_conjure_dual__21,
        'produce_conjure_dual',             produce_conjure_dual,
        'produce_conjure_quadruple__4123',  produce_conjure_quadruple__4123,
        'produce_conjure_single',           produce_conjure_single,
        'produce_conjure_triple__213',      produce_conjure_triple__213,
        'produce_conjure_triple__312',      produce_conjure_triple__312,
        'produce_conjure_triple',           produce_conjure_triple,
        'produce_conjure_tuple',            produce_conjure_tuple,
        'produce_conjure_unique_dual',      produce_conjure_unique_dual,
        'program_exit',                     program_exit,
        'qd',                               qd,
        'qi',                               qi,
        'qj',                               qj,
        'qk',                               qk,
        'ql',                               ql,
        'qn',                               qn,
        'qs',                               qs,
        'raise_unknown_line',               raise_unknown_line,
        'read_text_from_path',              read_text_from_path,
        'return_self',                      return_self,
        'wd0',                              wd0,
        'wd1',                              wd1,
        'wd',                               wd,
        'wi',                               wi,
        'wj',                               wj,
        'wk',                               wk,
        'wn',                               wn,
        'ws',                               ws,
        'z_initialize',                     z_initialize,


        #
        #   Values
        #
        'parse_context',        parse_context,
        'slice_all',            slice_all,
        'tuple_of_2_nones',     ((none, none)),
    )
