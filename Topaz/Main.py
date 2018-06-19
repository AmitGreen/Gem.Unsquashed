#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    module_path.insert(1, path_absolute(path_join(module_path[0], '..')))


    import Gem


@gem('Topaz.Main')
def gem():
    require_gem('Topaz.ConjureDual')
    require_gem('Topaz.ConjureQuadruple')
    require_gem('Topaz.ConjureSingle')
    require_gem('Topaz.ConjureTreeComment')
    require_gem('Topaz.ConjureTriple')
    require_gem('Topaz.Drove')
    require_gem('Topaz.ExceptionChain')
    require_gem('Topaz.Herd')
    require_gem('Topaz.Path')
    require_gem('Topaz.Pattern')
    require_gem('Topaz.PortrayString')
    require_gem('Topaz.Sequence')
    require_gem('Topaz.Series')
    require_gem('Topaz.StringOutput')


    @share
    def main(arguments):
        test_conjure_dual()
        test_conjure_quadruple()
        test_conjure_single()
        test_conjure_triple()
        test_conjure_tree_comment()
        test_drove()
        test_herd()
        test_pattern()
        test_portray_raw_string()
        test_remove_path()
        test_rename_path()
        test_sequence()
        test_series()
        test_string_output()
        test_exception_chain()
