#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Topaz.CacheSupport')
    require_gem('Topaz.Core')


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


    def test_conjure_dual__X(cache, conjure_numbered_shape, final_scrub = true):
        test_list = ((
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


        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [7, 5, 3, 2, 1]:
            total = 0

            for [number, shape] in test_list:
                v = conjure_numbered_shape(number, shape)
                total += 1

                if not (total % loop):
                    add(v)

            del v

            assert cache.count_nested() == length(test_list)

            #if 7 is 7:
            #    my_line('BEFORE: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    dump_caches(cache.name)

            cache.scrub()

            #if 7 is 7:
            #    my_line('AFTER: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    dump_caches(cache.name)

            assert cache.count_nested() is length(keep_set)

            #if 7 is 7:
            #    my_line('keeping %d of %d', length(keep_set), length(test_list))

        if final_scrub:
            del add, keep_set

            cache.scrub()

            assert cache.count_nested() is 0

            #if 7:
            #    my_line('CLEANUP COMPLETE')


    def test_conjure_unique_dual():
        numbered_shape_cache = create_cache('numbered_shape', nub = Number.value.__get__)

        conjure_numbered_shape = produce_conjure_unique_dual(
                                     'numbered_shape',
                                     NumberedShape,
                                     cache = numbered_shape_cache,
                                 )

        test_conjure_dual__X(numbered_shape_cache, conjure_numbered_shape)


    def test_conjure_unique_dual__21():
        shape_number_cache = create_cache('shape_number', nub = Shape.name.__get__)

        conjure_numbered_shape__21 = produce_conjure_unique_dual__21(
                                         'shape_number',
                                         NumberedShape,
                                         cache = shape_number_cache,
                                     )

        test_conjure_dual__X(shape_number_cache, conjure_numbered_shape__21, final_scrub = false)

        for v in [circle, ellipse, moon, pentagon, square, star, trapazoid, triangle]:
            w = shape_number_cache[v]

            if w.is_herd:
                value = 1

                for [number, x] in w.items_sorted_by_key():
                    assert number.value is value
                    assert x.number is number
                    assert x.shape  is v

                    value += 1
            else:
                assert w.number.value is 1


    @share
    def test_conjure_dual():
        test_conjure_unique_dual()
        test_conjure_unique_dual__21()

        line('PASSED: test_conjure_dual')

        #dump_caches('numbered_shape')
        #dump_caches('shape_number')
