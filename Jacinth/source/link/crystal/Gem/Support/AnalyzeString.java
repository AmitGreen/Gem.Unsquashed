//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AsciiTable;
import link.crystal.Gem.Support.EphemeralStringState;
import link.crystal.Gem.Support.OverallStringState;


//
//  How to combine OverallStringState with EphemeralStringState.
//
//      1.  Do we want a raw string?  (And can we do a raw string?)
//
//          1A. Do we prefer Apostrophe?
//
//                  Then use the `OverallStringState.RA` to choose either:
//
//                      `EphemeralStringState.RA` OR
//                      `EphemeralStringState.RQ`
//
//                  Normally it will pick the `.RA` member;
//
//                      Only Exception:
//
//                          When the string starts with an apostrophe `'`, then it will pick the `.RQ` member
//                          (so the string is quoted with `"` if possible).
//
//          1B.  Do we prefer quotation marks?
//
//                  Then use the `OverallStringState.RQ` to choose either:
//
//                      `EphemeralStringState.RA` OR
//                      `EphemeralStringState.RQ`
//
//                  Normally it will pick the `.RA` member;
//
//                      Only Exception:
//
//                          When the string starts with a quotation mark `"`, then it will pick the `.RA` member
//                          (so the string is quoted with `'` if possible).
//                              
//      2.  Are we going to do a normal string?
//
//          2A. Do we prefer Apostrophe?
//
//                  Then use `OverallStringState.PA` to choose either:
//
//                      `EphemeralStringState.PC` OR
//                      `EphemeralStringState.PS` OR
//
//                          -- OR -- (if there is a backslash in the string)
//
//                      `EphemeralStringState.KC` OR
//                      `EphemeralStringState.KS` OR
//
//                  Normally it will pick the `.PC` or `.KC` member;
//
//                      Only Exception:
//
//                          When the string starts with an apostrophe `'`, then it will pick the `.PS` or `.KS` member
//                          (so the string is quoted with `"` if possible).
//
//          2A. Do we prefer Quotation Mark?
//
//                  Then use `OverallStringState.PQ` to choose either:
//
//                      `EphemeralStringState.PC` OR
//                      `EphemeralStringState.PS` OR
//
//                          -- OR -- (if there is a backslash in the string)
//
//                      `EphemeralStringState.KC` OR
//                      `EphemeralStringState.KS` OR
//
//                  Normally it will pick the `.PS` or `.KS` member;
//
//                      Only Exception:
//
//                          When the string starts with a quotation mark `"`, then it will pick the `.PC` or `.KC` member
//                          (so the string is quoted with `'` if possible).
//
public abstract class   AnalyzeString
    extends             Gem_Object//<Inspection>
{
    //
    //  Array indexes
    //
    public static final int                     RA =  1;        //  Raw String with '
    public static final int                     RQ =  2;        //  Raw String with "
    public static final int                     KC =  3;        //  Backslash & '''
    public static final int                     KS =  4;        //  Backslash & """
    public static final int                     PC =  5;        //  Normal & '''
    public static final int                     PS =  6;        //  Normal & """

    public static final int                     KA =  7;        //  Backslash & '
    public static final int                     KQ =  8;        //  Backslash & "
    public static final int                     PA =  9;        //  Normal & '
    public static final int                     PQ = 10;        //  Normal & "
    public static final int                     RC = 11;        //  Raw String with '''
    public static final int                     RS = 12;        //  Raw String with """

    public static final String[]                index_names = new String[] {
            "0",
            "RA", "RQ", "KC", "KS", "PC", "PS",
            "KA", "KQ", "PA", "PQ", "RC", "RS",
        };


    //
    //   States (overall)
    //
    //       E = Empty
    //       K = Backslash
    //       L = Lemon (Unprintable)
    //       N = Normal
    //       T = Starts with "
    //       U = Starts with '
    //
    private static final OverallStringState     E  = OverallStringState.create("E");
    private static final OverallStringState     K  = OverallStringState.create("K");
    private static final OverallStringState     L  = OverallStringState.create("L");
    private static final OverallStringState     N  = OverallStringState.create("N");
    private static final OverallStringState     TK = OverallStringState.create("TK");
    private static final OverallStringState     TL = OverallStringState.create("TL");
    private static final OverallStringState     T  = OverallStringState.create("T");        //  Means: TN
    private static final OverallStringState     UK = OverallStringState.create("UK");
    private static final OverallStringState     UL = OverallStringState.create("UL");
    private static final OverallStringState     U  = OverallStringState.create("U");        //  Means: UN


    //
    //  States ('has' & ending)
    //
    //      A = '
    //      B = ''
    //      C = '''
    //
    //      K = \
    //      N = normal
    //
    //      Q = "
    //      R = ""
    //      S = """
    //
    private static final EphemeralStringState   state(final String debug_name)
    {
        return EphemeralStringState.create(debug_name);
    }


    private static final EphemeralStringState   A_A  = state("A_A");    //  Has '; ends in '
    private static final EphemeralStringState   A_B  = state("A_B");    //  Has '; ends in ''
    private static final EphemeralStringState   A_K  = state("A_K");    //  Has '; ends in \
    private static final EphemeralStringState   A_N  = state("A_N");    //  Has '

    private static final EphemeralStringState   AQ_A = state("AQ_A");   //  Has ' & "; ends in '
    private static final EphemeralStringState   AQ_B = state("AQ_B");   //  Has ' & "; ends in ''
    private static final EphemeralStringState   AQ_K = state("AQ_K");   //  Has ' & "; ends in \
    private static final EphemeralStringState   AQ_N = state("AQ_N");   //  Has ' & "
    private static final EphemeralStringState   AQ_Q = state("AQ_Q");   //  Has ' & "; ends in "
    private static final EphemeralStringState   AQ_R = state("AQ_R");   //  Has ' & "; ends in ""

    private static final EphemeralStringState   AS_A = state("AS_A");   //  Has ' & """; ends in '
    private static final EphemeralStringState   AS_B = state("AS_B");   //  Has ' & """; ends in ''
    private static final EphemeralStringState   AS_K = state("AS_K");   //  Has ' & """; ends in \
    private static final EphemeralStringState   AS_N = state("AS_N");   //  Has ' & """
    private static final EphemeralStringState   AS_Q = state("AS_Q");   //  Has ' & """; ends in "   or \"
    private static final EphemeralStringState   AS_R = state("AS_R");   //  Has ' & """; ends in ""
    private static final EphemeralStringState   AS_S = state("AS_S");   //  Has ' & """; ends in """

    private static final EphemeralStringState   C_A  = state("C_A");    //  Has '''; ends in '
    private static final EphemeralStringState   C_B  = state("C_B");    //  Has '''; ends in ''
    private static final EphemeralStringState   C_C  = state("C_C");    //  Has '''; ends in '''
    private static final EphemeralStringState   C_K  = state("C_K");    //  Has '''; ends in \
    private static final EphemeralStringState   C_N  = state("C_N");    //  Has '''

    private static final EphemeralStringState   CQ_A = state("CQ_A");   //  Has ''' & "; ends in '
    private static final EphemeralStringState   CQ_B = state("CQ_B");   //  Has ''' & "; ends in ''
    private static final EphemeralStringState   CQ_C = state("CQ_C");   //  Has ''' & "; ends in '''
    private static final EphemeralStringState   CQ_K = state("CQ_K");   //  Has ''' & "; ends in \
    private static final EphemeralStringState   CQ_N = state("CQ_N");   //  Has ''' & "
    private static final EphemeralStringState   CQ_Q = state("CQ_Q");   //  Has ''' & "; ends in "
    private static final EphemeralStringState   CQ_R = state("CQ_R");   //  Has ''' & "; ends in ""

    private static final EphemeralStringState   CS_A = state("CS_A");   //  Has ''' & """; ends in '
    private static final EphemeralStringState   CS_B = state("CS_B");   //  Has ''' & """; ends in ''
    private static final EphemeralStringState   CS_C = state("CS_C");   //  Has ''' & """; ends in '''
    private static final EphemeralStringState   CS_N = state("CS_N");   //  Has ''' & """
    private static final EphemeralStringState   CS_Q = state("CS_Q");   //  Has ''' & """; ends in "
    private static final EphemeralStringState   CS_R = state("CS_R");   //  Has ''' & """; ends in ""
    private static final EphemeralStringState   CS_S = state("CS_S");   //  Has ''' & """; ends in """

    private static final EphemeralStringState   N_K  = state("N_K");    //  normal; ends in \
    private static final EphemeralStringState   N_N  = state("N_N");    //  normal

    private static final EphemeralStringState   Q_K  = state("Q_K");    //  Has "; ends in \
    private static final EphemeralStringState   Q_N  = state("Q_N");    //  Has "
    private static final EphemeralStringState   Q_Q  = state("Q_Q");    //  Has "; ends in "
    private static final EphemeralStringState   Q_R  = state("Q_R");    //  Has "; ends in ""

    private static final EphemeralStringState   S_K  = state("S_K");    //  Has """: ends in \
    private static final EphemeralStringState   S_N  = state("S_N");    //  Has """
    private static final EphemeralStringState   S_Q  = state("S_Q");    //  Has """; ends in "
    private static final EphemeralStringState   S_R  = state("S_R");    //  Has """; ends in ""
    private static final EphemeralStringState   S_S  = state("S_S");    //  Has """; ends in """


    private static final boolean        finish()
    {
        final OverallStringState        _ = null;

        //          '   \   L   "  ra  rq  pc  ps, K  L
        E .overall (U,  K,  L,  T, RA, RQ, PC, PS, _, _);
        K .overall (_,  K,  L,  _, RA, RQ, KC, KS, 7, _);
        L .overall (_,  L,  L,  _,  0,  _, KC, KS, _, 7);
        N .overall (N,  K,  L,  N, RA, RQ, PC, PS, _, _);
        TK.overall (_,  TK, TL, _, RA,  _, KC,  _, 7, _);
        TL.overall (_,  TL, TL, _,  0,  _, KC,  _, _, 7);
        T .overall (_,  TK, TL, _, RA,  _, PC,  _, _, _);
        UK.overall (_,  UK, UL, _, RQ,  _, KS,  _, 7, _);
        UL.overall (_,  UL, TL, _,  0,  _, KS,  _, _, 7);
        U .overall (_,  UK, UL, _, RQ,  _, PS,  _, _, _);

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        A_A  .setup(A_B,  A_K,  A_N,  AQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '; ends in '
        A_B  .setup(C_C,  A_K,  A_N,  AQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '; ends in ''
        A_K  .setup(A_N,  A_N,  A_N,  A_N,   0,  _, KQ,  _,  0,  _,  _);    //  Has '; ends in \
        A_N  .setup(A_A,  A_K,  A_N,  AQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        AQ_A .setup(AQ_B, AQ_K, AQ_N, AQ_Q, RS,  _, KS,  _, KS,  _,  _);    //  Has ' & "; ends in '
        AQ_B .setup(CQ_C, AQ_K, AQ_N, AQ_Q, RS,  _, KS,  _, KS,  _,  _);    //  Has ' & "; ends in ''
        AQ_K .setup(AQ_N, AQ_N, AQ_N, AQ_N,  0,  _, KC, KS,  0,  _,  _);    //  Has ' & "; ends in \
        AQ_N .setup(AQ_A, AQ_K, AQ_N, AQ_Q, RC, RS, KC, KS, PC, PS,  _);    //  Has ' & "
        AQ_Q .setup(AQ_A, AQ_K, AQ_N, AQ_R, RC,  _, KC,  _, KC,  _,  _);    //  Has ' & "; ends in "
        AQ_R .setup(AQ_A, AQ_K, AQ_N, AS_S, RC,  _, KC,  _, KC,  _,  _);    //  Has ' & "; ends in ""

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        AS_A .setup(AS_B, AS_K, AS_N, AS_Q,  0,  _, KS,  _, KS,  _,  _);    //  Has ' & """; ends in '
        AS_B .setup(CS_C, AS_K, AS_N, AS_Q,  0,  _, KS,  _, KS,  _,  _);    //  Has ' & """; ends in ''
        AS_K .setup(AS_N, AS_N, AS_N, AS_N,  0,  _, KC,  _,  0,  _,  _);    //  Has ' & """; ends in \
        AS_N .setup(AS_A, AS_K, AS_N, AS_Q, RC,  _, KC,  _, PC,  _,  _);    //  Has ' & """
        AS_Q .setup(AS_A, AS_K, AS_N, AS_R, RC,  _, KC,  _, KC,  _,  _);    //  Has ' & """; ends in "
        AS_R .setup(AS_A, AS_K, AS_N, AS_S, RC,  _, KC,  _, KC,  _,  _);    //  Has ' & """; ends in ""
        AS_S .setup(AS_A, AS_K, AS_N, AS_R, RC,  _, KC,  _, KC,  _,  1);    //  Has ' & """; ends in """

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        C_A  .setup(C_B,  C_K,  C_N,  CQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '''; ends in '
        C_B  .setup(C_C,  C_K,  C_N,  CQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '''; ends in ''
        C_C  .setup(C_B,  C_K,  C_N,  CQ_Q, RQ,  _, KQ,  _, PQ,  _, -1);    //  Has '''; ends in '''
        C_K  .setup(C_N,  C_N,  C_N,  C_N,   0,  _, KQ,  _,  0,  _,  _);    //  Has '''; ends in \
        C_N  .setup(C_A,  C_K,  C_N,  CQ_Q, RQ,  _, KQ,  _, PQ,  _,  _);    //  Has '''

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        CQ_A .setup(CQ_B, CQ_K, CQ_N, CQ_Q, RS,  _, KS,  _, PS,  _,  _);    //  Has ''' & "; ends in '
        CQ_B .setup(CQ_C, CQ_K, CQ_N, CQ_Q, RS,  _, KS,  _, PS,  _,  _);    //  Has ''' & "; ends in ''
        CQ_C .setup(CQ_B, CQ_K, CQ_N, CQ_Q, RS,  _, KS,  _, PS,  _, -1);    //  Has ''' & "; ends in '''
        CQ_K .setup(CQ_N, CQ_N, CQ_N, CQ_N,  0,  _, KS,  _,  0,  _,  _);    //  Has ''' & "; ends in \
        CQ_N .setup(CQ_A, CQ_K, CQ_N, CQ_Q, RS,  _, KS,  _, PS,  _,  _);    //  Has ''' & "
        CQ_Q .setup(CQ_A, CQ_K, CQ_N, CQ_R,  0,  _, KC,  _, KC,  _,  _);    //  Has ''' & "; ends in "
        CQ_R .setup(CQ_A, CQ_K, CQ_N, CS_S,  0,  _, KC,  _, KC,  _,  _);    //  Has ''' & "; ends in ""

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        CS_A .setup(CS_B, CS_N, CS_N, CS_Q,  0,  _, KS, _,  KS,  _,  _);    //  Has ''' & """; ends in '
        CS_B .setup(CS_C, CS_N, CS_N, CS_Q,  0,  _, KS, _,  KS,  _,  _);    //  Has ''' & """; ends in ''
        CS_C .setup(CS_B, CS_N, CS_N, CS_Q,  0,  _, KS, _,  KS,  _, -1);    //  Has ''' & """; ends in '''
        CS_N .setup(CS_A, CS_N, CS_N, CS_Q,  0,  _, KC, KS, PC, PS,  _);    //  Has ''' & """
        CS_Q .setup(CS_A, CS_N, CS_N, CS_R,  0,  _, KC, _,  KC,  _,  _);    //  Has ''' & """; ends in "
        CS_R .setup(CS_A, CS_N, CS_N, CS_S,  0,  _, KC, _,  KC,  _,  _);    //  Has ''' & """; ends in ""
        CS_S .setup(CS_A, CS_N, CS_N, CS_R,  0,  _, KC, _,  KC,  _,  1);    //  Has ''' & """; ends in """

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        N_K  .setup(N_N,  N_N,  N_N,  N_N,   0,  _, KA, KS,  0,  _,  _);    //  normal; ends in \
        N_N  .setup(A_A,  N_K,  N_N,  Q_Q,  RA, RQ, KA, KS, PC, PS,  _);    //  normal

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        Q_K  .setup(Q_N,  Q_N,  Q_N,  Q_N,   0,  _, KA,  _,  0,  _,  _);    //  Has "; ends in \
        Q_N  .setup(AQ_A, Q_K,  Q_N,  Q_Q,  RA,  _, KA,  _, PA,  _,  _);    //  Has "
        Q_Q  .setup(AQ_A, Q_K,  Q_N,  Q_R,  RA,  _, KA,  _, PA,  _,  _);    //  Has "; ends in "
        Q_R  .setup(AQ_A, Q_K,  Q_N,  S_S,  RA,  _, KA,  _, PA,  _,  _);    //  Has "; ends in ""

        //          '     \     N     "     ra  rq  kc  ks  pc  ps, F3
        S_K  .setup(S_N,  S_N,  S_N,  S_N,   0,  _, KA,  _,  0,  _,  _);    //   Has """: ends in \
        S_N  .setup(AS_A, S_K,  S_N,  S_Q,  RA,  _, KA,  _, PA,  _,  _);    //   Has """
        S_Q  .setup(AS_A, S_K,  S_N,  S_R,  RA,  _, KA,  _, PA,  _,  _);    //   Has """; ends in "
        S_R  .setup(AS_A, S_K,  S_N,  S_S,  RA,  _, KA,  _, PA,  _,  _);    //   Has """; ends in ""
        S_S  .setup(AS_A, S_K,  S_N,  S_R,  RA,  _, KA,  _, PA,  _,  1);    //   Has """; ends in """

        EphemeralStringState.remove_cache__ALLY__AnalyzeString();

        return true;
    }


    private static final boolean        finished = finish();


    private static String               analyze_string(final String s)
    {
        /*:*/ OverallStringState        overall = AnalyzeString.E;
        final AsciiTable[]              table   = AsciiTable.table;

        final int                       total = s.length();

        /*:*/ int                       code_point = 0;
        /*:*/ int                       i          = 0;
        /*:*/ AsciiTable                glyph      = null;

        for (;;) {
            if (i == total) {
                line("{+}: completed: {}", overall);
                return null;
            }

            code_point = s.codePointAt(i);

            if (code_point >= 128) {
                i += Character.charCount(code_point);
                break;
            }

            i ++;

            glyph = table[code_point];

            if ( ! glyph.is_boring_printable) {
                break;
            }

            overall = AnalyzeString.N;
        }

        /*:*/ int                   favorite;
        /*:*/ EphemeralStringState  state;
        /*:*/ EphemeralStringState  raw_state;

        if (code_point == 34) {                                         //  34 = ordinal('"')
            overall  = overall.Q;
            favorite = 1;

            raw_state =
                state = AnalyzeString.Q_Q;
        } else if (code_point == 39) {                                  //  39 = ordinal("'")
            overall   = overall.A;
            favorite  = -1;

            raw_state =
                state = AnalyzeString.A_A;
        } else if (code_point == 92) {                                  //  92 = ordinal('\\')
            overall   = AnalyzeString.K;
            favorite  = 0;
            raw_state = AnalyzeString.N_K;
            state     = AnalyzeString.N_N;
        } else {
            overall   = AnalyzeString.L;
            favorite  = 0;

            raw_state =
                state = AnalyzeString.N_N;
        }

        /*:*/ int                   C = 0;
        /*:*/ int                   S = 0;

        while (i < total) {
            code_point = s.codePointAt(i);

            if (code_point >= 128) {
                overall   = AnalyzeString.L;
                state     = state.N;
                raw_state = raw_state.N;

                i += Character.charCount(code_point);
                continue;
            }

            i ++;

            glyph = table[code_point];

            if (glyph.is_boring_printable) {
                state     = state.N;
                raw_state = raw_state.N;
                continue;
            }

            if (code_point == 34) {                                     //  34 = ordinal('"')
                state     = state.Q;
                raw_state = raw_state.Q;
                favorite += 1;
                S        -= state.favorite_3;
                continue;
            }

            if (code_point == 39) {                                     //  39 = ordinal("'")
                state     = state.A;
                raw_state = raw_state.A;
                favorite -= 1;
                C        += state.favorite_3;
                continue;
            }

            if (code_point == 92) {                                     //  92 = ordinal('\\')
                overall   = overall.K;
                raw_state = raw_state.K;
                state     = state.N;
                continue;
            }

            overall   = overall.L;
            raw_state = raw_state.N;
            state     = state.N;
        }

        if (true) {
            line("{+}:  overall:  {p}", overall);
            line("{+}: favorite:  {p}", favorite);
            line("{+}:    state:  {p}", state);
            line("{+}:raw_state:  {p}", raw_state);
            line("{+}:        C:  {p}", C);
            line("{+}:        S:  {p}", S);
        }

        if (overall.is_K) {
            line("{+}:#1");
            return null;
        }

        if ( ( (S == C) && (favorite >= 0) ) || (S > C) ) {
            line("{+}:#2");
            return null;
        }

        line("{+}:#3");

        if (false) {
            line("{+}:  {p}: overall{}; state{}", s, overall, state);
            line("{+}:  overall.pq: {p}", overall.pq);
        }

        line("{+}: Going to call: {}", state.portray_functions[overall.pq].abbreviation);

        return state.portray_functions[overall.pq].portray_string(s);
    }


    public static String                analyze_raw_string(final String s)
    {
        /*:*/ OverallStringState        overall = AnalyzeString.E;
        final AsciiTable[]              table   = AsciiTable.table;

        final int                       total = s.length();

        /*:*/ int                       code_point = 0;
        /*:*/ int                       i          = 0;
        /*:*/ AsciiTable                glyph      = null;

        for (;;) {
            if (i == total) {
                line("{+}: completed: {}", overall);
                return null;
            }

            code_point = s.codePointAt(i);

            if (code_point >= 128) {
                i += Character.charCount(code_point);
                break;
            }

            i ++;

            glyph = table[code_point];

            if ( ! glyph.is_boring_printable) {
                break;
            }

            overall = AnalyzeString.N;
        }

        /*:*/ int                   favorite;
        /*:*/ EphemeralStringState  state;
        /*:*/ EphemeralStringState  raw_state;

        if (code_point == 34) {                                         //  34 = ordinal('"')
            overall  = overall.Q;
            favorite = 1;

            raw_state =
                state = AnalyzeString.Q_Q;
        } else if (code_point == 39) {                                  //  39 = ordinal("'")
            overall   = overall.A;
            favorite  = -1;

            raw_state =
                state = AnalyzeString.A_A;
        } else if (code_point == 92) {                                  //  92 = ordinal('\\')
            overall   = AnalyzeString.K;
            favorite  = 0;
            raw_state = AnalyzeString.N_K;
            state     = AnalyzeString.N_N;
        } else {
            overall   = AnalyzeString.L;
            favorite  = 0;

            raw_state =
                state = AnalyzeString.N_N;
        }

        /*:*/ int                   C = 0;
        /*:*/ int                   S = 0;

        while (i < total) {
            code_point = s.codePointAt(i);

            if (code_point >= 128) {
                overall   = AnalyzeString.L;
                state     = state.N;
                raw_state = raw_state.N;

                i += Character.charCount(code_point);
                continue;
            }

            i ++;

            glyph = table[code_point];

            if (glyph.is_boring_printable) {
                state     = state.N;
                raw_state = raw_state.N;
                continue;
            }

            if (code_point == 34) {                                     //  34 = ordinal('"')
                state     = state.Q;
                raw_state = raw_state.Q;
                favorite += 1;
                S        -= state.favorite_3;
                continue;
            }

            if (code_point == 39) {                                     //  39 = ordinal("'")
                state     = state.A;
                raw_state = raw_state.A;
                favorite -= 1;
                C        += state.favorite_3;
                continue;
            }

            if (code_point == 92) {                                     //  92 = ordinal('\\')
                overall   = overall.K;
                raw_state = raw_state.K;
                state     = state.N;
                continue;
            }

            overall   = overall.L;
            raw_state = raw_state.N;
            state     = state.N;
        }

        if (true) {
            line("{+}:   overall:  {p}", overall);
            line("{+}:  favorite:  {p}", favorite);
            line("{+}:     state:  {p}", state);
            line("{+}: raw_state:  {p}", raw_state);
            line("{+}:         C:  {p}", C);
            line("{+}:         S:  {p}", S);
        }

        if ( ( (S == C) && (favorite >= 0) ) || (S > C) ) {
            //
            //  Prefer apostrophe `'`
            //
            final int           raw_index = overall.ra;

            if (raw_index >= 0) {
                final PortrayString     raw = raw_state.portray_functions[raw_index];       //  ra * raw

                if (raw.is_valid) {
                    line("{+}: Going to call: {}", raw.abbreviation);

                    return raw.portray_string(s);
                }
            }

            final PortrayString         normal = state.portray_functions[overall.pa];       //  pa * normal

            line("{+}: Going to call: {}", normal.abbreviation);

            return normal.portray_string(s);
        }

        //
        //  Prefer apostrophe `"`
        //
        final int           raw_index = overall.rq;

        if (raw_index >= 0) {
            final PortrayString     raw = raw_state.portray_functions[raw_index];           //  rq * raw

            if (raw.is_valid) {
                line("{+}: Going to call: {}", raw.abbreviation);

                return raw.portray_string(s);
            }
        }

        final PortrayString         normal = state.portray_functions[overall.pq];           //  pq * normal

        line("{+}: Going to call: {}", normal.abbreviation);

        return normal.portray_string(s);
    }


    //
    //  Public (debug)
    //
    public static final void            dump()
    {
        line("Dump of AnalyzeString");
        OverallStringState.portray_header("member ");
        line("   E:  {p}", AnalyzeString.E);
        line("   K:  {p}", AnalyzeString.K);
        line("   L:  {p}", AnalyzeString.L);
        line("   N:  {p}", AnalyzeString.N);
        line("  TK:  {p}", AnalyzeString.TK);
        line("  TL:  {p}", AnalyzeString.TL);
        line("   T:  {p}", AnalyzeString.T);
        line("  UK:  {p}", AnalyzeString.UK);
        line("  UL:  {p}", AnalyzeString.UL);
        line("   U:  {p}", AnalyzeString.U);

        line("---");
        EphemeralStringState.portray_header(" member  ");
        line("   A_A:  {p}", AnalyzeString.A_A);
        line("   A_B:  {p}", AnalyzeString.A_B);
        line("   A_K:  {p}", AnalyzeString.A_K);
        line("   A_N:  {p}", AnalyzeString.A_N);
        line("---");
        line("  AQ_A:  {p}", AnalyzeString.AQ_A);
        line("  AQ_B:  {p}", AnalyzeString.AQ_B);
        line("  AQ_K:  {p}", AnalyzeString.AQ_K);
        line("  AQ_N:  {p}", AnalyzeString.AQ_N);
        line("  AQ_Q:  {p}", AnalyzeString.AQ_Q);
        line("  AQ_R:  {p}", AnalyzeString.AQ_R);
        line("---");
        line("  AS_A:  {p}", AnalyzeString.AS_A);
        line("  AS_B:  {p}", AnalyzeString.AS_B);
        line("  AS_K:  {p}", AnalyzeString.AS_K);
        line("  AS_N:  {p}", AnalyzeString.AS_N);
        line("  AS_Q:  {p}", AnalyzeString.AS_Q);
        line("  AS_R:  {p}", AnalyzeString.AS_R);
        line("  AS_S:  {p}", AnalyzeString.AS_S);
        line("---");
        line("   C_A:  {p}", AnalyzeString.C_A);
        line("   C_B:  {p}", AnalyzeString.C_B);
        line("   C_C:  {p}", AnalyzeString.C_C);
        line("   C_K:  {p}", AnalyzeString.C_K);
        line("   C_N:  {p}", AnalyzeString.C_N);
        line("---");
        line("  CQ_A:  {p}", AnalyzeString.CQ_A);
        line("  CQ_B:  {p}", AnalyzeString.CQ_B);
        line("  CQ_C:  {p}", AnalyzeString.CQ_C);
        line("  CQ_K:  {p}", AnalyzeString.CQ_K);
        line("  CQ_N:  {p}", AnalyzeString.CQ_N);
        line("  CQ_Q:  {p}", AnalyzeString.CQ_Q);
        line("  CQ_R:  {p}", AnalyzeString.CQ_R);
        line("---");
        line("  CS_A:  {p}", AnalyzeString.CS_A);
        line("  CS_B:  {p}", AnalyzeString.CS_B);
        line("  CS_C:  {p}", AnalyzeString.CS_C);
        line("  CS_N:  {p}", AnalyzeString.CS_N);
        line("  CS_Q:  {p}", AnalyzeString.CS_Q);
        line("  CS_R:  {p}", AnalyzeString.CS_R);
        line("  CS_S:  {p}", AnalyzeString.CS_S);
        line("---");
        line("   N_K:  {p}", AnalyzeString.N_K);
        line("   N_N:  {p}", AnalyzeString.N_N);
        line("---");
        line("   Q_K:  {p}", AnalyzeString.Q_K);
        line("   Q_N:  {p}", AnalyzeString.Q_N);
        line("   Q_Q:  {p}", AnalyzeString.Q_Q);
        line("   Q_R:  {p}", AnalyzeString.Q_R);
        line("---");
        line("   S_K:  {p}", AnalyzeString.S_K);
        line("   S_N:  {p}", AnalyzeString.S_N);
        line("   S_Q:  {p}", AnalyzeString.S_Q);
        line("   S_R:  {p}", AnalyzeString.S_R);
        line("   S_S:  {p}", AnalyzeString.S_S);

        line("End of dump of AnalyzeString");
    }


    //
    //  Public (Unit Test)
    //
    public static final void            show_analyze_string(final String s)
    {
        line("analysis of {p}: {}", s, analyze_string(s));
    }
}
