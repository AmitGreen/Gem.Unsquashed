#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.BlankSquare')
    require_gem('Crystal.Board')
    require_gem('Crystal.ChessBishop')
    require_gem('Crystal.ChessKing')
    require_gem('Crystal.ChessKnight')
    require_gem('Crystal.ChessPawn')
    require_gem('Crystal.Core')
    require_gem('Crystal.FrozenChessKing')
    require_gem('Crystal.Player')
    require_gem('Crystal.Square')
    require_gem('Crystal.VoidSquare')


    def action_and_dump(board):
        board.actions()
        line('---')
        board.dump_abbreviation()


    def bishop_pawn(board):
        board.add_special_x1(create_ally_chess_bishop)
        board.add_normal_x1 (create_ally_chess_pawn)
        action_and_dump(board)


    def knight_pawn(board):
        board.add_special_x1(create_ally_chess_knight)
        board.add_normal_x1 (create_ally_chess_pawn)
        action_and_dump(board)


    def pawn_pawn(board):
        board.add_special_x1(create_ally_chess_pawn)
        board.add_normal_x1 (create_ally_chess_pawn)
        action_and_dump(board)


    def command_test():
        pass


    def command_dump():
        pass
        #line('store_v0:  %s', store_v0)


    @share
    def command_game():
        command_test()
        command_dump()

        board = GameBoard(1, alice, create_enemy_chess_king(), create_ally_chess_king())

        board.dump_abbreviation()
        pawn_pawn(board)            #   Turn 1, Alice:  Pawn, Pawn
        bishop_pawn(board)          #   Turn 1, Bob:    Bishop, Pawn

        bishop_pawn(board)          #   Turn 2, Alice:  Bishop, Pawn
        knight_pawn(board)          #   Turn 2, Bob:    Knight, Pawn
