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


public class    MessageFormatter_4
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_4");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable          a;
    private SegmentFormattable          b;
    private SegmentFormattable          c;
    private SegmentFormattable          d;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_4(
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
        this.d        = d;
    }


    static public MessageFormatter_4    create(
            Zone                            z,
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d//,
        )
    {
        if ( ! (2 <= expected && expected <= 4)) {
            z.RAISE_runtime_exception("MessageFormatter_4.create: invalid value for `expected`<{0}>", expected);
        }

        return new MessageFormatter_4(expected, a, b, c, d);
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

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            z.RAISE_runtime_exception("2 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.select_2(builder, v, w);
        this.b.select_2(builder, v, w);
        this.c.select_2(builder, v, w);
        this.d.select_2(builder, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual   = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;
        SegmentFormattable              d = this.d;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        if (expected == 2) {
            a.select_2(builder, v, w);
            b.select_2(builder, v, w);
            c.select_2(builder, v, w);
            d.select_2(builder, v, w);

            return builder.finish__AND__recycle();
        }

        Object                          x = other_arguments[0];

        if (expected == 3) {
            a.select_3(builder, v, w, x);
            b.select_3(builder, v, w, x);
            c.select_3(builder, v, w, x);
            d.select_3(builder, v, w, x);

            return builder.finish__AND__recycle();
        }

        Object                          y = other_arguments[1];

        a.select_4(builder, v, w, x, y);
        b.select_4(builder, v, w, x, y);
        c.select_4(builder, v, w, x, y);
        d.select_4(builder, v, w, x, y);

        return builder.finish__AND__recycle();
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_4 " + this.a.portray(z) + " " + this.b.portray(z) + " " + this.c.portray(z) + ">";
    }
}
