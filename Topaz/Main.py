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
                #   A_A: ra
                #
                [   r"wink \"\"'",                  r'''r"wink \"\"'"'''                    ],

                #
                #   A_A: rq
                #
                [   r"ending single quote '",       r'''r"ending single quote '"'''         ],
                [   r"'",                           r'''r"'"'''                             ],

                #
                #   A_A/AQ_A: lemon: kc
                #   A_A/AQ_A: lemon: ks: not possible   (not allowed: """)
                #
                [   """wi\nk \\"\\"'""",            r'''"""wi\nk \\"\\"'"""'''              ],

                #
                #   A_A: backslash: kc/ks: not possible (always raw mode)
                #   A_A: pc/ps:            not possible (always raw mode)
                #

                #
                #   A_B: ra
                #
                [   r"\"two apostrophe\": ''",      r'''r"\"two apostrophe\": ''"'''        ],

                #
                #   A_B: rq
                #
                [   r"quoted: ''",                  r'''r"quoted: ''"'''                    ],

                #
                #   A_B/AQ_B: lemon: kc
                #   A_B/AQ_B, lemon: ks: not possible (not allowed """)
                #
                [   """wo\nk \\"\\"''""",           r'''"""wo\nk \\"\\"''"""'''             ],

                #
                #   A_B: backslash: kc/ks: not possible (always raw mode)
                #   A_B: pc/ps:            not possible (always raw mode)
                #

                #
                #   A_K: ra/rq: not possible (ends in \)
                #

                #
                #   A_K/A_N: lemon: kc
                #   A_K/A_N: lemon: ks: not possible (not allowed """)
                #
                [   "le'mo\n\\",                    portray("le'mo\n\\")                    ],

                #
                #   A_K/A_N: backslash: kc
                #   A_K/A_N: backslash: ks: not possible (not allowed """)
                #
                [   "apostrophe & backlash: '\\",   portray("apostrophe & backlash: '\\")   ],

                #
                #   A_N: ra
                #
                [   r"\"'\"",                       r'''r"\"'\""'''                         ],

                #
                #   A_N: rq
                #
                [   r"can't",                       r'''r"can't"'''                         ],

                #
                #   A_N: lemon: kc
                #   A_N: lemon: ks (not allowed """)
                #
                [   "ca\n't",                       portray("ca\n't"),                      ],

                #
                #   A_N: backslash: kc/ks: not possible (always raw mode)
                #   A_N: pc/ps:            not possible (always raw mode)
                #

                #
                #   AQ_A: ra
                #
                [   r"""End with "'": "'""",        r'''r"""End with "'": "'"""'''          ],
                [   r"""other way: " & '""",        r'''r"""other way: " & '"""'''          ],

                #
                #   AQ_B: ra
                #
                [   r"""prefer ", "", ', or ''""",  r'''r"""prefer ", "", ', or ''"""'''    ],

                #
                #   AQ_N: ra
                #
                [   r''''triple' is: ""\".''',      r"""r''''triple' is: ""\".'''"""        ],
                [   r''''"" ""'2''',                r"""r''''"" ""'2'''"""                  ],

                #
                #   AQ_N: rq
                #
                [   r'''"triple" is: ''\'.''',      r'''r""""triple" is: ''\'."""'''        ],
                [   r'''"'' ''"!''',                r'''r""""'' ''"!"""'''                  ],
                [   r'''the quotes: ' & "''',       r"""r'''the quotes: ' & "'''"""         ],
                [   r"""single: ', '' .vs. "?""",   r'''r"""single: ', '' .vs. "?"""'''     ],

                #
                #   AQ_Q: ra
                #
                [   r'''singles "'" & "''"''',      r"""r'''singles "'" & "''"'''"""        ],

                #
                #   AQ_Q: rq
                #
                [   r'''Wow: ''"''',                r"""r'''Wow: ''"'''"""                  ],

                #
                #   AQ_R: ra
                #
                [   r'''more quotes: '' & ""''',    r"""r'''more quotes: '' & ""'''"""      ],

                #
                #   AS_A (pc)
                #       End with ' & has """ internally
                #
                [   """': '""\"".'""",              r'''"""': '""\"".'"""'''                ],
                [   """\""\""\"".'""",              r'''"""\""\""\"".'"""'''                ],
                [   """3: '""\".'""",               r'''"""3: '""\".'"""'''                 ],

                #
                #   AS_N: ra
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r'''more """" than '!''',      """r'''more ""\"" than '!'''""",         ],

                #
                #   AS_N: rq
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r'''l''s """" t''n '!''',      """r'''l''s ""\"" t''n '!'''""",         ],

                #
                #   C_N: rq
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" & '''x\'''' - so use string concatanation so
                #       vim can properly parse it.
                #
                [   r"lots of ''''' - lots!",       """r"lots of ''''' - lots!""" + '"'     ],

                #
                #   CQ_N: ra
                #       Have to represent what we "expect" using \' or \" internally
                #
                [   r"""l""s '''' t""n "!""",      '''r"""l""s ''\'' t""n "!"""''',         ],

                #
                #   CQ_N: rq
                #
                [   r"""more '''' than "!""",      '''r"""more ''\'' than "!"""''',         ],

                #
                #   CQ_Q (ps)
                #       End with " & has ''' internally
                #
                [   '''\'333: "''\'."''',           r"""'''\'333: "''\'."'''"""             ],
                [   '''three: "''\''\''."''',       r"""'''three: "''\''\''."'''"""         ],    

                #
                #   Q_N: rq
                #
                [   r'\'"\'',                       r"""r'\'"\''"""                         ],

                #
                #   Q_Q: ra
                #
                [   r'"',                           r"""r'"'"""                             ],
                [   r'She said "hello"',            r"""r'She said "hello"'"""              ],

                #
                #   Q_R: ra
                #
                [   r'double quoted: ""',           r"""r'double quoted: ""'"""             ],

                #
                #   N_N: simple case
                #
                [   r'',                            r"r''"                                  ],
                [   r'test',                        r"r'test'"                              ],

                #
                #   N_N: ra
                #
                [   r'double backslash: \\',        r"r'double backslash: \\'"              ],

                #
                #   N_N: rq
                #
                [   r"\'",                          r'''r"\'"'''                            ],

                #
                #   N_K/N_N, backslash (kc)
                #
                [   'backslash: \\',                portray('backslash: \\')                ],

                #
                #   S_N: ra
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" & '''x\'''' - so use string concatanation so
                #       vim can properly parse it.
                #
                [   r'lots of """"" - lots!',       '''r'lots of """"" - lots!''' + "'"     ],

            ]:
            actual = portray_raw_string(s)

            if actual != expected:
                line('%r', s)
                line('  actual:   %s', actual)
                line('  expected: %s', expected)

                raise_value_error('portray_raw_string(%r): %r (expected: %r)', s, actual, expected)

        line('PASSED: portray_raw_string')
