#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Quartz.Line')
def gem():
    require_gem('Quartz.Core')


    @export
    class IndentedDashDashComment(Object):
        __slots__        = slots__indented_comment
        comment_operator = '--'
        display_name     = 'indented -- line'
        __init__         = construct__indented_comment
        __repr__         = display__indented_comment
        write            = write__indented_comment


    @export
    class DashDashComment(Object):
        __slots__ = ((
            'comment',                  #   Comment
            'newline',                  #   String
        ))


        def __init__(t, comment, newline):
            assert newline.is_token_newline

            t.comment = comment
            t.newline = newline


        def __repr__(t):
            if t.comment is '':
                return arrange('<-- %r>', t.newline.s)

            return arrange('<-- %r %r>', t.comment, t.newline.s)


        def write(t, w):
            w('#' + t.comment + t.newline.s)
