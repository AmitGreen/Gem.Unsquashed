#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Line')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    @export
    class EmptyLine(Token):
        __slots__    = (())
        display_name = 'empty-line'
