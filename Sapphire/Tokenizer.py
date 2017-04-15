#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenizer')
def gem():
    class Tokenizer(Object):
        __slots__ = ((
            's',                        #   None | String
            'i',                        #   None | Integer
            'j',                        #   None | Integer
        ))


        def __init__(t):
            t.j = t.i = t.s = none


    tokenizer = Tokenizer()


    del Tokenizer.__init__


    @share
    def z_initialize(data_lines):
        maximum_i = length(data_lines)
        q_data    = data_lines.__getitem__


        def GENERATOR_next_line():
            for i in iterate_range(maximum_i):
                s           = tokenizer.s = q_data(i)
                tokenizer.i = i
                tokenizer.j = 0

                yield s

            tokenizer.s = none
            tokenizer.i = none
            tokenizer.j = none

            yield none


        return next_method(GENERATOR_next_line())


    slot_j = Tokenizer.j
    slot_s = Tokenizer.s


    share(
        'qj',           Method(slot_j.__get__, tokenizer),
        'qs',           Method(slot_s.__get__, tokenizer),

        'zj',           Method(slot_j.__set__, tokenizer),
    )
