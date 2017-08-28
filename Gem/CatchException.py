#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.CatchException')
def gem():
    show = 0


    require_gem('Gem.ErrorNumber')
    require_gem('Gem.Exception')


    if is_python_3:
        #
        #   Since Python 3.* does not know about our special exception handling it sets
        #   the .__context__ of top-most thrown exception to the previous exception.
        #
        #   This code replaces the automatically assigned .__context__ with '.e' (i.e.:
        #   inserting our exception into the chain of exceptions).
        #
        #   NOTE:
        #       The previous exception has to be extracted with *BEFORE* .__exit__ is called
        #       (after .__exit__ is called the previous exception can no longer be found;
        #       as the current exception is returned by sys.exc_info (aka: exception_information))
        #
        class HandleException(Object):
            __slots__ = ((
                'e',                    #   BaseException
            ))


            def __init__(t, e):
                assert is_instance(e, BaseException)

                t.e = e


            def __enter__(t):
                return t.e


            def __exit__(t, e_type, e, e_traceback):
                if e_type is none:
                    assert e is e_traceback is none
                    return

                assert e_type is type(e)
                assert is_instance(e, BaseException)
                assert type(e_traceback) is Traceback

                previous = t.e.__context__

                if show is 7:
                    line('handle_exception: %s; previous: %s', e, previous)

                while 1:
                    context = e.__context__

                    if show is 7:
                        line('handle_exception: %s; context: %s', e, context)

                    if (context is none) or (context is previous):
                        e.__context__ = t.e

                        if show is 7:
                            line('handle_exception: %s; replaced context with: %s', e, t.e)

                        return

                    e = context


    class CatchOsError(Object):
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


        if is_python_3:
            def __exit__(t, e_type, e, traceback):
                if e_type is t.exception_type:
                    arguments = e.args

                    if (
                            type(arguments)   is Tuple
                        and length(arguments) is 2
                        and arguments[0]      == t.error_number
                        and e.filename        == t.path
                        and e.filename2       == t.path2
                    ):
                        t.caught = e                                    #   Python 3.* has 'fixed up' the exception

                        return true
        else:
            def __exit__(t, e_type, e, e_traceback):
                if e_type is t.exception_type:
                    arguments = e.args

                    if (
                            type(arguments)   is Tuple
                        and length(arguments) is 2
                        and arguments[0]      == t.error_number
                        and e.filename        == t.path
                        #and e.filename2      == t.path2                #   .filename2 does not appear in Python 2.*
                    ):
                        t.caught = fixup_caught_exception(              #   Only need this in Python 2.*
                                       e, e_traceback,
                                   )

                        return true


        def __repr__(t):
            return arrange('<CatchOsError %r %r>', t.exception_type, t.caught)


        if is_python_3:
            def handle_exception(t):
                assert t.caught is not none

                e = t.caught

                t.caught = none

                return HandleException(e)         #   Special override of automatic Python 3.* exception handling
        else:
            def handle_exception(t):
                assert t.caught is not none

                e = t.caught

                t.caught = none

                return CaughtExceptionContext(e)    #   Normal implementation of Python 2.* exception handling


        def cleanup(t):
            t.caught = none


        if is_python_2:
            __nonzero__ = __bool__


    @export
    def catch_FileNotFoundError(path, path2 = none):
        return CatchOsError(FileNotFoundError, ERROR_NO_ENTRY, path, path2)


    if is_python_2:
        @export
        def catch_OSError__FileNotFound(path):
            return CatchOsError(OSError, ERROR_NO_ENTRY, path, none)
