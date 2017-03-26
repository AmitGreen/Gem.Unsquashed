#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.StringOutput')
def gem():
    require_gem('Gem.SimpleStringIO')


    class StringOutput(Object):
        __slots__ = ((
            'f',                        #   StringIO
            'write',                    #   Method
        ))


        def __init__(t, f):
            t.f     = f
            t.write = f.write


        def close(t):
            f       = t.f
            t.write = t.f = none

            if f is not none:
                f.close()


        def finish(t):
            r = t.f.getvalue()

            t.close()

            return r


        def line(t, format = none, *arguments):
            if format is none:
                assert length(arguments) is 0

                t.write('\n')
                return

            t.write((format % arguments   if arguments else   format) + '\n')


    @export
    def create_StringOutput():
        return StringOutput(create_SimpleStringOutput())
