#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('Gem.Exception')
    require_gem('Gem.Sleep')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')


    from Gem import change_check_interval, fetch_check_interval
    from Gem import print_exception_chain, produce_conjure_dual, produce_conjure_triple, produce_conjure_triple__312
    from Gem import sleep


    share(
        'change_check_interval',            change_check_interval,
        'fetch_check_interval',             fetch_check_interval,
        'print_exception_chain',            print_exception_chain,
        'produce_conjure_dual',             produce_conjure_dual,
        'produce_conjure_triple',           produce_conjure_triple,
        'produce_conjure_triple__312',      produce_conjure_triple__312,
        'sleep',                            sleep,
    )
