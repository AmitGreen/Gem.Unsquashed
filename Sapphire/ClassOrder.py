#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CLASS_ORDER')
def gem():
    share(
        'CLASS_ORDER__NORMAL_TOKEN',            1,       #   Normal token
        'CLASS_ORDER__ARGUMENT_0',              2,       #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',            3,       #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',             4,       #   Indentation token
        'CLASS_ORDER__LINE_MARKER',             5,       #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',              6,       #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',            7,       #   CommentLine token
        'CLASS_ORDER__JOIN_TOKEN',              8,       #   Join token
    )
