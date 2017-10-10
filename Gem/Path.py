#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Path')
def gem():
    show = 0


    require_gem('Gem.CatchException')

    if is_python_3:
        require_gem('Gem.Codec')

    require_gem('Gem.ErrorNumber')
    require_gem('Gem.Import')

    if show is 7:
        require_gem('Gem.Traceback')


    PythonOperatingSystem = import_module('os')
    PythonPath            = import_module('os.path')


    open_path = PythonBuiltIn.open


    if is_python_2:
        PythonOperatingSystem = import_module('os')
        PythonPath            = import_module('os.path')
        python__rename_path   = PythonOperatingSystem.rename
        python__remove_path   = PythonOperatingSystem.remove


        def adjust_OSError_exception(e, path, path2 = none):
            assert type(e) is OSError

            arguments = e.args

            if (type(arguments) is Tuple) and (length(arguments) is 2):
                [error_number, message] = arguments

                if (
                        error_number is ERROR_NO_ACCESS
                    and ((e.filename is none) or (e.filename == path))
                    and path2 is none
                ):
                    r = PermissionError(error_number, message, path)
                    r.__cause__            = e.__cause__
                    r.__context__          = e.__context__
                    r.__suppress_context__ = e.__suppress_context__
                    r.__traceback__        = e.__traceback__
                    return r

                if (error_number is ERROR_NO_ENTRY) and ((e.filename is none) or (e.filename == path)):
                    r = FileNotFoundError(error_number, message, path, path2)
                    r.__cause__            = e.__cause__
                    r.__context__          = e.__context__
                    r.__suppress_context__ = e.__suppress_context__
                    r.__traceback__        = e.__traceback__
                    return r

            return e

        scope = {
                    'adjust_OSError_exception'    : adjust_OSError_exception,
                    'catch_OSError__FileNotFound' : catch_OSError__FileNotFound,
                    'export'                      : export,
                    'python__remove_path'         : python__remove_path,
                    'python__rename_path'         : python__rename_path,
                    'raising_exception_from'      : raising_exception_from,
                    'type'                        : type,
                }

        exec("""
if 7 is 7:
    def wrapper(
            adjust_OSError_exception    = adjust_OSError_exception,
            catch_OSError__FileNotFound = catch_OSError__FileNotFound,
            export                      = export,
            python__remove_path         = python__remove_path,
            python__rename_path         = python__rename_path,
            raising_exception_from      = raising_exception_from,
            type                        = type,
    ):
        @export
        def remove_path(path):
            with catch_OSError__FileNotFound(path) as cup:
                python__remove_path(path)

            if cup.caught:
                with cup.handle_exception() as e0:
                    #
                    #   NOTE:
                    #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
                    #       instead of inside adjust_OSError_exception()
                    #
                    e = adjust_OSError_exception(e0, path)

                    e_type      = type(e)
                    e_traceback = e.__traceback__

                    if e is not e0:
                        raising_exception_from(e, none)

                    raise e_type, e, e_traceback

                del e0


        @export
        def rename_path(from_path, to_path):
            #
            #   NOTE:
            #       In Python 2.0 'os.rename' throws an OSError with '.filename' set to none when the rename fails;
            #       hence the first paramater to catch_OSError__FileNotFound is set to none.
            #
            with catch_OSError__FileNotFound(none) as cup:
                python__rename_path(from_path, to_path)

            if cup.caught:
                with cup.handle_exception() as e0:
                    #
                    #   NOTE:
                    #       To avoid adding an extra frame in the traceback, the 'raise' must be issued in this function,
                    #       instead of inside adjust_OSError_exception()
                    #
                    e = adjust_OSError_exception(e0, from_path, to_path)

                    e_type      = type(e)
                    e_traceback = e.__traceback__

                    if e is not e0:
                        raising_exception_from(e, none)

                    raise e_type, e, e_traceback

                del e0


    wrapper()
""",
            scope,
            scope,
        )

        from Gem import rename_path, remove_path
    else:
        rename_path = PythonOperatingSystem.rename
        remove_path = PythonOperatingSystem.remove


        export(
            'remove_path',  remove_path,
            'rename_path',  rename_path,
        )


    @export
    @privileged_2
    def read_text_from_path(path):
        with open_path(path, 'r') as f:
            return f.read()


    if is_python_2:
        @export
        @privileged_2
        def write_binary_to_path(path, data):
            with open_path(path, 'wb') as f:
                return f.write(data)
    else:
        @export
        @privileged_2
        def write_binary_to_path(path, data):
            if type(data) is String:
                data = encode_ascii(data)

            with open_path(path, 'wb') as f:
                return f.write(data)


    @export
    def remove_path__ignore_file_not_found(path):
        with catch_FileNotFoundError(path) as e:
            remove_path(path)

        return e.caught is none


    @export
    def rename_path__ignore_file_not_found(from_path, to_path):
        with catch_FileNotFoundError(from_path, to_path) as e:
            rename_path(from_path, to_path)

        if show is 7:
            if e.caught is not none:
                line('=== rename_path__ignore_file_not_found(%s, %s) ===', from_path, to_path)
                print_exception_chain(e.caught)


        return e.caught is none


    export(
        'path_basename',            PythonPath.basename,
        'path_join',                PythonPath.join,
        'path_split_extension',     PythonPath.splitext,
    )

    restricted(
        'open_path',    PythonBuiltIn.open,
    )
