#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Core')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Gem.Global')
    require_gem('Gem.Map')
    require_gem('Gem.Method')
    require_gem('Gem.System')


    from Gem import create_cache, dump_caches, empty_herd, gem_global
    from Gem import produce_conjure_by_name__V2, produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import reference_count, values_tuple_sorted_by_key


    gem_global.testing = true


    share(
        #
        #   Imported functions
        #
        'create_cache',                         create_cache,
        'dump_caches',                          dump_caches,
        'produce_conjure_by_name__V2',          produce_conjure_by_name__V2,
        'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'reference_count',                      reference_count,
        'values_tuple_sorted_by_key',           values_tuple_sorted_by_key,


        #
        #   Imported Values
        #
        'empty_herd',   empty_herd,
    )
