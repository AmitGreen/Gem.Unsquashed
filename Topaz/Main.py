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
    require_gem('Topaz.Cache')
    require_gem('Topaz.ConjureTreeComment')
    require_gem('Topaz.ExceptionChain')
    require_gem('Topaz.Path')
    require_gem('Topaz.Pattern')
    require_gem('Topaz.PortrayString')
    require_gem('Topaz.StringOutput')


    @share
    def main(arguments):
        test_cache()
        test_conjure_tree_comment()
        test_pattern()
        test_portray_raw_string()
        test_remove_path()
        test_rename_path()
        test_string_output()
        #test_exception_chain()
