#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Traceback')
def gem():
    require_gem('Gem.Import')
    require_gem('Gem.Output')


    PythonTraceback = import_module('traceback')


    python_print_exception = PythonTraceback.print_exception


    if is_python_3:
        @export
        def print_exception_chain(e):
            assert is_instance(e, BaseException)

            e_type      = type(e)
            e_traceback = e.__traceback__

            assert type(e_traceback) is Traceback

            flush_standard_output()
            python_print_exception(e_type, e, e_traceback)
            flush_standard_error()
    else:
        def print_single_exception(e):
            assert is_instance(e, BaseException)

            e_type = type(e)

            if '__cause__' not in e.__dict__:
                python_print_exception(e_type, e, none)
                return

            cause = e.__cause__

            if cause is not none:
                print_single_exception(cause)

                write_standard_error(
                          '\n'
                        + 'The above exception was the direct cause of the following exception:\n'
                        + '\n'
                    )

            elif e.__suppress_context__:
                pass
            else:
                context = e.__context__

                if context is not none:
                    print_single_exception(context)

                    write_standard_error(
                              '\n'
                            + 'During handling of the above exception, another exception occurred:\n'
                            + '\n'
                        )


            python_print_exception(e_type, e, e.__traceback__)

            
        @export
        def print_exception_chain(e):
            flush_standard_output()
            print_single_exception(e)
            flush_standard_error()
