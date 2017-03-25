#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    module_path.insert(1, path_absolute(path_join(module_path[0], '..')))


    import Gem


@gem('Tremolite.Main')
def gem():
    require_gem('Tremolite.Build')
    require_gem('Tremolite.Compile')
    require_gem('Tremolite.Parse')


    @share
    def main():
        for [pattern, test] in [
                [   'x' + END_OF_STRING,                                          'x'         ],
                [   'x' + GROUP('abc', 'y') + END_OF_STRING,                      'xy'        ],
                [   'x' + GROUP('abc', 'y') + GROUP('z', 'z') + END_OF_STRING,    'xyz'       ],
        ]:
            compiled = pattern.compile_ascii_regular_expression()
            m        = compiled.match(test)

            line('%s', pattern)
            line('  %r %r', m.group(), m.groups())
