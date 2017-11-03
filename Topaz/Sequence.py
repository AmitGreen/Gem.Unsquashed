#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Sequence')
def gem():
    require_gem('Gem.Sequence')
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


    from Gem import create_sequence_1, create_sequence_2, create_sequence_3, create_sequence_4, create_sequence_many
    from Gem import sequence_0


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


    def test_sequence_create():
        portray_s0 = "{,}"
        portray_s1 = "{" + portray(one) + "}"
        portray_s2 = "{" + portray_s1[1:-1] + ", " + portray(two  ) + "}"
        portray_s3 = "{" + portray_s2[1:-1] + ", " + portray(three) + "}"
        portray_s4 = "{" + portray_s3[1:-1] + ", " + portray(four ) + "}"
        portray_s5 = "{" + portray_s4[1:-1] + ", " + portray(five ) + "}"

        for loop in [1, 2]:
            s0 = sequence_0
            s1 = create_sequence_1(one)
            s2 = create_sequence_2(one, two)
            s3 = create_sequence_3(one, two, three)
            s4 = create_sequence_4(one, two, three, four)
            s5 = create_sequence_many( ((one, two, three, four, five)) )

            assert Tuple(s0) == (())
            assert Tuple(s1) == ((one,))
            assert Tuple(s2) == ((one, two))
            assert Tuple(s3) == ((one, two, three))
            assert Tuple(s4) == ((one, two, three, four))
            assert Tuple(s5) == ((one, two, three, four, five))

            assert portray(s0) == portray_s0
            assert portray(s1) == portray_s1
            assert portray(s2) == portray_s2
            assert portray(s3) == portray_s3
            assert portray(s4) == portray_s4
            assert portray(s5) == portray_s5


    @share
    def test_sequence():
        test_sequence_create()

        line('PASSED: sequence')
