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
                [   OPTIONAL('bc') + OPTIONAL(EXACT('d') + 'g' | EXACT('hi') + 'j') + 'x' + END_OF_STRING,  'hijx'      ],
                [   'x' + ('lemo' + ANY('a-z') | GROUP('abc', 'y')) + END_OF_STRING,                        'xy'        ],
                [   'x' + GROUP('abc', ANY('a-z', 'A-Z')) + GROUP('z', 'z') + END_OF_STRING,                'xYz'       ],
                [   OPTIONAL('a') + ONE_OR_MORE('x') + ZERO_OR_MORE('yz') + END_OF_STRING,                  'xx'        ],
                [   'a' + (EXACT('b') | 'ci') + 'd',                                                        'acid'      ],
        ]:
            line('%s', pattern)
            line('%r', pattern)

            compiled = pattern.compile_ascii_regular_expression()
            m        = compiled.match(test)

            line('  %r %r', m.group(), m.groups())
            line()
