#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Topaz.Core')


    from Gem import create_cache, empty_horde, produce_conjure_by_name__V2, produce_conjure_unique_dual, dump_caches


    @share
    def test_cache():
        class Number(Object):
            __slots__ = ((
                'name',                     #   String+
                'value',                    #   String+
            ))


            is_horde = false


            def __init__(t, name, value):
                t.name  = name
                t.value = value


            def display_token(t):
                return arrange('<number %r %d>', t.name, t.value)


        Number.nub = Number.value.__get__


        class Color(Object):
            __slots__ = ((
                'name',                     #   String+
            ))


            def __init__(t, name):
                t.name = name


            def display_token(t):
                return arrange('<color %s>', t.name)


        class Shape(Object):
            __slots__ = ((
                'name',                     #   String+
            ))


            def __init__(t, name):
                t.name = name


            def display_token(t):
                return arrange('<shape %s>', t.name)


        Shape.nub = Shape.name.__get__


        class ColoredShape(Object):
            __slots__ = ((
                'color',                    #   Color
                'shape',                    #   Shape
            ))


            is_horde = false


            def __init__(t, color, shape):
                t.color = color
                t.shape = shape


            def display_token(t):
                return arrange('<colored-shape %s %s>', t.color.name, t.shape.name)


       #ColoredShape.k1 = ColoredShape.color
        ColoredShape.k2 = ColoredShape.shape


        #
        #   Conjure functions
        #
        number_cache   = create_cache('number')
        lookup_number  = number_cache.lookup
        provide_number = number_cache.provide


        def conjure_number(name, value):
            r = lookup_number(value)

            if r is not none:
                assert r.name == name

                return r

            r = Number(intern_string(name), intern_integer(value))

            return provide_number(r.value, r)


        conjure_color = produce_conjure_by_name__V2('color', Color)
        conjure_shape = produce_conjure_by_name__V2('shape', Shape)

        conjure_colored_shape = produce_conjure_unique_dual(
                                    'colored_shape',
                                    ColoredShape,
                                    nub = Color.name.__get__,
                                )


        five  = conjure_number('five',  5)
        four  = conjure_number('four',  4)
        one   = conjure_number('one',   1)
        seven = conjure_number('seven', 7)
        six   = conjure_number('six',   6)
        three = conjure_number('three', 3)
        two   = conjure_number('two',   2)
        zero  = conjure_number('zero',  0)

        red   = conjure_color('red')
        green = conjure_color('green')
        blue  = conjure_color('blue')

        circle   = conjure_shape('circle')
        square   = conjure_shape('square')
        triangle = conjure_shape('triangle')

        blue_circle  = conjure_colored_shape(blue,  circle)
        green_circle = conjure_colored_shape(green, circle)
        green_square = conjure_colored_shape(green, square)
        red_triangle = conjure_colored_shape(red,   triangle)
        red_square   = conjure_colored_shape(red,   square)
        red_circle   = conjure_colored_shape(red,   circle)


        def test_conjure_again():
            assert one  is conjure_number('one',  1)
            assert two  is conjure_number('two',  2)
            assert zero is conjure_number('zero', 0)

            assert red is conjure_color('red')

            assert blue_circle  is conjure_colored_shape(blue,  circle)
            assert red_circle   is conjure_colored_shape(red,   circle)
            assert green_circle is conjure_colored_shape(green, circle)


        #
        #   Verify sort of 0 element horde's
        #
        def test_horde_0__sort():
            assert empty_horde.items_sorted_by_key() is (())


        #
        #   Verify sort of 1 element horde's
        #
        def test_horde_1__sort():
            horde = empty_horde.provision(zero, zero.value)

            assert horde.items_sorted_by_key() == (( ((zero, zero.value)), ))


        #
        #   Verify sort of 2 & 3 element horde's
        #
        def test_horde_23__sort():
            expected_order = (( ((zero, 0)), ((one, 1)) ))

            for [a, b] in [
                    [zero, one],
                    [one, zero],
            ]:
                horde = empty_horde
                horde = horde.provision(a, a.value)
                horde = horde.provision(b, b.value)

                horde__2 = horde

                for loop in [1, 2]:
                    horde__2 = horde__2.provision(a, a.value)
                    horde__2 = horde__2.provision(b, b.value)

                assert horde is horde__2
                assert Tuple(horde.items_sorted_by_key()) == expected_order

            expected_order = (( ((zero, 0)), ((one, 1)), ((two, 2)) ))

            for [a, b, c] in [
                    [zero, one,  two ],
                    [zero, two,  one ],
                    [one,  zero, two ],
                    [one,  two,  zero],
                    [two,  zero, one ],
                    [two,  one,  zero],
            ]:
                horde = empty_horde
                horde = horde.provision(a, a.value)
                horde = horde.provision(b, b.value)

                horde__2 = horde

                for loop in [1, 2]:
                    horde__2 = horde__2.provision(a, a.value)
                    horde__2 = horde__2.provision(b, b.value)
                    horde__2 = horde__2.provision(c, c.value)

                assert horde is horde__2
                assert horde.items_sorted_by_key() == expected_order


        def test_horde_4567__sort():
            expected = [
                           ((zero,  zero .value)),
                           ((one,   one  .value)),
                           ((two,   two  .value)),
                           ((three, three.value)),
                           ((four,  four .value)),
                           ((five,  five .value)),
                           ((six,   six  .value)),
                           ((seven, seven.value)),
                       ]

            for add in [
                [   zero,   one,    two,    three                                   ],
                [   one,    three,  two,    zero                                    ],
                [   four,   zero,   one,    three,  two                             ],
                [   three,  zero,   two,    one,    four                            ],
                [   one,    three,  four,   zero,   five,   two,                    ],
                [   zero,   six,    four,   five,   two,    one,    three           ],
#               [   five,   three,  two,    seven,  one,    zero,   six,    four    ],
            ]:
                horde = empty_horde

                for v in add:
                    horde = horde.provision(v, v.value)

                assert horde.items_sorted_by_key() == expected[:length(add)]


        test_conjure_again()
        test_horde_0__sort()
        test_horde_1__sort()
        test_horde_23__sort()
        test_horde_4567__sort()

        line('PASSED: test_cache')

        dump_caches('number')
        dump_caches('colored_shape')
