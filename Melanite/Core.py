#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Melanite.Core')
def gem():
    require_gem('Gem.Exception')
    require_gem('Gem.Traceback')
    require_gem('Gem.System')


    from Gem import print_exception_chain, program_exit


    share(
        'print_exception_chain',    print_exception_chain,
        'program_exit',             program_exit,
    )
