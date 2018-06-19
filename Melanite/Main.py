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


@gem('Melanite.Main')
def gem():
    require_gem('Melanite.Core')


    def command_development():
        raise_runtime_error('incomplete: command_development')


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return command_development()

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'dev':
                return command_development()

            raise_runtime_error('unknown option: %r', option)
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
