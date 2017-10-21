#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.StringOutput')
def gem():
    require_gem('Gem.SimpleStringIO')


    class ChangePrefix(Object):
        __slots__ = ((
            'f',                        #   StringOutput
            'old_prefix',               #   String
            'old_prefix_always',        #   String
            'old_prefix_blanks',        #   String
            'ending',                   #   None | String
            'prefix',                   #   String
            'prefix_short',             #   Zero | String
            'prefix_always',            #   Zero | String
        ))


        def __init__(t, f, ending, prefix, prefix_short = 0, prefix_always = 0):
            t.f                 = f
            t.old_prefix        = f._prefix
            t.old_prefix_always = f._prefix_always
            t.old_prefix_blanks = f._prefix_blanks
            t.ending            = ending
            t.prefix            = prefix
            t.prefix_short      = prefix_short
            t.prefix_always     = prefix_always


        def __enter__(t):
            t.f._prefix = t.prefix

            if t.prefix_always is not 0:
                t.f._prefix_always = t.prefix_always
                t.f._prefix_blanks = t.prefix_short + '\n'

            return t


        def __exit__(t, e_type, e, e_traceback):
            t.f._prefix        = t.old_prefix
            t.f._prefix_always = t.old_prefix_always
            t.f._prefix_blanks = t.old_prefix_blanks

            if e is none:
                if t.ending is not none:
                    if t.f.position is 1:
                        t.f.line()

                    t.f.line(t.ending)


    @export
    class StringOutput(Object):
        __slots__ = ((
            'f',                        #   StringIO
            '_prefix',                  #   String
            '_prefix_always',           #   String
            '_prefix_blanks',           #   String
            'result',                   #   None | String
            '_blank',                   #   Integer
            'position',                 #   Integer
            'write',                    #   Method
        ))


        def __init__(t, f):
            t.f              = f
            t._prefix        = ''
            t._prefix_always = ''
            t._prefix_blanks = '\n'
            t.result         = none
            t._blank         = -1
            t.position       = 0
            t.write          = f.write


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


        def flush(t):
            if t.position is 1:
                t.write('\n')
                t.position = 0

            if t._blank > 0:
                t.write(t._prefix_blanks * t._blank)

            t._blank = 0


        def indent(t, header = none, ending = none, prefix = 4):
            if header is not none:
                t.line(header)

            return ChangePrefix(t, ending, t._prefix + prefix * ' ')


        def change_prefix(t, prefix_short, prefix_always):
            assert t._prefix is t._prefix_always is ''

            return ChangePrefix(t, none, prefix_always, prefix_short = prefix_short, prefix_always = prefix_always)


        def finish(t):
            r = t.result = t.f.getvalue()

            t.close()

            return r


        def partial(t, format = none, *arguments):
            if t.position is 1:
                t.write(format % arguments   if arguments else   format)
                return

            if t._blank > 0:
                t.write(
                      t._prefix_blanks * t._blank
                    + t._prefix
                    + (format % arguments   if arguments else   format)
                )
            else:
                t.write(t._prefix + (format % arguments   if arguments else   format))

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

                t.write(t._prefix_blanks)

                if t._blank > 0:
                    t._blank -= 1

                t.position = 0
                return

            if t._blank > 0:
                t.write(
                      t._prefix_blanks * t._blank
                    + t._prefix
                    + (format % arguments   if arguments else   format)
                    + '\n'
                )

                t.position = t._blank = 0
                return

            t.write(t._prefix + (format % arguments   if arguments else   format) + '\n')
            t.position = t._blank = 0


        def write_multiline(t, multiline):
            data = multiline.splitlines()
            line = t.line

            i          = 0
            maximum_m1 = length(data) - 1

            for s in data:
                if i == maximum_m1:
                    t.partial(s)
                    return

                line(s)
                i += 1


    @export
    def create_StringOutput():
        return StringOutput(create_SimpleStringOutput())
