#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Nub')
def gem():
    require_gem('Sapphire.Core')


    nub_cache   = create_cache('nub')
    lookup_nub  = nub_cache.lookup
    provide_nub = nub_cache.provide


    class Nub(Object):
        __slots__ = ((
            'a',                        #   Any
        ))


        def __init__(t, a):
            t.a = a


        def __cmp__(t, that):
            return t.a.order(that.a)


    @static_method
    def conjure_nub(a):
        return (lookup_nub(a)) or (provide_nub(a, Nub(a)))


    share(
        'conjure_nub',      conjure_nub,
    )
