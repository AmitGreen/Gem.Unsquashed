//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class      OverallStringState
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
    public       OverallStringState     L;
    public       OverallStringState     Q;
    public       int                    ra;
    public       int                    rq;
    public       int                    pc;
    public       int                    ps;
    public       boolean                is_K;


    //
    //  Constructor, Factory, & Overall initialization
    //
    private                             OverallStringState(final String debug_name)
    {
        this.debug_name = debug_name;
    //  this.A          = null;
    //  this.K          = null;
    //  this.L          = null;
    //  this.Q          = null;
    //  this.ra         = 0;
    //  this.rq         = 0;
    //  this.pc         = 0;
    //  this.ps         = 0;
    //  this.is_K       = false;
    }


    public static final OverallStringState  create(final String debug_name)
    {
        return new OverallStringState(debug_name);
    }


    public void                         overall(
            final OverallStringState            A,
            final OverallStringState            K,
            final OverallStringState            L,
            final OverallStringState            Q,
            final Object                        ra,
            final Object                        rq,
            final Object                        pc,
            final Object                        ps,
            final Object                        is_K//,
        )
    {
        if (is_K == null) {
            assert fact( ! this.debug_name.endsWith("K"), "this.debug_name does NOT end with a 'K'");
        } else {
            assert fact(((Integer) is_K) == 7,            "((Integer) is_K) == 7");
            assert fact(this.debug_name.endsWith("K"),    "this.debug_name ends with a 'K'");
        }

        if (ra != null) {
            assert fact_between(0, (Integer) ra, 6);
        }

        if (rq != null) {
            assert fact_between(0, (Integer) ra, 6);
        }

        if (pc != null) {
            assert fact_between(0, (Integer) pc, 6);
        }

        if (ps != null) {
            assert fact_between(0, (Integer) ps, 6);
        }

        final int                       ra_value = (ra == null ? -1       : (Integer) ra);
        final int                       rq_value = (rq == null ? ra_value : (Integer) rq);
        final int                       pc_value = (pc == null ? -1       : (Integer) pc);
        final int                       ps_value = (ps == null ? pc_value : (Integer) ps);

        this.A    = A;
        this.K    = K;
        this.L    = L;
        this.Q    = Q;
        this.ra   = ra_value - 1;
        this.rq   = rq_value - 1;
        this.pc   = pc_value - 1;
        this.ps   = ps_value - 1;
        this.is_K = (is_K != null);
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
        final OverallStringState        A  = this.A;
        final OverallStringState        K  = this.K;
        final OverallStringState        L  = this.L;
        final OverallStringState        Q  = this.Q;
        final int                       ra = this.ra + 1;
        final int                       rq = this.rq + 1;
        final int                       pc = this.pc + 1;
        final int                       ps = this.ps + 1;

        final String[]                  index_names = AnalyzeString.index_names;

        builder.augment("<OverallStringState {}; {} {} {} {}; {} {} {} {}",
                        String.format("%2s", this.debug_name),
                        String.format("%2s", (A  == null ? "." : A.debug_name)),
                        String.format("%2s", (K  == null ? "." : K.debug_name)),
                        String.format("%2s", (L  == null ? "." : L.debug_name)),
                        String.format("%2s", (Q  == null ? "." : Q.debug_name)),
                        String.format("%2s", (ra == -1   ? "." : index_names[ra])),
                        String.format("%2s", (rq == -1   ? "." : index_names[rq])),
                        String.format("%2s", (pc == -1   ? "." : index_names[pc])),
                        String.format("%2s", (ps == -1   ? "." : index_names[ps])));

        if (this.is_K) {
            builder.append("; is_K");
        }

        builder.append(">");
    }
}
