#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.StringOutput')
def gem():
    require_gem('Gem.SimpleStringIO')


    class Indent(Object):
        __slots__ = ((
            'f',                        #   StringOutput
            'old_prefix',               #   String
            'ending',                   #   None | String
            'prefix',                   #   String
        ))


        def __init__(t, f, ending, prefix):
            t.f          = f
            t.old_prefix = f.prefix
            t.ending     = ending
            t.prefix     = prefix


        def __enter__(t):
            t.f.prefix += t.prefix

            return t


        def __exit__(t, e_type, e, e_traceback):
            t.f.prefix = t.old_prefix

            if e is none:
                if t.ending is not none:
                    if t.f.position is 1:
                        t.f.line()

                    t.f.line(t.ending)


    @export
    class StringOutput(Object):
        __slots__ = ((
            'f',                        #   StringIO
            'prefix',                   #   String
            'result',                   #   None | String
            '_blank',                   #   Integer
            'position',                 #   Integer
            'write',                    #   Method
        ))


        def __init__(t, f):
            t.f        = f
            t.prefix   = ''
            t.result   = none
            t._blank   = -1
            t.position = 0
            t.write    = f.write


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, e_traceback):
            if e_type is none:
                t.finish()
            else:
                t.close()


        def blank(t):
            assert t.position is 0

            if t._blank is 0:
                t._blank = 1


        def blank2(t):
            assert t.position is 0

            if 0 <= t._blank < 2:
                t._blank = 2


        def blank_suppress(t):
            assert t.position is 0

            t._blank = -1


        def close(t):
            f       = t.f
            t.write = t.f = none

            if f is not none:
                f.close()


        def indent(t, header = none, ending = none, prefix = 4):
            if header is not none:
                t.line(header)

            return Indent(t, ending, prefix * ' ')


        def finish(t):
            r = t.result = t.f.getvalue()

            t.close()

            return r


        def partial(t, format = none, *arguments):
            if t.position is 1:
                t.write(format % arguments   if arguments else   format)
                return

            if (t._blank > 0):
                t.write('\n' * t._blank + t.prefix + (format % arguments   if arguments else   format))
                t._blank   = 0
                t.position = 1
                return

            t.write(t.prefix + (format % arguments   if arguments else   format))
            t._blank   = 0
            t.position = 1


        def line(t, format = none, *arguments):
            if t.position is 1:
                if format is none:
                    assert length(arguments) is 0

                    t.write('\n')
                else:
                    t.write((format % arguments   if arguments else   format) + '\n')

                t.position = 0
                return

            if format is none:
                assert length(arguments) is 0

                t.write('\n')

                if t._blank > 0:
                    t._blank -= 1

                t.position = 0
                return

            if t._blank > 0:
                t.write('\n' * t._blank + t.prefix + (format % arguments   if arguments else   format) + '\n')
                t.position = t._blank = 0
                return

            t.write(t.prefix + (format % arguments   if arguments else   format) + '\n')
            t.position = t._blank = 0


    @export
    def create_StringOutput():
        return StringOutput(create_SimpleStringOutput())
