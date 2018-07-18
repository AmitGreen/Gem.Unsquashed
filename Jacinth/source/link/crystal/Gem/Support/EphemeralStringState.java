//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import java.util.HashMap;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.PortrayString;


public final class      EphemeralStringState
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("EphemeralStringState");


    //
    //  Static members
    //
    private static final PortrayString[]    portray_table = new PortrayString[] {
            PortrayString.portray_string__invalid,              //  0

            PortrayString.raw_with_apostrophe,                  //  RA
            PortrayString.raw_with_quotation_mark,              //  RQ

            PortrayString.backslash_with_triple_apostrophe,     //  KC
            PortrayString.backslash_with_triple_quotation_mark, //  KS

            PortrayString.normal_with_triple_apostrophe,        //  PC
            PortrayString.normal_with_triple_quotation_mark,    //  PS

            PortrayString.backslash_with_apostrophe,            //  KA
            PortrayString.backslash_with_quotation_mark,        //  KQ

            PortrayString.normal_with_apostrophe,               //  PA
            PortrayString.normal_with_quotation_mark,           //  PQ

            PortrayString.raw_with_triple_apostrophe,           //  RC
            PortrayString.raw_with_triple_quotation_mark,       //  RQ
        };


    private static /*:*/ HashMap<Integer, PortrayString[]>  portray_cache = (
                new HashMap<Integer, PortrayString[]>(37)       //      //  Currently uses 17 entries
            );


    //
    //  Members
    //
    public final String                 debug_name;
    public /*:*/ EphemeralStringState   A;
    public /*:*/ EphemeralStringState   K;
    public /*:*/ EphemeralStringState   N;
    public /*:*/ EphemeralStringState   Q;

    public /*:*/ boolean                rawable;
    public /*:*/ PortrayString[]        portray_functions;

    //
    //  Tracking ''' & """ for normal portray
    //
    public /*:*/ int                    favorite_3;
    public /*:*/ boolean                end_C;
    public /*:*/ boolean                end_S;


    //
    //  Constructor, Factory, & Setup
    //
    private                             EphemeralStringState(final String debug_name)
    {
        this.debug_name = debug_name;

    //  this.A                 = vacant
    //  this.K                 = vacant
    //  this.N                 = vacant
    //  this.Q                 = vacant

    //  this.rawable           = vacant
    //  this.portray_functions = vacant

    //  this.favorite_3 = vacant
    //  this.end_C      = vacant
    //  this.end_S      = vacant
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
            final int                           ra,
            final Object                        rq,
            final int                           kc,
            final Object                        ks,
            final int                           pc,
            final Object                        ps,
            final Object                        F3//,
        )
    {
        if (ra == 0) {
            assert fact_null(rq, "rq");
        } else {
            assert fact_between(1, ra, 12);

            if (rq != null) {
                assert fact_between(0, (Integer) ra, 12);
            }
        }

        assert fact_between(1, kc, 12);

        if (ks != null) {
            assert fact_between(1, (Integer) ks, 12);
        }

        if (pc == 0) {
            assert fact_null(ps, "ps");
        } else {
            assert fact_between(1, (Integer) pc, 12);

            if (ps != null) {
                assert fact_between(0, (Integer) ps, 12);
            }
        }

        if (F3 != null) {
            assert fact_between(-1, (Integer) F3, 1);
        }

        final int                       rq_value = (rq == null ? ra : (Integer) rq);
        final int                       ks_value = (ks == null ? kc : (Integer) ks);
        final int                       ps_value = (ps == null ? pc : (Integer) ps);
        final int                       F3_value = (F3 == null ? 0  : (Integer) F3);

        final int                       portray_key = (
                  (ra       << 20)
                | (rq_value << 16)
                | (kc       << 12)
                | (ks_value <<  8)
                | (pc       <<  4)
                | (ps_value      )
            );

        final HashMap<Integer, PortrayString[]>     portray_cache = this.portray_cache;

        /*:*/ PortrayString[]           portray_functions = portray_cache.get(portray_key);

        if (portray_functions == null) {
            final PortrayString[]       portray_table = this.portray_table;

            portray_functions = new PortrayString[] {
                    portray_table[ra],
                    portray_table[rq_value],
                    portray_table[kc],
                    portray_table[ks_value],
                    portray_table[pc],
                    portray_table[ps_value],
                };

            portray_cache.put(portray_key, portray_functions);
        }

        this.A = A;
        this.K = K;
        this.N = N;
        this.Q = Q;

        this.rawable           = (ra != 0);
        this.portray_functions = portray_functions;

        this.favorite_3 = F3_value;
        this.end_C      = (F3_value == -1);
        this.end_S      = (F3_value ==  1);
    }


    //
    //  Interface Inspectable
    //
    //  NOTE:
    //      Also includes helper function `portray_header` which is not part of `Interface Inspectable`.
    //
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        final EphemeralStringState      A                 = this.A;
        final EphemeralStringState      K                 = this.K;
        final EphemeralStringState      N                 = this.N;
        final EphemeralStringState      Q                 = this.Q;
        final PortrayString[]           portray_functions = this.portray_functions;
        final int                       F3                = this.favorite_3;

        builder.augment("<EphemeralStringState {}; {} {} {} {}; {}; {} {} {} {} {} {}; {} {} {}>",
                        String.format("%5s", this.debug_name),
                        String.format("%5s", (A  == null ? "." : A.debug_name)),
                        String.format("%5s", (K  == null ? "." : K.debug_name)),
                        String.format("%5s", (N  == null ? "." : N.debug_name)),
                        String.format("%5s", (Q  == null ? "." : Q.debug_name)),
                        (this.rawable ? "R" : "."),
                        String.format("%2s", portray_functions[0].abbreviation),
                        String.format("%2s", portray_functions[1].abbreviation),
                        String.format("%2s", portray_functions[2].abbreviation),
                        String.format("%2s", portray_functions[3].abbreviation),
                        String.format("%2s", portray_functions[4].abbreviation),
                        String.format("%2s", portray_functions[5].abbreviation),
                        (F3 == -1   ? "-1" : F3 == 1 ? " 1" : " ."),
                        (this.end_C ? "C" : "."),
                        (this.end_S ? "S" : "."));
    }


    static public final void            portray_header(final String prefix)
    {
        line("{} --------------------- name;     A     K     N     Q; R; ra rq kc ks pc ps; F3 C S", prefix);
    }


    //
    //  Public
    //
    static public final void            remove_cache__ALLY__AnalyzeString()
    {
    //  line("Cache total: {}", EphemeralStringState.portray_cache.size());

        EphemeralStringState.portray_cache = null;
    }
}
