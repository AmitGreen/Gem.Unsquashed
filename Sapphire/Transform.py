#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Transform')
def gem():
    class SapphireTransform(Object):
        __slots__ = ((
            'remove_comments',          #   Boolean
            'remove_indentation',       #   Boolean
        ))


        def __init__(t, remove_comments, remove_indentation):
            t.remove_comments    = remove_comments
            t.remove_indentation = remove_indentation


    @share
    def create_sapphire_transform(
            remove_comments    = false,
            remove_indentation = false,
    ):
        total = remove_comments + remove_indentation

        if total is 0:
            return 0

        return SapphireTransform(remove_comments, remove_indentation)
