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
        ))


        def __init__(t, name):
            t.name = name


        def setup(t, apostrophe, backslash, normal, quotation_mark, finish_normal, finish_other):
            t.apostrophe     = apostrophe
            t.backslash      = backslash
            t.normal         = normal
            t.quotation_mark = quotation_mark

            t.finish_normal = finish_normal
            t.finish_other  = finish_other


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
    #       M = normal -- might end in ", "", ', or ''
    #
    #       Q = "
    #       R = ""
    #       S = """
    #
    #       X = non-ascii
    #
    start  = state('start')
    X      = state('X')

    A_A    = state('A_A')       #   Has '; ends in '
    A_B    = state('A_B')       #   Has '; ends in ''
    A_K    = state('A_K')       #   Has '; ends in \
    A_N    = state('A_N')       #   Has '

    AQ_A   = state('AQ_A')      #   Has ' & "; ends in '
    AQ_B   = state('AQ_b')      #   Has ' & "; ends in ''
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

    K_K    = state('K_K')       #   Has \; ends in \
    K_N    = state('K_N')       #   Has \

    KQ_K   = state('KQ_K')      #   Has \ & "; ends in \
    KQ_N   = state('KQ_N')      #   Has \ & "
    KQ_Q   = state('KQ_Q')      #   Has \ & "; ends in "
    KQ_R   = state('KQ_R')      #   Has \ & "; ends in ""

    KS_K   = state('KS_K')      #   Has \ & """: ends in \
    KS_M   = state('KS_N')      #   Has \ & """; might end in " or ""

    N_N    = state('N_N')       #   totally normal, nothing to see here

    Q_N    = state('N_N')       #   Has "
    Q_Q    = state('N_N')       #   Has "; ends in "
    Q_R    = state('N_N')       #   Has "; ends in " in ""

    S_M    = state('N_N')       #   Has """; might end in " or ""


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
    start.setup(A_A,    K_K,    N_N,    Q_Q,    I,  _)
    X    .setup(X,      X,      X,      X,      P,  P)

    #           '       \       N_N     "       N   O
    A_A  .setup(A_B,    A_K,    A_N,    AQ_Q,   _,  Q)
    A_B  .setup(C_M,    A_K,    A_N,    AQ_Q,   _,  Q)
    A_K  .setup(A_N,    A_N,    A_N,    AQ_Q,   P,  P)
    A_N  .setup(A_A,    A_K,    A_N,    AQ_Q,   _,  Q)

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
    K_K  .setup(K_N,    K_N,    K_N,    K_N,    P,  P)
    K_N  .setup(A_A,    K_K,    K_N,    KQ_Q,   A,  Q)

    #           '       \       N_N     "       N   O
    KQ_K .setup(KQ_N,   KQ_N,   KQ_N,   KQ_N,   P,  P)
    KQ_N .setup(AQ_A,   KQ_K,   KQ_N,   KQ_Q,   A,  A)
    KQ_Q .setup(AQ_A,   KQ_K,   KQ_N,   KQ_R,   A,  A)
    KQ_R .setup(AQ_A,   KQ_K,   KQ_N,   KS_M,   A,  A)

    #           '       \       N_N     "       N   O
    KS_K .setup(KS_M,   KS_M,   KS_M,   KS_M,   P,  P)
    KS_M .setup(AS_A,   KS_K,   KS_M,   KS_M,   A,  A)

    #           '       \       N_N     "       N   O
    N_N  .setup(A_A,    K_K,    N_N,    Q_Q,    A,  _)

    #           '       \       N_N     "       N   O
    Q_N  .setup(AQ_A,   KQ_K,   Q_N,    Q_Q,    A,  _)
    Q_Q  .setup(AQ_A,   KQ_K,   Q_N,    Q_R,    A,  _)
    Q_R  .setup(AQ_A,   KQ_K,   Q_N,    S_M,    A,  _)

    #           '       \       N_N     "       N   O
    S_M  .setup(AS_A,   KS_M,   S_M,    S_M,    A,  _)


    del PortrayStringState.__init__, PortrayStringState.setup


    @export
    def portray_raw_K_string(favorite, state, iterator, s):
        for c in iterator:
            #old = state.name
            a = lookup_ascii(c, unknown_ascii)

            if a.is_portray_boring:
                state = state.normal
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

            if a.is_backslash:
                state = state.backslash
                #line('%s: %r, %s, %s', old, c, state.name, last.name)
                continue

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
            return portray_raw_K_string(0, K_K, iterator, s)

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
