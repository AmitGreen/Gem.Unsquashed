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

            #
            #   Z
            #
            'is_triple',                #   Boolean
            'finish_apostrope',         #   Function -> String
            'finish_quotation_mark',    #   Function -> String
        ))


        def __init__(t, name):
            t.name = name


        def end(t, apostrophe, backslash, quotation_mark, is_triple, finish_apostrope, finish_quotation_mark):
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
            t.is_triple             = Boolean(is_triple)
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
    X    .setup(X,      X,      X,      X,      P,  P)

    #           '       \       N       "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_B  .setup(C_M,    A_K,    A_N,    AQ_Q,   Q,  Q)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   Q,  Q)

    #           '       \       N       "       N   O
    AQ_A .setup(AQ_B,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_B .setup(CQ_M,   AQ_K,   AQ_N,   AQ_Q,   S,  S)
    AQ_K .setup(AQ_N,   AQ_N,   AQ_N,   AQ_N,   P,  P)
    AQ_N .setup(AQ_A,   AQ_K,   AQ_N,   AQ_Q,   C,  S)
    AQ_Q .setup(AQ_A,   AQ_K,   AQ_N,   AQ_R,   C,  C)
    AQ_R .setup(AQ_A,   AQ_K,   AQ_N,   AS_M,   C,  C)

    #           '       \       N       "       N   O
    AS_A .setup(AS_B,   AS_K,   AS_M,   AS_M,   P,  P)
    AS_B .setup(X,      AS_K,   AS_M,   AS_M,   P,  P)
    AS_K .setup(AS_M,   AS_M,   AS_M,   AS_M,   P,  P)
    AS_M .setup(AS_A,   AS_K,   AS_M,   AS_M,   C,  C)

    #           '       \       N       "       N   O
    C_K  .setup(C_M,    C_M,    C_M,    C_M,    P,  P)
    C_M  .setup(C_M,    C_K,    C_M,    CQ_Q,   Q,  Q)

    #           '       \       N       "       N   O
    CQ_K .setup(CQ_M,   CQ_M,   CQ_M,   CQ_M,   P,  P)
    CQ_M .setup(CQ_M,   CQ_K,   CQ_M,   CQ_Q,   S,  S)
    CQ_Q .setup(CQ_M,   CQ_K,   CQ_M,   CQ_R,   P,  P)
    CQ_R .setup(CQ_M,   CQ_K,   CQ_M,   X,      P,  P)

    #           '       \       N       "       N   O
    N_K  .setup(N_N,    N_N,    N_N,    N_N,    P,  P)
    N_N  .setup(A_A,    N_K,    N_N,    Q_Q,    A,  Q)

    #           '       \       N       "       N   O
    Q_K  .setup(Q_N,    Q_N,    Q_N,    Q_N,    P,  P)
    Q_N  .setup(AQ_A,   Q_K,    Q_N,    Q_Q,    A,  A)
    Q_Q  .setup(AQ_A,   Q_K,    Q_N,    Q_R,    A,  A)
    Q_R  .setup(AQ_A,   Q_K,    Q_N,    S_M,    A,  A)

    #           '       \       N       "       N   O
    S_K  .setup(S_M,    S_M,    S_M,    S_M,    P,  P)
    S_M  .setup(AS_A,   S_M,    S_M,    S_M,    A,  A)


    #
    #   K States
    #
    K      = state('K')         #   Normal
    KA     = state('KA')        #   Has '
    KAQ    = state('KAQ')       #   Has ' & "
    KAS    = state('KAS')       #   Has ' & """
    KAT    = state('KAT')       #   Has ' & \"""
    KC     = state('KC')        #   Has '''
    KCQ    = state('KCQ')       #   Has ''' & "
    KCS    = state('KCS')       #   Has ''' & """
    KCT    = state('KCT')       #   Has ''' & \"""
    KF     = state('KF')        #   Has \'''
    KFQ    = state('KFQ')       #   Has \''' & "
    KFS    = state('KFS')       #   Has \''' & """
    KFT    = state('KFT')       #   Has \''' & \"""
    KQ     = state('KQ')        #   Has "
    KS     = state('KQ')        #   Has """
    KT     = state('KT')        #   Has \"""
    KX     = state('KX')        #   Has unprintable

    #          '    '''   \'''  "     """   \"""  N   O   '   "
    K  .Ksetup(KA,  KC,   KF,   KQ,   KS,   KT,   Q,  Q,  _,  _)
    KA .Ksetup(KA,  KC,   KF,   KAQ,  KAS,  KAT,  Q,  Q,  Q,  _)
    KAQ.Ksetup(KAQ, KCQ,  KFQ,  KAQ,  KAS,  KAT,  C,  S,  S,  C)
    KAS.Ksetup(KAS, KCS,  KFS,  KAS,  KAS,  KAS,  C,  C,  P,  C)
    KAT.Ksetup(KAT, KCT,  KFT,  KAT,  KAS,  KAT,  C,  S,  S,  C)
    KC .Ksetup(KC,  KC,   KC,   KCQ,  KCS,  KCT,  Q,  Q,  Q,  _)
    KCQ.Ksetup(KCQ, KCQ,  KCQ,  KCQ,  KCS,  KCT,  S,  S,  S,  P)
    KCS.Ksetup(KCS, KCS,  KCS,  KCS,  KCS,  KCS,  P,  P,  P,  P)
    KCT.Ksetup(KCT, KCT,  KCT,  KCT,  KCS,  KCT,  S,  S,  S,  P)
    KF .Ksetup(KF,  KC,   KF,   KFQ,  KFS,  KFT,  Q,  Q,  Q,  _)
    KFQ.Ksetup(KFQ, KCQ,  KFQ,  KFQ,  KFS,  KFT,  C,  S,  S,  C)
    KFS.Ksetup(KFS, KCS,  KFS,  KFS,  KFS,  KFS,  C,  C,  P,  C)
    KFT.Ksetup(KFT, KCT,  KFT,  KFT,  KFS,  KFT,  C,  S,  S,  C)
    KQ .Ksetup(KAQ, KCQ,  KFQ,  KQ,   KS,   KT,   A,  A,  _,  A)
    KS .Ksetup(KAS, KCS,  KFS,  KS,   KS,   KS,   A,  A,  _,  A)
    KT .Ksetup(KAT, KCT,  KFT,  KT,   KS,   KT,   A,  A,  _,  A)
    KX .Ksetup(KX,  KX,   KX,   KX,   KX,   KX,   P,  P,  P,  P)

    #
    #   End states
    #
    ZA = state('ZA')      #       A = ends in '
    ZB = state('ZB')      #       B = ends in ''
    ZC = state('ZC')      #       C = ends in '''
    ZD = state('ZD')      #       D = ends in \'
    ZE = state('ZE')      #       E = ends in \''
    ZF = state('ZF')      #       F = ends in \'''
    ZG = state('ZG')      #       G = ends in \''''

    ZK = state('ZK')      #       Z = ends in \
    ZN = state('ZN')      #       N = normal

    ZQ = state('ZQ')      #       Q = ends in "
    ZR = state('ZR')      #       R = ends in ""
    ZS = state('ZS')      #       S = ends in """
    ZT = state('ZT')      #       T = ends in \"
    ZU = state('ZU')      #       U = ends in \""
    ZV = state('ZV')      #       V = ends in \"""
    ZW = state('ZW')      #       V = ends in \""""


    finish_apostrope      = PortrayStringState.finish_apostrope     .__get__
    finish_normal         = PortrayStringState.finish_normal        .__get__
    finish_other          = PortrayStringState.finish_other         .__get__
    finish_quotation_mark = PortrayStringState.finish_quotation_mark.__get__


    def finish_portray(state):
        return portray_string


    ZA.end(ZB, ZK, ZQ, 0, finish_apostrope,      finish_apostrope)
    ZB.end(ZC, ZK, ZQ, 0, finish_apostrope,      finish_apostrope)
    ZC.end(ZA, ZK, ZQ, 1, finish_apostrope,      finish_apostrope)
    ZD.end(ZE, ZK, ZQ, 1, finish_normal,         finish_other)
    ZE.end(ZF, ZK, ZQ, 0, finish_apostrope,      finish_apostrope)
    ZF.end(ZG, ZK, ZQ, 0, finish_apostrope,      finish_apostrope)
    ZG.end(ZB, ZK, ZQ, 0, finish_apostrope,      finish_apostrope)

    ZK.end(ZD, ZN, ZT, 0, finish_portray,        finish_portray)
    ZN.end(ZA, ZK, ZQ, 0, finish_normal,         finish_other)

    ZQ.end(ZA, ZK, ZR, 0, finish_quotation_mark, finish_quotation_mark)
    ZR.end(ZA, ZK, ZS, 0, finish_quotation_mark, finish_quotation_mark)
    ZS.end(ZA, ZK, ZQ, 1, finish_quotation_mark, finish_quotation_mark)
    ZT.end(ZA, ZK, ZU, 1, finish_quotation_mark, finish_quotation_mark)
    ZU.end(ZA, ZK, ZV, 0, finish_quotation_mark, finish_quotation_mark)
    ZV.end(ZA, ZK, ZW, 0, finish_quotation_mark, finish_quotation_mark)
    ZW.end(ZA, ZK, ZR, 0, finish_quotation_mark, finish_quotation_mark)


    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_K_string(favorite, state, iterator, s):
        #line('portray_raw_K_string(%d, %s, %r, %r)', favorite, state, iterator, s)
        last = ZK

        for c in iterator:
            old_state = state.name
            old_last  = state.name

            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                last  = ZN
                state = state.normal
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_backslash:
                last  = last .backslash
                state = state.backslash
                line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_double_quote:
                favorite += 1
                last  = last .quotation_mark
                state = state.quotation_mark
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            if a.is_single_quote:
                favorite -= 1
                last  = last .apostrophe
                state = state.apostrophe
                #line('%r: %s => %s; %s => %s', c,  old_state, state.name, old_last, last.name)
                continue

            assert not a.is_printable

            return portray_string(s)

        line('final of %r: %d, %s, %s', s, favorite, state.name, last.name)

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
