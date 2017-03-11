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
    X_A  = state('X_A')
    X_B  = state('X_B')
    X_C  = state('X_C')
    X_N  = state('X_N')
    X_Q  = state('X_Q')
    X_R  = state('X_R')
    X_S  = state('X_S')

    A_A  = state('A_A')       #   Has '; ends in '
    A_B  = state('A_B')       #   Has '; ends in ''
    A_D  = state('A_D')       #   Has '; ends in \'
    A_E  = state('A_E')       #   Has '; ends in \''
    A_F  = state('A_F')       #   Has '; ends in \'''
    A_K  = state('A_K')       #   Has '; ends in \
    A_N  = state('A_N')       #   Has '

    AQ_A = state('AQ_A')      #   Has ' & "; ends in '
    AQ_B = state('AQ_B')      #   Has ' & "; ends in ''
    AQ_D = state('AQ_D')      #   Has ' & "; ends in \'
    AQ_E = state('AQ_E')      #   Has ' & "; ends in \''
    AQ_F = state('AQ_F')      #   Has ' & "; ends in \'''
    AQ_K = state('AQ_K')      #   Has ' & "; ends in \
    AQ_N = state('AQ_N')      #   Has ' & "
    AQ_Q = state('AQ_Q')      #   Has ' & "; ends in "
    AQ_R = state('AQ_R')      #   Has ' & "; ends in ""
    AQ_T = state('AQ_T')      #   Has ' & "; ends in \"
    AQ_U = state('AQ_U')      #   Has ' & "; ends in \""
    AQ_V = state('AQ_V')      #   Has ' & "; ends in \"""

    AS_A = state('AS_A')      #   Has ' & """; ends in '
    AS_B = state('AS_B')      #   Has ' & """; ends in ''
    AS_D = state('AS_D')      #   Has ' & """; ends in \'
    AS_E = state('AS_E')      #   Has ' & """; ends in \''
    AS_F = state('AS_F')      #   Has ' & """; ends in \'''
    AS_K = state('AS_K')      #   Has ' & """; ends in \
    AS_N = state('AS_N')      #   Has ' & """
    AS_Q = state('AS_Q')      #   Has ' & """; ends in "
    AS_R = state('AS_R')      #   Has ' & """; ends in ""
    AS_S = state('AS_S')      #   Has ' & """; ends in """

    C_A  = state('C_A')       #   Has '''; ends in '
    C_B  = state('C_B')       #   Has '''; ends in ''
    C_C  = state('C_C')       #   Has '''; ends in '''
    C_K  = state('C_K')       #   Has '''; ends in \
    C_N  = state('C_N')       #   Has '''
    C_T  = state('C_T')       #   Has '''; ends in \"

    CQ_A = state('CQ_A')      #   Has ''' & "; ends in '
    CQ_B = state('CQ_B')      #   Has ''' & "; ends in ''
    CQ_C = state('CQ_C')      #   Has ''' & "; ends in '''
    CQ_K = state('CQ_K')      #   Has ''' & "; ends in \
    CQ_N = state('CQ_N')      #   Has ''' & "
    CQ_Q = state('CQ_Q')      #   Has ''' & "; ends in "
    CQ_R = state('CQ_R')      #   Has ''' & "; ends in ""
    CQ_T = state('CQ_R')      #   Has ''' & "; ends in \"
    CQ_U = state('CQ_R')      #   Has ''' & "; ends in \""
    CQ_V = state('CQ_R')      #   Has ''' & "; ends in \"""

    N_K  = state('N_K')       #   normal; ends in \
    N_N  = state('N_N')       #   totally normal, nothing to see here

    Q_K  = state('Q_K')       #   Has "; ends in \
    Q_N  = state('Q_N')       #   Has "
    Q_Q  = state('Q_Q')       #   Has "; ends in "
    Q_R  = state('Q_R')       #   Has "; ends in " in ""

    S_K  = state('S_K')       #   Has """: ends in \
    S_M  = state('S_M')       #   Has """; might end in " or ""


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
    X_A  .setup(X_B,    X_N,    X_N,    X_Q,    P,  P)
    X_B  .setup(X_C,    X_N,    X_N,    X_Q,    P,  P)
    X_C  .setup(X_A,    X_N,    X_N,    X_Q,    P,  P)
    X_N  .setup(X_A,    X_N,    X_N,    X_Q,    P,  P)
    X_Q  .setup(X_A,    X_N,    X_N,    X_R,    P,  P)
    X_R  .setup(X_A,    X_N,    X_N,    X_S,    P,  P)
    X_S  .setup(X_A,    X_N,    X_N,    X_Q,    P,  P)

    #           '       \       N       "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_B  .setup(C_C,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_D  .setup(A_E,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_E  .setup(A_F,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_F  .setup(C_A,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)

    #           '       \       N       "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_B .setup(CQ_C,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_D .setup(AQ_E,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_E .setup(AQ_F,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_F .setup(CQ_A,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_K .setup(AQ_D,   AQ_N,   AQ_N,   AQ_T,   P,  P)
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_S,   C,  C)
    AQ_T .setup(AQ_A,   AQ_K,   AQ_N,   AQ_U,   C,  S)
    AQ_U .setup(AQ_A,   AQ_K,   AQ_N,   AQ_V,   C,  C)
    AQ_V .setup(AQ_A,   AQ_K,   AQ_N,   AS_Q,   C,  C)

    #           '       \       N       "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_N,   AS_Q,   P,  P)
    AS_B .setup(X_C,    AS_K,   AS_N,   AS_Q,   P,  P)
    AS_D .setup(AS_E,   AS_K,   AS_N,   AS_Q,   C,  C)
    AS_E .setup(AS_F,   AS_K,   AS_N,   AS_Q,   P,  P)
    AS_F .setup(X_A,    AS_K,   AS_N,   AS_Q,   P,  P)
    AS_K .setup(AS_D,   AS_N,   AS_N,   AS_Q,   P,  P)
    AS_N .setup(AS_A,   AS_K,   AS_N,   AS_Q,   C,  C)
    AS_Q .setup(AS_A,   AS_K,   AS_N,   AS_R,   C,  C)
    AS_R .setup(AS_A,   AS_K,   AS_N,   AS_S,   C,  C)
    AS_S .setup(AS_A,   AS_K,   AS_N,   AS_Q,   C,  C)

    #           '       \       N       "       N   O
    C_A  .setup(C_B,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_B  .setup(C_C,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_C  .setup(C_A,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_K  .setup(C_A,    C_N,    C_N,    C_T,    P,  P)
    C_N  .setup(C_A,    C_K,    C_N,    CQ_Q,   Q,  Q)
    C_T  .setup(C_A,    C_K,    C_N,    CQ_U,   Q,  Q)

    #           '       \       N       "       N   O
    CQ_A .setup(CQ_B,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_B .setup(CQ_C,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_C .setup(CQ_A,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_K .setup(CQ_A,   CQ_N,   CQ_N,   CQ_U,   P,  P)
    CQ_N .setup(CQ_A,   CQ_K,   CQ_N,   CQ_Q,   S,  S)
    CQ_Q .setup(CQ_A,   CQ_K,   CQ_N,   CQ_R,   P,  P)
    CQ_R .setup(CQ_A,   CQ_K,   CQ_N,   X_Q,    P,  P)
    CQ_T .setup(CQ_A,   CQ_K,   CQ_N,   CQ_U,   S,  S)
    CQ_U .setup(CQ_A,   CQ_K,   CQ_N,   CQ_V,   P,  P)
    CQ_V .setup(CQ_A,   CQ_K,   CQ_N,   X_R,    P,  P)

    #           '       \       N       "       N   O
    N_K  .setup(N_N,    N_N,    N_N,    N_N,    P,  P)
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)

    #           '       \       N       "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_M,    A,  A)
    #Q_T
    #Q_U
    #Q_V

    #           '       \       N       "       N   O
    #S_A
    #S_B
    #S_C
    S_K  .setup(S_M,    S_M,    S_M,    S_M,    P,  P)
    S_M  .setup(AS_A,   S_M,    S_M,    S_M,    A,  A)
    #S_N


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
