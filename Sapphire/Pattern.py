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

        comma           = NAME('comma',           ',')
        comment_newline = NAME('comment_newline', P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        period          = NAME('period',          '.')
        name            = NAME('name',            letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))

        keyword_as           = NAME('as',                   'as')
        left_parenthesis     = NAME('left_parenthesis',     '(')                                #   )
        left_parenthesis__ow = NAME('left_parenthesis__ow', '(' + ow)                           #   )
        name1                = NAME('name1',                name)
        name2                = NAME('name2',                name)
        name3                = NAME('name3',                name)
        name4                = NAME('name4',                name)
        number               = NAME('number',               '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        ow_comma_ow          = NAME('ow_comma_ow',          ow + comma + ow)
        ow_comment_newline   = NAME('ow_comment_newline',   ow + comment_newline)
        ow_dot_ow            = NAME('dot',                  ow + period + ow)
        w_as_w               = NAME('w_as_w',               w + 'as' + w)
        w_import_w           = NAME('w_import_w',           w + 'import' + w)

        #   (
        ow__right_parenthesis__colon__ow = NAME('ow__right_parenthesis__colon__ow', ow + ')' + ow + ':' + ow)

        #   (
        right_parenthesis = NAME('right_parenthesis',     ')')

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

        #
        #   OLD
        #
        #   (
        OLD__middle_ow = NAME('OLD__middle_ow',  P(w + NOT_FOLLOWED_BY(ANY_OF(LINEFEED, ' ', '#'))))

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
        MATCH(
            'atom1_match',
            name | number | single_quote,
        )

        MATCH(
           'decorator1_match',
            (
                  ow
                + P(G(left_parenthesis) + ow + P(G(right_parenthesis) + ow))
                + Q(comment_newline)
            ),
        )

        MATCH(
           'postfix1_match',
            (
                  ow
                + P(G(left_parenthesis__ow) + P(G(right_parenthesis) + ow))
                + Q(comment_newline)
            ),
        )

        MATCH(
            'single_quote_match',
            single_quote,
        )

        MATCH(
            'argument1_operator1_match',
            ow + G(right_parenthesis) + ow + G(comment_newline),
        )


        #
        #   Expressions 7
        #
        MATCH(
            'argument7_1_match',
            (
                  (G(name) | G(number) | G(single_quote))
                + G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + OLD__middle_ow)     #   ]
            )
        )

        MATCH(
            'argument7_1A_match',
            G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + OLD__middle_ow)          #   ]
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
            'line1_match',
            (
                  Q('indented', w)
                + P(G('token', '@' | name) + ow)
                + P(P(pound_G_comment) + G('newline', LINEFEED))
            ),
        )

        MATCH(
            'define1_parenthesis_match',
            (
                  ow__left_parenthesis__ow
                + P(ow__right_parenthesis__colon__ow + G(comment_newline))
            ),
        )

        FULL_MATCH(
            'define1__right_parenthesis__colon__match',
            G(ow__right_parenthesis__colon__ow) + G(comment_newline),
        )

        MATCH(
            'from1_module_match',
            ow + G('operator', period | 'import') + ow,
        )

        MATCH(
            'from1_as_match',
            (
                  ow
                + (
                        G('operator', keyword_as | comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'comma1_or_newline_match',
            (
                  ow
                + (
                        G(comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'import1_module_match',
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
            'class_match',
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

        create_match_code('../Sapphire/Match.py', '2017 Amit Green', 'Sapphire.Match')
