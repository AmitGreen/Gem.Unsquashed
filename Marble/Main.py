#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
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


@gem('Marble.Main')
def gem():
    require_gem('Marble.Core')
    require_gem('Marble.NestedConjure')


    @share
    def main(arguments):
        create_nested_conjure('2017-2018', 'Amit Green')
