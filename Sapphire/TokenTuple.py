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


        nub = static_conjure_nub


        def order(a, b):
            if a is b:  return 0

            r = a.class_order - b.class_order

            if r < 0:   return -1
            if r > 0:   return 1

            a_total = length(a)
            b_total = length(b)
            total   = minimum(a_total, b_total)

            a_next = next_method(iterate(a))
            b_next = next_method(iterate(b))

            while total:
                r = a_next().order(b_next())

                if r < 0:   return -1
                if r > 0:   return 1

                total -= 1

            if a_total < b_total:   return -1
            if a_total > b_total:   return 1

            raise_runtime_error('a<%r> == b<%r>: but not identical', a, b)


        def write(t, w):
            for v in t:
                v.write(w)
