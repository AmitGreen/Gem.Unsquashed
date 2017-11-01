#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Map')
def gem():
    #
    #   view_items
    #       Access the .viewitems method of a Map.
    #
    #       (Deals with the annoyance of .viewitems method named .viewitems in Python 2.0, but .items in
    #       Python 3.0)
    #
    view_items =  (Map.viewitems    if is_python_2 else   Map.items)
    view_values = (Map.viewvalues   if is_python_2 else   Map.values)


    if is_python_2:
        @export
        def first_map_item(mapping):
            return iterate(view_items(mapping)).next()
    else:
        @export
        def first_map_item(mapping):
            return iterate(view_items(mapping)).__next__()


    @built_in
    def iterate_items_sorted_by_key(mapping):
        value = mapping.__getitem__

        for k in sorted_list(mapping):
            yield (( k, value(k) ))


    @built_in
    def iterate_values_sorted_by_key(mapping, key = none):
        value = mapping.__getitem__

        if key is none:
            for k in sorted_list(mapping):
                yield value(k)
        else:
            for k in sorted_list(mapping, key = key):
                yield value(k)


    @export
    def values_tuple_sorted_by_key(mapping):
        value = mapping.__getitem__

        return Tuple(value(k)   for k in sorted_list(mapping))


    built_in(
        'view_items',   view_items,
        'view_values',  view_values,
    )
