#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Line')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    slots__indented_comment = ((
        'indented',                     #   TokenIndented
        'comment',                      #   String+
        'newline',                      #   TokenNewline
    ))


    def construct__indented_comment(t, indented, comment, newline):
        assert (indented.is_token_indented) and (newline.is_token_newline)

        t.indented = indented
        t.comment  = comment
        t.newline  = newline


    def display__indented_comment(t):
        if t.comment is '':
            return arrange('<%s %r %r>', t.display_name, t.indented.s, t.newline.s)

        return arrange('<%s %r %r %r>', t.display_name, t.indented.s, t.comment, t.newline.s)


    def write__indented_comment(t, w):
        w(t.indented.s + '#' + t.comment + t.newline.s)


    @export
    class EmptyLine(Token):
        __slots__    = (())
        display_name = 'empty-line'


    @export
    class IndentedPoundSignCommentLine(Object):
        __slots__    = slots__indented_comment
        display_name = 'indented-#-line'
        __init__     = construct__indented_comment
        __repr__     = display__indented_comment
        write        = write__indented_comment


    @export
    class TokenNewline(Token):
        display_name     = 'newline'
        is_token_newline = true


    @export
    class PoundSignCommentLine(Object):
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
                return arrange('<#-line %r>', t.newline.s)

            return arrange('<#-line %r %r>', t.comment, t.newline.s)


        def write(t, w):
            w('#' + t.comment + t.newline.s)
