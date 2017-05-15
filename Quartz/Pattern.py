#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Quartz.Pattern')
def gem():
    require_gem('Quartz.Core')
    require_gem('Tremolite.Build')
    require_gem('Tremolite.CreateMatch')
    require_gem('Tremolite.Name')


    from Tremolite import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT
    from Tremolite import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_FOLLOWED_BY
    from Tremolite import ONE_OR_MORE, OPTIONAL, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    FULL_MATCH = MATCH
    P          = OPTIONAL


    @share
    def create_quartz_match():
        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))
        ow                         = NAME('ow',                         ZERO_OR_MORE(' '))

        name = NAME('name', letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))

        #
        #   Generic
        #
        comment_newline = NAME('comment_newline',  P('#' + ZERO_OR_MORE(DOT)) + LINEFEED)
        name_match      = MATCH('name_match', name)


        ow_comment_newline  = NAME('ow_comment_newline',   ow + comment_newline)

        #
        #   With internal group
        #
        pound_G_comment = NAME('pound_G_comment', '#' + G('comment', ZERO_OR_MORE(DOT)))


        #
        #   MySQL 5.6
        #
        FULL_MATCH(
            'mysql_line_match',
            ow + P(pound_G_comment) + LINEFEED,
        )


        #
        #   Create ../Quartz/Match.py
        #
        create_match_code('../Quartz/Match.py', '2017 Amit Green', 'Quartz.Match')
