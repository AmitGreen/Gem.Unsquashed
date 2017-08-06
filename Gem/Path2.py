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


    PythonOperatingSystem = import_module('os')
    PythonPath            = import_module('os.path')
    python__rename_path   = PythonOperatingSystem.rename
    python__remove_path   = PythonOperatingSystem.remove


    def adjust_OSError_exception(path, path2 = none):
        [e_type, e, e_traceback] = e_all = exception_information()

        assert e_type is OSError

        arguments = e.args

        if (type(arguments) is Tuple) and (length(arguments) is 2):
            [error_number, message] = arguments

            if (error_number is ERROR_NO_ACCESS) and ((e.filename is none) or (e.filename == path)) and (path2 is none):
                return ((PermissionError, ((error_number, message, path)), e_traceback))

            if (error_number is ERROR_NO_ENTRY) and ((e.filename is none) or (e.filename == path)):
                return ((FileNotFoundError, ((error_number, message, path, path2)), e_traceback))

        return e_all


    @export
    def remove_path(path):
        try:
            python__remove_path(path)
        except OSError as e:
            #
            #   NOTE:
            #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
            #       instead of inside adjust_OSError_exception()
            #
            [e_type, e, e_traceback] = adjust_OSError_exception(path)

            raise e_type, e, e_traceback


    @export
    def rename_path(from_path, to_path):
        try:
            python__rename_path(from_path, to_path)
        except OSError as e:
            #
            #   NOTE:
            #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
            #       instead of inside adjust_OSError_exception()
            #
            [e_type, e, e_traceback] = adjust_OSError_exception(from_path, to_path)

            raise e_type, e, e_traceback
