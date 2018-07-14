//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AsciiTable;


public abstract class   AnalyzeString
    extends             Gem_Object//<Inspection>
{
    //
    //   States (overall)
    //
    //       E = Empty
    //       K = Backslash
    //       L = Lemon
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
    private static final OverallStringState     T  = OverallStringState.create("T");
    private static final OverallStringState     UK = OverallStringState.create("UK");
    private static final OverallStringState     UL = OverallStringState.create("UL");
    private static final OverallStringState     U  = OverallStringState.create("U");


    private static boolean              finish()
    {
        final OverallStringState        _ = null;

        E .overall (U,  K,  L,  T);
        K .overall (_,  K,  L,  _);
        L .overall (_,  L,  L,  _);
        N .overall (N,  K,  L,  N);
        TK.overall (_,  TK, TL, _);
        TL.overall (_,  TL, TL, _);
        T .overall (_,  TK, TL, _);
        UK.overall (_,  UK, UL, _);
        UL.overall (_,  UL, TL, _);
        U .overall (_,  UK, UL, _);

        return true;
    }


    private static final boolean        finished = finish();


    //
    //  Public (debug)
    //
    public static final void            dump()
    {
        line("Dump of AnalyzeString");
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
        line("End of dump of AnalyzeString");
    }


    //
    //  Public (Unit Test)
    //
    public static final void            show_analyze_string(final String s)
    {
        line("analysis of {p}: ...", s);
    }
}


final class             OverallStringState
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("OverallStringState");


    //
    //  Members
    //
    public final String                 debug_name;
    public       OverallStringState     A;
    public       OverallStringState     K;
    public       OverallStringState     N;
    public       OverallStringState     Q;


    //
    //  Constructor, Factory, & Overall initialization
    //
    private                             OverallStringState(final String debug_name)
    {
        this.debug_name = debug_name;
    //  this.A          = null;
    //  this.K          = null;
    //  this.N          = null;
    //  this.Q          = null;
    }


    public static final OverallStringState  create(final String debug_name)
    {
        return new OverallStringState(debug_name);
    }

   
    public void                         overall(
            final OverallStringState            A,
            final OverallStringState            K,
            final OverallStringState            N,
            final OverallStringState            Q//,
        )
    {
        this.A = A;
        this.K = K;
        this.N = N;
        this.Q = Q;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(final Gem_StringBuilder builder)
    {
        final OverallStringState        A = this.A;
        final OverallStringState        K = this.K;
        final OverallStringState        N = this.N;
        final OverallStringState        Q = this.Q;

        builder.augment("<OverallStringState {}; {} {} {} {}>",
                        String.format("%2s", this.debug_name),
                        String.format("%2s", (A == null ? "." : A.debug_name)),
                        String.format("%2s", (K == null ? "." : K.debug_name)),
                        String.format("%2s", (N == null ? "." : N.debug_name)),
                        String.format("%2s", (Q == null ? "." : Q.debug_name)));
    }
}
