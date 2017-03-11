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
            #   K
            #
            'C',                        #   PortrayStringState
            'S',                        #   PortrayStringState

            #
            #   Y
            #
            'is_3',                     #   Boolean
            'ZA',                       #   Function -> String
            'ZQ',                       #   Function -> String
        ))


        def __init__(t, name):
            t.name = name


        def end(t, A, K, Q, is_3, ZA, ZQ):
            t.A = A
            t.K = K
            #
            #   N         Not applicatble
            #
            t.Q = Q

            #
            #   ZN   Not applicatble
            #   ZO   Not applicatble
            #
            t.is_3 = Boolean(is_3)
            t.ZA   = ZA
            t.ZQ   = ZQ


        def Ksetup(t, A, C, Q, S, ZN, ZO, ZA, ZQ):
            t.A = A
            #
            #   K   Not applicable
            #   N   Not applicable
            #
            t.Q = Q

            t.C = C
            t.S = S

            t.ZN = ZN
            t.ZO = ZO

            t.ZA = ZA
            t.ZQ = ZQ


        def setup(t, A, K, N, Q, ZN, ZO):
            t.A = A
            t.K = K
            t.N = N
            t.Q = Q

            t.ZN = ZN
            t.ZO = ZO

            #
            #   C     Not applicable
            #   S     Not applicable
            #   ZA    Not applicable
            #   ZQ    Not applicable
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
    #       G = '   or \'
    #       H = ''  or \''
    #       J = ''' or \'''
    #
    #       K = \
    #       L = non-ascii (AKA: "Lemon")
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
    L_G  = state('L_G')         #   Has unprintinable; ends in '   or \'
    L_H  = state('L_H')         #   Has unprintinable; ends in ''  or \''
    L_J  = state('L_J')         #   Has unprintinable; ends in ''' or \'''
    L_N  = state('L_N')         #   Has unprintable
    L_W  = state('L_W')         #   Has unprintinable; ends in "   or \"
    L_Y  = state('L_Y')         #   Has unprintinable; ends in ""  or \""
    L_Z  = state('L_Z')         #   Has unprintinable; ends in """ or \"""

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

    N_D  = state('N_D')         #   normal; ends in \'
    N_K  = state('N_K')         #   normal; ends in \
    N_N  = state('N_N')         #   totally normal, nothing to see here
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
    #   Backslash States
    #
    K   = state('K')         #   Normal
    KA  = state('KA')        #   Has '
    KAQ = state('KAQ')       #   Has ' & "
    KAS = state('KAS')       #   Has ' & """
    KC  = state('KC')        #   Has '''
    KCQ = state('KCQ')       #   Has ''' & "
    KCS = state('KCS')       #   Has ''' & """
    KQ  = state('KQ')        #   Has "
    KS  = state('KQ')        #   Has """
    KX  = state('KX')        #   Has unprintable


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


    #           '       \       N       "       N   O
    L_G  .setup(L_H,    L_N,    L_N,    L_W,    P,  P)
    L_H  .setup(L_J,    L_N,    L_N,    L_W,    P,  P)
    L_J  .setup(L_G,    L_N,    L_N,    L_W,    P,  P)
    L_N  .setup(L_G,    L_N,    L_N,    L_W,    P,  P)
    L_W  .setup(L_G,    L_N,    L_N,    L_Y,    P,  P)
    L_Y  .setup(L_G,    L_N,    L_N,    L_Z,    P,  P)
    L_Z  .setup(L_G,    L_N,    L_N,    L_W,    P,  P)

    #           '       \       N       "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_B  .setup(C_J,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_D  .setup(A_E,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_E  .setup(A_F,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_F  .setup(C_G,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)

    #           '       \       N       "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_B .setup(CQ_J,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_D .setup(AQ_E,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_E .setup(AQ_F,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_F .setup(CQ_G,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_K .setup(AQ_D,   AQ_N,   AQ_N,   AQ_T,   P,  P)
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_Z,   C,  C)
    AQ_T .setup(AQ_A,   AQ_K,   AQ_N,   AQ_U,   C,  S)
    AQ_U .setup(AQ_A,   AQ_K,   AQ_N,   AQ_V,   C,  C)
    AQ_V .setup(AQ_A,   AQ_K,   AQ_N,   AS_W,   C,  C)

    #           '       \       N       "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_N,   AS_W,   P,  P)
    AS_B .setup(L_J,    AS_K,   AS_N,   AS_W,   P,  P)
    AS_D .setup(AS_E,   AS_K,   AS_N,   AS_W,   C,  C)
    AS_E .setup(AS_F,   AS_K,   AS_N,   AS_W,   P,  P)
    AS_F .setup(L_G,    AS_K,   AS_N,   AS_W,   P,  P)
    AS_K .setup(AS_D,   AS_N,   AS_N,   AS_W,   P,  P)
    AS_N .setup(AS_A,   AS_K,   AS_N,   AS_W,   C,  C)
    AS_W .setup(AS_A,   AS_K,   AS_N,   AS_Y,   C,  C)
    AS_Y .setup(AS_A,   AS_K,   AS_N,   AS_Z,   C,  C)
    AS_Z .setup(AS_A,   AS_K,   AS_N,   AS_W,   C,  C)

    #           '       \       N       "       N   O
    C_G  .setup(C_H,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_H  .setup(C_J,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_J  .setup(C_G,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_K  .setup(C_G,    C_N,    C_N,    C_T,    P,  P)
    C_N  .setup(C_G,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_T  .setup(C_G,    C_K,    C_N,    CQ_U,   Q,  Q)

    #           '       \       N       "       N   O
    CQ_G .setup(CQ_H,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_H .setup(CQ_J,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_J .setup(CQ_G,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_K .setup(CQ_G,   CQ_N,   CQ_N,   CQ_U,   P,  P)
    CQ_N .setup(CQ_G,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_Q .setup(CQ_G,   CQ_K,   CQ_N,   CQ_R,   P,  P)
    CQ_R .setup(CQ_G,   CQ_K,   CQ_N,   L_W,    P,  P)
    CQ_T .setup(CQ_G,   CQ_K,   CQ_N,   CQ_U,   S,  S)
    CQ_U .setup(CQ_G,   CQ_K,   CQ_N,   CQ_V,   P,  P)
    CQ_V .setup(CQ_G,   CQ_K,   CQ_N,   L_Y,    P,  P)

    #           '       \       N       "       N   O
    N_D  .setup(A_E,    N_K,    N_N,    Q_Q,    A,  Q)
    N_K  .setup(N_D,    N_N,    N_N,    N_T,    P,  P)
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)
    N_T  .setup(A_A,    N_K,    N_N,    Q_U,    A,  Q)

    #           '       \       N       "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_Z,    A,  A)
    Q_T  .setup(AQ_A,   Q_K,    Q_N,    Q_U,    A,  A)
    Q_U  .setup(AQ_A,   Q_K,    Q_N,    Q_V,    A,  A)
    Q_V  .setup(AQ_A,   Q_K,    Q_N,    S_W,    A,  A)

    #           '       \       N       "       N   O
    S_D  .setup(AS_E,   S_N,    S_N,    S_W,    A,  A)
    S_K  .setup(S_D,    S_N,    S_N,    S_W,    P,  P)
    S_N  .setup(AS_A,   S_N,    S_N,    S_N,    A,  A)
    S_W  .setup(AS_A,   S_N,    S_N,    S_Y,    A,  A)
    S_Y  .setup(AS_A,   S_N,    S_N,    S_Z,    A,  A)
    S_Z  .setup(AS_A,   S_N,    S_N,    S_W,    A,  A)


    #
    #   Backslash States
    #
    #          '    '''   "     """   N   O   '   "
    K  .Ksetup(KA,  KC,   KQ,   KS,   A,  Q,  _,  _)
    KA .Ksetup(KA,  KC,   KAQ,  KAS,  Q,  Q,  Q,  _)
    KAQ.Ksetup(KAQ, KCQ,  KAQ,  KAS,  C,  S,  S,  C)
    KAS.Ksetup(KAS, KCS,  KAS,  KAS,  C,  C,  P,  C)
    KC .Ksetup(KC,  KC,   KCQ,  KCS,  Q,  Q,  Q,  _)
    KCQ.Ksetup(KCQ, KCQ,  KCQ,  KCS,  S,  S,  S,  P)
    KCS.Ksetup(KCS, KCS,  KCS,  KCS,  P,  P,  P,  P)
    KQ .Ksetup(KAQ, KCQ,  KQ,   KS,   A,  A,  _,  A)
    KS .Ksetup(KAS, KCS,  KS,   KS,   A,  A,  _,  A)
    KX .Ksetup(KX,  KX,   KX,   KX,   P,  P,  P,  P)


    #
    #   End states
    #
    YA = state('ZA')      #       A = ends in '
    YB = state('ZB')      #       B = ends in ''
    YC = state('ZC')      #       C = ends in '''
    YD = state('ZD')      #       D = ends in \'
    YE = state('ZE')      #       E = ends in \''
    YF = state('ZF')      #       F = ends in \'''
    YG = state('ZG')      #       G = ends in \''''

    YK = state('ZK')      #       Z = ends in \
    YN = state('ZN')      #       N = normal

    YQ = state('ZQ')      #       Q = ends in "
    YR = state('ZR')      #       R = ends in ""
    YS = state('ZS')      #       S = ends in """
    YT = state('ZT')      #       T = ends in \"
    YU = state('ZU')      #       U = ends in \""
    YV = state('ZV')      #       V = ends in \"""
    YW = state('ZW')      #       V = ends in \""""


    def finish_portray(state):
        return portray_string


    ZA = PortrayStringState.ZA.__get__
    ZN = PortrayStringState.ZN.__get__
    ZO = PortrayStringState.ZO.__get__
    ZP = finish_portray
    ZQ = PortrayStringState.ZQ.__get__


    YA.end(YB, YK, YQ, 0, ZA, ZA)
    YB.end(YC, YK, YQ, 0, ZA, ZA)
    YC.end(YA, YK, YQ, 1, ZA, ZA)
    YD.end(YE, YK, YQ, 1, ZN, ZO)
    YE.end(YF, YK, YQ, 0, ZA, ZA)
    YF.end(YG, YK, YQ, 0, ZA, ZA)
    YG.end(YB, YK, YQ, 0, ZA, ZA)

    YK.end(YD, YN, YT, 0, ZP, ZP)
    YN.end(YA, YK, YQ, 0, ZN, ZO)

    YQ.end(YA, YK, YR, 0, ZQ, ZQ)
    YR.end(YA, YK, YS, 0, ZQ, ZQ)
    YS.end(YA, YK, YQ, 1, ZQ, ZQ)
    YT.end(YA, YK, YU, 1, ZN, ZO)
    YU.end(YA, YK, YV, 0, ZQ, ZQ)
    YV.end(YA, YK, YW, 0, ZQ, ZQ)
    YW.end(YA, YK, YR, 0, ZQ, ZQ)


    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_K_string(favorite, state, iterator, s):
        #line('portray_raw_K_string(%d, %s, %r, %r)', favorite, state, iterator, s)
        last = YK

        for c in iterator:
            old_state = state.name
            old_last  = state.name

            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                last  = YN
                state = state.N
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_backslash:
                last  = last .K
                state = state.K
                line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_double_quote:
                favorite += 1
                last  = last .Q
                state = state.Q
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_single_quote:
                favorite -= 1
                last  = last .A
                state = state.A
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            assert not a.is_printable

            return portray_string(s)

        #line('final of %r: %d, %s, %s', s, favorite, state.name, last.name)

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
                state = state.N
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_backslash:
                return portray_raw_K_string(favorite, state.K, iterator, s)


            if a.is_double_quote:
                favorite += 1
                state = state.Q
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_single_quote:
                favorite -= 1
                state = state.A
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            assert not a.is_printable

            return portray_string(s)

        #line('final: %d,%s,%s', favorite, state.name, last.name)

        if favorite >= 0:
            return state.ZN(s)

        return state.ZO(s)
