#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.MosiacSymbol')
def gem():
    class FunctionSymbol(Object):
        __slots__ = ((
            'header',                   #   FunctionHeader
            'body',                     #   Statement+
            'parameters',               #   None | FunctionParameter | Tuple of FunctionParameter
            'locals',                   #   None | FunctionLocal | Tuple of { FunctionLocal | FunctionParameter }
            'cells',                    #   None | ( CellFunctionParameter | CellLocal )
                                        #       | Tuple of ( CellFunctionParameter | CellLocal )
            'free_variables',           #   None | FreeVariable | Tuple of FreeVariable
            'globals',                  #   None | GlobalVariable | Tuple of GlobalVariable
        ))


        def __init__(t, header, body, parameters, locals, cells, free_variables, globals):
            t.header         = header
            t.body           = body
            t.parameters     = parameters
            t.locals         = locals
            t.cells          = cells
            t.free_variables = free_variables
            t.globals        = globals
