#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
def boot(module_name):
    #test
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


    def test_development(module_name = 'hma', remove_comments = false):
        if fast_cache is 0:
            require_gem('Sapphire.Pattern')

            create_sapphire_match()

        require_gem('Sapphire.Development')

        development(module_name, remove_comments)

        if fast_cache is not 0:
            for s in sorted_list(fast_cache):
                line('Unused: %s', s)


    def test_parse1():
        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        parse_python('test.py', test = 7)


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
            
            if option == 'rc':
                return test_development(module_name = 'hma2', remove_comments = true)

            if option == 'dev':
                if 1:
                    return test_development(module_name = 'hma', remove_comments = true)

                return test_parse1()

            if option == 'x':
                return test_development(module_name = 'hma2')

            raise_runtime_error('unknown option: %r', option)

        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
