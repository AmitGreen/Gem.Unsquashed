#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Core')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Gem.DumpCache')
    require_gem('Gem.Global')
    require_gem('Gem.Map')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.System')


    from Gem import create_cache, create_herd_2, create_horde_2, dump_cache_to_string, empty_herd, gem_global
    from Gem import print_cache, produce_conjure_by_name__V2
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import reference_count, values_tuple_sorted_by_key, write_binary_to_path


    gem_global.testing = true


    share(
        #
        #   Imported functions
        #
        'create_cache',                         create_cache,
        'create_herd_2',                        create_herd_2,
        'create_horde_2',                       create_horde_2,
        'dump_cache_to_string',                 dump_cache_to_string,
        'print_cache',                          print_cache,
        'produce_conjure_by_name__V2',          produce_conjure_by_name__V2,
        'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'reference_count',                      reference_count,
        'values_tuple_sorted_by_key',           values_tuple_sorted_by_key,
        'write_binary_to_path',                 write_binary_to_path,



        #
        #   Imported Values
        #
        'empty_herd',   empty_herd,
    )
