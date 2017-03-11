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

            'ZN',                       #   Function -> String
            'ZO',                       #   Function -> String

            #
            #   Tracking ''' & """ for normal portray
            #
            'favorite_3',               #   Integer
        ))


        def __init__(t, name):
            t.name = name


        def setup(t, A, K, N, Q, ZN, ZO, F3 = 0):
            t.A = A
            t.K = K
            t.N = N
            t.Q = Q

            t.ZN = ZN
            t.ZO = ZO

            t.favorite_3 = F3


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
    #       G = '   or \'
    #       H = ''  or \''
    #       J = ''' or \'''
    #
    #       K = \
    #       L = unprintable [AKA: "Lemon"]
    #       N = normal
    #
    #       Q = "
    #       R = ""
    #       S = """
    #
    #       T = \"
    #       U = \""
    #       V = \"""
    #
    #       W = "   or \"
    #       Y = ""  or \""
    #       Z = """ or \"""
    #
    A_A  = state('A_A')         #   Has '; ends in '
    A_B  = state('A_B')         #   Has '; ends in ''
    A_D  = state('A_D')         #   Has '; ends in \'
    A_E  = state('A_E')         #   Has '; ends in \''
    A_F  = state('A_F')         #   Has '; ends in \'''
    A_K  = state('A_K')         #   Has '; ends in \
    A_N  = state('A_N')         #   Has '

    AQ_A = state('AQ_A')        #   Has ' & "; ends in '
    AQ_B = state('AQ_B')        #   Has ' & "; ends in ''
    AQ_D = state('AQ_D')        #   Has ' & "; ends in \'
    AQ_E = state('AQ_E')        #   Has ' & "; ends in \''
    AQ_F = state('AQ_F')        #   Has ' & "; ends in \'''
    AQ_K = state('AQ_K')        #   Has ' & "; ends in \
    AQ_N = state('AQ_N')        #   Has ' & "
    AQ_Q = state('AQ_Q')        #   Has ' & "; ends in "
    AQ_R = state('AQ_R')        #   Has ' & "; ends in ""
    AQ_T = state('AQ_T')        #   Has ' & "; ends in \"
    AQ_U = state('AQ_U')        #   Has ' & "; ends in \""
    AQ_V = state('AQ_V')        #   Has ' & "; ends in \"""

    AS_A = state('AS_A')        #   Has ' & """; ends in '
    AS_B = state('AS_B')        #   Has ' & """; ends in ''
    AS_D = state('AS_D')        #   Has ' & """; ends in \'
    AS_E = state('AS_E')        #   Has ' & """; ends in \''
    AS_F = state('AS_F')        #   Has ' & """; ends in \'''
    AS_K = state('AS_K')        #   Has ' & """; ends in \
    AS_N = state('AS_N')        #   Has ' & """
    AS_W = state('AS_W')        #   Has ' & """; ends in "   or \"
    AS_Y = state('AS_Y')        #   Has ' & """; ends in ""  or \""
    AS_Z = state('AS_Z')        #   Has ' & """; ends in """ or \"""

    C_G  = state('C_G')         #   Has '''; ends in '   or \'
    C_H  = state('C_H')         #   Has '''; ends in ''  or \''
    C_J  = state('C_J')         #   Has '''; ends in ''' or \'''
    C_K  = state('C_K')         #   Has '''; ends in \
    C_N  = state('C_N')         #   Has '''
    C_T  = state('C_T')         #   Has '''; ends in \"

    CQ_G = state('CQ_G')        #   Has ''' & "; ends in '   or \'
    CQ_H = state('CQ_H')        #   Has ''' & "; ends in ''  or \''
    CQ_J = state('CQ_J')        #   Has ''' & "; ends in ''' or \'''
    CQ_K = state('CQ_K')        #   Has ''' & "; ends in \
    CQ_N = state('CQ_N')        #   Has ''' & "
    CQ_Q = state('CQ_Q')        #   Has ''' & "; ends in "
    CQ_R = state('CQ_R')        #   Has ''' & "; ends in ""
    CQ_T = state('CQ_R')        #   Has ''' & "; ends in \"
    CQ_U = state('CQ_R')        #   Has ''' & "; ends in \""
    CQ_V = state('CQ_R')        #   Has ''' & "; ends in \"""

    CS_G = state('CS_G')        #   Has ''' & """; ends in '   or \'
    CS_H = state('CS_H')        #   Has ''' & """; ends in ''  or \''
    CS_J = state('CS_J')        #   Has ''' & """; ends in ''' or \'''
    CS_N = state('CS_N')        #   Has ''' & """
    CS_W = state('CS_W')        #   Has ''' & """; ends in "   or \"
    CS_Y = state('CS_Y')        #   Has ''' & """; ends in ""  or \""
    CS_Z = state('CS_Z')        #   Has ''' & """; ends in """ or \"""

    L_G  = state('L_G')         #   Lemon; ends in '   or \'
    L_H  = state('L_H')         #   Lemon; ends in ''  or \''
    L_J  = state('L_J')         #   Lemon; ends in ''' or \'''
    L_N  = state('L_N')         #   Lemon
    L_W  = state('L_W')         #   Lemon; ends in "   or \"
    L_Y  = state('L_Y')         #   Lemon; ends in ""  or \""
    L_Z  = state('L_Z')         #   Lemon; ends in """ or \"""

    N_D  = state('N_D')         #   normal; ends in \'
    N_K  = state('N_K')         #   normal; ends in \
    N_N  = state('N_N')         #   normal
    N_T  = state('N_T')         #   normal; ends in \"

    Q_K  = state('Q_K')         #   Has "; ends in \
    Q_N  = state('Q_N')         #   Has "
    Q_Q  = state('Q_Q')         #   Has "; ends in "
    Q_R  = state('Q_R')         #   Has "; ends in ""
    Q_T  = state('Q_T')         #   Has "; ends in \"
    Q_U  = state('Q_U')         #   Has "; ends in \""
    Q_V  = state('Q_V')         #   Has "; ends in \"""

    S_D  = state('S_D')         #   Has """: ends in \'
    S_K  = state('S_K')         #   Has """: ends in \
    S_N  = state('S_N')         #   Has """
    S_W  = state('S_W')         #   Has """; ends in "   or \"
    S_Y  = state('S_Y')         #   Has """; ends in ""  or \""
    S_Z  = state('S_Z')         #   Has """; ends in """ or \"""


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
    A_B  .setup(C_J,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '; ends in ''
    A_D  .setup(A_E,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '; ends in \'
    A_E  .setup(A_F,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '; ends in \''
    A_F  .setup(C_G,    A_K,    A_N,    AQ_Q,   Q,  Q, F3 = -1)         #   Has '; ends in \'''
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)                  #   Has '; ends in \
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)                  #   Has '

    #           '       \       N       "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)                  #   Has ' & "; ends in '
    AQ_B .setup(CQ_J,   AQ_K,   AQ_N,   AQ_Q,   S,  S)                  #   Has ' & "; ends in ''
    AQ_D .setup(AQ_E,   AQ_K,   AQ_N,   AQ_Q,   C,  S)                  #   Has ' & "; ends in \'
    AQ_E .setup(AQ_F,   AQ_K,   AQ_N,   AQ_Q,   S,  S)                  #   Has ' & "; ends in \''
    AQ_F .setup(CQ_G,   AQ_K,   AQ_N,   AQ_Q,   S,  S, F3 = -1)         #   Has ' & "; ends in \'''
    AQ_K .setup(AQ_D,   AQ_N,   AQ_N,   AQ_T,   P,  P)                  #   Has ' & "; ends in \
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)                  #   Has ' & "
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)                  #   Has ' & "; ends in "
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_Z,   C,  C)                  #   Has ' & "; ends in ""
    AQ_T .setup(AQ_A,   AQ_K,   AQ_N,   AQ_U,   C,  S)                  #   Has ' & "; ends in \"
    AQ_U .setup(AQ_A,   AQ_K,   AQ_N,   AQ_V,   C,  C)                  #   Has ' & "; ends in \""
    AQ_V .setup(AQ_A,   AQ_K,   AQ_N,   AS_W,   C,  C, F3 = 1)          #   Has ' & "; ends in \"""

    #           '       \       N       "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_N,   AS_W,   P,  P)                  #   Has ' & """; ends in '
    AS_B .setup(CS_J,   AS_K,   AS_N,   AS_W,   P,  P)                  #   Has ' & """; ends in ''
    AS_D .setup(AS_E,   AS_K,   AS_N,   AS_W,   C,  C)                  #   Has ' & """; ends in \'
    AS_E .setup(AS_F,   AS_K,   AS_N,   AS_W,   P,  P)                  #   Has ' & """; ends in \''
    AS_F .setup(CS_G,   AS_K,   AS_N,   AS_W,   P,  P, F3 = -1)         #   Has ' & """; ends in \'''
    AS_K .setup(AS_D,   AS_N,   AS_N,   AS_W,   P,  P)                  #   Has ' & """; ends in \
    AS_N .setup(AS_A,   AS_K,   AS_N,   AS_W,   C,  C)                  #   Has ' & """
    AS_W .setup(AS_A,   AS_K,   AS_N,   AS_Y,   C,  C)                  #   Has ' & """; ends in "   or \"
    AS_Y .setup(AS_A,   AS_K,   AS_N,   AS_Z,   C,  C)                  #   Has ' & """; ends in ""  or \""
    AS_Z .setup(AS_A,   AS_K,   AS_N,   AS_W,   C,  C, F3 = 1)          #   Has ' & """; ends in """ or \"""

    #           '       \       N       "       N   O
    C_G  .setup(C_H,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''; ends in ''  or \''
    C_H  .setup(C_J,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''; ends in ''  or \''
    C_J  .setup(C_G,    C_K,    C_N,    CQ_Q,   Q,  Q, F3 = -1)         #   Has '''; ends in ''' or \'''
    C_K  .setup(C_G,    C_N,    C_N,    C_T,    P,  P)                  #   Has '''; ends in \
    C_N  .setup(C_G,    C_K,    C_N,    CQ_Q,   Q,  Q)                  #   Has '''
    C_T  .setup(C_G,    C_K,    C_N,    CQ_U,   Q,  Q)                  #   Has '''; ends in \"

    #           '       \       N       "       N   O
    CQ_G .setup(CQ_H,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "; ends in '   or \'
    CQ_H .setup(CQ_J,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "; ends in ''  or \''
    CQ_J .setup(CQ_G,   CQ_K,   CQ_N,   CQ_Q,   S,  S, F3 = -1)         #   Has ''' & "; ends in ''' or \'''
    CQ_K .setup(CQ_G,   CQ_N,   CQ_N,   CQ_U,   P,  P)                  #   Has ''' & "; ends in \
    CQ_N .setup(CQ_G,   CQ_K,   CQ_N,   CQ_Q,   S,  S)                  #   Has ''' & "
    CQ_Q .setup(CQ_G,   CQ_K,   CQ_N,   CQ_R,   P,  P)                  #   Has ''' & "; ends in "
    CQ_R .setup(CQ_G,   CQ_K,   CQ_N,   CS_W,   P,  P)                  #   Has ''' & "; ends in ""
    CQ_T .setup(CQ_G,   CQ_K,   CQ_N,   CQ_U,   S,  S)                  #   Has ''' & "; ends in \"
    CQ_U .setup(CQ_G,   CQ_K,   CQ_N,   CQ_V,   P,  P)                  #   Has ''' & "; ends in \""
    CQ_V .setup(CQ_G,   CQ_K,   CQ_N,   CS_Y,   P,  P, F3 = 1)          #   Has ''' & "; ends in \"""

    #           '       \       N       "       N   O
    CS_G .setup(CS_H,   CS_N,   CS_N,   CS_W,   P,  P)                  #   Has ''' or """; ends in '   or \'
    CS_H .setup(CS_J,   CS_N,   CS_N,   CS_W,   P,  P)                  #   Has ''' or """; ends in ''  or \''
    CS_J .setup(CS_G,   CS_N,   CS_N,   CS_W,   P,  P, F3 = -1)         #   Has ''' or """; ends in ''' or \'''
    CS_N .setup(CS_G,   CS_N,   CS_N,   CS_W,   P,  P)                  #   Has ''' or """
    CS_W .setup(CS_G,   CS_N,   CS_N,   CS_Y,   P,  P)                  #   Has ''' or """; ends in "   or \"
    CS_Y .setup(CS_G,   CS_N,   CS_N,   CS_Z,   P,  P)                  #   Has ''' or """; ends in ""  or \""
    CS_Z .setup(CS_G,   CS_N,   CS_N,   CS_W,   P,  P, F3 = 1)          #   Has ''' or """; ends in """ or \"""

    #           '       \       N       "       N   O
    L_G  .setup(L_H,    L_N,    L_N,    L_W,    P,  P)                  #   Lemon; ends in '   or \'
    L_H  .setup(L_J,    L_N,    L_N,    L_W,    P,  P)                  #   Lemon; ends in ''  or \''
    L_J  .setup(L_G,    L_N,    L_N,    L_W,    P,  P, F3 = -1)         #   Lemon; ends in ''' or \'''
    L_N  .setup(L_G,    L_N,    L_N,    L_W,    P,  P)                  #   Lemon
    L_W  .setup(L_G,    L_N,    L_N,    L_Y,    P,  P)                  #   Lemon; ends in "   or \"
    L_Y  .setup(L_G,    L_N,    L_N,    L_Z,    P,  P)                  #   Lemon; ends in ""  or \""
    L_Z  .setup(L_G,    L_N,    L_N,    L_W,    P,  P, F3 = 1)          #   Lemon; ends in """ or \"""

    #           '       \       N       "       N   O
    N_D  .setup(A_E,    N_K,    N_N,    Q_Q,    A,  Q)                  #   normal; ends in \'
    N_K  .setup(N_D,    N_N,    N_N,    N_T,    P,  P)                  #   normal; ends in \
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)                  #   normal
    N_T  .setup(A_A,    N_K,    N_N,    Q_U,    A,  Q)                  #   normal; ends in \"

    #           '       \       N       "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)                  #   Has "; ends in \
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)                  #   Has "
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)                  #   Has "; ends in "
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_Z,    A,  A)                  #   Has "; ends in ""
    Q_T  .setup(AQ_A,   Q_K,    Q_N,    Q_U,    A,  A)                  #   Has "; ends in \"
    Q_U  .setup(AQ_A,   Q_K,    Q_N,    Q_V,    A,  A)                  #   Has "; ends in \""
    Q_V  .setup(AQ_A,   Q_K,    Q_N,    S_W,    A,  A, F3 = 1)          #   Has "; ends in \"""

    #           '       \       N       "       N   O
    S_D  .setup(AS_E,   S_N,    S_N,    S_W,    A,  A)                  #   Has """: ends in \'
    S_K  .setup(S_D,    S_N,    S_N,    S_W,    P,  P)                  #   Has """: ends in \
    S_N  .setup(AS_A,   S_N,    S_N,    S_N,    A,  A)                  #   Has """
    S_W  .setup(AS_A,   S_N,    S_N,    S_Y,    A,  A)                  #   Has """; ends in "   or \"
    S_Y  .setup(AS_A,   S_N,    S_N,    S_Z,    A,  A)                  #   Has """; ends in ""  or \""
    S_Z  .setup(AS_A,   S_N,    S_N,    S_W,    A,  A, F3 = 1)          #   Has """; ends in """ or \"""

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
            return state.ZN(s)

        return state.ZO(s)


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
            return portray_raw_K_string(0, 0, N_K, iterator, s)

        if a.is_double_quote:
            favorite = 1
            state = Q_Q
        elif a.is_single_quote:
            favorite = -1
            state = A_A
        else:
            favorite = 0
            state    = L_N

        favorite_3 = 0

        for c in iterator:
            #old = state.name
            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                state = state.N

                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_backslash:
                return portray_raw_K_string(favorite, favorite_3, state.K, iterator, s)


            if a.is_double_quote:
                state       = state.Q
                favorite   += 1
                favorite_3 += state.favorite_3

                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_single_quote:
                state       = state.A
                favorite   -= 1
                favorite_3 += state.favorite_3

                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            assert not a.is_printable

            state = L_N

        #line('final: %d,%s,%s', favorite, state.name, last.name)

        if favorite >= 0:
            return state.ZN(s)

        return state.ZO(s)
