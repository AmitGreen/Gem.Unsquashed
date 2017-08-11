#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.System')
def gem():
    export(
        'python_frame',     PythonSystem._getframe,
        'python_version',   PythonSystem.version,
    )
