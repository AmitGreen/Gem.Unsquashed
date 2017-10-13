#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Transform')
def gem():
    require_gem('Sapphire.Indentation')


    class SapphireTransform(Object):
        __slots__ = ((
            'remove_comments',          #   Boolean
            'remove_indentation',       #   Boolean
            'indentation',              #   Vacant | Indentation
            'indentation_stack',        #   Vacant | List
            '_push_indentation',        #   Vacant | Method
            '_pop_indentation',         #   Vacant | Method
        ))


        def __init__(t, remove_comments, remove_indentation):
            t.remove_comments    = remove_comments
            t.remove_indentation = remove_indentation

            if remove_indentation:
                t.indentation       = empty_indentation
                t.indentation_stack = indentation_stack = []
                t._push_indentation = indentation_stack.append
                t._pop_indentation  = Method(indentation_stack.pop, -1)


        def pop_indentation(t):
            r = t.indentation = t._pop_indentation()

            return r


        def push_indentation(t, indentation):
            t.indentation = indentation
            t._push_indentation(indentation)


    @share
    def create_sapphire_transform(
            remove_comments    = false,
            remove_indentation = false,
    ):
        total = remove_comments + remove_indentation

        if total is 0:
            return 0

        return SapphireTransform(remove_comments, remove_indentation)
