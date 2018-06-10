#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Pearl.Method')
def gem():
    #
    #   is_name
    #
    @export
    def is_name__0(t, name):
        return false


    #
    #   is_name
    #
    @export
    def order__s(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            if a.s < b.s:   return -1
            if a.s > b.s:   return 1

            return 0

        if a_order < b_order: return -1

        assert a_order > b_order

        return 1
