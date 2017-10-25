#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Core')
def gem():
    require_gem('Gem.Global')
    require_gem('Gem.Map')
    require_gem('Gem.Method')
    require_gem('Gem.System')


    from Gem import gem_global, reference_count, values_tuple_sorted_by_key


    gem_global.testing = true


    share(
        #
        #   Imported functions
        #
        'reference_count',              reference_count,
        'values_tuple_sorted_by_key',   values_tuple_sorted_by_key,
    )
