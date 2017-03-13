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


@gem('Topaz.Main')
def gem():
    require_gem('Gem.Exception')
    require_gem('Gem.PortrayString')


    from Gem import portray_raw_string, raise_value_error


    @share
    def main():
        for [s, expected] in [
                #
                #   N_N: simple case
                #
                [   r'',                            r"r''"                              ],
                [   r'test',                        r"r'test'"                          ],

                #
                #   N_N (ra & rq)
                #
                [   r'double backslash: \\',        r"r'double backslash: \\'"          ],
                [   r"\'",                          r'''r"\'"'''                        ],

                #
                #   A_A (rq)
                #
                [   r"ending single quote '",       r'''r"ending single quote '"'''     ],
                [   r"'",                           r'''r"'"'''                         ],

                #
                #   A_B (rq)
                #
                [   r"quoted: ''",                  r'''r"quoted: ''"'''                ],

                #
                #   A_N (ra)
                #
                [   r"\"'\"",                       r'''r"\"'\""'''                     ],

                #
                #   A_N (rq)
                #
                [   r"can't",                       r'''r"can't"'''                     ],

                #
                #   AQ_A (ra)
                #
                [   r"""End with "'": "'""",        r'''r"""End with "'": "'"""'''      ],
                [   r"""other way: " & '""",        r'''r"""other way: " & '"""'''      ],

                #
                #   AQ_B (ra)
                #
                [   r"""prefer ", "", ', or ''""",  r'''r"""prefer ", "", ', or ''"""'''],

                #
                #   AQ_N (ra)
                #
                [   r''''triple' is: ""\".''',      r"""r''''triple' is: ""\".'''"""    ],
                [   r''''"" ""'2''',                r"""r''''"" ""'2'''"""              ],

                #
                #   AQ_N (rq)
                #
                [   r'''"triple" is: ''\'.''',      r'''r""""triple" is: ''\'."""'''    ],
                [   r'''"'' ''"!''',                r'''r""""'' ''"!"""'''              ],
                [   r'''the quotes: ' & "''',       r"""r'''the quotes: ' & "'''"""     ],
                [   r"""single: ', '' .vs. "?""",   r'''r"""single: ', '' .vs. "?"""''' ],

                #
                #   AQ_Q (ra)
                #
                [   r'''singles "'" & "''"''',      r"""r'''singles "'" & "''"'''"""    ],

                #
                #   AQ_Q (rq)
                #
                [   r'''Wow: ''"''',                r"""r'''Wow: ''"'''"""              ],

                #
                #   AQ_R (ra)
                #
                [   r'''more quotes: '' & ""''',    r"""r'''more quotes: '' & ""'''"""  ],

                #
                #   AS_N (ra)
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r'''more """" than '!''',      """r'''more ""\"" than '!'''""",     ],

                #
                #   AS_N (rq)
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r'''l''s """" t''n '!''',      """r'''l''s ""\"" t''n '!'''""",     ],

                #
                #   C_N (rq)
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" & '''x\'''' - so use string concatanation so
                #       vim can properly parse it.
                #
                [   r"lots of ''''' - lots!",       """r"lots of ''''' - lots!""" + '"' ],

                #
                #   CQ_N (ra)
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r"""l""s '''' t""n "!""",      '''r"""l""s ''\'' t""n "!"""''',     ],

                #
                #   CQ_N (rq)
                #
                [   r"""more '''' than "!""",      '''r"""more ''\'' than "!"""''',     ],

                #
                #   Q_N (rq)
                #
                [   r'\'"\'',                       r"""r'\'"\''"""                     ],

                #
                #   Q_Q (ra)
                #
                [   r'"',                           r"""r'"'"""                         ],
                [   r'She said "hello"',            r"""r'She said "hello"'"""          ],

                #
                #   Q_R (ra)
                #
                [   r'double quoted: ""',           r"""r'double quoted: ""'"""         ],

                #
                #   S_N (ra)
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" & '''x\'''' - so use string concatanation so
                #       vim can properly parse it.
                #
                [   r'lots of """"" - lots!',       '''r'lots of """"" - lots!''' + "'" ],

                #
                #   N_N, backslash (kc)
                #
                [   'backslash: \\',                portray('backslash: \\')            ],

                #
                #   CQ_Q (ps)
                #       End with " & has ''' internally
                #
                [   '''\'333: "''\'."''',           r"""'''\'333: "''\'."'''"""         ],
                [   '''three: "''\''\''."''',       r"""'''three: "''\''\''."'''"""     ],    

                #
                #   AS_A (pc)
                #       End with ' & has """ internally
                #
                [   """': '""\"".'""",              r'''"""': '""\"".'"""'''            ],
                [   """\""\""\"".'""",              r'''"""\""\""\"".'"""'''            ],
                [   """3: '""\".'""",               r'''"""3: '""\".'"""'''             ],
        ]:
            actual = portray_raw_string(s)

            if actual != expected:
                line('%r', s)
                line('  actual:   %s', actual)
                line('  expected: %s', expected)

                raise_value_error('portray_raw_string(%r): %r (expected: %r)', s, actual, expected)

        line('PASSED: portray_raw_string')
