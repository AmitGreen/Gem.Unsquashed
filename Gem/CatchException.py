#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.CatchException')
def gem():
    require_gem('Gem.ErrorNumber')
    require_gem('Gem.Exception')


    class CatchFileNotFoundException(Object):
        __slots__ = ((
            'exception_type',           #   Type
            'error_number',             #   Integer
            'path',                     #   String+
            'path2',                    #   String+
            'caught',                   #   None | FileNotFoundError
        ))


        def __init__(t, exception_type, error_number, path, path2):
            t.exception_type = exception_type
            t.error_number   = error_number
            t.path           = path
            t.path2          = path2
            t.caught         = none


        def __bool__(t):
            return t.caught is not none


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, traceback):
            if e_type is t.exception_type:
                arguments = e.args

                if (
                        type(arguments)   is Tuple
                    and length(arguments) is 2
                    and arguments[0]      == t.error_number
                    and e.filename        == t.path
                ):
                    t.caught = e

                    return true


        def __repr__(t):
            return arrange('<CatchException %r %r>', t.exception_type, t.caught)


        if is_python_2:
            __nonzero__ = __bool__


    @export
    def catch_FileNotFoundError(path, path2 = none):
        return CatchFileNotFoundException(FileNotFoundError, ERROR_NO_ENTRY, path, path2)
