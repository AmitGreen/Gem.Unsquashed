#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
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
    module_path.insert(2, path_absolute(path_join(module_path[0], '../../Gem-py')))


    import Gem


@gem('Onyx.Main')
def gem():
    require_gem('Onyx.Core')
    require_gem('Onyx.Development')


    @share
    def main(arguments):
        command_development()
