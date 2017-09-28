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
    from Tremolite import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_ANY_OF, NOT_FOLLOWED_BY
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
        assign_operator     = NAME('assign_operator',     '=')
        colon               = NAME('colon',               ':')
        comma               = NAME('comma',               ',')
        comment_newline     = NAME('comment_newline',     P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        compare_equal       = NAME('compare_equal',       '==')
        dot                 = NAME('dot',                 '.')
        equal_sign          = NAME('equal_sign',          '=')
        greater_than_sign   = NAME('greater_than_sign',   '>')
        keyword_as          = NAME('as',                  'as')
        keyword_else        = NAME('else',                'else')
        keyword_except      = NAME('except',              'except')
        keyword_finally     = NAME('finally',             'finally')
        keyword_for         = NAME('for',                 'for')
        keyword_if          = NAME('if',                  'if')
        keyword_import      = NAME('import',              'import')
        keyword_in          = NAME('in',                  'in')
        keyword_is          = NAME('is',                  'is')
        keyword_not         = NAME('not',                 'not')
        keyword_or          = NAME('or',                  'or')
        keyword_try         = NAME('try',                 'try')
        left_brace          = NAME('left_brace',          '{')                                #   }
        left_parenthesis    = NAME('left_parenthesis',    '(')                                #   )
        left_square_bracket = NAME('left_square_bracket', '[')                                #   ]
        less_than_sign      = NAME('less_than_sign',      '<')
        logical_and_sign    = NAME('logical_and_sign',    '&')
        logical_or_sign     = NAME('logical_or_sign',     '|')
        minus_sign          = NAME('minus_sign',          '-')
        not_equal           = NAME('not_equal',           '!=')
        percent_sign        = NAME('percent_sign',        '%')
        plus_sign           = NAME('plus_sign',           '+')
        slash_sign          = NAME('slash_sign',          '/')
        star_sign           = NAME('star',                '*')
        tilde_sign          = NAME('tilde',               '~')

        name                = NAME('name',   letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        number              = NAME('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        period              = NAME('period', '.')

        double_quote = NAME(
                           'double_quote',
                           (
                                  '"'
                                + (
                                        (
                                              '"'
                                            + OPTIONAL(
                                                    '"'
                                                  + ONE_OR_MORE(
                                                          PRINTABLE_MINUS('"', '\\')
                                                        | BACKSLASH + PRINTABLE
                                                        | '"' + P('"') + NOT_FOLLOWED_BY('"')
                                                    ) + '"""'
                                              )
                                      )
                                      | ONE_OR_MORE(PRINTABLE_MINUS('"', '\\') | BACKSLASH + PRINTABLE) + '"'
                                  )
                           ),
                       )

        single_quote = NAME(
                           'single_quote',
                           (
                                  "'"
                                + (
                                        (
                                              "'"
                                            + OPTIONAL(
                                                    "'"
                                                  + ONE_OR_MORE(
                                                          PRINTABLE_MINUS("'", '\\')
                                                        | BACKSLASH + PRINTABLE
                                                        | "'" + P("'") + NOT_FOLLOWED_BY("'")
                                                    ) + "'''"
                                              )
                                      )
                                      | ONE_OR_MORE(PRINTABLE_MINUS("'", '\\') | BACKSLASH + PRINTABLE) + "'"
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
        keyword_in__ow  = NAME('keyword_in__ow',  keyword_in  + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))
        keyword_is__ow  = NAME('keyword_is__ow',  keyword_is  + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))
        keyword_not__ow = NAME('keyword_not__ow', keyword_not + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))

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
        MATCH(
            'line_match',
            (
                  G('indented', ow)
                + Q(
                      'something',
                      (
                            #
                            #   Note:
                            #       Both 'keyword' and 'quote' must preceed 'atom', since otherwise they would
                            #       [partially] match 'atom'
                            #
                            G(
                                'keyword',
                                keyword_else | keyword_except | keyword_finally | keyword_try,
                            ) + ow + G(colon) + ow
                          | OPTIONAL('r') + G('quote', double_quote | single_quote) + ow
                          | G('atom', number | '@' | name) + ow
                          | G(
                                'operator',
                                ANY_OF(right_parenthesis, minus_sign, right_square_bracket, right_brace, tilde_sign)
                            ) + ow
                          | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                          | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
                          | G(left_brace__ow)          + P(G(right_brace)          + ow)
                      ),
                  )
                + Q(
                      'comment_newline',
                      P(
                            '#'
                          + G('comment', ZERO_OR_MORE(ow + ONE_OR_MORE(NOT_ANY_OF('\x00-\x1F', ' '))))
                          + ow
                      )
                      + G('newline', LINEFEED)
                  )
            ),
        )

        MATCH(
            'atom_match',
            (
                  OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preceed 'name'
                | G('atom', number | name) + ow
                | G(
                      'operator',
                      ANY_OF(
                          right_parenthesis, star_sign, minus_sign, colon, right_square_bracket, right_brace,
                          tilde_sign,
                      ),
                  ) + ow
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
            ) + Q(comment_newline),
        )

        MATCH(
           'operator_match',
            (
                  G(
                      'operator',
                       (
                             (
                                   ANY_OF(
                                       logical_and_sign, percent_sign, plus_sign, minus_sign, equal_sign,
                                       logical_or_sign,
                                   )
                                 | greater_than_sign + P(greater_than_sign)
                                 | less_than_sign    + P(less_than_sign)
                                 | star_sign         + P(star_sign)
                                 | slash_sign        + P(slash_sign)
                             ) + P(equal_sign)
                           | ANY_OF(right_parenthesis, dot, right_square_bracket, right_brace)
                           | not_equal
                       ),
                  ) + ow
                | G(left_parenthesis__ow) + P(G(right_parenthesis) + ow)
                | G(left_square_bracket__ow) + P(G('tail_index__ow', colon + ow) + P(G(right_square_bracket) + ow))
                | G(comma) + ow + P(G('comma_suffix', right_parenthesis | right_square_bracket) + ow)
                | G(colon) + ow + P(G('head_index', right_square_bracket) + ow)
                | (
                        G(
                            'keyword',
                            (
                                  'a' + (EXACT('nd') | 's')
                                | keyword_else
                                | keyword_for
                                | 'i' + ANY_OF('f', 'n')
                                | keyword_or
                            ),
                        )
                      + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore))
                  )
                | G(keyword_is__ow)  + Q('is_not', keyword_not__ow)
                | G(keyword_not__ow) + Q('not_in', keyword_in__ow)
            ) + Q(comment_newline),
        )


        #
        #   Statements - Parse 1
        #
        MATCH(
            'header_parenthesis_match1',
            (
                  G(left_parenthesis) + ow + P(G(right_parenthesis) + ow + P(G(colon) + ow))
                + Q(comment_newline)
            ),
        )

        MATCH(
            'parameter_atom_match',
            (
                  Q(star_sign) + G(name) + ow
                | G(right_parenthesis) + ow + P(G(colon) + ow)
            ) + Q(comment_newline),
        )

        MATCH(
            'parameter_operator_match',
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
            ) + Q(comment_newline),
        )

        FULL_MATCH(
            'parameter_colon_newline_match',
            G(colon) + ow + comment_newline,
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
        #   Create ../Sapphire/Match.py
        #
        create_match_code('../Sapphire/Match.py', '2017 Amit Green', 'Sapphire.Match')
