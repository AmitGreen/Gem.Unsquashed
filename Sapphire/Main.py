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


@gem('Sapphire.Main')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Pattern')


    @share
    def main():
        create_sapphire_match()

        require_gem('Sapphire.Parse')               #   Must be after 'create_sapphire_match'

        #parse_python_from_path('test.py')
        parse_python_from_path('../Sapphire/Main.py')
        #parse_python_from_path('../Gem/Absent.py')
