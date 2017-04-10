#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Pattern')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Tremolite.Build')
    require_gem('Tremolite.CreateMatch')
    require_gem('Tremolite.Name')


    from Tremolite import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT, FULL_MATCH
    from Tremolite import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_FOLLOWED_BY
    from Tremolite import ONE_OR_MORE, OPTIONAL as P, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    @share
    def create_sapphire_match():
        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))
        ow                         = NAME('ow',                         ZERO_OR_MORE(' '))
        w                          = NAME('w',                          ONE_OR_MORE(' '))

        name      = NAME('name',      letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        middle_ow = NAME('middle_ow', P(w + NOT_FOLLOWED_BY(ANY_OF(LINEFEED, ' ', '#'))))

        comma                    = NAME('comma',                    ow + ',' + ow)
        dot                      = NAME('dot',                      ow + '.' + ow)
        keyword__as__w           = NAME('keyword__as__w',           w + 'as' + w)
        keyword__import__w       = NAME('keyword__import__w',       w + 'import' + w)
        left_parenthesis         = NAME('left_parenthesis',         ow + '(' + ow)
        name1                    = NAME('name1',                    name)
        name2                    = NAME('name2',                    name)
        name3                    = NAME('name3',                    name)
        name4                    = NAME('name4',                    name)
        newline                  = NAME('newline',                  ow + P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        number                   = NAME('number',                   '0' | ANY_OF('1-9') + ZERO_OR_MORE('0-9'))
        right_parenthesis__colon = NAME('right_parenthesis__colon', ow + ')' + ow + ':')
        right_parenthesis        = NAME('right_parenthesis',        ow + ')' + middle_ow)

        single_quote = NAME(
                           'single_quote',
                           (
                                  "'" + ONE_OR_MORE(BACKSLASH + PRINTABLE | PRINTABLE_MINUS("'", '\\')) + "'"
                                | ("''" + NOT_FOLLOWED_BY("'"))
                           )
                       )


        #
        #   With internal group
        #
        G_comment = NAME('comment', '#' + G('comment', ZERO_OR_MORE(DOT)))

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
        #   Expressions
        #
        MATCH(
            'argument_1_match',
            (
                  (G(name) | G(number) | G(single_quote))
                + G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + middle_ow)     #   ]
            )
        )

        MATCH(
            'argument_1A_match',
            G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',', '[')) + middle_ow)          #   ]
        )

        MATCH(
            'argument_2_match',
            (
                  (G(name) | G(number) | G(single_quote))
                + G('operator__ow', ow + G('operator', ANY_OF('(', ')', ',')) + middle_ow)
            ),
        )

        MATCH(
            'argument_postfix_match',
            #   (
            G('operator__ow', ow + G('operator', ANY_OF(')', ',')) + middle_ow)
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
                  P(G(dot) + G('right', name))
                + G('operator__ow', ow + G('operator', ANY_OF('(')) + ow)
                + P(G(name) | G(number) | G(single_quote))
                + P(
                        #   (
                        G('right_parenthesis', ow + ')')
                      + P(G(newline) + END_OF_PATTERN)
                  )
            )
        )

        FULL_MATCH('statement_postfix_match', G(newline))


        #
        #   Statements - Parse 1
        #
        MATCH(
            'line1_match',
            (
                  Q('indented', w)
                + P(G('token', '@' | name) + ow)
                + P(P(G_comment) + G('newline', LINEFEED) + END_OF_PATTERN)
            ),
            debug = true,
        )

        MATCH(
            'define1_parenthesis_match',
            (
                  left_parenthesis
                + P(right_parenthesis__colon + G(newline) + END_OF_PATTERN)
            ),
        )

        FULL_MATCH(
            'define1__right_parenthesis__colon__match',
            G(right_parenthesis__colon) + G(newline),
        )


        #
        #   Statements - Parse 7
        #
        MATCH(
            'line7_match',
            G('indented', ow)
                + (
                        G__keyword__ow + P(G('newline_1', LINEFEED) + END_OF_PATTERN)
                      | G(name)
                      | (G_comment | EMPTY) + G('newline_2', LINEFEED) + END_OF_PATTERN
                  )
        )

        FULL_MATCH(
            'class_match',
            G(name1) + G(left_parenthesis) + G(name2) + G(right_parenthesis__colon) + G(newline),
        )

        FULL_MATCH(
            'define7_match',
            G(name1) + G(left_parenthesis) + Q(name2) + G(right_parenthesis__colon) + G(newline),
        )

        MATCH(
            'from_1_match',
            (
                  G(name1) + P(G(dot) + G(name2))
                + G(keyword__import__w) + G(name3)
                + G(keyword__as__w) + G(name4)
                + (G(comma) | G(newline) + END_OF_PATTERN)
            )
        )

        MATCH(
            'from_2_match',
            G(name1) + G(keyword__as__w) + G(name2) + (G(comma) | G(newline) + END_OF_PATTERN)
        )

        FULL_MATCH('import_match', G(name1) + G(newline))

        FULL_MATCH(
            'expression_match',
            (
                  G(name)
                + P(G(left_parenthesis) + P(G(single_quote)) + G(right_parenthesis))
                + G(newline)
            ),
        )

        create_match_code('../Sapphire/Match.py', '2017 Amit Green', 'Sapphire.Match')
