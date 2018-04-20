#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Player')
def gem():
    #require_gem('Crystal.Core')


    class Player(Object):
        __slots__ = ((
            'name',                     #   String+
        ))


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<Player %s>', t.name)


    alice = Player('Alice')
    bob   = Player('Bob')


    share(
        'alice',        alice,
        'bob',          bob,
    )
