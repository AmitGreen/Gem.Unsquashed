#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.RawString_3')
def gem():
    require_gem('Gem.Ascii')
    require_gem('Gem.Exception')


    class PortrayStringState(Object):
        __slots__ = ((
            'name',                     #   String

            'apostrophe',               #   PortrayStringState
            'backslash',                #   PortrayStringState
            'normal',                   #   PortrayStringState
            'quotation_mark',           #   PortrayStringState

            'finish_normal',            #   Function -> String
            'finish_other',             #   Function -> String

            'finish_apostrope',         #   Function -> String
            'finish_quotation_mark',    #   Function -> String
        ))


        def __init__(t, name):
            t.name = name


        def end(t, apostrophe, backslash, quotation_mark, finish_apostrope, finish_quotation_mark):
            t.apostrophe     = apostrophe
            t.backslash      = backslash
            #
            #   normal         Not applicatble
            #
            t.quotation_mark = quotation_mark

            #
            #   finish_normal   Not applicatble
            #   finish_other    Not applicatble
            #
            t.finish_apostrope      = finish_apostrope
            t.finish_quotation_mark = finish_quotation_mark


        def setup(t, apostrophe, backslash, normal, quotation_mark, finish_normal, finish_other):
            t.apostrophe     = apostrophe
            t.backslash      = backslash
            t.normal         = normal
            t.quotation_mark = quotation_mark

            t.finish_normal = finish_normal
            t.finish_other  = finish_other

            #
            #   finish_apostrope         Not applicable
            #   finish_quotation_mark    Not applicable
            #


    state = PortrayStringState


    #
    #   states
    #
    #       A = '
    #       B = ''
    #       C = ''
    #
    #       D = \'
    #       E = \''
    #       F = \'''
    #
    #       K = \
    #       N = normal
    #       M = normal -- might end in ", "", ', or ''
    #
    #       Q = "
    #       R = ""
    #       S = """
    #
    #       T = \"
    #       U = \""
    #       V = \"""
    #
    #       X = non-ascii
    #
    X      = state('X')

    A_A    = state('A_A')       #   Has '; ends in '
    A_B    = state('A_B')       #   Has '; ends in ''
    A_K    = state('A_K')       #   Has '; ends in \
    A_N    = state('A_N')       #   Has '

    AQ_A   = state('AQ_A')      #   Has ' & "; ends in '
    AQ_B   = state('AQ_B')      #   Has ' & "; ends in ''
    AQ_K   = state('AQ_K')      #   Has ' & "; ends in \
    AQ_N   = state('AQ_N')      #   Has ' & "
    AQ_Q   = state('AQ_Q')      #   Has ' & "; ends in "
    AQ_R   = state('AQ_R')      #   Has ' & "; ends in ""

    AS_A   = state('AS_A')      #   Has ' & """; ends in '
    AS_B   = state('AS_B')      #   Has ' & """; ends in ''
    AS_K   = state('AS_K')      #   Has ' & """; ends in \
    AS_M   = state('AS_M')      #   Has ' & """; might end in " or ""

    C_K    = state('C_K')       #   Has '''; ends in \
    C_M    = state('C_M')       #   Has '''; might end in ' or ""

    CQ_K   = state('CQ_K')      #   Has ''' & "; ends in \
    CQ_M   = state('CQ_M')      #   Has ''' & "; might end in ' or ''
    CQ_Q   = state('CQ_Q')      #   Has ''' & "; ends in "
    CQ_R   = state('CQ_R')      #   Has ''' & "; ends in ""

    N_K    = state('N_K')       #   normal; ends in \
    N_N    = state('N_N')       #   totally normal, nothing to see here

    Q_K    = state('Q_K')       #   Has "; ends in \
    Q_N    = state('Q_N')       #   Has "
    Q_Q    = state('Q_Q')       #   Has "; ends in "
    Q_R    = state('Q_R')       #   Has "; ends in " in ""

    S_K    = state('S_K')       #   Has """: ends in \
    S_M    = state('S_M')       #   Has """; might end in " or ""


    #
    #   End states
    #
    end_A = state('end_A')      #       A = ends in '
    end_B = state('end_B')      #       B = ends in ''
    end_C = state('end_C')      #       C = ends in '''

    end_D = state('end_D')      #       D = ends in \'
    end_E = state('end_E')      #       E = ends in \''
    end_F = state('end_F')      #       F = ends in \'''

    end_K = state('end_K')      #       K = ends in \
    end_N = state('end_N')      #       N = normal

    end_Q = state('end_Q')      #       Q = ends in "
    end_R = state('end_R')      #       R = ends in ""
    end_S = state('end_S')      #       S = ends in """

    end_T = state('end_T')      #       T = ends in \"
    end_U = state('end_U')      #       U = ends in \""
    end_V = state('end_V')      #       V = ends in \"""


    finish_apostrope      = PortrayStringState.finish_apostrope     .__get__
    finish_normal         = PortrayStringState.finish_normal        .__get__
    finish_other          = PortrayStringState.finish_other         .__get__
    finish_quotation_mark = PortrayStringState.finish_quotation_mark.__get__


    def finish_portray(state):
        return portray_string


    end_A.end(end_B, end_K, end_Q, finish_apostrope,      finish_apostrope)
    end_B.end(end_C, end_K, end_Q, finish_apostrope,      finish_apostrope)
    end_C.end(end_C, end_K, end_Q, finish_apostrope,      finish_apostrope)
    end_D.end(end_A, end_K, end_Q, finish_apostrope,      finish_apostrope)

    end_K.end(end_D, end_N, end_T, finish_portray,        finish_portray)
    end_N.end(end_A, end_K, end_Q, finish_normal,         finish_other)

    end_Q.end(end_A, end_K, end_R, finish_quotation_mark, finish_quotation_mark)
    end_R.end(end_A, end_K, end_S, finish_quotation_mark, finish_quotation_mark)
    end_S.end(end_A, end_K, end_S, finish_quotation_mark, finish_quotation_mark)
    end_T.end(end_A, end_K, end_Q, finish_quotation_mark, finish_quotation_mark)


    #
    #   Results
    #
    def portray_raw_string_empty(s):
        assert (s == '') and (r"r''" is intern_string(r"r''"))

        return r"r''"


    def portray_raw_string_with_apostrophe(s):
        return "r'" + s + "'"


    if __debug__:
        def portray_raw_string_invalid(s):
            raise_runtime_error('portray_raw_string_invalid called on %r', s)


    def portray_raw_string_with_quotation_mark(s):
        return 'r"' + s + '"'


    portray_string = String.__repr__


    def portray_raw_string_with_triple_apostrophe(s):
        return "r'''" + s + "'''"


    def portray_raw_string_with_triple_quotation_mark(s):
        return 'r"""' + s + '"""'


    A = portray_raw_string_with_apostrophe
    C = portray_raw_string_with_triple_apostrophe
    I = portray_raw_string_empty
    Q = portray_raw_string_with_quotation_mark
    P = portray_string
    S = portray_raw_string_with_triple_quotation_mark
    _ = (portray_raw_string_invalid  if __debug__ else   portray_string)


    #           '       \       N_N     "       N   O
    X    .setup(X,      X,      X,      X,      P,  P)

    #           '       \       N_N     "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_B  .setup(C_M,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)

    #           '       \       N_N     "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_B .setup(CQ_M,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_K .setup(AQ_N,   AQ_N,   AQ_N,   AQ_N,   P,  P)
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_M,   C,  C)

    #           '       \       N_N     "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_M,   AS_M,   P,  P)
    AS_B .setup(X,      AS_K,   AS_M,   AS_M,   P,  P)
    AS_K .setup(AS_M,   AS_M,   AS_M,   AS_M,   P,  P)
    AS_M .setup(AS_A,   AS_K,   AS_M,   AS_M,   C,  C)

    #           '       \       N_N     "       N   O
    C_K  .setup(C_M,    C_M,    C_M,    C_M,    P,  P)
    C_M  .setup(C_M,    C_K,    C_M,    CQ_Q,   Q,  Q)

    #           '       \       N_N     "       N   O
    CQ_K .setup(CQ_M,   CQ_M,   CQ_M,   CQ_M,   P,  P)
    CQ_M .setup(CQ_M,   CQ_K,   CQ_M,   CQ_Q,   S,  S)
    CQ_Q .setup(CQ_M,   CQ_K,   CQ_M,   CQ_R,   P,  P)
    CQ_R .setup(CQ_M,   CQ_K,   CQ_M,   X,      P,  P)

    #           '       \       N_N     "       N   O
    N_K  .setup(N_N,    N_N,    N_N,    N_N,    P,  P)
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)

    #           '       \       N_N     "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_M,    A,  A)

    #           '       \       N_N     "       N   O
    S_K  .setup(S_M,    S_M,    S_M,    S_M,    P,  P)
    S_M  .setup(AS_A,   S_M,    S_M,    S_M,    A,  A)


    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_K_string(favorite, state, iterator, s):
        line('portray_raw_K_string(%d, %s, %r, %r)', favorite, state, iterator, s)

        for c in iterator:
            old = state.name
            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                state = state.normal
                line('%s: %r, %s', old, c, state.name)
                continue

            if a.is_backslash:
                state = state.backslash
                line('%s: %r, %s', old, c, state.name)
                continue

            if a.is_double_quote:
                favorite += 1
                state = state.quotation_mark
                line('%s: %r, %s', old, c, state.name)
                continue

            if a.is_single_quote:
                favorite -= 1
                state = state.apostrophe
                line('%s: %r, %s', old, c, state.name)
                continue

            assert not a.is_printable

            return portray_string(s)

        line('final: %d, %s', favorite, state.name)

        if favorite >= 0:
            return state.finish_normal(s)

        return state.finish_other(s)


    @export
    def portray_raw_string(s):
        iterator = iterate(s)

        #
        #   Simple case
        #
        for c in iterator:
            a = lookup_ascii(c, unknown_ascii)

            if not a.is_portray_boring:
                break
        else:
            return "r'" + s + "'"

        #
        #   Complex case
        #
        if a.is_backslash:
            return portray_raw_K_string(0, N_K, iterator, s)

        if a.is_double_quote:
            favorite = 1
            state = Q_Q

        elif a.is_single_quote:
            favorite = -1
            state = A_A

        else:
            assert not a.is_printable

            return portray_string(s)

        for c in iterator:
            #old = state.name
            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                state = state.normal
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_backslash:
                return portray_raw_K_string(favorite, state.backslash, iterator, s)


            if a.is_double_quote:
                favorite += 1
                state = state.quotation_mark
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_single_quote:
                favorite -= 1
                state = state.apostrophe
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            assert not a.is_printable

            return portray_string(s)

        #line('final: %d,%s,%s', favorite, state.name, last.name)

        if favorite >= 0:
            return state.finish_normal(s)

        return state.finish_other(s)
