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
    public /*:*/ OverallStringState     A;
    public /*:*/ OverallStringState     K;
    public /*:*/ OverallStringState     L;
    public /*:*/ OverallStringState     Q;
    public /*:*/ int                    ra;
    public /*:*/ int                    rq;
    public /*:*/ int                    pa;
    public /*:*/ int                    pq;
    public /*:*/ boolean                is_K;


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
    //  this.pa         = 0;
    //  this.pq         = 0;
    //  this.is_K       = false;
    }


    public static final OverallStringState  create(final String debug_name)
    {
        return new OverallStringState(debug_name);
    }


    public final void                   overall(
            final OverallStringState            A,
            final OverallStringState            K,
            final OverallStringState            L,
            final OverallStringState            Q,
            final Object                        ra,
            final Object                        rq,
            final Object                        pa,
            final Object                        pq,
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

        if (pa != null) {
            assert fact_between(0, (Integer) pa, 6);
        }

        if (pq != null) {
            assert fact_between(0, (Integer) pq, 6);
        }

        final int                       ra_value = (ra == null ? -1       : (Integer) ra);
        final int                       rq_value = (rq == null ? ra_value : (Integer) rq);
        final int                       pa_value = (pa == null ? -1       : (Integer) pa);
        final int                       pq_value = (pq == null ? pa_value : (Integer) pq);

        this.A    = A;
        this.K    = K;
        this.L    = L;
        this.Q    = Q;
        this.ra   = ra_value - 1;
        this.rq   = rq_value - 1;
        this.pa   = pa_value - 1;
        this.pq   = pq_value - 1;
        this.is_K = (is_K != null);
    }


    //
    //  Interface Inspectable
    //
    //  NOTE:
    //      Also includes helper function `portray_header` which is not part of `Interface Inspectable`.
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        final OverallStringState        A  = this.A;
        final OverallStringState        K  = this.K;
        final OverallStringState        L  = this.L;
        final OverallStringState        Q  = this.Q;
        final int                       ra = this.ra + 1;
        final int                       rq = this.rq + 1;
        final int                       pa = this.pa + 1;
        final int                       pq = this.pq + 1;

        final String[]                  index_names = AnalyzeString.index_names;

        builder.augment("<OverallStringState {}; {} {} {} {}; {} {} {} {}",
                        String.format("%2s", this.debug_name),
                        String.format("%2s", (A  == null ? "." : A.debug_name)),
                        String.format("%2s", (K  == null ? "." : K.debug_name)),
                        String.format("%2s", (L  == null ? "." : L.debug_name)),
                        String.format("%2s", (Q  == null ? "." : Q.debug_name)),
                        String.format("%2s", (ra == -1   ? "." : index_names[ra])),
                        String.format("%2s", (rq == -1   ? "." : index_names[rq])),
                        String.format("%2s", (pa == -1   ? "." : index_names[pa])),
                        String.format("%2s", (pq == -1   ? "." : index_names[pq])));

        if (this.is_K) {
            builder.append("; is_K");
        }

        builder.append(">");
    }


    static public final void            portray_header(final String prefix)
    {
        line("{} ---------------- name;  A  K  L  Q; ra rq pa pq; is_K", prefix);
    }
}
