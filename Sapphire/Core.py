#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')


    from Gem import create_DelayedFileOutput, create_StringOutput, produce_cache_functions, read_text_from_path


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'produce_cache_functions',      produce_cache_functions,
        'read_text_from_path',          read_text_from_path,

        #
        #   Values
        #
        'tuple_of_2_nones',             ((none, none)),
        'tuple_of_3_nones',             ((none, none, none)),
    )
