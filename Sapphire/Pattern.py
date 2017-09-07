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

        #
        #   Simple patterns
        #
        colon               = NAME('colon',               ':')
        comma               = NAME('comma',               ',')
        comment_newline     = NAME('comment_newline',     P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        compare_equal       = NAME('compare_equal',       '==')
        dot                 = NAME('dot',                 '.')
        assign_operator     = NAME('assign_operator',     '=')
        equal_sign          = NAME('equal_sign',          '=')
        keyword_as          = NAME('as',                  'as')
        keyword_except      = NAME('except',              'except')
        keyword_if          = NAME('if',                  'if')
        keyword_import      = NAME('import',              'import')
        keyword_in          = NAME('in',                  'in')
        keyword_not         = NAME('not',                 'not')
        keyword_or          = NAME('or',                  'or')
        keyword_try         = NAME('try',                 'try')
        left_brace          = NAME('left_brace',          '{')                                #   }
        left_parenthesis    = NAME('left_parenthesis',    '(')                                #   )
        left_square_bracket = NAME('left_square_bracket', '[')                                #   ]

        name                = NAME('name',   letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        number              = NAME('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        period              = NAME('period', '.')

        double_quote = NAME(
                           'double_quote',
                           (
                                  '"'
                                + (
                                        ONE_OR_MORE(PRINTABLE_MINUS('"', '\\') | BACKSLASH + PRINTABLE) + '"'
                                      | ('"' + NOT_FOLLOWED_BY('"'))
                                  )
                           ),
                       )

        single_quote = NAME(
                           'single_quote',
                           (
                                  "'"
                                + (
                                        ONE_OR_MORE(PRINTABLE_MINUS("'", '\\') | BACKSLASH + PRINTABLE) + "'"
                                      | ("'" + NOT_FOLLOWED_BY("'"))
                                  )
                           ),
                       )


        #   [(
        right_brace             = NAME('right_brace',             '}')
        right_parenthesis       = NAME('right_parenthesis',       ')')
        right_square_bracket    = NAME('right_square_bracket',    ']')

        #
        #   More complicated patterns
        #
        left_brace__ow          = NAME('left_brace__ow',          left_brace + ow)
        left_square_bracket__ow = NAME('left_square_bracket__ow', left_square_bracket + ow)
        left_parenthesis__ow    = NAME('left_parenthesis__ow',    left_parenthesis + ow)
        name1                   = NAME('name1',                   name)
        name2                   = NAME('name2',                   name)
        name3                   = NAME('name3',                   name)
        name4                   = NAME('name4',                   name)
        ow_comma_ow             = NAME('ow_comma_ow',             ow + comma + ow)
        ow_comment_newline      = NAME('ow_comment_newline',      ow + comment_newline)
        ow_dot_ow               = NAME('ow_dot_ow',               ow + period + ow)
        w_as_w                  = NAME('w_as_w',                  w + keyword_as + w)
        w_import_w              = NAME('w_import_w',              w + keyword_import + w)

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
        name_match             = MATCH('name_match', name)
        name_ow_match          = MATCH('name_ow_match', G(name) + ow + Q(comment_newline))
        next_nested_line_match = MATCH('next_nested_line_match', ow + Q(comment_newline))


        #
        #   Expressions 1
        #
        FULL_MATCH('ow_comment_newline_match', G(ow_comment_newline))
        
        MATCH(
            'argument_atom_match',
            (
                  (
                        G('keyword', keyword_if | keyword_not)
                      + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore))
                  )
                | OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preced 'name'
                | G('atom', name | number) + ow
                #
                #<differs-from: atom-match>
                #
                #   (
                #
                | G('operator', ANY_OF('-', ')')) + ow
                #</differs>
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
#               | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
            ) + Q(comment_newline),
        )


        MATCH(
            'atom_match',
            (
                  (
                        G('keyword', keyword_if | keyword_not)
                      + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore))
                  )
                | OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preced 'name'
                | G('atom', name | number) + ow
                #
                #<differs-from: {argument,index}_atom_match>
                #
                | G('operator', ANY_OF('-')) + ow
                #</differs-from>
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
#               | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
            ) + Q(comment_newline),
        )

        MATCH(
            'index_atom_match',
            (
                  (
                        G('keyword', keyword_if | keyword_not)
                      + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore))
                  )
                | OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preced 'name'
                | G('atom', name | number) + ow
                #
                #<differs-from: atom-match>
                #
                #   [
                #
                | G('operator', ANY_OF('-', ']')) + ow
                #</differs>
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
#               | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
            ) + Q(comment_newline),
        )


        MATCH(
           'operator_match',
            (
                (
                      (
                            G(
                                'operator',
                                 (
                                       ANY_OF('+', '<', '=') + P('=')
                                     | colon | comma | dot
                                     | keyword_as | keyword_in | keyword_or
                                     | right_parenthesis
                                     | right_square_bracket
                                 ),
                            )
                          + ow
                      )
                    | G(left_parenthesis__ow)    + P(G(right_parenthesis) + ow)
                    | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
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
            'header_parenthesis_match1',
            (
                  G(left_parenthesis) + ow + P(G(right_parenthesis) + ow + P(G(colon) + ow))
                + Q(comment_newline)
            ),
        )

        MATCH(
            'parameter_argument_match',
            (
                  (
                        G(name) + ow
                      | G(right_parenthesis) + ow + P(G(colon) + ow)
                  )
                + Q(comment_newline)
            ),
        )
            
        MATCH(
            'parameter_operator_match',
            (
                  (
                        G(equal_sign) + ow
                      | (
                              G(comma) + ow
                            + P(
                                    G('comma_RP', right_parenthesis) + ow
                                  + P(G('comma_RP_colon', colon) + ow)
                              )
                        )
                      | G(right_parenthesis) + ow + P(G(colon) + ow)
                  )
                + Q(comment_newline)
            ),
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
