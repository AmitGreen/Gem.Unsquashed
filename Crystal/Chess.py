#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Player')
def gem():
    #require_gem('Crystal.Core')


    class Chess_King(Object):
        attack         = 1
        initial_health = 20


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



    class Ally_Chess_King(Chess_King):
        ally      = true
        card_name = 'Ally_Chess_King'
        enemy     = false


        @property
        def mirror(t):
            if t._mirror is not 0:
                return t._mirror

            r = \
                t._mirror = conjure_enemy_chess_king(t.current_health, t.maximum_health)

            r._mirror = t

            return r


    class Enemy_Chess_King(Chess_King):
        ally      = true
        card_name = 'Enemy_Chess_King'
        enemy     = false


        @property
        def mirror(t):
            if t._mirror is not 0:
                return t._mirror

            r = \
                t._mirror = conjure_ally_chess_king(t.current_health, t.maximum_health)

            r._mirror = t

            return r


    Ally_Chess_King.k1 = Ally_Chess_King.current_health
    Ally_Chess_King.k2 = Ally_Chess_King.maximum_health


    Enemy_Chess_King.k1 = Enemy_Chess_King.current_health
    Enemy_Chess_King.k2 = Enemy_Chess_King.maximum_health


    conjure_ally_chess_king  = produce_conjure_dual('ally_chess_king', Ally_Chess_King)
    conjure_enemy_chess_king = produce_conjure_dual('enemy_chess_king', Enemy_Chess_King)


    initial_ally_chess_king  = conjure_ally_chess_king (Chess_King.initial_health, Chess_King.initial_health)
    initial_enemy_chess_king = conjure_enemy_chess_king(Chess_King.initial_health, Chess_King.initial_health)


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
