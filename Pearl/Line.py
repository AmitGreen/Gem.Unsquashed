#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Line')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    #
    #<comment>
    #
    slots__comment = ((
        'comment',                      #   String+
        'newline',                      #   TokenNewline
    ))


    export(
        'slots__comment',       slots__comment,
    )


    @export
    def construct__comment(t, comment, newline):
        assert newline.is_token_newline

        t.comment  = comment
        t.newline  = newline


    @export
    def display__comment(t):
        if t.comment is '':
            return arrange('<%s %r>', t.display_name, t.newline.s)

        return arrange('<%s %r %r>', t.display_name, t.comment, t.newline.s)


    @export
    def write__comment(t, w):
        w(t.comment_operator + t.comment + t.newline.s)
    #</indented-comment>


    #
    #<indented-comment>
    #
    slots__indented_comment = ((
        'indented',                     #   TokenIndented
        'comment',                      #   String+
        'newline',                      #   TokenNewline
    ))


    export(
        'slots__indented_comment',      slots__indented_comment,
    )


    @export
    def construct__indented_comment(t, indented, comment, newline):
        assert (indented.is_token_indented) and (newline.is_token_newline)

        t.indented = indented
        t.comment  = comment
        t.newline  = newline


    @export
    def display__indented_comment(t):
        if t.comment is '':
            return arrange('<%s %r %r>', t.display_name, t.indented.s, t.newline.s)

        return arrange('<%s %r %r %r>', t.display_name, t.indented.s, t.comment, t.newline.s)


    @export
    def write__indented_comment(t, w):
        w(t.indented.s + t.comment_operator + t.comment + t.newline.s)
    #</indented-comment>


    @export
    class EmptyLine(Token):
        __slots__    = (())
        display_name = 'empty-line'


    @export
    class IndentedPoundSignCommentLine(Object):
        __slots__        = slots__indented_comment
        comment_operator = '#'
        display_name     = 'indented-#-line'
        __init__         = construct__indented_comment
        __repr__         = display__indented_comment
        write            = write__indented_comment


    @export
    class PoundSignCommentLine(Object):
        __slots__        = slots__comment
        comment_operator = '#'
        display_name     = '#-line'
        __init__         = construct__comment
        __repr__         = display__comment
        write            = write__comment
