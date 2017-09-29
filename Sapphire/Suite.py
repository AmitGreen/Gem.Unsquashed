#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Suite')
def gem():
    suite_cache = {}


    class CommentSuite(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def count_newlines(t):
            total = 0

            for v in t:
                total += v.count_newlines()

            return total


        def display_token(t):
            return arrange('<comment-suite %s>', ' '.join(v.display_token()   for v in t))


        def write(t, v):
            for v in t:
                v.write(w)


    conjure_comment_suit = produce_conjure_tuple('comment-suite', CommentSuite, suite_cache)


    append_cache('suite', suite_cache)


    share(
        'conjure_comment_suit',     conjure_comment_suit,
    )
