#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Traceback')
def gem():
    require_gem('Gem.Import')
    require_gem('Gem.Output')


    PythonTraceback = import_module('traceback')


    python_print_exception = PythonTraceback.print_exception


    @export
    def print_exception(e):
        assert is_instance(e, BaseException)

        e_type      = type(e)
        e_traceback = e.__traceback__

        assert type(e_traceback) is Traceback

        flush_standard_output()
        python_print_exception(e_type, e, e_traceback)
        flush_standard_error()
