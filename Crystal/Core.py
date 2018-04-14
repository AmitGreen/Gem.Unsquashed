#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Crystal.Core')
def gem():
    require_gem('Gem.Global')


    from Gem import gem_global


    gem_global.testing = true
