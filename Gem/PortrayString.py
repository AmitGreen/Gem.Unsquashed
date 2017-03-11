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
            'F',                        #   PortrayStringState
            'S',                        #   PortrayStringState
            'V',                        #   PortrayStringState

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


        def Ksetup(t, A, C, F, Q, S, V, ZN, ZO, ZA, ZQ):
            t.A = A
            #
            #   K   Not applicable
            #   N   Not applicable
            #
            t.Q = Q

            t.C = C
            t.F = F
            t.S = S
            t.V = V

            t.ZN = ZN
            t.ZO = ZO

            t.ZA = ZA
            t.ZQ = ZQ


        def setup(t, A, K, N, Q, ZN, ZO, V):
            t.A = A
            t.K = K
            t.N = N
            t.Q = Q

            t.ZN = ZN
            t.ZO = ZO

            #
            #   C     Not applicable
            #   F     Not applicable
            #   S     Not applicable
            #   V     Not applicable
            #   ZA    Not applicable
            #   ZQ    Not applicable
            #

            t.V = V


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
    X    = state('X')

    A_A  = state('A_A')       #   Has '; ends in '
    A_B  = state('A_B')       #   Has '; ends in ''
    A_K  = state('A_K')       #   Has '; ends in \
    A_N  = state('A_N')       #   Has '

    AQ_A = state('AQ_A')      #   Has ' & "; ends in '
    AQ_B = state('AQ_B')      #   Has ' & "; ends in ''
    AQ_K = state('AQ_K')      #   Has ' & "; ends in \
    AQ_N = state('AQ_N')      #   Has ' & "
    AQ_Q = state('AQ_Q')      #   Has ' & "; ends in "
    AQ_R = state('AQ_R')      #   Has ' & "; ends in ""

    AS_A = state('AS_A')      #   Has ' & """; ends in '
    AS_B = state('AS_B')      #   Has ' & """; ends in ''
    AS_K = state('AS_K')      #   Has ' & """; ends in \
    AS_M = state('AS_M')      #   Has ' & """; might end in " or ""

    C_K  = state('C_K')       #   Has '''; ends in \
    C_M  = state('C_M')       #   Has '''; might end in ' or ""

    CQ_K = state('CQ_K')      #   Has ''' & "; ends in \
    CQ_M = state('CQ_M')      #   Has ''' & "; might end in ' or ''
    CQ_Q = state('CQ_Q')      #   Has ''' & "; ends in "
    CQ_R = state('CQ_R')      #   Has ''' & "; ends in ""

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
    KAV = state('KAV')       #   Has ' & \"""
    KC  = state('KC')        #   Has '''
    KCQ = state('KCQ')       #   Has ''' & "
    KCS = state('KCS')       #   Has ''' & """
    KCV = state('KCV')       #   Has ''' & \"""
    KF  = state('KF')        #   Has \'''
    KFQ = state('KFQ')       #   Has \''' & "
    KFS = state('KFS')       #   Has \''' & """
    KFV = state('KFV')       #   Has \''' & \"""
    KQ  = state('KQ')        #   Has "
    KS  = state('KQ')        #   Has """
    KV  = state('KV')        #   Has \"""
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


    K   = state('K')         #   Normal
    KA  = state('KA')        #   Has '
    KAQ = state('KAQ')       #   Has ' & "
    KAS = state('KAS')       #   Has ' & """
    KAV = state('KAV')       #   Has ' & \"""
    KC  = state('KC')        #   Has '''
    KCQ = state('KCQ')       #   Has ''' & "
    KCS = state('KCS')       #   Has ''' & """
    KCV = state('KCV')       #   Has ''' & \"""
    KF  = state('KF')        #   Has \'''
    KFQ = state('KFQ')       #   Has \''' & "
    KFS = state('KFS')       #   Has \''' & """
    KFV = state('KFV')       #   Has \''' & \"""
    KQ  = state('KQ')        #   Has "
    KS  = state('KQ')        #   Has """
    KV  = state('KV')        #   Has \"""
    KX  = state('KX')        #   Has unprintable

    #           '       \       N       "       N   O   \
    X    .setup(X,      X,      X,      X,      P,  P,  KX)

    #           '       \       N       "       N   O   \
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q,  KA)
    A_B  .setup(C_M,    A_K,    A_N,    AQ_Q,   Q,  Q,  KA)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P,  KA)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q,  KA)

    #           '       \       N       "       N   O   \
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S,  KAQ)
    AQ_B .setup(CQ_M,   AQ_K,   AQ_N,   AQ_Q,   S,  S,  KAQ)
    AQ_K .setup(AQ_N,   AQ_N,   AQ_N,   AQ_N,   P,  P,  KAQ)
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S,  KAQ)
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C,  KAQ)
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_M,   C,  C,  KAQ)

    #           '       \       N       "       N   O   \
    AS_A .setup(AS_B,   AS_K,   AS_M,   AS_M,   P,  P,  KAS)
    AS_B .setup(X,      AS_K,   AS_M,   AS_M,   P,  P,  KAS)
    AS_K .setup(AS_M,   AS_M,   AS_M,   AS_M,   P,  P,  KAS)
    AS_M .setup(AS_A,   AS_K,   AS_M,   AS_M,   C,  C,  KAS)

    #           '       \       N       "       N   O   \
    C_K  .setup(C_M,    C_M,    C_M,    C_M,    P,  P,  KC)
    C_M  .setup(C_M,    C_K,    C_M,    CQ_Q,   Q,  Q,  KC)

    #           '       \       N       "       N   O   \
    CQ_K .setup(CQ_M,   CQ_M,   CQ_M,   CQ_M,   P,  P,  KCQ)
    CQ_M .setup(CQ_M,   CQ_K,   CQ_M,   CQ_Q,   S,  S,  KCQ)
    CQ_Q .setup(CQ_M,   CQ_K,   CQ_M,   CQ_R,   P,  P,  KCQ)
    CQ_R .setup(CQ_M,   CQ_K,   CQ_M,   X,      P,  P,  KCQ)

    #           '       \       N       "       N   O   \
    N_K  .setup(N_N,    N_N,    N_N,    N_N,    P,  P,  K)
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q,  K)

    #           '       \       N       "       N   O   \
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P,  KQ)
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A,  KQ)
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A,  KQ)
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_M,    A,  A,  KQ)

    #           '       \       N       "       N   O
    S_K  .setup(S_M,    S_M,    S_M,    S_M,    P,  P,  KS)
    S_M  .setup(AS_A,   S_M,    S_M,    S_M,    A,  A,  KS)


    #
    #   Backslash States
    #
    #          '    '''   \'''  "     """   \"""  N   O   '   "
    K  .Ksetup(KA,  KC,   KF,   KQ,   KS,   KV,   A,  Q,  _,  _)
    KA .Ksetup(KA,  KC,   KF,   KAQ,  KAS,  KAV,  Q,  Q,  Q,  _)
    KAQ.Ksetup(KAQ, KCQ,  KFQ,  KAQ,  KAS,  KAV,  C,  S,  S,  C)
    KAS.Ksetup(KAS, KCS,  KFS,  KAS,  KAS,  KAS,  C,  C,  P,  C)
    KAV.Ksetup(KAV, KCV,  KFV,  KAV,  KAS,  KAV,  C,  S,  S,  C)
    KC .Ksetup(KC,  KC,   KC,   KCQ,  KCS,  KCV,  Q,  Q,  Q,  _)
    KCQ.Ksetup(KCQ, KCQ,  KCQ,  KCQ,  KCS,  KCV,  S,  S,  S,  P)
    KCS.Ksetup(KCS, KCS,  KCS,  KCS,  KCS,  KCS,  P,  P,  P,  P)
    KCV.Ksetup(KCV, KCV,  KCV,  KCV,  KCS,  KCV,  S,  S,  S,  P)
    KF .Ksetup(KF,  KC,   KF,   KFQ,  KFS,  KFV,  Q,  Q,  Q,  _)
    KFQ.Ksetup(KFQ, KCQ,  KFQ,  KFQ,  KFS,  KFV,  C,  S,  S,  C)
    KFS.Ksetup(KFS, KCS,  KFS,  KFS,  KFS,  KFS,  C,  C,  P,  C)
    KFV.Ksetup(KFV, KCV,  KFV,  KFV,  KFS,  KFV,  C,  S,  S,  C)
    KQ .Ksetup(KAQ, KCQ,  KFQ,  KQ,   KS,   KV,   A,  A,  _,  A)
    KS .Ksetup(KAS, KCS,  KFS,  KS,   KS,   KS,   A,  A,  _,  A)
    KV .Ksetup(KAV, KCV,  KFV,  KV,   KS,   KV,   A,  A,  _,  A)
    KX .Ksetup(KX,  KX,   KX,   KX,   KX,   KX,   P,  P,  P,  P)

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

        line('final of %r: %d, %s, %s', s, favorite, state.name, last.name)

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
