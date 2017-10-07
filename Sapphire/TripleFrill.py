#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleFrill')
def gem():
    triple_frill_cache  = {}
    lookup_triple_frill = triple_frill_cache.get
    store_triple_frill  = triple_frill_cache.__setitem__


    class Commented_XY_Frill(TripleTwig):
        __slots__ = (())
        comment   = TripleTwig.a
        x         = TripleTwig.b
        y         = TripleTwig.c

        display_name   = '#xy-frill'
        frill_estimate = 3

        __init__       = construct__abc
        __repr__       = portray__abc
        count_newlines = count_newlines__abc
        display_token  = display_token__abc


    class XYZ_Frill(TripleTwig):
        __slots__ = (())
        comment   = 0
        x         = TripleTwig.a
        y         = TripleTwig.b
        z         = TripleTwig.c

        display_name   = 'xyz-frill'
        frill_estimate = 3

        __init__       = construct__abc
        __repr__       = portray__abc
        count_newlines = count_newlines__abc
        display_token  = display_token__abc


    conjure_commented_xy_frill = produce_conjure_triple(
                                     'commented-xy-frill',
                                     Commented_XY_Frill,
                                     triple_frill_cache,
                                     lookup_triple_frill,
                                     store_triple_frill,
                                 )

    conjure_xyz_frill = produce_conjure_triple(
                            'xyz-frill',
                            XYZ_Frill,
                            triple_frill_cache,
                            lookup_triple_frill,
                            store_triple_frill,
                        )


    append_cache('triple-frill', triple_frill_cache)


    share(
        'conjure_commented_xy_frill',   conjure_commented_xy_frill,
        'conjure_xyz_frill',            conjure_xyz_frill,
    )
