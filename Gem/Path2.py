#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
#   NOTE:
#       Due to the fact that python 3.0 rejects 'raise' with three parameters, this code is in a seperate file
#       only used by Python 2.
#
@gem('Gem.Path2')
def gem():
    require_gem('Gem.ErrorNumber')
    require_gem('Gem.Import')


    assert is_python_2


    PythonOperatingSystem = import_module('os')
    PythonPath            = import_module('os.path')
    python__rename_path   = PythonOperatingSystem.rename
    python__remove_path   = PythonOperatingSystem.remove


    def adjust_OSError_exception(e, path, path2 = none):
        assert type(e) is OSError

        arguments = e.args

        if (type(arguments) is Tuple) and (length(arguments) is 2):
            [error_number, message] = arguments

            if (error_number is ERROR_NO_ACCESS) and ((e.filename is none) or (e.filename == path)) and (path2 is none):
                r = PermissionError(error_number, message, path)
                r.__context__   = e
                r.__traceback__ = e.__traceback__
                return r

            if (error_number is ERROR_NO_ENTRY) and ((e.filename is none) or (e.filename == path)):
                r = FileNotFoundError(error_number, message, path, path2)
                r.__context__   = e
                r.__traceback__ = e.__traceback__
                return r

        return e


    @export
    def remove_path(path):
        try:
            python__remove_path(path)
        except OSError as e:
            caught_exception(e)

            #
            #   NOTE:
            #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
            #       instead of inside adjust_OSError_exception()
            #
            e = adjust_OSError_exception(e, path)

            e_type      = type(e)
            e_traceback = e.__traceback__

            raise e_type, e, e_traceback


    @export
    def rename_path(from_path, to_path):
        try:
            python__rename_path(from_path, to_path)
        except OSError as e:
            caught_exception(e)

            #
            #   NOTE:
            #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
            #       instead of inside adjust_OSError_exception()
            #
            e = adjust_OSError_exception(e, from_path, to_path)

            e_type      = type(e)
            e_traceback = e.__traceback__

            raise e_type, e, e_traceback
