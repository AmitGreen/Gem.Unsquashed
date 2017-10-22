#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Series')
def gem():
    require_gem('Gem.GarbageCollection')
    require_gem('Gem.Series')
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


    from Gem import create_series_0, create_series_1, create_series_2, create_series_3, create_series_4
    from Gem import create_series_0, create_series_1, create_series_2, create_series_3, create_series_4
    from Gem import dump_series_statistics, collect_garbage


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


    def test_series_create():
        for loop in [1, 2, 3, 4]:
            s0 = create_series_0()
            s1 = create_series_1(one)
            s2 = create_series_2(one, two)
            s3 = create_series_3(one, two, three)

            assert s0.finish() is (())
            assert s1.finish() == ((one,))
            assert s2.finish() == ((one, two))
            assert s3.finish() == ((one, two, three))

            del s0, s1, s2, s3
            collect_garbage()


    @share
    def test_series():
        test_series_create()

        line('PASSED: series')

        dump_series_statistics()
