#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.PortrayString')
def gem():
    require_gem('Gem.Ascii')
    require_gem('Gem.Exception')
    require_gem('Gem.StringIO')


    P = String.__repr__


    class PortrayStringState(Object):
        __slots__ = ((
            'A',                        #   PortrayStringState
            'K',                        #   PortrayStringState
            'N',                        #   PortrayStringState
            'Q',                        #   PortrayStringState

            'kc',                       #   Function -> String
            'ks',                       #   Function -> String

            'pc',                       #   Function -> String
            'ps',                       #   Function -> String

            'ra',                       #   Function -> String
            'rq',                       #   Function -> String


            #
            #   Tracking ''' & """ for normal portray
            #
            'favorite_3',               #   Integer
            'triple',                   #   Boolean
        ))


        if __debug__:
            __slots__ = ((
                'name',                 #   String
            )) + __slots__


        if __debug__:
            def __init__(t, name):
                t.name = name
        else:
            def __init__(t, name):
                pass


        if __debug__:
            def __repr__(t):
                return arrange('<PortrayStringState %s>', t.name)

                
        def setup(self, A, K, N, Q, t = 0, ra = 0, rq = 0, kc = 0, ks = 0, pc = 0, ps = 0, F3 = 0):
            assert (t is 0) or (t is 1)

            if ra is 0:
                assert rq is 0

                ra = P

            if rq is 0:
                rq = ra

            if kc is 0:
                assert ks is 0

                kc = P

            if ks is 0:
                ks = kc

            if pc is 0:
                assert ps is 0

                pc = P

            if ps is 0:
                ps = pc

            self.A = A
            self.K = K
            self.N = N
            self.Q = Q

            self.kc = (kc) or (P)
            self.ks = (ks) or (kc) or (P)

            self.pc = pc
            self.ps = (ps) or (pc)

            self.ra = ra
            self.rq = (rq) or (ra)

            self.favorite_3 = F3
            self.triple     = Boolean(t)


    state = PortrayStringState


    #
    #   states
    #
    #       A = '
    #       B = ''
    #       C = ''
    #
    #       K = \
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
    portray_inside_triple = {
                                A_B : 0,
                                C_A : intern_string(r"'"),
                                C_B : intern_string(r"'"),
                                C_C : intern_string(r"\'"),
                                C_N : 0,

                                Q_R : 0,
                                S_N : 0,
                                S_Q : intern_string(r'"'),
                                S_R : intern_string(r'"'),
                                S_S : intern_string(r'\"'),
                            }.__getitem__


    portray_last_inside_triple = {
                                     A_B : intern_string(r"'''"),
                                     C_A : intern_string(r"\''''"),
                                     C_B : intern_string(r"\''''"),
                                     C_C : intern_string(r"\''''"),
                                     C_N : intern_string(r"'''"),

                                     Q_R : intern_string(r'"""'),
                                     S_N : intern_string(r'"""'),
                                     S_Q : intern_string(r'\""""'),
                                     S_R : intern_string(r'\""""'),
                                     S_S : intern_string(r'\""""'),
                                 }.__getitem__


    def portray_backslash_string_with_triple_apostrophe(s):
        #line('KC: %r', s)

        f     = create_StringOutput()
        w     = f.write
        state = A_B

        w("'''")

        for c in s:
            a = lookup_ascii(c)

            if a is none:
                if state is not C_N:
                    if state is not A_B:
                        w(portray_inside_triple(state))

                    state = C_N

                w(portray(c)[1:-1])
                continue

            if a.is_apostrophe:
                previous = portray_inside_triple(state)

                if previous is not 0:
                    w(previous)

                state = state.A
                continue

            if state is not C_N:
                if state is not A_B:
                    w(portray_inside_triple(state))

                state = C_N

            w(a.portray)

        w(portray_last_inside_triple(state))

        return f.getvalue()


    def portray_backslash_string_with_triple_quotation_mark(s):
        #line('KS: %r', s)

        f     = create_StringOutput()
        w     = f.write
        state = Q_R

        w('"""')

        for c in s:
            a = lookup_ascii(c)

            if a is none:
                if state is not S_N:
                    if state is not Q_R:
                        w(portray_inside_triple(state))

                    state = S_N

                w(portray(c)[1:-1])
                continue

            if a.is_quotation_mark:
                previous = portray_inside_triple(state)

                if previous is not 0:
                    w(previous)

                state = state.Q
                continue

            if state is not S_N:
                if state is not Q_R:
                    w(portray_inside_triple(state))

                state = S_N

            w(a.portray)

        w(portray_last_inside_triple(state))

        return f.getvalue()


    def portray_raw_string_with_apostrophe(s):
        return "r'" + s + "'"


    def portray_raw_string_with_quotation_mark(s):
        return 'r"' + s + '"'


    def portray_raw_string_with_triple_apostrophe(s):
        return "r'''" + s + "'''"


    def portray_raw_string_with_triple_quotation_mark(s):
        return 'r"""' + s + '"""'


    def portray_string_with_triple_apostrophe(s):
        return "'''" + s + "'''"


    def portray_string_with_triple_quotation_mark(s):
        return '"""' + s + '"""'


    KC = portray_backslash_string_with_triple_apostrophe
    KS = portray_backslash_string_with_triple_quotation_mark

    PC = portray_string_with_triple_apostrophe
    PS = portray_string_with_triple_quotation_mark

    RA = portray_raw_string_with_apostrophe
    RC = portray_raw_string_with_triple_apostrophe
    RQ = portray_raw_string_with_quotation_mark
    RS = portray_raw_string_with_triple_quotation_mark

    _ = 0


    #           '     \     N     "
    A_A  .setup(A_B,  A_K,  A_N,  AQ_Q, _, RQ, _)                           #   Has '; ends in '
    A_B  .setup(C_C,  A_K,  A_N,  AQ_Q, _, RQ, _)                           #   Has '; ends in ''
    A_K  .setup(A_N,  A_N,  A_N,  A_N)                                      #   Has '; ends in \
    A_N  .setup(A_A,  A_K,  A_N,  AQ_Q, _, RQ, _)                           #   Has '

    #           '     \     N     "
    AQ_A .setup(AQ_B, AQ_K, AQ_N, AQ_Q, 1, RS, _,  KS, _,  KS, _)           #   Has ' & "; ends in '
    AQ_B .setup(CQ_C, AQ_K, AQ_N, AQ_Q, 1, RS, _,  KS, _,  KS, _)           #   Has ' & "; ends in ''
    AQ_K .setup(AQ_N, AQ_N, AQ_N, AQ_N, 1, _,  _,  KC, KS, PC, PS)          #   Has ' & "; ends in \
    AQ_N .setup(AQ_A, AQ_K, AQ_N, AQ_Q, 1, RC, RS, KC, KS, PC, PS)          #   Has ' & "
    AQ_Q .setup(AQ_A, AQ_K, AQ_N, AQ_R, 1, RC, _,  KC, _,  KC, _)           #   Has ' & "; ends in "
    AQ_R .setup(AQ_A, AQ_K, AQ_N, AS_S, 1, RC, _,  KC, _,  KC, _)           #   Has ' & "; ends in ""

    #           '     \     N     "
    AS_A .setup(AS_B, AS_K, AS_N, AS_Q, 1, _,  _,  KS, _,  KS, _)           #   Has ' & """; ends in '
    AS_B .setup(CS_C, AS_K, AS_N, AS_Q, 1, _,  _,  KS, _,  KS, _)           #   Has ' & """; ends in ''
    AS_K .setup(AS_N, AS_N, AS_N, AS_N, 1, _,  _,  KC, _,  PC, _)           #   Has ' & """; ends in \
    AS_N .setup(AS_A, AS_K, AS_N, AS_Q, 1, RC, _,  KC, _,  PC, _)           #   Has ' & """
    AS_Q .setup(AS_A, AS_K, AS_N, AS_R, 1, RC, _,  KC, _,  KC, _)           #   Has ' & """; ends in "
    AS_R .setup(AS_A, AS_K, AS_N, AS_S, 1, RC, _,  KC, _,  KC, _)           #   Has ' & """; ends in ""
    AS_S .setup(AS_A, AS_K, AS_N, AS_R, 1, RC, _,  KC, _,  KC, _,  F3 = 1)  #   Has ' & """; ends in """

    #           '     \     N     "
    C_A  .setup(C_B,  C_K,  C_N,  CQ_Q, _, RQ, _)                           #   Has '''; ends in '
    C_B  .setup(C_C,  C_K,  C_N,  CQ_Q, _, RQ, _)                           #   Has '''; ends in ''
    C_C  .setup(C_B,  C_K,  C_N,  CQ_Q, _, RQ, _,  F3 = -1)                 #   Has '''; ends in '''
    C_K  .setup(C_N,  C_N,  C_N,  C_N)                                      #   Has '''; ends in \
    C_N  .setup(C_A,  C_K,  C_N,  CQ_Q, _, RQ, _)                           #   Has '''

    #           '     \     N     "
    CQ_A .setup(CQ_B, CQ_K, CQ_N, CQ_Q, 1, RS, _,  KS, _,  PS, _)           #   Has ''' & "; ends in '
    CQ_B .setup(CQ_C, CQ_K, CQ_N, CQ_Q, 1, RS, _,  KS, _,  PS, _)           #   Has ''' & "; ends in ''
    CQ_C .setup(CQ_B, CQ_K, CQ_N, CQ_Q, 1, RS, _,  KS, _,  PS, _,  F3 = -1) #   Has ''' & "; ends in '''
    CQ_K .setup(CQ_N, CQ_N, CQ_N, CQ_N, 1, _,  _,  KS, _,  PS, _)           #   Has ''' & "; ends in \
    CQ_N .setup(CQ_A, CQ_K, CQ_N, CQ_Q, 1, RS, _,  KS, _,  PS, _)           #   Has ''' & "
    CQ_Q .setup(CQ_A, CQ_K, CQ_N, CQ_R, 1, _,  _,  KC, _,  KC, _)           #   Has ''' & "; ends in "
    CQ_R .setup(CQ_A, CQ_K, CQ_N, CS_S, 1, _,  _,  KC, _,  KC, _)           #   Has ''' & "; ends in ""

    #           '     \     N     
    CS_A .setup(CS_B, CS_N, CS_N, CS_Q, 1, _,  _,  KS, _,  KS, _)           #   Has ''' & """; ends in '
    CS_B .setup(CS_C, CS_N, CS_N, CS_Q, 1, _,  _,  KS, _,  KS, _)           #   Has ''' & """; ends in ''
    CS_C .setup(CS_B, CS_N, CS_N, CS_Q, 1, _,  _,  KS, _,  KS, _,  F3 = -1) #   Has ''' & """; ends in '''
    CS_N .setup(CS_A, CS_N, CS_N, CS_Q, 1, _,  _,  KC, KS, PC, PS)          #   Has ''' & """
    CS_Q .setup(CS_A, CS_N, CS_N, CS_R, 1, _,  _,  KC, _,  KC, _)           #   Has ''' & """; ends in "
    CS_R .setup(CS_A, CS_N, CS_N, CS_S, 1, _,  _,  KC, _,  KC, _)           #   Has ''' & """; ends in ""
    CS_S .setup(CS_A, CS_N, CS_N, CS_R, 1, _,  _,  KC, _,  KC, _,  F3 = 1)  #   Has ''' & """; ends in """

    #           '     \     N     "
    N_K  .setup(N_N,  N_N,  N_N,  N_N)                                      #   normal; ends in \
    N_N  .setup(A_A,  N_K,  N_N,  Q_Q,  _, RA, RQ)                          #   normal

    #           '     \     N     "
    Q_K  .setup(Q_N,  Q_N,  Q_N,  Q_N)                                      #   Has "; ends in \
    Q_N  .setup(AQ_A, Q_K,  Q_N,  Q_Q,  _, RA, _)                           #   Has "
    Q_Q  .setup(AQ_A, Q_K,  Q_N,  Q_R,  _, RA, _)                           #   Has "; ends in "
    Q_R  .setup(AQ_A, Q_K,  Q_N,  S_S,  _, RA, _)                           #   Has "; ends in ""

    #           '     \     N     "
    S_K  .setup(S_N,  S_N,  S_N,  S_N)                                      #   Has """: ends in \
    S_N  .setup(AS_A, S_K,  S_N,  S_Q,  _, RA, _)                           #   Has """
    S_Q  .setup(AS_A, S_K,  S_N,  S_R,  _, RA, _)                           #   Has """; ends in "
    S_R  .setup(AS_A, S_K,  S_N,  S_S,  _, RA, _)                           #   Has """; ends in ""
    S_S  .setup(AS_A, S_K,  S_N,  S_R,  _, RA, _,  F3 = 1)                  #   Has """; ends in """


    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_string(s):
        iterator = iterate(s)

        #
        #   Simple case
        #
        for c in iterator:
            a = lookup_ascii(c, unknown_ascii)

            #line('c: %r, a: %r', c, a)

            if not a.is_portray_boring:
                break
        else:
            #line('portray_raw_string(%r): simple', s)

            return "r'" + s + "'"

        #
        #   Complex case
        #
        #line('portray_raw_string(%r): %s', s, a)

        if a.is_backslash:
            #line('  %r: backslash: %s, %s', c, N_K.name, N_N.name)

            backslash = 7
            lemon     = favorite  = 0
            raw_state = N_K
            state     = N_N
        else:
            backslash = 0

            if a.is_quotation_mark:
                #line('  %r: %s, %s', c, Q_Q.name, Q_Q.name)

                favorite = 1
                lemon    = 0
                raw_state = state = Q_Q
            elif a.is_apostrophe:
                #line('  %r: %s, %s', c, A_A.name, A_A.name)

                favorite  = -1
                lemon     = 0
                raw_state = state = A_A
            else:
                #line('  %r: lemon: %s, %s', c, N_N.name, N_N.name)

                favorite  = 0
                lemon     = 7
                raw_state = state = N_N

        favorite_3 = 0

        for c in iterator:
            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                #line('  %r: %s => %s, %s => %s', c, raw_state.name, raw_state.N.name, state.name, state.N.name)

                raw_state = raw_state.N
                state     = state.N

                continue

            if a.is_backslash:
                #line('  %r: backslash: %s => %s, %s => %s', c, raw_state.name, raw_state.K.name, state.name, state.N.name)

                backslash = 7
                raw_state = raw_state.K
                state     = state.N
                continue

            if a.is_quotation_mark:
                #line('  %r: %s => %s, %s => %s', c, raw_state.name, raw_state.Q.name, state.name, state.Q.name)

                raw_state   = raw_state.Q
                state       = state.Q
                favorite   += 1
                favorite_3 += state.favorite_3
                continue

            if a.is_apostrophe:
                #line('  %r: %s => %s, %s => %s', c, raw_state.name, raw_state.A.name, state.name, state.A.name)

                raw_state   = raw_state.A
                state       = state.A
                favorite   -= 1
                favorite_3 += state.favorite_3
                continue

            assert not a.is_printable


            #line('  %r: lemon: %s => %s, %s => %s', c, raw_state.name, raw_state.N.name, state.name, state.N.name)

            lemon = 7
            raw_state = raw_state.N
            state     = raw_state.N

        #line('  final %r: %d/%d/%s/%s, %s, %s', s, favorite, favorite_3, backslash, lemon, raw_state.name, state.name)

        if lemon is 7:
            if favorite_3 >= 0:
                #if raw_state is not state:
                #    #line('  %r: %s/%s: lemon, kc', s, raw_state.name, state.name)

                #line('  %s: lemon, kc', state.name)
                return state.kc(s)

            #if raw_state is not state:
            #    #line('  %r: %s/%s: lemon, ks', s, raw_state.name, state.name)

            #line('  %s: lemon, ks', state.name)
            return state.ks(s)

        if raw_state.ra is P:
            if backslash is 7:
                if favorite_3 >= 0:
                    #if raw_state is not state:
                    #    #line('  %r: %s/%s: P, backslash, kc', s, raw_state.name, state.name)

                    #line('  %s: P, backslash, kc', state.name)
                    return state.kc(s)

                #if raw_state is not state:
                #    #line('  %r: %s/%s: P, backslash, ks', s, raw_state.name, state.name)

                #line('  %s: P, backslash, ks', state.name)
                return state.ks(s)

            if favorite_3 >= 0:
                #line('  %s: P, pc', state.name)
                return state.pc(s)

            #line('  %s: P, ps', state.name)
            return state.ps(s)

        if favorite >= 0:
            #line('  %s: ra', raw_state.name)
            return raw_state.ra(s)

        #line('  %s: rq', raw_state.name)
        return raw_state.rq(s)


    export(
        'N_N',  N_N,
    )
