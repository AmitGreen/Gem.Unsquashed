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


    def test_development():
        if gem_fast is 0:
            create_sapphire_match()

        require_gem('Sapphire.Development')

        development()


    def test_parse1():
        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        path = 'test.py'

        parse_python(path)


    def test_parse2():
        require_gem('Sapphire.Parse2')                      #   Must be after 'create_sapphire_match'

        parse2_python_from_path('test2.py')


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return test_parse1()

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]
            
            if option == 'dev':
                if 7:
                    return test_development()

                return test_parse1()

            raise_runtime_error('unknown option: %r', option)

        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
