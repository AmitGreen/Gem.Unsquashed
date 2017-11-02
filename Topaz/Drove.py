#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Drove')
def gem():
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')

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



    def test_drove_provision():
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

        expected_values = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))


        for total in iterate_range(0, 11):
            drove = empty_herd

            for i in iterate_range(0, total):
                v = expected_items[i]

                drove = drove.provision(v[0], v[1])

            assert drove.total                        == total
            assert Tuple(drove.items_sorted_by_key()) == expected_items[:total]
            assert Tuple(drove.ordered_values())      == expected_values[:total]


    @share
    def test_drove():
        test_drove_provision()

        line('PASSED: drove')
