#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


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

    red    = conjure_color('red')
    white  = conjure_color('white')
    purple = conjure_color('purple')
    green  = conjure_color('green')
    silver = conjure_color('silver')
    black  = conjure_color('black')
    blue   = conjure_color('blue')
    yellow = conjure_color('yellow')
    cyan   = conjure_color('cyan')

    small  = conjure_size('small')
    tiny   = conjure_size('tiny')
    large  = conjure_size('large')
    medium = conjure_size('medium')

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


    triple_test_list = ((
            ((  one,    red,    small,  circle,     0   )),
            ((  one,    red,    small,  star,       7   )),
            ((  one,    red,    small,  moon,       7   )),     #   Test Horde_23.scrub resampling

            ((  two,    blue,   large,  trapazoid,  0   )),
            ((  two,    blue,   large,  pentagon,   7   )),
            ((  two,    blue,   large,  square,     7   )),
            ((  two,    blue,   large,  triangle,   7   )),
            ((  two,    blue,   large,  oval,       7   )),     #   Test Horde_Many.scrub resampling

            ((  three,  green,  small,  moon,       7   )), 
            ((  three,  green,  medium, moon,       0   )), 
            ((  three,  green,  small,  star,       7   )), 
            ((  three,  green,  small,  trapazoid,  7   )), 

            ((  four,   blue,   large,  moon,       7   )), 
            ((  four,   blue,   large,  star,       7   )), 
            ((  four,   white,  small,  square,     0   )), 
            ((  four,   yellow, small,  square,     0   )), 
            ((  four,   blue,   medium, moon,       0   )), 

            ((  five,   black,  medium, square,     7   )),
            ((  five,   white,  small,  star,       7   )),
            ((  five,   white,  large,  moon,       0   )),
            ((  five,   white,  large,  pentagon,   7   )),
            ((  five,   white,  tiny,   star,       0   )),
            ((  five,   white,  large,  star,       0   )),
            ((  five,   black,  medium, star,       7   )),
            ((  five,   black,  medium, moon,       7   )),
            ((  five,   black,  medium, triangle,   7   )),

            ((  six,    yellow, tiny,   moon,       0   )),
            ((  six,    yellow, large,  moon,       7   )),
            ((  six,    yellow, medium, star,       7   )),
            ((  six,    yellow, small,  pentagon,   7   )),

            ((  seven,  white,  tiny,   square,     7   )),
            ((  seven,  white,  tiny,   moon,       7   )),
            ((  seven,  white,  large,  pentagon,   7   )),
        ))


    def test_final_scrub(cache):
        cache.scrub()

        assert cache.count_nested() is 0

        #my_line('scrubed cache %s', cache.name)


    def test_conjure_quadruple__X__scrub(cache, conjure_numbered_color_size_shape):
        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [0, 7, 5, 3, 2, 1]:
            total = 0

            for [number, color, size, shape, keep] in triple_test_list:
                v = conjure_numbered_color_size_shape(number, color, size, shape)
                total += 1

                if loop is 0:
                    if keep:
                        add(v)
                    #else:
                    #    if v not in keep_set:
                    #        my_line('will discard: %r', v)
                else:
                    if not (total % loop):
                        add(v)
                    #else:
                    #    if v not in keep_set:
                    #        my_line('will discard: %r', v)
            del v

            assert cache.count_nested() == length(triple_test_list)

            #if 7 is 7:
            #    my_line('BEFORE: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            cache.scrub()

            #if 7 is 7:
            #    my_line('AFTER: (loop %d)', loop)
            #    #for v in keep_set:
            #    #    my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            assert cache.count_nested() == length(keep_set)

            #if 7 is 7:
            #    my_line('keeping %d of %d', length(keep_set), length(triple_test_list))
            #    line()


    def test_conjure_unique_quadruple():
        cache = create_cache('numbered_colored_size_shape', nub = Number.value.__get__)

        conjure_numbered_colored_size_shape = produce_conjure_unique_quadruple(
                                                  'numbered_colored_size_shape',
                                                  NumberedColoredSizeShape,
                                                  cache,
                                              )

        test_conjure_quadruple__X__scrub(cache, conjure_numbered_colored_size_shape)
        test_final_scrub(cache)


    @share
    def test_conjure_quadruple():
        test_conjure_unique_quadruple()

        line('PASSED: conjure_quadruple')

        #print_cache('numbered_colored_shape')
        #print_cache('shape_number_color__312')
