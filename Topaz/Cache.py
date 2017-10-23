#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Topaz.Core')


    from Gem import create_cache, dump_caches, empty_herd, produce_conjure_by_name__V2
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21


    @share
    def test_cache():
        class Number(Object):
            __slots__ = ((
                'name',                     #   String+
                'value',                    #   String+
            ))


            is_herd = false


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


        class NumberedShape(Object):
            __slots__ = ((
                'number',                   #   Number
                'shape',                    #   Shape
            ))


            is_herd = false


            def __init__(t, number, shape):
                t.number = number
                t.shape  = shape


            def __repr__(t):
                return arrange('<numbered-shape %d %s>', t.number.value, t.shape.name)


            display_token = __repr__


        NumberedShape.k1 = NumberedShape.number
        NumberedShape.k2 = NumberedShape.shape


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

        eight = conjure_number('eight', 8)
        five  = conjure_number('five',  5)
        four  = conjure_number('four',  4)
        nine  = conjure_number('nine',  9)
        one   = conjure_number('one',   1)
        seven = conjure_number('seven', 7)
        six   = conjure_number('six',   6)
        three = conjure_number('three', 3)
        two   = conjure_number('two',   2)
        zero  = conjure_number('zero',  0)

        red   = conjure_color('red')
        green = conjure_color('green')
        blue  = conjure_color('blue')

        circle    = conjure_shape('circle')
        ellipse   = conjure_shape('ellipse')
        moon      = conjure_shape('moon')
        pentagon  = conjure_shape('pentagon')
        square    = conjure_shape('square')
        star      = conjure_shape('star')
        trapazoid = conjure_shape('trapazoid')
        triangle  = conjure_shape('triangle')


        def test_conjure_again():
            assert one   is conjure_number('one',  1)
            assert two   is conjure_number('two',  2)
            assert zero  is conjure_number('zero', 0)
            assert three is conjure_number('three', 3)
            assert four  is conjure_number('four',  4)
            assert five  is conjure_number('five',  5)
            assert six   is conjure_number('six',   6)
            assert seven is conjure_number('seven', 7)
            assert eight is conjure_number('eight', 8)
            assert nine  is conjure_number('nine',  9)

            assert red   is conjure_color('red')
            assert green is conjure_color('green')
            assert blue  is conjure_color('blue')

            assert circle    is conjure_shape('circle')
            assert ellipse   is conjure_shape('ellipse')
            assert moon      is conjure_shape('moon')
            assert pentagon  is conjure_shape('pentagon')
            assert square    is conjure_shape('square')
            assert star      is conjure_shape('star')
            assert trapazoid is conjure_shape('trapazoid')
            assert triangle  is conjure_shape('triangle')





        def test_conjure_dual__X(cache, conjure_numbered_shape):
            for loop in [1, 2]:
                for [number, shape] in [
                    [   one,   circle       ],
                    [   three, circle       ],
                    [   two,   circle       ],

                    [   two,   ellipse      ],
                    [   one,   ellipse      ],
                    [   seven, ellipse      ],
                    [   six,   ellipse      ],
                    [   three, ellipse      ],
                    [   five,  ellipse      ],
                    [   four,  ellipse      ],

                    [   two,   moon         ],
                    [   five,  moon         ],
                    [   three, moon         ],
                    [   four,  moon         ],
                    [   one,   moon         ],

                    [   five,  pentagon     ],
                    [   four,  pentagon     ],
                    [   one,   pentagon     ],
                    [   six,   pentagon     ],
                    [   three, pentagon     ],
                    [   two,   pentagon     ],

                    [   one,  square        ],
                    [   two,  square        ],

                    [   four,  star         ],
                    [   three, star         ],
                    [   two,   star         ],
                    [   one,   star         ],

                    [   five,  trapazoid    ],
                    [   four,  trapazoid    ],
                    [   six,   trapazoid    ],
                    [   three, trapazoid    ],
                    [   nine,  trapazoid    ],
                    [   eight, trapazoid    ],
                    [   two,   trapazoid    ],
                    [   one,   trapazoid    ],
                    [   seven, trapazoid    ],

                    [   one, triangle       ],
                ]:
                    conjure_numbered_shape(number, shape)


            if cache is not 0:
                #
                #   If the cache is 'shape_number' then we can verify the second key is ordered numbers.
                #
                for v in [circle, ellipse, moon, pentagon, square, star, trapazoid, triangle]:
                    w = cache[v]

                    if w.is_herd:
                        value = 1

                        for [number, x] in w.items_sorted_by_key():
                            assert number.value is value
                            assert x.number is number
                            assert x.shape  is v

                            value += 1
                    else:
                        assert w.number.value is 1


            expected_items = ((
                                 ((zero,  zero .value)),
                                 ((one,   one  .value)),
                                 ((two,   two  .value)),
                                 ((three, three.value)),
                                 ((four,  four .value)),
                                 ((five,  five .value)),
                                 ((six,   six  .value)),
                                 ((seven, seven.value)),
                                 ((eight, eight.value)),
                                 ((nine,  nine .value)),
                             ))


            #
            #   Verify sort of 0 element herd's
            #
            def test_herd_0__sort():
                assert empty_herd.items_sorted_by_key() is (())


            #
            #   Verify sort of 1 element herd's
            #
            def test_herd_1__sort():
                herd = empty_herd.provision(zero, zero.value)

                assert herd.items_sorted_by_key() == expected_items[:1]


            #
            #   Verify sort of 2 & 3 element herd's
            #
            def test_herd_23__sort():
                for [a, b] in [
                        [zero, one],
                        [one, zero],
                ]:
                    herd = empty_herd
                    herd = herd.provision(a, a.value)
                    herd = herd.provision(b, b.value)

                    herd__2 = herd

                    for loop in [1, 2]:
                        herd__2 = herd__2.provision(a, a.value)
                        herd__2 = herd__2.provision(b, b.value)

                    assert herd is herd__2
                    assert herd.items_sorted_by_key() == expected_items[:2]


                for [a, b, c] in [
                        [zero, one,  two ],
                        [zero, two,  one ],
                        [one,  zero, two ],
                        [one,  two,  zero],
                        [two,  zero, one ],
                        [two,  one,  zero],
                ]:
                    herd = empty_herd
                    herd = herd.provision(a, a.value)
                    herd = herd.provision(b, b.value)
                    herd = herd.provision(c, c.value)

                    herd__2 = herd

                    for loop in [1, 2]:
                        herd__2 = herd__2.provision(a, a.value)
                        herd__2 = herd__2.provision(b, b.value)
                        herd__2 = herd__2.provision(c, c.value)

                    assert herd is herd__2
                    assert herd.items_sorted_by_key() == expected_items[:3]


            def test_herd_4567__sort():
                for add in [
                    [   zero,   one,    two,    three                                   ],
                    [   one,    three,  two,    zero                                    ],
                    [   four,   zero,   one,    three,  two                             ],
                    [   three,  zero,   two,    one,    four                            ],
                    [   one,    three,  four,   zero,   five,   two,                    ],
                    [   zero,   six,    four,   five,   two,    one,    three           ],
                ]:
                    herd = empty_herd

                    for loop in [1, 2]:
                        for v in add:
                            herd = herd.provision(v, v.value)

                    assert Tuple(herd.items_sorted_by_key()) == expected_items[:length(add)]


            def test_herd_many__sort():
                for add in [
                    [   five,   three,  two,    seven,  one,    zero,   six,    four                    ],
                    [   seven,  six,    three,  five,   zero,   one,    two,    eight,  four            ],
                    [   one,    two,    zero,   nine,   five,   eight,  four,   six,    three,  seven   ],
                ]:
                    herd = empty_herd

                    for loop in [1, 2]:
                        for v in add:
                            herd = herd.provision(v, v.value)

                    assert Tuple(herd.items_sorted_by_key()) == expected_items[:length(add)]

            test_herd_0__sort()
            test_herd_1__sort()
            test_herd_23__sort()
            test_herd_4567__sort()
            test_herd_many__sort()


        def test_conjure_unique_dual():
            conjure_numbered_shape = produce_conjure_unique_dual(
                                         'numbered_shape',
                                         NumberedShape,
                                         nub = Number.value.__get__,
                                     )

            test_conjure_dual__X(0, conjure_numbered_shape)


        def test_conjure_unique_dual__21():
            numbered_shape_cache__21 = create_cache('shape_number', nub = Shape.name.__get__)

            conjure_numbered_shape__21 = produce_conjure_unique_dual__21(
                                             'shape_number',
                                             NumberedShape,
                                             cache = numbered_shape_cache__21,
                                         )

            test_conjure_dual__X(numbered_shape_cache__21, conjure_numbered_shape__21)


        test_conjure_again()
        test_conjure_unique_dual__21()
        test_conjure_unique_dual()


        line('PASSED: test_cache')

        #dump_caches('numbered_shape')
        #dump_caches('shape_number')
