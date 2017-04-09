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
    from Tremolite import ONE_OR_MORE, OPTIONAL, Q, PRINTABLE, PRINTABLE_MINUS, ZERO_OR_MORE


    @share
    def create_sapphire_match():
        ow = NAME('ow', ZERO_OR_MORE(' '))
        w  = NAME('w', ONE_OR_MORE(' '))

        middle_ow = NAME('middle_ow', OPTIONAL(w + NOT_FOLLOWED_BY(ANY_OF(LINEFEED, ' ', '#'))))

        newline = NAME       ('newline', ow + OPTIONAL('#' + ZERO_OR_MORE(DOT)) + LINEFEED)

        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))

        name   = NAME('name', letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        name1  = NAME('name1', name)
        name2  = NAME('name2', name)
        name3_G  = NAMED_GROUP('name3', name)
        name4_G  = NAMED_GROUP('name4', name)
        number_G = NAMED_GROUP('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE('0-9'))

        single_quote_G = NAMED_GROUP(
                           'single_quote',
                           (
                                  "'" + ONE_OR_MORE(BACKSLASH + PRINTABLE | PRINTABLE_MINUS("'", '\\')) + "'"
                                | ("''" + NOT_FOLLOWED_BY("'"))
                           )
                       )

        left_parenthesis__N         = NAME      ('left_parenthesis__N',          ow + '(' + ow)
        right_parenthesis__colon__N = NAMED_GROUP('right_parenthesis__colon__N', ow + ')' + ow + ':')

        comma_G                     = NAMED_GROUP('comma',                    ow + ',' + ow)
        dot_G                       = NAMED_GROUP('dot',                      ow + '.' + ow)
        left_parenthesis__G         = NAMED_GROUP('left_parenthesis',         left_parenthesis__N)
        right_parenthesis__colon__G = NAMED_GROUP('right_parenthesis__colon', right_parenthesis__colon__N)
        right_parenthesis__G        = NAMED_GROUP('right_parenthesis',        ow + ')' + middle_ow)

        keyword__as__w = NAMED_GROUP('keyword__as__w', w + 'as' + w)

        keyword__import__w = NAMED_GROUP('keyword__import__w', w + 'import' + w)

        keyword__ow = NAMED_GROUP(
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

        comment = NAME('comment', '#' + G('comment', ZERO_OR_MORE(DOT)))

        #
        #   Generic
        #
        name_match = MATCH('name_match', name, debug = true)

        #
        #   Expressions
        #
        MATCH(
            'argument_1_match',
            (
                  (G(name) | number_G | single_quote_G)
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
                  (G(name) | number_G | single_quote_G)
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
                  (G(name) | number_G)
                + G('operator__ow', ow + G('operator', ANY_OF(']')) + ow)
            )
        )

        MATCH(
            'statement_expression_match',
            (
                  OPTIONAL(dot_G + G('right', name))
                + G('operator__ow', ow + G('operator', ANY_OF('(')) + ow)
                + OPTIONAL(G(name) | number_G | single_quote_G)
                + OPTIONAL(
                        #   (
                        G('right_parenthesis', ow + ')')
                      + OPTIONAL(G(newline) + END_OF_PATTERN)
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
                  ow
                + OPTIONAL(G('token', '@' | name) + ow)
                + OPTIONAL(OPTIONAL(comment) + G('newline', LINEFEED) + END_OF_PATTERN)
            ),
        )

        MATCH(
            'define1_parenthesis_match',
            (
                  left_parenthesis__N
                + OPTIONAL(right_parenthesis__colon__N + G(newline) + END_OF_PATTERN)
            ),
            debug = true,
        )

        MATCH(
            'define1__right_parenthesis__colon__match',
            right_parenthesis__colon__G + G(newline) + END_OF_PATTERN,
            debug = true,
        )

        FULL_MATCH(
            'define1_match2',
            left_parenthesis__G + Q(name2) + right_parenthesis__colon__G + G(newline),
        )


        #
        #   Statements - Parse 7
        #
        MATCH(
            'line7_match',
            G('indented', ow)
                + (
                        keyword__ow + OPTIONAL(G('newline_1', LINEFEED) + END_OF_PATTERN)
                      | G(name)
                      | (comment | EMPTY) + G('newline_2', LINEFEED) + END_OF_PATTERN
                  )
        )

        FULL_MATCH(
            'class_match',
            G(name1) + left_parenthesis__G + G(name2) + right_parenthesis__colon__G + G(newline),
        )

        FULL_MATCH(
            'define7_match',
            G(name1) + left_parenthesis__G + Q(name2) + right_parenthesis__colon__G + G(newline),
        )

        MATCH(
            'from_1_match',
            (
                  G(name1) + OPTIONAL(dot_G + G(name2))
                + keyword__import__w + name3_G
                + keyword__as__w + name4_G
                + (comma_G | G(newline) + END_OF_PATTERN)
            )
        )

        MATCH(
            'from_2_match',
            G(name1) + keyword__as__w + G(name2) + (comma_G | G(newline) + END_OF_PATTERN)
        )

        FULL_MATCH('import_match', G(name1) + G(newline))

        FULL_MATCH(
            'expression_match',
            (
                  G(name)
                + OPTIONAL(left_parenthesis__G + OPTIONAL(single_quote_G) + right_parenthesis__G)
                + G(newline)
            ),
        )

        create_match_code('../Sapphire/Match.py', '2017 Amit Green', 'Sapphire.Match')
