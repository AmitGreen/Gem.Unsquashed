#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Match')
def gem():
    require_gem('Tremolite.Build')
    require_gem('Tremolite.Core')


    class TremoliteMatch(Object):
        __slots__ = ((
            'name',                     #   String
            'pattern',                  #   TremoliteBase+
        ))


        def __init__(t, name, pattern):
            t.name    = name
            t.pattern = pattern


        def __repr__(t):
            return arrange('<TremoliteMatch %s %r>', t.name, t.pattern)


    [cache, insert] = produce_cache_and_insert_function('tremolite.match')


    @export
    def MATCH(name, pattern):
        assert (type(name) is String) and (length(name) > 0)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        name = intern_string(name)

        return insert(name, TremoliteMatch(name, pattern))


    @export
    def create_match_code(path, copyright, module_name):
        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright %s.  All rights reserved.', copyright)
            f.line('#')
            f.line('@gem(%r)', module_name)
            
            with f.indent('def gem():'):
                f.line('require_gem(%r)', 'Tremolite.Compile')
                f.blank2()
                f.line('from Tremolite.Compile import compile_regular_expression')

                f.blank2()
                with f.indent('def M(regular_expression, code, groups = 0, flags = 0):'):
                    f.line('return compile_regular_expression(regular_expression, code, groups, flags).match')
                f.blank2()

                with f.indent('C = (', ').__getitem__'):
                    f.line('#')
                    f.line('#<copyright>')
                    f.line("#   The following is produced from python's standard library")
                    f.line("#   'sre_compile.py', function 'compile' and is thus:")
                    f.line('#')
                    f.line('#       Copyright (c) 1998-2001 by Secret Labs AB.  All rights reserved.')
                    f.line('#')
                    f.line("#       This version of the SRE library can be redistributed under CNRI's")
                    f.line('#       Python 1.6 license.  For any other use, please contact Secret Labs')
                    f.line('#       AB (info@pythonware.com).')
                    f.line('#')
                    f.line('#   (Currently the same copyright is used for both python 2.7 & 3.5 versions)')
                    f.line('#')
                    f.line('#   P.S.:  To make things simple, all *changes* to the original code below are dual licensed under')
                    f.line('#          both (1) the MIT License that the rest of Gem is licensed; and (2) under the exact same')
                    f.line('''#          "CNRI's Python 1.6" license as the original code.''')
                    f.line('#')
                    f.line('#   NOTE:  Dual copyright only applies to the changes, not to the original code which is obviously')
                    f.line('#          only licensed under the original license.')
                    f.line('#')

                    for v in iterate_values_sorted_by_key(cache):
                        [code, groups, flags] = parse_ascii_regular_expression(v.pattern.regular_expression)

                        f.blank()
                        f.line('#')
                        f.line('#   %s', portray_string(v.pattern.regular_expression))
                        f.line('#')
                        f.line('%s,', portray_string(code)   if type(code) is String else   portray(code))

                        if groups is not 0:
                            f.line('%s,', portray(groups))

                    f.blank()
                    f.line('#</copyright>')

                index = 0

                for v in iterate_values_sorted_by_key(cache):
                    [code, groups, flags] = parse_ascii_regular_expression(v.pattern.regular_expression)

                    f.blank()
                    f.line('#')
                    f.line('#   %s', v.name)
                    f.line('#')
                    f.line('#       %s', v.pattern)
                    f.line('#')

                    with f.indent(
                            arrange('%s = M(', v.name),
                            ')',
                    ):
                        f.line('%s,', portray_string(v.pattern.regular_expression))
                        f.line('C(%d),', index)
                        index += 1

                        if groups is not 0:
                            f.line('C(%d),', index)
                            index += 1
                        elif flags is not 0:
                            f.line('0,')

                        if flags is not 0:
                            f.line('%d,', flags)

                f.blank2()

                with f.indent(
                    'export(',
                    ')',
                    8,
                ):
                    for v in iterate_values_sorted_by_key(cache):
                        f.line('%-30s%s,', arrange('%r,', v.name), v.name)

            data = f.finish()

        for s in data.splitlines():
            line(s)
