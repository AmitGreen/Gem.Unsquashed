#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Line')
def gem():
    require_gem('Pearl.Core')
    require_gem('Pearl.Token')


    @export
    class EmptyLine(Token):
        __slots__ = (())


        def __repr__(t):
            return arrange('<EmptyLine %r>', t.s)


    @export
    class IndentedPoundSignComment(Object):
        __slots__ = ((
            'indented',                 #   TokenIndented
            'comment',                  #   String+
            'newline',                  #   TokeNewline
        ))


        def __init__(t, indented, comment, newline):
            assert (indented.is_token_indented) and (newline.is_token_newline)

            t.indented = indented
            t.comment  = comment
            t.newline  = newline


        def __repr__(t):
            if t.comment is '':
                return arrange('<indented-# %r %r>', t.indented.s, t.newline.s)

            return arrange('<indented-# %r %r %r>', t.indented.s, t.comment, t.newline.s)


        def write(t, w):
            w(t.indented.s + '#' + t.comment + t.newline.s)


    @export
    class PoundSignComment(Object):
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
                return arrange('<# %r>', t.newline)

            return arrange('<# %r %r>', t.comment, t.newline)


        def write(t, w):
            w('#' + t.comment + t.newline.s)
