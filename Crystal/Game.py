#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.Core')
    require_gem('Crystal.Player')


    @share
    def command_game():
        line('Alice:  %s', alice)
        line('Bob:    %s', bob)
