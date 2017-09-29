#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TokenTuple')
def gem():
    class TokenTuple(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def count_newlines(t):
            total = 0

            for v in t:
                total += v.count_newlines()

            return total


        def display_token(t):
            return arrange('<%s %s>', t.display_name, ' '.join(v.display_token()   for v in t))


        def write(t, v):
            for v in t:
                v.write(w)
