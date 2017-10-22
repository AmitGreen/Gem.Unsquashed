#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Topaz.Core')


    from Gem import produce_conjure_by_name__V2, produce_conjure_unique_dual, dump_caches


    @share
    def test_cache():
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


            def less_than(t, that):
                return t.name < that.name


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


        conjure_color         = produce_conjure_by_name__V2('color', Color)
        conjure_shape         = produce_conjure_by_name__V2('shape', Shape)

        conjure_colored_shape = produce_conjure_unique_dual(
                                    'colored_shape',
                                    ColoredShape,
                                    fetch_key_1 = Color.name.__get__,
                                )


        red   = conjure_color('red')
        green = conjure_color('green')
        blue  = conjure_color('blue')

        circle   = conjure_shape('circle')
        square   = conjure_shape('square')
        triangle = conjure_shape('triangle')

        blue_circle  = conjure_colored_shape(blue,  circle)
        green_circle = conjure_colored_shape(green, circle)
        green_square = conjure_colored_shape(green, square)
        red_circle   = conjure_colored_shape(red,   circle)

        assert red is conjure_color('red')

        assert blue_circle  is conjure_colored_shape(blue,  circle)
        assert red_circle   is conjure_colored_shape(red,   circle)
        assert green_circle is conjure_colored_shape(green, circle)

        line('PASSED: test_cache')

        dump_caches('colored_shape')
