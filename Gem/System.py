#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.System')
def gem():
    python_frame = PythonSystem._getframe


    caller_frame_0 = Method(python_frame, 0)
    caller_frame_1 = Method(python_frame, 1)


    @built_in
    def my_name():
        return caller_frame_1().f_code.co_name
 

    export(
        'caller_frame_1',   caller_frame_1,
        'python_frame',     PythonSystem._getframe,
        'python_version',   PythonSystem.version,
    )
