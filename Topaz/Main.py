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
            #<A_A>
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
                #   A_A/AQ_A: lemon: ks: not possible   (''' not allowed)
                #
                [   """wi\nk \\"\\"'""",            r'''"""wi\nk \\"\\"'"""'''              ],

                #
                #   A_A: backslash: kc/ks: not possible (always raw mode)
                #   A_A: pc/ps:            not possible (always raw mode)
                #
            #</A_A>

            #<A_B>
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
                #   A_B/AQ_B, lemon: ks: not possible (''' not allowed)
                #
                [   """wo\nk \\"\\"''""",           r'''"""wo\nk \\"\\"''"""'''             ],

                #
                #   A_B: backslash: kc/ks: not possible (always raw mode)
                #   A_B: pc/ps:            not possible (always raw mode)
                #
            #</A_B>

            #<A_K>
                #
                #   A_K/A_N: ra/rq:         not possible (ends in \)
                #   A_K/A_N: lemon: kc
                #   A_K/A_N: lemon: ks: not possible (''' not allowed)
                #
                [   "le'mo\n\\",                    portray("le'mo\n\\")                    ],

                #
                #   A_K/A_N: backslash: kc
                #   A_K/A_N: backslash: ks: not possible (''' not allowed)
                #
                [   "apostrophe & backlash: '\\",   portray("apostrophe & backlash: '\\")   ],

                #
                #   A_K: pc/ps: not possible (always backslash)
                #
            #</A_K>

            #<A_N>
                #
                #   A_N: ra
                #
                #       NOTE: Ends in ", which is a little confusing.  We could theoretically use ''', hence:
                #             r'''\"'\"''' -- but that doesn't seem much clearer.
                #
                [   r"\"'\"",                       r'''r"\"'\""'''                         ],

                #
                #   A_N: rq
                #
                [   r"can't",                       r'''r"can't"'''                         ],

                #
                #   A_N: lemon: kc
                #   A_N: lemon: ks (''' not allowed)
                #
                [   "ca\n't",                       portray("ca\n't"),                      ],

                #
                #   A_N: backslash: kc/ks: not possible (always raw mode)
                #   A_N: pc/ps:            not possible (always raw mode)
                #
            #</A_N>

            #<AQ_A>
                #
                #   AQ_A: ra
                #
                [   r"""End with "'": "'""",        r'''r"""End with "'": "'"""'''          ],

                #
                #   AQ_A: rq
                #
                [   r"""other way: '"' & '""",      r'''r"""other way: '"' & '"""'''        ],

                #
                #   AQ_A: lemon: kc
                #   AQ_A: lemon: ks (''' not allowed)
                #
                [   """"lemo\n's"'""",              r'''"""\"lemo\n's"'"""'''               ],

                #
                #   AQ_A: backslash: kc/ks: not possible (always raw mode)
                #   AQ_A: pc/ps:            not possible (always raw mode)
                #
            #</AQ_A>

            #<AQ_B>
                #
                #   AQ_B: ra
                #
                [   r"""prefer ", "", ', or ''""",  r'''r"""prefer ", "", ', or ''"""'''    ],

                #
                #   AQ_B: rq
                #
                [   r"""prefer ', '', ", or ''""",  r'''r"""prefer ', '', ", or ''"""'''    ],

                #
                #   AQ_B: lemon: kc
                #   AQ_B: lemon: ks (''' not allowed)
                #
                [   """"more lemo\n''s"'""",        r'''"""\"more lemo\n''s"'"""'''         ],

                #
                #   AQ_B: backslash: kc/ks: not possible (always raw mode)
                #   AQ_B: pc/ps:            not possible (always raw mode)
                #
            #</AQ_B>

            #<AQ_K>
                #
                #   AQ_K/AQ_N: ra/rq:     not possible (ends in \)
                #   AQ_K/AQ_N: lemon: kc
                #   AQ_K/AQ_N: lemon: ks: not possible (''' not allowed)
                #
                [   '''le'"mo"\n\\''',              r"""'''le'"mo"\n\\'''"""                ],

                #
                #   AQ_K/AQ_N: backslash: kc
                #   AQ_K/AQ_N: backslash: ks: not possible (''' not allowed)
                #
                [   '''all ", ', & \\''',           r"""'''all ", ', & \\'''"""             ],

                #
                #   A_QK: pc/ps: not possible (always backslash)
                #
            #</AQ_K>

            #<AQ_N>
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
                [   r"""single: ', '' .vs. "?""",   r'''r"""single: ', '' .vs. "?"""'''     ],

                #
                #   AQ_N: lemon: kc
                #   AQ_N: lemon: ks (''' not allowed)
                #
                [   """lemo\n''s "yet" again""",    r"""'''lemo\n''s "yet" again'''"""      ],

                #
                #   AQ_N: backslash: kc/ks: not possible (always raw mode)
                #   AQ_N: pc/ps:            not possible (always raw mode)
                #
            #</AQ_N>

            #<AQ_Q>
                #
                #   AQ_Q: ra
                #
                [   r'''singles "'" & "''"''',      r"""r'''singles "'" & "''"'''"""        ],
                [   r'''the quotes: ' & "''',       r"""r'''the quotes: ' & "'''"""         ],

                #
                #   AQ_Q: rq
                #
                [   r'''Wow: ''"''',                r"""r'''Wow: ''"'''"""                  ],

                #
                #   AQ_Q: lemon: kc
                #   AQ_Q: lemon: ks (''' not allowed)
                #
                [   '''lemo\n's are "sour"''',      r"""'''lemo\n's are "sour"'''"""        ],

                #
                #   AQ_Q: backslash: kc/ks: not possible (always raw mode)
                #   AQ_Q: pc/ps:            not possible (always raw mode)
                #
            #</AQ_Q>

            #<AQ_R>
                #
                #   AQ_R: ra
                #
                [   r'''more quotes: '' & ""''',    r"""r'''more quotes: '' & ""'''"""      ],

                #
                #   AQ_R: rq
                #
                [   r'''compare: ''+'' .vs. ""''',  r"""r'''compare: ''+'' .vs. ""'''"""    ],

                #
                #   AQ_R: lemon: kc
                #   AQ_R: lemon: ks (''' not allowed)
                #
                [   '''yep - lemo\n's ""sour""''',  r"""'''yep - lemo\n's ""sour""'''"""    ],

                #
                #   AQ_R: backslash: kc/ks: not possible (always raw mode)
                #   AQ_R: pc/ps:            not possible (always raw mode)
                #
            #</AQ_R>

            #<AS_A>
                #
                #   AS_A: ra:         not possible (always portray)
                #   AS_A: rq:         not possible (always portray)
                #   AS_A: lemon: kc
                #   AS_A: lemon: ks: not possible (''' not allowed)
                #
                [   """\""\"\tab'""",               r'''"""\""\"\tab'"""'''                 ],

                #
                #   AS_A: backslash: kc
                #   AS_A: backslash: ks: not possible (''' not allowed)
                #
                [   """\""\"\\non-tab'""",          r'''"""\""\"\\non-tab'"""'''            ],

                #
                #   AS_A: pc
                #   AS_A: ps: not possible (''' not allowed)
                #
                [   """': '""\"".'""",              r'''"""': '""\"".'"""'''                ],
                [   """3: '""\".'""",               r'''"""3: '""\".'"""'''                 ],
            #</AS_A>

            #<AS_B>
                #
                #   AS_B: ra:         not possible (always portray)
                #   AS_B: rq:         not possible (always portray)
                #   AS_B: lemon: kc
                #   AS_B: lemon: ks: not possible (''' not allowed)
                #
                [   """\""\"AS_B\n''""",            r'''"""\""\"AS_B\n''"""'''              ],

                #
                #   AS_B: backslash: kc
                #   AS_B: backslash: ks: not possible (''' not allowed)
                #
                [   """\""\"\\AS_B''""",            r'''"""\""\"\\AS_B''"""'''              ],

                #
                #   AS_B: pc
                #   AS_B: ps: not possible (''' not allowed)
                #
                [   """\""\""\"".''""",             r'''"""\""\""\"".''"""'''               ],
            #</AS_B>

            #<AS_K>
                #
                #   AS_K/AS_N: ra/rq:     not possible (ends in \)
                #   AS_K/AS_N: lemon: kc
                #   AS_K/AS_N: lemon: ks: not possible (''' not allowed)
                #
                [   '''le'"""mo"""\n\\''',          """'''le'""\"mo""\"\\n\\\\'''"""        ],

                #
                #   AS_K/A_N: backslash: kc
                #   AS_K/A_N: backslash: ks: not possible (''' not allowed)
                #
                [   '''all """, ', & \\''',         """'''all ""\", ', & \\\\'''"""         ],

                #
                #   AS_K: pc/ps: not possible (always backslash)
                #
            #</AS_K>

            #<AS_N>
                #
                #   AS_N: ra
                #       Have to represent what we "expect" using \" internally
                #
                [   r'''more """" than '!''',      """r'''more ""\"" than '!'''""",         ],

                #
                #   AS_N: rq
                #       Have to represent what we "expect" using \" internally
                #
                [   r'''l''s """" t''n '!''',      """r'''l''s ""\"" t''n '!'''""",         ],

                #
                #   AS_N: lemon: kc
                #   AS_N: lemon: ks: not possible (''' not allowed)
                #       Have to represent what we "expect" using \" internally
                #
                [   '''"""'now' AS_\n''',          """'''""\"'now' AS_\\n'''"""             ],

                #
                #   AS_N: backslash: kc/ks: not possible (always raw mode)
                #   AS_N: pc/ps:            not possible (always raw mode)
                #
            #</AS_N>

            #<C_A>
                #
                #   C_A: ra - not possible (" not allowed)
                #   C_A: rq
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" - so use string concatanation so vim can properly parse
                #       it.
                #
                [   r"lots of ''''' - more'",       """r"lots of ''''' - more'""" + '"'     ],

                #
                #   C_A:  lemon: kc: not possible (""" not allowed)
                #   C_A:  lemon: ks
                #       Have to represent what we "expect" using \' internally
                #
                [   "'''@C_N + e\nding '",          '''"''\'@C_N + e\\nding '"'''           ],

                #
                #   C_A: backslash: kc/ks: not possible (always raw mode)
                #   C_A: pc/ps:            not possible (always raw mode)
                #
            #</C_A>

            #<C_B>
                #
                #   C_B: ra - not possible (" not allowed)
                #   C_B: rq
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" - so use string concatanation so vim can properly parse
                #       it.
                #
                [   r"lots of ''''' - extra''",     """r"lots of ''''' - extra''""" + '"'   ],

                #
                #   C_B:  lemon: kc: not possible (""" not allowed)
                #   C_B:  lemon: ks
                #       Have to represent what we "expect" using \' internally
                #
                [   "'''@C_N + 2x e\nding ''",     '''"''\'@C_N + 2x e\\nding ''"'''        ],

                #
                #   C_B: backslash: kc/ks: not possible (always raw mode)
                #   C_B: pc/ps:            not possible (always raw mode)
                #
            #</C_B>

            #<C_C>
                #
                #   C_C: ra - not possible (" not allowed)
                #   C_C: rq
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" - so use string concatanation so vim can properly parse
                #       it.
                #
                [   r"abundance of '''''''",        r"""r"abundance of '''''''""" + '"'     ],

                #
                #   C_C:  lemon: kc: not possible (""" not allowed)
                #   C_C:  lemon: ks
                #       Have to represent what we "expect" using \' internally
                #
                [   "'''C_C is a pali\ndrome'''",   '''"''\'C_C is a pali\\ndrome''\'"'''   ],

                #
                #   C_C: backslash: kc/ks: not possible (always raw mode)
                #   C_C: pc/ps:            not possible (always raw mode)
                #
            #</C_C>

            #<C_K>
                #
                #   C_K/C_N: ra/rq:     not possible (ends in \)
                #   C_K/C_N: lemon: kc: not possible (""" not allowed)
                #   C_K/C_N: lemon: ks
                #
                [   "''''Super\n?'''\\",            """\"''''Super\\n?'''\\\\""" + '"'      ],

                #
                #   C_K/C_N: backslash: kc (""" not allowed)
                #   C_K/C_N: backslash: ks
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" - so use string concatanation so vim can properly parse
                #       it.
                #
                [
                    "''''supercalifragilisticexpialidocious?'''\\",
                    """\"''''supercalifragilisticexpialidocious?'''\\\\""" + '"'
                ],

                #
                #   C_K: pc/ps: not possible (always backslash)
                #
            #</C_K>

            #<C_N>
                #
                #   C_N: ra - not possible (" not allowed)
                #   C_N: rq
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" - so use string concatanation so vim can properly parse
                #       it.
                #
                [   r"lots of ''''' - lots!",       """r"lots of ''''' - lots!""" + '"'     ],

                #
                #   C_N:  lemon: kc: not possible (""" not allowed)
                #   C_N:  lemon: ks
                #       Have to represent what we "expect" using \' internally
                #
                [   "'''@C_\n",                    '''"''\'@C_\\n"'''                       ],

                #
                #   C_N: backslash: kc/ks: not possible (always raw mode)
                #   C_N: pc/ps:            not possible (always raw mode)
                #
            #</C_N>

            #<CQ_A>
                #
                #   CQ_A: ra: not possible (""" not allowed)
                #   CQ_A: rq
                #
                [   r"""End '''with "'": "'""",   '''r"""End ''\'with "'": "'"""'''         ],

                #
                #   CQ_A: lemon: kc: not possible (""" not allowed)
                #   CQ_A: lemon: ks
                #
                [   """\"lemo\n'''s"'""",           '''"""\\"lemo\\n''\'s"'"""'''           ],

                #
                #   CQ_A: backslash: kc/ks: not possible (always raw mode)
                #   CQ_A: pc/ps:            not possible (always raw mode)
                #
            #</CQ_A>

            #<CQ_B>
                #
                #   CQ_B: ra: not possible (""" not allowed)
                #   CQ_B: rq
                #
                [   r"""More "quotes" ''' & ''""",  '''r"""More "quotes" ''\' & ''"""'''    ],

                #
                #   CQ_B: lemon: kc: not possible (""" not allowed)
                #   CQ_B: lemon: ks
                #
                [   """\"lemo\n"ade'''s''""",   '''"""\\"lemo\\n"ade''\'s''"""'''           ],

                #
                #   CQ_B: backslash: kc/ks: not possible (always raw mode)
                #   CQ_B: pc/ps:            not possible (always raw mode)
                #
            #</CQ_A>

            #<CQ_C>
                #
                #   CQ_C: ra: not possible (""" not allowed)
                #   CQ_C: rq
                #
                [   r"""End with 3x "'": "'''""",   '''r"""End with 3x "'": "''\'"""'''     ],

                #
                #   CQ_C: lemon: kc: not possible (""" not allowed)
                #   CQ_C: lemon: ks
                #
                [   """'''"\tables"'''""",          '''"""''\'"\\tables"''\'"""'''          ],

                #
                #   CQ_C: backslash: kc/ks: not possible (always raw mode)
                #   CQ_C: pc/ps:            not possible (always raw mode)
                #
            #</CQ_C>

            #<CQ_K>
                #
                #   CQ_K/CQ_N: ra/rq:     not possible (ends in \)
                #   CQ_K/CQ_N: lemon: kc: not possible (""" not allowed)
                #   CQ_K/CQ_N: lemon: ks
                #
                [   """le'''"mo"\n\\""",            '''"""le''\'"mo"\\n\\\\"""'''           ],

                #
                #   CQ_K/C_N: backslash: kc: not possible (""" not allowed)
                #   CQ_K/C_N: backslash: ks
                #
                [   """deja vu: ", ''', & \\""",    '''"""deja vu: ", ''\', & \\\\"""'''    ],

                #
                #   CQ_K: pc/ps: not possible (always backslash)
                #
            #</CQ_K>

            #<CQ_N>
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
                #   CQ_C: lemon: kc: not possible (""" not allowed)
                #   CQ_N: lemon: ks
                #
                [   """'''"\rake"''' leaves""",     '''"""''\'"\\rake"''\' leaves"""'''     ],

                #
                #   CQ_K/C_N: backslash: kc: not possible (""" not allowed)
                #   CQ_K/C_N: backslash: ks
                #
                [
                    """been "there", '''done that'''\\""",
                    '''"""been "there", ''\'done that''\'\\\\"""'''
                ],

                #
                #   CQ_N: pc/ps:            not possible (always raw mode)
                #
            #</CQ_N>

            #<CQ_Q>
                #
                #   CQ_Q: ra/qs: not possible (ends in " so can't use either ''' or """ around it)
                #

                #
                #   CQ_Q: lemon: kc: not possible (""" not allowed)
                #   CQ_Q: lemon: ks
                #
                [   '''\''\'\t"''',                 """'''\\''\\'\\t"'''"""                 ],

                #
                #   CQ_Q: pc: not possible (""" not allowed)
                #   CQ_Q: ps
                #
                [   '''\'333: "''\'."''',           r"""'''\'333: "''\'."'''"""             ],
            #</CQ_Q>

            #<CQ_R>
                #
                #   CQ_R: ra/qs: not possible (ends in " so can't use either ''' or """ around it)
                #

                #
                #   CQ_R: lemon: kc: not possible (""" not allowed)
                #   CQ_R: lemon: ks
                #
                [   '''almos\t done: ''\'""''',  """'''almos\\t done: ''\\'""'''"""         ],

                #
                #   CQ_R: pc: not possible (""" not allowed)
                #   CQ_R: ps
                #
                [   '''three: "''\''\''.""''',      r"""'''three: "''\''\''.""'''"""        ],
            #</CQ_R>

            #<N_K>
                #
                #   N_K/N_N: ra/rq:     not possible (ends in \)
                #   N_K/N_N: lemon: kc
                #   N_K/N_N: lemon: ks: not possible (''' not allowed)
                #
                [   'more lemo\ns\\',       "'more lemo\\ns\\\\'"                           ],

                #
                #   N_K/N_N: backslash: kc
                #   N_K/N_N: backslash: ks: not possible (''' not allowed)
                #
                [   'not a real lemon\\',  "'not a real lemon\\\\'"                         ],

                #
                #   N_K: pc/ps: not possible (always backslash)
                #
            #</N_K>

            #<N_N>
                #
                #   N_N: simple cases
                #
                [   r'',                            r"r''"                                  ],
                [   r'test#2',                      r"r'test#2'"                            ],

                #
                #   N_N: ra
                #
                [   r'double backslash: \\',        r"r'double backslash: \\'"              ],

                #
                #   N_N: rq
                #
                [   r"\'",                          r'''r"\'"'''                            ],

                #
                #   N_N: lemon: kc
                #   N_N: lemon: ks: not possible (''' not allowed)
                #
                [   'A \normal lemo\n',             "'A \\normal lemo\\n'"                  ],

                #
                #   N_K/N_N: backslash: kc
                #   N_K/N_N: backslash: ks: not possible (''' not allowed)
                #
                [   'backslash: \\',                "'backslash: \\\\'"                     ],

                #
                #   N_N: pc/ps: not possible (always raw mode)
                #
            #</N_N>

            #<Q_K>
                #
                #   Q_K/Q_N: ra/rq:     not possible (ends in \)
                #   Q_K/Q_N: lemon: kc
                #   Q_K/Q_N: lemon: ks: not possible (''' not allowed)
                #
                [   'le"mo"\nade\\',                """'le"mo"\\nade\\\\'"""                ],

                #
                #   Q_K/A_N: backslash: kc
                #   Q_K/A_N: backslash: ks: not possible (''' not allowed)
                #
                [   'just " & \\',                  """'just " & \\\\'"""                   ],

                #
                #   Q_K: pc/ps: not possible (always backslash)
                #
            #</Q_K>

            #<Q_N>
                #
                #   Q_N: ra
                #
                [   r'" is a quotation mark',       r"""r'" is a quotation mark'"""         ],

                #
                #   Q_N: rq
                #
                [   r'\'"\'',                       r"""r'\'"\''"""                         ],

                #
                #   Q_N: lemon: kc
                #   Q_N: lemon: ks: not possible (''' not allowed)
                #
                [   'A "\normal" lemo\n',           """'A "\\normal" lemo\\n'"""            ],

                #
                #   Q_N: pc/ps: not possible (always raw)
                #
            #</Q_N>

            #<Q_Q>
                #
                #   Q_Q: ra
                #
                [   r'"',                           r"""r'"'"""                             ],

                #
                #   Q_Q: rq
                #
                [   r'She \'said\' \'hello"',       r"""r'She \'said\' \'hello"'"""         ],

                #
                #   Q_Q: lemon: kc
                #   Q_Q: lemon: ks: not possible (''' not allowed)
                #
                [   'lemo\n "orchard"',             """'lemo\\n "orchard"'"""               ],

                #
                #   Q_Q: pc/ps: not possible (always raw)
                #
            #</Q_Q>

            #<Q_R>
                #
                #   Q_R: ra
                #
                [   r'double quoted: ""',           r"""r'double quoted: ""'"""             ],

                #
                #   Q_R: rq
                #
                [   r'More \'\'\' than ""',         r"""r'More \'\'\' than ""'"""           ],

                #
                #   Q_R: lemon: kc
                #   Q_R: lemon: ks: not possible (''' not allowed)
                #
                [   'lemo\n"s and quotes""',        """'lemo\\n"s and quotes""'"""          ],

                #
                #   Q_Q: pc/ps: not possible (always raw)
                #
            #</Q_R>

            #<S_N>
                #
                #   S_N: ra
                #
                #   NOTE:
                #       vim 7.4 gets confused with """x\"""" & '''x\'''' - so use string concatanation so
                #       vim can properly parse it.
                #
                [   r'lots of """"" - lots!',       '''r'lots of """"" - lots!''' + "'"     ],
            #</S_N>
        ]:
            if s is 0:
                break

            actual = portray_raw_string(s)

            if actual != expected:
                line('%r', s)
                line('  actual:   %s', actual)
                line('  expected: %s', expected)

                raise_value_error('portray_raw_string(%r): %r (expected: %r)', s, actual, expected)

        line('PASSED: portray_raw_string')
