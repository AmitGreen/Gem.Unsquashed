#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CreateMeta')
def gem():
    adjusted_meta_cache = {}

    lookup_adjusted_meta  = adjusted_meta_cache.get
    provide_adjusted_meta = adjusted_meta_cache.setdefault


    @share
    def create_Meta_WithNewlines(Meta, constructor):
        assert lookup_adjusted_meta(Meta) is none

        return provide_adjusted_meta(
                   Meta,
                   Type(
                       arrange('%s_WithNewlines', Meta.__name__),
                       ((Meta,)),
                       {
                           '__slots__' : ((
                               'newlines',                 #   Integer { > 0 }
                               'ends_in_newline',          #   Boolean
                           )),

                           '__init__' : constructor,
                       },
                    ),
                )


    @share
    def create_Meta_Many(Meta, constructor):
        assert Meta.__name__.endswith('_1')
        assert lookup_adjusted_meta(Meta) is none

        return provide_adjusted_meta(
                   Meta,
                   Type(
                       arrange('%s_Many', Meta.__name__[:-2]),
                       ((Meta,)),
                       {
                           '__slots__' : ((
                               'newlines',                 #   Integer { > 1 }
                           )),

                           '__init__' : constructor
                       },
                   ),
                )



    @share
    def dump_newline_meta_cache():
        for k in iterate_values_sorted_by_key({ k.__name__ : k   for k in adjusted_meta_cache }):
            line('%s:', k.__name__)
            line('    %s', adjusted_meta_cache[k].__name__)


    share(
        'lookup_adjusted_meta',     lookup_adjusted_meta,
    )
