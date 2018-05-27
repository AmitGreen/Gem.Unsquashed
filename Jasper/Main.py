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


@gem('Jasper.Main')
def gem():
    require_gem('Jasper.Core')


    choice = 3
    show   = 0


    def command_combine(
            module_name        = 'hma',
            remove_comments    = false,
            remove_indentation = false,
    ):
        require_gem('Jasper.Transform')

        vary = create_jasper_transform(
                   remove_comments    = remove_comments,
                   remove_indentation = remove_indentation,
               )

        if fast_cache is 0:
            require_gem('Jasper.Pattern')

            create_jasper_match()

        require_gem('Jasper.Combine')

        command_combine__X(module_name, vary)

        if fast_cache is not 0:
            for s in sorted_list(fast_cache):
                line('Unused: %s', s)


    def command_development():
        require_gem('Jasper.Development')

        development()


    def command_parse1(
            remove_comments    = false,
            remove_indentation = false,
            show               = 0,
    ):
        require_gem('Jasper.Pattern')

        create_jasper_match()

        require_gem('Jasper.Transform')
        require_gem('Jasper.Parse')                       #   Must be after 'create_jasper_match'

        vary = create_jasper_transform(
                   remove_comments    = remove_comments,
                   remove_indentation = remove_indentation,
               )

        parse_python('test.py', vary = vary, test = 7, show = show)

        #for name in ['arguments-2', 'list-expression-2', 'range-index', 'tuple-expression-2']:
        #    print_cache(name)

        print_cache()


    def test_parse2():
        require_gem('Jasper.Parse2')                      #   Must be after 'create_jasper_match'

        parse2_python_from_path('test2.py')


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return command_parse1()

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'combine':
                return command_combine(
                           module_name        = 'hma',
                           remove_comments    = true,
                           remove_indentation = true,
                       )

            if option == 'combine2':
                return command_combine(module_name = 'hma2')

            if option == 'dev':
                if choice is 1:
                    return command_development()

                if choice is 2:
                    return command_parse1(
                               remove_comments    = true,
                               remove_indentation = true,
                               show               = show,
                           )

                if choice is 3:
                    return command_combine(
                               module_name        = 'hma',
                               remove_comments    = true,
                               remove_indentation = true,
                           )

                raise_runtime_error('unknown choice: %d', choice)

            if option == 'parse':
                return command_parse1(show = 7)

            raise_runtime_error('unknown option: %r', option)

        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
