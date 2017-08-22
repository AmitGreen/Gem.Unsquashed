#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Output')
def gem():
    standard_error  = PythonSystem.stderr
    standard_output = PythonSystem.stdout


    flush_standard_error  = standard_error .flush
    flush_standard_output = standard_output.flush
    write_standard_error  = standard_error .write
    write_standard_output = standard_output.write


    export(
        #
        #   Functions
        #
        'flush_standard_error',     flush_standard_error,
        'flush_standard_output',    flush_standard_output,
        'write_standard_error',     write_standard_error,
        'write_standard_output',    write_standard_output,
    )
