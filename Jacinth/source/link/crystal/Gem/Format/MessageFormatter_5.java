//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    MessageFormatter_5
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_5");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable          a;
    private SegmentFormattable          b;
    private SegmentFormattable          c;
    private SegmentFormattable          d;
    private SegmentFormattable          e;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_5(
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d,
            SegmentFormattable              e//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
        this.d        = d;
        this.e        = e;
    }


    static public MessageFormatter_5    create(
            Zone                            z,
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d,
            SegmentFormattable              e//,
        )
    {
        if ( ! (2 <= expected && expected <= 5)) {
            z.RAISE_runtime_exception("MessageFormatter_5.create: invalid value for `expected`<{0}>", expected);
        }

        return new MessageFormatter_5(expected, a, b, c, d, e);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    public String                       arrange(Zone z, int depth, Object v)
    {
        if (this.expected != 1) {
            z.RAISE_runtime_exception("1 argument given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);
        this.c.choose(builder, depth, v);
        this.d.choose(builder, depth, v);
        this.e.choose(builder, depth, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            z.RAISE_runtime_exception("2 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.choose(builder, v, w);
        this.b.choose(builder, v, w);
        this.c.choose(builder, v, w);
        this.d.choose(builder, v, w);
        this.e.choose(builder, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x)
    {
        if (this.expected != 3) {
            z.RAISE_runtime_exception("3 arguments given (expected {0})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.choose(builder, v, w, x);
        this.b.choose(builder, v, w, x);
        this.c.choose(builder, v, w, x);
        this.d.choose(builder, v, w, x);
        this.e.choose(builder, v, w, x);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x, Object y)
    {
        if (this.expected != 4) {
            z.RAISE_runtime_exception("4 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.choose(builder, v, w, x, y);
        this.b.choose(builder, v, w, x, y);
        this.c.choose(builder, v, w, x, y);
        this.d.choose(builder, v, w, x, y);
        this.e.choose(builder, v, w, x, y);

        return builder.toString();
    }


    public String                       arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        if (this.expected != 5) {
            z.RAISE_runtime_exception("5 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.choose(builder, v, w, x, y4, y5);
        this.b.choose(builder, v, w, x, y4, y5);
        this.c.choose(builder, v, w, x, y4, y5);
        this.d.choose(builder, v, w, x, y4, y5);
        this.e.choose(builder, v, w, x, y4, y5);

        return builder.finish__AND__recycle();
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_5 " + this.a.portray(z) + " " + this.b.portray(z) + " " + this.c.portray(z) + ">";
    }
}
