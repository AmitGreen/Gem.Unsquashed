#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleFrill')
def gem():
    triple_frill_cache  = {}
    lookup_triple_frill = triple_frill_cache.get
    store_triple_frill  = triple_frill_cache.__setitem__


    class Commented_VW_Frill(TripleTwig):
        __slots__ = (())
        comment   = TripleTwig.a
        v         = TripleTwig.b
        w         = TripleTwig.c

        display_name   = '#xy-frill'
        frill_estimate = 3

        __init__       = construct__abc
        __repr__       = portray__abc
        count_newlines = count_newlines__abc
        display_token  = display_token__abc


    class VWX_Frill(TripleTwig):
        __slots__ = (())
        comment   = 0
        v         = TripleTwig.a
        w         = TripleTwig.b
        x         = TripleTwig.c

        display_name   = 'xyz-frill'
        frill_estimate = 3

        __init__       = construct__abc
        __repr__       = portray__abc
        count_newlines = count_newlines__abc
        display_token  = display_token__abc


    conjure_commented_vw_frill = produce_conjure_triple(
                                     '#vw-frill',
                                     Commented_VW_Frill,
                                     triple_frill_cache,
                                     lookup_triple_frill,
                                     store_triple_frill,
                                 )

    conjure_vwx_frill = produce_conjure_triple(
                            'vwx-frill',
                            VWX_Frill,
                            triple_frill_cache,
                            lookup_triple_frill,
                            store_triple_frill,
                        )


    append_cache('triple-frill', triple_frill_cache)


    share(
        'conjure_commented_vw_frill',   conjure_commented_vw_frill,
        'conjure_vwx_frill',            conjure_vwx_frill,
    )
