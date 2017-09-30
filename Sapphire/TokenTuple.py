#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TokenTuple')
def gem():
    @share
    class TokenTuple(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def count_newlines(t):
            return sum(v.count_newlines()   for v in t)


        def display_token(t):
            return arrange('<%s %s>', t.display_name, ' '.join(v.display_token()   for v in t))


        def write(t, w):
            for v in t:
                v.write(w)
