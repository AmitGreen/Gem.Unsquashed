#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DumpToken')
def gem():
    require_gem('Sapphire.Tree')


    @share
    def dump_token(name, token):
        with create_StringOutput() as f:
            f.line('===  %s  ===', name)
            token.dump_token(f)

        partial(f.result)
