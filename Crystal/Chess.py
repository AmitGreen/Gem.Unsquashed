#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Chess')
def gem():
    #require_gem('Crystal.Core')


    class Chess_King(Object):
        __slots__ = ((
            'current_health',           #   Integer
            'maximum_health',           #   Integer
            '_mirror',                  #   Zero|Chess_King+
        ))


        def __init__(t, current_health, maximum_health):
            t.current_health = current_health
            t.maximum_health = maximum_health
            t._mirror        = 0

        
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



    class Ally_Chess_King(Chess_King):
        abbreviation   = 'WK'
        ally           = true
        attack         = 1
        card_name      = 'Ally-Chess-King'
        empty_square   = false
        enemy          = false
        initial_health = 20


        def action(t, board, square):
            assert square is square_a1

            board.a2 = board.a2.attacked(t.attack)


    class Enemy_Chess_King(Chess_King):
        abbreviation   = 'BK'
        ally           = false
        attack         = 1
        card_name      = 'Enemy-Chess-King'
        empty_square   = false
        enemy          = true
        initial_health = 20


        def attacked(t, attack):
            health = t.current_health - attack

            if health < 0:
                health = 0

            return conjure_enemy_chess_king(health, t.maximum_health)



    Ally_Chess_King.k1 = Ally_Chess_King.current_health
    Ally_Chess_King.k2 = Ally_Chess_King.maximum_health


    Enemy_Chess_King.k1 = Enemy_Chess_King.current_health
    Enemy_Chess_King.k2 = Enemy_Chess_King.maximum_health


    conjure_ally_chess_king  = produce_conjure_dual('ally_chess_king', Ally_Chess_King)
    conjure_enemy_chess_king = produce_conjure_dual('enemy_chess_king', Enemy_Chess_King)


    initial_ally_chess_king  = conjure_ally_chess_king(
            Ally_Chess_King .initial_health,
            Ally_Chess_King .initial_health,
        )

    initial_enemy_chess_king = conjure_enemy_chess_king(
            Enemy_Chess_King.initial_health,
            Enemy_Chess_King.initial_health,
        )


    def produce_mirror_method(Meta, conjure_mirror):
        @property
        def mirror(t):
            if t._mirror is not 0:
                return t._mirror

            r = \
                t._mirror = conjure_mirror(t.current_health, t.maximum_health)

            r._mirror = t

            return r


        Meta.mirror = mirror


    produce_mirror_method(Ally_Chess_King,  conjure_enemy_chess_king)
    produce_mirror_method(Enemy_Chess_King, conjure_ally_chess_king)


    share(
        'initial_ally_chess_king',      initial_ally_chess_king,
        'initial_enemy_chess_king',     initial_enemy_chess_king,
    )
