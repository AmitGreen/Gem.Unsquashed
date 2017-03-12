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

            'A',                        #   PortrayStringState
            'K',                        #   PortrayStringState
            'N',                        #   PortrayStringState
            'Q',                        #   PortrayStringState

            'RN',                       #   Function -> String
            'RO',                       #   Function -> String

            #
            #   Tracking ''' & """ for normal portray
            #
            'favorite_3',               #   Integer
        ))


        def __init__(t, name):
            t.name = name


        def setup(t, A, K, N, Q, RN, RO, F3 = 0):
            t.A = A
            t.K = K
            t.N = N
            t.Q = Q

            t.RN = RN
            t.RO = RO

            t.favorite_3 = F3


    state = PortrayStringState


    #
    #   states
    #
    #       A = '
    #       B = ''
    #       C = ''
    #
    #       K = \
    #       L = unprintable [AKA: "Lemon"]
    #       N = normal
    #
    #       Q = "
    #       R = ""
    #       S = """
    #
    A_A  = state('A_A')         #   Has '; ends in '
    A_B  = state('A_B')         #   Has '; ends in ''
    A_K  = state('A_K')         #   Has '; ends in \
    A_N  = state('A_N')         #   Has '

    AQ_A = state('AQ_A')        #   Has ' & "; ends in '
    AQ_B = state('AQ_B')        #   Has ' & "; ends in ''
    AQ_K = state('AQ_K')        #   Has ' & "; ends in \
    AQ_N = state('AQ_N')        #   Has ' & "
    AQ_Q = state('AQ_Q')        #   Has ' & "; ends in "
    AQ_R = state('AQ_R')        #   Has ' & "; ends in ""

    AS_A = state('AS_A')        #   Has ' & """; ends in '
    AS_B = state('AS_B')        #   Has ' & """; ends in ''
    AS_K = state('AS_K')        #   Has ' & """; ends in \
    AS_N = state('AS_N')        #   Has ' & """
    AS_Q = state('AS_Q')        #   Has ' & """; ends in "   or \"
    AS_R = state('AS_R')        #   Has ' & """; ends in ""
    AS_S = state('AS_S')        #   Has ' & """; ends in """

    C_A  = state('C_A')         #   Has '''; ends in '
    C_B  = state('C_B')         #   Has '''; ends in ''
    C_C  = state('C_C')         #   Has '''; ends in '''
    C_K  = state('C_K')         #   Has '''; ends in \
    C_N  = state('C_N')         #   Has '''

    CQ_A = state('CQ_A')        #   Has ''' & "; ends in '
    CQ_B = state('CQ_B')        #   Has ''' & "; ends in ''
    CQ_C = state('CQ_C')        #   Has ''' & "; ends in '''
    CQ_K = state('CQ_K')        #   Has ''' & "; ends in \
    CQ_N = state('CQ_N')        #   Has ''' & "
    CQ_Q = state('CQ_Q')        #   Has ''' & "; ends in "
    CQ_R = state('CQ_R')        #   Has ''' & "; ends in ""

    CS_A = state('CS_A')        #   Has ''' & """; ends in '
    CS_B = state('CS_B')        #   Has ''' & """; ends in ''
    CS_C = state('CS_C')        #   Has ''' & """; ends in '''
    CS_N = state('CS_N')        #   Has ''' & """
    CS_Q = state('CS_Q')        #   Has ''' & """; ends in "
    CS_R = state('CS_R')        #   Has ''' & """; ends in ""
    CS_S = state('CS_S')        #   Has ''' & """; ends in """

    L_A  = state('L_A')         #   Lemon; ends in '
    L_B  = state('L_B')         #   Lemon; ends in ''
    L_C  = state('L_C')         #   Lemon; ends in '''
    L_N  = state('L_N')         #   Lemon
    L_Q  = state('L_Q')         #   Lemon; ends in "
    L_R  = state('L_R')         #   Lemon; ends in ""
    L_S  = state('L_S')         #   Lemon; ends in """

    N_K  = state('N_K')         #   normal; ends in \
    N_N  = state('N_N')         #   normal

    Q_K  = state('Q_K')         #   Has "; ends in \
    Q_N  = state('Q_N')         #   Has "
    Q_Q  = state('Q_Q')         #   Has "; ends in "
    Q_R  = state('Q_R')         #   Has "; ends in ""

    S_K  = state('S_K')         #   Has """: ends in \
    S_N  = state('S_N')         #   Has """
    S_Q  = state('S_Q')         #   Has """; ends in "
    S_R  = state('S_R')         #   Has """; ends in ""
    S_S  = state('S_S')         #   Has """; ends in """


    #
    #   Results
    #
    def portray_raw_string_empty(s):
        assert (s == '') and (r"r''" is intern_string(r"r''"))

        return r"r''"


    def portray_raw_string_with_apostrophe(s):
        return "r'" + s + "'"


    #if __debug__:
    #    def portray_raw_string_invalid(s):
    #        raise_runtime_error('portray_raw_string_invalid called on %r', s)


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
    #_ = (portray_raw_string_invalid  if __debug__ else   portray_string)


    #           '       \       N       "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '; ends in '
    A_B  .setup(C_C,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '; ends in ''
    A_K  .setup(A_N,    A_N,    A_N,    A_N,    P,  P)                  #   Has '; ends in \
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '

    #           '       \       N       "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)                  #   Has ' & "; ends in '
    AQ_B .setup(CQ_C,   AQ_K,   AQ_N,   AQ_Q,   S,  S)                  #   Has ' & "; ends in ''
    AQ_K .setup(AQ_N,   AQ_N,   AQ_N,   AQ_N,   P,  P)                  #   Has ' & "; ends in \
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)                  #   Has ' & "
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)                  #   Has ' & "; ends in "
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_S,   C,  C)                  #   Has ' & "; ends in ""

    #           '       \       N       "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_N,   AS_Q,   P,  P)                  #   Has ' & """; ends in '
    AS_B .setup(CS_C,   AS_K,   AS_N,   AS_Q,   P,  P)                  #   Has ' & """; ends in ''
    AS_K .setup(AS_N,   AS_N,   AS_N,   AS_N,   P,  P)                  #   Has ' & """; ends in \
    AS_N .setup(AS_A,   AS_K,   AS_N,   AS_Q,   C,  C)                  #   Has ' & """
    AS_Q .setup(AS_A,   AS_K,   AS_N,   AS_R,   C,  C)                  #   Has ' & """; ends in "
    AS_R .setup(AS_A,   AS_K,   AS_N,   AS_S,   C,  C)                  #   Has ' & """; ends in ""
    AS_S .setup(AS_A,   AS_K,   AS_N,   AS_Q,   C,  C, F3 = 1)          #   Has ' & """; ends in """

    #           '       \       N       "       N   O
    C_A  .setup(C_B,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''; ends in '
    C_B  .setup(C_C,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''; ends in ''
    C_C  .setup(C_A,    C_K,    C_N,    CQ_Q,   Q,  Q, F3 = -1)         #   Has '''; ends in '''
    C_K  .setup(C_N,    C_N,    C_N,    C_N,    P,  P)                  #   Has '''; ends in \
    C_N  .setup(C_A,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''

    #           '       \       N       "       N   O
    CQ_A .setup(CQ_B,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "; ends in '
    CQ_B .setup(CQ_C,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "; ends in ''
    CQ_C .setup(CQ_A,   CQ_K,   CQ_N,   CQ_Q,   S,  S, F3 = -1)         #   Has ''' & "; ends in '''
    CQ_K .setup(CQ_A,   CQ_N,   CQ_N,   CQ_N,   P,  P)                  #   Has ''' & "; ends in \
    CQ_N .setup(CQ_A,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "
    CQ_Q .setup(CQ_A,   CQ_K,   CQ_N,   CQ_R,   P,  P)                  #   Has ''' & "; ends in "
    CQ_R .setup(CQ_A,   CQ_K,   CQ_N,   CS_Q,   P,  P)                  #   Has ''' & "; ends in ""

    #           '       \       N       "       N   O
    CS_A .setup(CS_B,   CS_N,   CS_N,   CS_Q,   P,  P)                  #   Has ''' & """; ends in '
    CS_B .setup(CS_C,   CS_N,   CS_N,   CS_Q,   P,  P)                  #   Has ''' & """; ends in ''
    CS_C .setup(CS_A,   CS_N,   CS_N,   CS_Q,   P,  P, F3 = -1)         #   Has ''' & """; ends in '''
    CS_N .setup(CS_A,   CS_N,   CS_N,   CS_Q,   P,  P)                  #   Has ''' & """
    CS_Q .setup(CS_A,   CS_N,   CS_N,   CS_R,   P,  P)                  #   Has ''' & """; ends in "
    CS_R .setup(CS_A,   CS_N,   CS_N,   CS_S,   P,  P)                  #   Has ''' & """; ends in ""
    CS_S .setup(CS_A,   CS_N,   CS_N,   CS_Q,   P,  P, F3 = 1)          #   Has ''' & """; ends in """

    #           '       \       N       "       N   O
    L_A  .setup(L_B,    L_N,    L_N,    L_Q,    P,  P)                  #   Lemon; ends in '
    L_B  .setup(L_C,    L_N,    L_N,    L_Q,    P,  P)                  #   Lemon; ends in ''
    L_C  .setup(L_A,    L_N,    L_N,    L_Q,    P,  P, F3 = -1)         #   Lemon; ends in '''
    L_N  .setup(L_A,    L_N,    L_N,    L_Q,    P,  P)                  #   Lemon
    L_Q  .setup(L_A,    L_N,    L_N,    L_R,    P,  P)                  #   Lemon; ends in "
    L_R  .setup(L_A,    L_N,    L_N,    L_S,    P,  P)                  #   Lemon; ends in ""
    L_S  .setup(L_A,    L_N,    L_N,    L_Q,    P,  P, F3 = 1)          #   Lemon; ends in """

    #           '       \       N       "       N   O
    N_K  .setup(N_N,    N_N,    N_N,    N_N,    P,  P)                  #   normal; ends in \
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)                  #   normal

    #           '       \       N       "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)                  #   Has "; ends in \
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)                  #   Has "
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)                  #   Has "; ends in "
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_S,    A,  A)                  #   Has "; ends in ""

    #           '       \       N       "       N   O
    S_K  .setup(S_N,    S_N,    S_N,    S_N,    P,  P)                  #   Has """: ends in \
    S_N  .setup(AS_A,   S_K,    S_N,    S_N,    A,  A)                  #   Has """
    S_Q  .setup(AS_A,   S_K,    S_N,    S_R,    A,  A)                  #   Has """; ends in "
    S_R  .setup(AS_A,   S_K,    S_N,    S_S,    A,  A)                  #   Has """; ends in ""
    S_S  .setup(AS_A,   S_K,    S_N,    S_Q,    A,  A, F3 = 1)          #   Has """; ends in """

    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_K_string(favorite, favorite_3, state, iterator, s):
        #line('portray_raw_K_string(%d, %s, %r, %r)', favorite, state, iterator, s)

        for c in iterator:
            #old_state = state.name

            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                state = state.N

                #line('%r: %s => %s; %s => %s', c,  old_state, state.name)
                continue

            if a.is_backslash:
                state = state.K

                #line('%r: %s => %s', c,  old_state, state.name)
                continue

            if a.is_double_quote:
                state       = state.Q
                favorite   += 1
                favorite_3 += state.favorite_3

                #line('%r: %s => %s', c,  old_state, state.name)
                continue

            if a.is_single_quote:
                state       = state.A
                favorite   -= 1
                favorite_3 += state.favorite_3

                #line('%r: %s => %s', c,  old_state, state.name)
                continue

            assert not a.is_printable

            state = L_N

        #line('final of %r: %d, %s', s, favorite, state.name)

        if favorite >= 0:
            return state.RN(s)

        return state.RO(s)


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
        #line('portray_raw_string(%r)', s)

        if a.is_backslash:
            backslash = true
            favorite  = 0
            raw_state = N_K
            state     = N_N
        else:
            backslash = false

            if a.is_double_quote:
                favorite = 1
                raw_state = state = Q_Q
            elif a.is_single_quote:
                favorite  = -1
                raw_state = state = A_A
            else:
                favorite  = 0
                raw_state = state = L_N

        favorite_3 = 0

        for c in iterator:
            #old     = state.name
            #raw_old = raw_state.name

            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                raw_state = raw_state.N
                state     = state.N

                #line('  %r: %s => %s, %s => %s', c, raw_old, raw_state.name, old, state.name)
                continue

            if a.is_backslash:
                backslash = true
                raw_state = raw_state.K
                state     = state.N

                #line('  %r: %s => %s, %s => %s', c, raw_old, raw_state.name, old, state.name)
                continue

            if a.is_double_quote:
                raw_state   = raw_state.Q
                state       = state.Q
                favorite   += 1
                favorite_3 += state.favorite_3

                #line('  %r: %s => %s, %s => %s', c, raw_old, raw_state.name, old, state.name)
                continue

            if a.is_single_quote:
                raw_state   = raw_state.A
                state       = state.A
                favorite   -= 1
                favorite_3 += state.favorite_3

                #line('  %r: %s => %s, %s => %s', c, raw_old, raw_state.name, old, state.name)
                continue

            assert not a.is_printable

            state = L_N

        #line('  final %r: %d, %s, %s', s, favorite, raw_state.name, state.name)

        if favorite >= 0:
            return raw_state.RN(s)

        return raw_state.RO(s)
