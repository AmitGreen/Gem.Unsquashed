#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.DelayedFileOutput')
def gem():
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')


    from Gem import create_StringOutput


    class DelayedFileOutput(Object):
        __slots__ = ((
            'path',                     #   String+
            'f',                        #   File
            '_write',                   #   Method
        ))


        def __init__(t, path):
            t.path   = path
            t._write = t.f  = none


        @privileged
        def __enter__(t):
            assert t.f is none

            t.f      = f       = create_StringOutput()
            t._write = f.write

            return t


        def __exit__(t, e_type, e, traceback):
            f        = t.f
            t._write = t.f = none

            if e is not none:
                f.close()
                t.path = none
                return

            data = f.finish()

            path     = t.path
            path_new = t.path_new       #   Grab t.path_new & t.path_old before zapping t.path
            path_old = t.path_old

            t.path = none

            write_binary_to_path(path_new, data)
            remove_path__ignore_file_not_found(path_old)
            rename_path__ignore_file_not_found(path, path_old)
            rename_path(path_new, path)


        def line(t, format = none, *arguments):
            if format is none:
                assert length(arguments) is 0

                t._write('\n')
                return

            t._write((format % arguments   if arguments else   format) + '\n')


        @property
        def path_new(t):
            return arrange('%s.new', t.path)


        @property
        def path_old(t):
            return arrange('%s.old', t.path)


    export(
        'create_DelayedFileOutput',     DelayedFileOutput,
    )
