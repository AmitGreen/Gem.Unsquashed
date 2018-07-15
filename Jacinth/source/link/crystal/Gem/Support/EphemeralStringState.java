//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


final class             EphemeralStringState
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("EphemeralStringState");


    //
    //  Members
    //
    public final String                 debug_name;
    public       EphemeralStringState   A;
    public       EphemeralStringState   K;
    public       EphemeralStringState   N;
    public       EphemeralStringState   Q;

    public       int                    ra;
    public       int                    rq;

    public       int                    kc;
    public       int                    ks;

    public       int                    pc;
    public       int                    ps;


    //
    //  Tracking ''' & """ for normal portray
    //
    public       int                    favorite_3;
    public       boolean                end_C;
    public       boolean                end_S;


    //
    //  Constructor, Factory, & Setup
    //
    private                             EphemeralStringState(final String debug_name)
    {
        this.debug_name = debug_name;
    //  this.A          = null;
    //  this.K          = null;
    //  this.N          = null;
    //  this.Q          = null;

    //  this.ra         = 0;
    //  this.rq         = 0;

    //  this.kc         = 0;
    //  this.ks         = 0;

    //  this.pc         = 0;
    //  this.ps         = 0;

    //  this.favorite_3 = 0;
    //  this.end_C      = 0;
    //  this.end_S      = 0;
    }


    public static final EphemeralStringState    create(final String debug_name)
    {
        return new EphemeralStringState(debug_name);
    }


    public final void                   setup(
            final EphemeralStringState          A,
            final EphemeralStringState          K,
            final EphemeralStringState          N,
            final EphemeralStringState          Q,
            final Object                        ra,
            final Object                        rq,
            final Object                        kc,
            final Object                        ks,
            final Object                        pc,
            final Object                        ps,
            final Object                        F3//,
        )
    {
        if (ra == null) {
            assert fact_null(rq, "rq");
        } else {
            assert fact_between(0, (Integer) ra, 8);
        }

        if (rq != null) {
            assert fact_between(0, (Integer) ra, 8);
        }

        if (kc == null) {
            assert fact_null(ks, "ks");
        } else {
            assert fact_between(0, (Integer) kc, 8);
        }

        if (ks != null) {
            assert fact_between(0, (Integer) ks, 8);
        }

        if (pc == null) {
            assert fact_null(ps, "ps");
        } else {
            assert fact_between(0, (Integer) pc, 8);
        }

        if (ps != null) {
            assert fact_between(0, (Integer) ps, 8);
        }

        if (F3 != null) {
            assert fact_between(-1, (Integer) F3, 1);
        }

        final int                       ra_value = (ra == null ? AnalyzeString.P : (Integer) ra);
        final int                       rq_value = (rq == null ? ra_value        : (Integer) rq);
        final int                       kc_value = (kc == null ? AnalyzeString.P : (Integer) kc);
        final int                       ks_value = (ks == null ? kc_value        : (Integer) ks);
        final int                       pc_value = (pc == null ? AnalyzeString.P : (Integer) pc);
        final int                       ps_value = (ps == null ? pc_value        : (Integer) ps);
        final int                       F3_value = (F3 == null ? 0               : (Integer) F3);

        this.A  = A;
        this.K  = K;
        this.N  = N;
        this.Q  = Q;
        this.ra = ra_value;
        this.rq = rq_value;
        this.kc = kc_value;
        this.ks = ks_value;
        this.pc = pc_value;
        this.ps = ps_value;

        this.favorite_3 = F3_value;
        this.end_C      = (F3_value == -1);
        this.end_S      = (F3_value ==  1);
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
        final EphemeralStringState      A  = this.A;
        final EphemeralStringState      K  = this.K;
        final EphemeralStringState      N  = this.N;
        final EphemeralStringState      Q  = this.Q;
        final int                       ra = this.ra;
        final int                       rq = this.rq;
        final int                       kc = this.kc;
        final int                       ks = this.ks;
        final int                       pc = this.pc;
        final int                       ps = this.ps;
        final int                       F3 = this.favorite_3;

        final String[]                  index_names = AnalyzeString.index_names;

        builder.augment("<EphemeralStringState {}; {} {} {} {}; {} {} {} {} {} {}; {} {} {}>",
                        String.format("%5s", this.debug_name),
                        String.format("%5s", (A  == null ? "." : A.debug_name)),
                        String.format("%5s", (K  == null ? "." : K.debug_name)),
                        String.format("%5s", (N  == null ? "." : N.debug_name)),
                        String.format("%5s", (Q  == null ? "." : Q.debug_name)),
                        String.format("%2s", (ra == -1   ? "." : index_names[ra])),
                        String.format("%2s", (rq == -1   ? "." : index_names[rq])),
                        String.format("%2s", (kc == -1   ? "." : index_names[kc])),
                        String.format("%2s", (ks == -1   ? "." : index_names[ks])),
                        String.format("%2s", (pc == -1   ? "." : index_names[pc])),
                        String.format("%2s", (ps == -1   ? "." : index_names[ps])),
                        (F3 == -1   ? "-1" : F3 == 1 ? " 1" : " ."),
                        (this.end_C ? "C" : "."),
                        (this.end_S ? "S" : "."));
    }
}
