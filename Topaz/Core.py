#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Core')
def gem():
    require_gem('Gem.Configuration')
    require_gem('Gem.Exception')
    require_gem('Gem.Map')


    from Gem import gem_configuration, iterate_items_sorted_by_key, values_tuple_sorted_by_key


    gem_configuration.testing = true


    share(
        #
        #   Imported functions
        #
        'iterate_items_sorted_by_key',  iterate_items_sorted_by_key,
        'values_tuple_sorted_by_key',   values_tuple_sorted_by_key,
    )
