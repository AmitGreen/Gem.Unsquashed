#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Pattern')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Tremolite.Build')
    require_gem('Tremolite.CreateMatch')
    require_gem('Tremolite.Name')


    from Tremolite import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT
    from Tremolite import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_FOLLOWED_BY
    from Tremolite import ONE_OR_MORE, OPTIONAL, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    FULL_MATCH = MATCH
    P          = OPTIONAL


    @share
    def create_sapphire_match():
        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))
        ow                         = NAME('ow',                         ZERO_OR_MORE(' '))
        w                          = NAME('w',                          ONE_OR_MORE(' '))

        colon               = NAME('colon',               ':')
        comma               = NAME('comma',               ',')
        comment_newline     = NAME('comment_newline',     P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        compare_equal       = NAME('compare_equal',       '==')
        dot                 = NAME('dot',                 '.')
        assign_operator     = NAME('assign_operator',     '=')
        equal_sign          = NAME('equal_sign',          '=')
        keyword_as          = NAME('as',                  'as')
        keyword_except      = NAME('except',              'except')
        keyword_import      = NAME('import',              'import')
        keyword_try         = NAME('try',                 'try')
        left_parenthesis    = NAME('left_parenthesis',    '(')                                #   )
        left_square_bracket = NAME('left_square_bracket', '[')                                #   ]

        name                = NAME('name',   letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        number              = NAME('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        period              = NAME('period', '.')

        single_quote = NAME(
                           'single_quote',
                           (
                                  "'"
                                + (
                                        ONE_OR_MORE(BACKSLASH + PRINTABLE | PRINTABLE_MINUS("'", '\\')) + "'"
                                      | ("'" + NOT_FOLLOWED_BY("'"))
                                  )
                           ),
                       )


        #   [(
        right_parenthesis    = NAME('right_parenthesis',    ')')
        right_square_bracket = NAME('right_square_bracket', ']')

        left_parenthesis__ow = NAME('left_parenthesis__ow', left_parenthesis + ow)
        name1                = NAME('name1',                name)
        name2                = NAME('name2',                name)
        name3                = NAME('name3',                name)
        name4                = NAME('name4',                name)
        ow_comma_ow          = NAME('ow_comma_ow',          ow + comma + ow)
        ow_comment_newline   = NAME('ow_comment_newline',   ow + comment_newline)
        ow_dot_ow            = NAME('ow_dot_ow',            ow + period + ow)
        w_as_w               = NAME('w_as_w',               w + keyword_as + w)
        w_import_w           = NAME('w_import_w',           w + keyword_import + w)

        right_parenthesis__colon     = NAME('right_parenthesis__colon',     right_parenthesis + ow + colon)
        ow__right_parenthesis__colon = NAME('ow__right_parenthesis__colon', ow + right_parenthesis + ow + colon)

        ow__right_parenthesis__colon__ow = NAME(
                                               'ow__right_parenthesis__colon__ow',
                                               ow + right_parenthesis + ow + colon + ow,
                                           )

        #
        #   OLD
        #
        #   (
        OLD__middle_ow = NAME('OLD__middle_ow', P(w + NOT_FOLLOWED_BY(ANY_OF(LINEFEED, '#'))))

        OLD__right_parenthesis   = NAME('OLD__right_parenthesis',   ow + ')' + OLD__middle_ow)
        ow__left_parenthesis__ow = NAME('ow__left_parenthesis__ow', ow + '(' + ow)              #   )

        #
        #   With internal group
        #
        pound_G_comment = NAME('pound_G_comment', '#' + G('comment', ZERO_OR_MORE(DOT)))

        G__keyword__ow = NAMED_GROUP(
                          'keyword__ow',
                          (
                                G(
                                    'keyword',
                                    (
                                          '@'
                                        | (
                                                (EXACT('def') | 'class' | 'from' | 'import' | 'return')
                                              + NOT_FOLLOWED_BY(alphanumeric_or_underscore)
                                          )
                                    )
                                )
                              + ow
                          ),
                      )


        #
        #   Generic
        #
        name_match = MATCH('name_match', name)


        #
        #   Expressions 1
        #
        FULL_MATCH('ow_comment_newline_match', G(ow_comment_newline))
        
        MATCH(
            'atom_match',
            (
                  G('atom', name | number | single_quote) + ow
                | G(left_parenthesis__ow) + P(G(right_parenthesis) + ow)
            ) + Q(comment_newline),
        )

        MATCH(
            'atom_match1',
            name | number | single_quote,
        )

        MATCH(
           'decorator_postfix_match1',
            (
                  ow
                + P(G(left_parenthesis__ow) + P(G(right_parenthesis) + ow))
                + Q(comment_newline)
            ),
        )

        MATCH(
           'operator_match',
            (
                (
                      (
                            G(
                                'operator',
                                 (
                                       ANY_OF('=') + P('=')
                                     | colon
                                     | comma
                                     | dot
                                     | keyword_as
                                     | left_square_bracket
                                     | right_parenthesis
                                     | right_square_bracket
                                 ),
                            )
                          + ow
                      )
                    | G(left_parenthesis__ow) + P(G(right_parenthesis) + ow)
                )
                + Q(comment_newline)
            ),
        )

        MATCH(
            'single_quote_match',
            single_quote,
        )

        MATCH(
            'statement_postfix_operator_match1',
            (
                  G('operator', assign_operator | dot) + ow
                | G(left_parenthesis__ow) + P(G(right_parenthesis) + ow) + Q(comment_newline)
            ),
        )


        #
        #   Expressions 7
        #
        MATCH(
            'argument7_1_match',
            (
                  (G(name) | G(number) | G(single_quote))
                + G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + OLD__middle_ow)        #   ]
            )
        )

        MATCH(
            'argument7_1A_match',
            G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + OLD__middle_ow)              #   ]
        )

        MATCH(
            'argument7_2_match',
            (
                  (G(name) | G(number) | G(single_quote))
                + G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',')) + OLD__middle_ow)
            ),
        )

        MATCH(
            'argument7_postfix_match',
            #   (
            G('operator__ow', ow + G('operator', ANY_OF(')', ',')) + OLD__middle_ow)
        )

        MATCH(
            'index_1_match',
            (
                  (G(name) | G(number))
                + G('operator__ow', ow + G('operator', ANY_OF(']')) + ow)
            )
        )

        MATCH(
            'statement_expression_match',
            (
                  P(G(ow_dot_ow) + G('right', name))
                + G('operator__ow', ow + G('operator', ANY_OF('(')) + ow)
                + P(G(name) | G(number) | G(single_quote))
                + P(
                        #   (
                        G('right_parenthesis', ow + ')')
                      + Q(ow_comment_newline)
                  )
            )
        )

        FULL_MATCH('statement_postfix_match', G(ow_comment_newline))


        #
        #   Statements - Parse 1
        #
        MATCH(
            'line_match1',
            (
                  G('indented', ow)
                + P(
                       G('keyword', keyword_except | keyword_try) + ow + colon + ow
                      |G('token', '@' | name) + ow
                  )
                + P(P(pound_G_comment) + G('newline', LINEFEED))
            ),
        )

        MATCH(
            'class_parenthesis_match1',
            (
                  ow
                + (
                        (
                              G(left_parenthesis) + ow
                            + P(right_parenthesis__colon + G('ow_comment_newline_1', ow_comment_newline))
                        )
                      | (colon + G('ow_comment_newline_2', ow_comment_newline))
                  )
            ),
        )

        MATCH(
            'define_parenthesis_match1',
            (
                  ow__left_parenthesis__ow
                + P(right_parenthesis__colon + G(ow_comment_newline))
            ),
        )

        FULL_MATCH(
            'right_parenthesis__colon__match',
            G(ow__right_parenthesis__colon) + G(ow_comment_newline),
        )

        MATCH(
            'from_module_match1',
            ow + G('operator', period | 'import') + ow,
        )

        MATCH(
            'from_as_match1',
            (
                  ow
                + (
                        G('operator', keyword_as | comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'comma_or_newline_match1',
            (
                  ow
                + (
                        G(comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'import_module_match1',
            (
                  ow
                + (
                        G('operator', period | keyword_as | comma) + ow
                      | comment_newline
                  )
            ),
        )


        #
        #   Statements - Parse 7
        #
        MATCH(
            'line7_match',
            G('indented', ow)
                + (
                        G__keyword__ow + Q('newline_1', LINEFEED)
                      | G(name)
                      | P(pound_G_comment) + G('newline_2', LINEFEED)
                  )
        )

        FULL_MATCH(
            'class7_match',
            (
                  G(name1)
                + G('left_parenthesis', ow__left_parenthesis__ow)
                + G(name2)
                + G(ow__right_parenthesis__colon__ow)
                + G(comment_newline)
            ),
        )

        FULL_MATCH(
            'define7_match',
            (
                  G(name1)
                + G('left_parenthesis', ow__left_parenthesis__ow)
                + Q(name2)
                + G(ow__right_parenthesis__colon__ow)
                + G(comment_newline)
            ),
        )

        MATCH(
            'from7_1_match',
            (
                  G(name1) + P(G(ow_dot_ow) + G(name2))
                + G(w_import_w) + G(name3)
                + G(w_as_w) + G(name4)
                + (G(ow_comma_ow) | G(ow_comment_newline))
            ),
        )

        MATCH(
            'from_2_match',
            G(name1) + G(w_as_w) + G(name2) + (G(ow_comma_ow) | G(ow_comment_newline)),
        )

        FULL_MATCH('import7_match', G(name1) + G(ow_comment_newline))

        FULL_MATCH(
            'expression_match',
            (
                  G(name)
                + P(G('left_parenthesis', ow__left_parenthesis__ow) + P(G(single_quote)) + G(OLD__right_parenthesis))
                + G(ow_comment_newline)
            ),
        )


        #
        #   Create ../Sapphire/Match.py
        #
        create_match_code('../Sapphire/Match.py', '2017 Amit Green', 'Sapphire.Match')
