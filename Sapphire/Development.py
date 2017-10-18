#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    @share
    def development():
        raise_runtime_error('development: incomplete')
