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


    depth = 1


    @share
    def main():
        try:
            #for k in introspection(Gem):
            #    print k

            create_sapphire_match()

            if (depth == 7) or (depth == 99):
                require_gem('Sapphire.Parse7')                      #   Must be after 'create_sapphire_match'

                parse7_python_from_path('../Sapphire/Main.py')

            if (depth == 1) or (depth == 99):
                require_gem('Sapphire.Parse1')                      #   Must be after 'create_sapphire_match'

                parse1_python_from_path('test.py')
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
