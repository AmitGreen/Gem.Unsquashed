#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Herd')
def gem():
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


    #
    #   SimpleNumber
    #
    class SimpleNumber(Object):
        __slots__ = ((
            'value',                    #   String+
        ))


        is_herd = false


        def __init__(t, value):
            t.value = value


        def __repr__(t):
            return arrange('<Simple-number %d>', t.value)


        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    simple_nub = SimpleNumber.value.__get__


    #
    #   Number: Specific instances
    #
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


    def test_herd_scrub():
        for total in iterate_range(2, 10):
            for mask in iterate_range(0, 2 ** total): #<< (total - 1)):
                herd   = empty_herd
                many   = []
                append = many.append

                for i in iterate_range(total):
                    v    = SimpleNumber(i)
                    herd = herd.provision(i, v)

                    append(v)

                v = 0

                bits = 1

                for i in iterate_range(total):
                    if mask & bits:
                        many[i] = 0

                    bits = bits * 2 #bits <<= 1

                herd = herd.scrub()

                many = Tuple(v   for v in many   if v is not 0)

                if length(many) is 0:
                    assert herd is 0
                elif length(many) is 1:
                    assert herd is many[0]
                else:
                    if total >= 8:
                        assert Tuple(sorted_list(herd.values(), key = simple_nub)) == many
                    else:
                        assert herd.values() == many


    def test_herd_sorting():
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


    @share
    def test_herd():
        test_herd_scrub()
        test_herd_sorting()

        line('PASSED: herd')
