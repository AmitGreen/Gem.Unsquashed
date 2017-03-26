#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Match')
def gem():
    require_gem('Tremolite.Core')


    class TremoliteMatch(Object):
        __slots__ = ((
            'name',                     #   String
            'pattern',                  #   String
        ))
