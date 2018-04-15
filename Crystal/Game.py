#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.Core')
    require_gem('Crystal.Board')
    require_gem('Crystal.ChessKing')
    require_gem('Crystal.Player')
    require_gem('Crystal.Square')


    def command_test():
        pass


    def command_dump():
        line('empty_square:  %s', empty_square)


    @share
    def command_game():
        command_test()
        command_dump()

        board = GameBoard(1, alice, create_enemy_chess_king(), create_ally_chess_king())

        board.dump_abbreviation()

        board.actions()
        line('---')
        board.dump_abbreviation()
