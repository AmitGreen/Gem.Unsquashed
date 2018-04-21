
#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessKing')
def gem():
    require_gem('Crystal.ChessKing')


    class FrozenChessKing(Object):
        __slots__ = ((
            'current_health',           #   Integer
            'maximum_health',           #   Integer
        ))


        def __init__(t, current_health, maximum_health):
            t.current_health = current_health
            t.maximum_health = maximum_health


        def __repr__(t):
            if t.initial_health == t.maximum_health:
                return arrange('<%s %d>', t.card_name, t.current_health)

            return arrange('<%s %d; maximum %d>', t.card_name, t.current_health, t.maximum_health)


        def portray_abbreviation(t):
            return t.abbreviation


        def portray_numbers(t):
            if t.maximum_health == t.initial_health:
                return arrange('%d/%d', t.attack, t.current_health)

            return arrange('%d/%d(%d)', t.attack, t.current_health, t.maximum_health)



    class FrozenAllyChessKing(FrozenChessKing):
        abbreviation    = 'ZWK'
        ally            = true
        attack          = 1
        card_name       = 'Frozen-Ally-Chess-King'
        enemy           = false
        initial_health  = 20
        is_blank_square = false
        is_card         = true


    class FrozenEnemyChessKing(FrozenChessKing):
        abbreviation    = 'ZBK'
        ally            = false
        attack          = 1
        card_name       = 'Frozen-Enemy-Chess-King'
        enemy           = true
        initial_health  = 20
        is_blank_square = false
        is_card         = true



    FrozenAllyChessKing.k1 = FrozenAllyChessKing.current_health
    FrozenAllyChessKing.k2 = FrozenAllyChessKing.maximum_health


    FrozenEnemyChessKing.k1 = FrozenEnemyChessKing.current_health
    FrozenEnemyChessKing.k2 = FrozenEnemyChessKing.maximum_health


    conjure_frozen_ally_chess_king  = produce_conjure_dual('frozen_ally_chess_king', FrozenAllyChessKing)
    conjure_frozen_enemy_chess_king = produce_conjure_dual('frozen_enemy_chess_king', FrozenEnemyChessKing)


    share(
        'conjure_frozen_ally_chess_king',   conjure_frozen_ally_chess_king,
        'conjure_frozen_enemy_chess_king',  conjure_frozen_enemy_chess_king,
    )
