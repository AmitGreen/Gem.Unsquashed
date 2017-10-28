#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Topaz.Core')


    show_address_and_references = 0


    #
    #   Color
    #
    class Color(Object):
        __slots__ = ((
            'name',                     #   String+
        ))


        is_herd = false


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<color %s>', t.name)


        display_token = __repr__


    Color.nub = Color.name.__get__


    #
    #   Number
    #
    @share
    class Number(Object):
        __slots__ = ((
            'name',                     #   String+
            'value',                    #   String+
        ))


        is_herd = false


        def __init__(t, name, value):
            t.name  = name
            t.value = value


        def __repr__(t):
            return arrange('<number %r %d>', t.name, t.value)


        display_token = __repr__
        increment_skip = 0
        scrub          = 0


    Number.nub = Number.value.__get__


    #
    #   NumberedColoredShape
    #
    @share
    class NumberedColoredShape(Object):
        __slots__ = ((
            'number',                   #   Number
            'color',                    #   Color
            'shape',                    #   Shape
        ))


        is_herd = false


        def __init__(t, number, color, shape):
            t.number = number
            t.color  = color
            t.shape  = shape


        def __repr__(t):
            if show_address_and_references is 7:
                count = reference_count(t)
                return arrange('<numbered-colored-shape@%x#%d %d %s %s>',
                           address_of(t), count, t.number.value, t.color.name, t.shape.name)

            return arrange('<numbered-colored-shape %d %s %s>',
                           t.number.value, t.color.name, t.shape.name)



        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    NumberedColoredShape.k1 = NumberedColoredShape.number
    NumberedColoredShape.k2 = NumberedColoredShape.color
    NumberedColoredShape.k3 = NumberedColoredShape.shape


    #
    #   NumberedColoredSizeShape
    #
    @share
    class NumberedColoredSizeShape(Object):
        __slots__ = ((
            'number',                   #   Number
            'color',                    #   Color
            'size',                     #   Size
            'shape',                    #   Shape
        ))


        is_herd = false


        def __init__(t, number, color, size, shape):
            t.number = number
            t.color  = color
            t.size   = size
            t.shape  = shape


        def __repr__(t):
            if show_address_and_references is 7:
                count = reference_count(t)
                return arrange('<numbered-colored-size-shape@%x#%d %d %s %s %s>',
                           address_of(t), count, t.number.value, t.color.name, t.size.name, t.shape.name)

            return arrange('<numbered-colored-size-shape %d %s %s %s>',
                           t.number.value, t.color.name, t.size.name, t.shape.name)



        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    NumberedColoredSizeShape.k1 = NumberedColoredSizeShape.number
    NumberedColoredSizeShape.k2 = NumberedColoredSizeShape.color
    NumberedColoredSizeShape.k3 = NumberedColoredSizeShape.size
    NumberedColoredSizeShape.k4 = NumberedColoredSizeShape.shape


    #
    #   NumberedShape
    #
    @share
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
            if show_address_and_references is 7:
                count = reference_count(t)
                return arrange('<numbered-shape@%x ->#%d %d %s>', address_of(t), count, t.number.value, t.shape.name)

            return arrange('<numbered-shape %d %s>', t.number.value, t.shape.name)


        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    NumberedShape.k1 = NumberedShape.number
    NumberedShape.k2 = NumberedShape.shape


    #
    #   Shape
    #
    @share
    class Shape(Object):
        __slots__ = ((
            'name',                     #   String+
        ))


        is_herd = false


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<shape %s>', t.name)


        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    Shape.nub = Shape.name.__get__


    #
    #   Size
    #
    class Size(Object):
        __slots__ = ((
            'name',                     #   String+
        ))


        is_herd = false


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<size %s>', t.name)


        display_token  = __repr__
        increment_skip = 0
        scrub          = 0


    Size.nub = Size.name.__get__


    #
    #   Conjure functions (Number)
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


    #
    #   Conjure functions (other)
    #
    conjure_color = produce_conjure_by_name__V2('color', Color)
    conjure_shape = produce_conjure_by_name__V2('shape', Shape)
    conjure_size  = produce_conjure_by_name__V2('size',  Size)


    share(
        'conjure_color',        conjure_color,
        'conjure_number',       conjure_number,
        'conjure_shape',        conjure_shape,
        'conjure_size',         conjure_size,
    )
