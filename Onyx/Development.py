#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Onyx.Development')
def gem():
    require_gem('Onyx.Core')


    @share
    def command_development():
        line('onyx development')
