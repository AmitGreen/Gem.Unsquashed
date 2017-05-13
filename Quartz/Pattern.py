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

        name  = NAME('name', letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))

        #
        #   Generic
        #
        name_match = MATCH('name_match', name)


        #
        #   Create ../Quartz/Match.py
        #
        create_match_code('../Quartz/Match.py', '2017 Amit Green', 'Quartz.Match')
