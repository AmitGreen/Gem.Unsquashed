#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Topaz.CacheSupport')
    require_gem('Topaz.Core')
    require_gem('Topaz.GeneratedConjureDual')
    require_gem('Topaz.GeneratedNew')


    show = 0


    #
    #   Specific instances
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

    circle    = conjure_shape('circle')
    ellipse   = conjure_shape('ellipse')
    moon      = conjure_shape('moon')
    pentagon  = conjure_shape('pentagon')
    oval      = conjure_shape('oval')
    square    = conjure_shape('square')
    polygon   = conjure_shape('polygon')
    star      = conjure_shape('star')
    trapazoid = conjure_shape('trapazoid')
    triangle  = conjure_shape('triangle')


    #
    #   dual_test_list
    #
    dual_test_list = ((
            ((   one,   circle       )),
            ((   three, circle       )),
            ((   two,   circle       )),

            ((   two,   ellipse      )),
            ((   one,   ellipse      )),
            ((   seven, ellipse      )),
            ((   six,   ellipse      )),
            ((   three, ellipse      )),
            ((   five,  ellipse      )),
            ((   four,  ellipse      )),

            ((   two,   moon         )),
            ((   five,  moon         )),
            ((   three, moon         )),
            ((   four,  moon         )),
            ((   one,   moon         )),

            ((   five,  pentagon     )),
            ((   four,  pentagon     )),
            ((   one,   pentagon     )),
            ((   six,   pentagon     )),
            ((   three, pentagon     )),
            ((   two,   pentagon     )),

            ((   one,  square        )),
            ((   two,  square        )),

            ((   four,  star         )),
            ((   three, star         )),
            ((   two,   star         )),
            ((   one,   star         )),

            ((   five,  trapazoid    )),
            ((   four,  trapazoid    )),
            ((   six,   trapazoid    )),
            ((   three, trapazoid    )),
            ((   nine,  trapazoid    )),
            ((   eight, trapazoid    )),
            ((   two,   trapazoid    )),
            ((   one,   trapazoid    )),        #   Herd_Many.scrub
            ((   seven, trapazoid    )),

            ((   one, triangle       )),
        ))


    def test_final_scrub(cache):
        cache.scrub()

        assert cache.count_nested() is 0

        #my_line('scrubed cache %s', cache.name)


    def test_conjure_dual__X__scrub(cache, conjure_numbered_shape):
        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [7, 5, 3, 2, 1]:
            total = 0

            for [number, shape] in dual_test_list:
                v = conjure_numbered_shape(number, shape)
                total += 1

                if not (total % loop):
                    add(v)

            del v

            assert cache.count_nested() == length(dual_test_list)

            #if 7 is 7:
            #    my_line('BEFORE: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            cache.scrub()

            #if 7 is 7:
            #    my_line('AFTER: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            assert cache.count_nested() is length(keep_set)

            #if 7 is 7:
            #    my_line('keeping %d of %d', length(keep_set), length(dual_test_list))


    def test_conjure_dual__X__verify(cache, simplified_conjure_dual):
        cache_dump = dump_cache_to_string(cache)

        test_final_scrub(cache)

        for [number, shape] in dual_test_list:
            simplified_conjure_dual(number, shape)

        assert cache_dump == dump_cache_to_string(cache)

        if show is 7:
            partial(cache_dump)


    def test_conjure_unique_dual():
        cache = create_cache('numbered_shape', nub = Number.value.__get__)

        test_conjure_dual__X__scrub(
            cache,
            produce_conjure_unique_dual('numbered_shape', NumberedShape, cache),
        )

        #
        #   Verify the following produce the same cache structure:
        #
        #       1.  produce_conjure_unique_dual     (above)
        #       2.  produce_simplified_conjure_dual
        #       3.  produce_NEW_conjure_dual
        #
        test_conjure_dual__X__verify(
            cache,
            produce_simplified_conjure_dual('simplified_numbered_shape', NumberedShape, cache),
        )

        test_conjure_dual__X__verify(
            cache,
            produce_NEW_conjure_dual('NEW_numbered_shape', NumberedShape, cache),
        )

        test_final_scrub(cache)


    def test_conjure_unique_dual__21():
        cache = create_cache('shape_number', nub = Shape.name.__get__)

        test_conjure_dual__X__scrub(
            cache,
            produce_conjure_unique_dual__21('shape_number', NumberedShape, cache),
        )


        #
        #   Verify that the dual test list is ordered as expected
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

        del v, w, x


        #
        #   Verify the following produce the same cache structure:
        #
        #       1.  produce_conjure_unique_dual__21     (above)
        #       2.  produce_simplified_conjure_dual__21
        #       3.  produce_NEW_conjure_dual__21
        #
        test_conjure_dual__X__verify(
            cache,
            produce_simplified_conjure_dual__21('simplified_shape_number', NumberedShape, cache),
        )

        if produce_NEW_conjure_dual__21 is not 0:
            test_conjure_dual__X__verify(
                cache,
                produce_NEW_conjure_dual__21('NEW_numbered_shape', NumberedShape, cache),
            )

        test_final_scrub(cache)


    @share
    def test_conjure_dual():
        test_conjure_unique_dual()
        test_conjure_unique_dual__21()

        line('PASSED: conjure_dual')
