//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.OutputFunctions;


public class    MessageFormatter_5
    extends     Gem_Object<Inspection>
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
        int                             expected = this.expected;

        int                             actual = 1;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;
        SegmentFormattable              d = this.d;
        SegmentFormattable              e = this.e;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        a.choose(builder, depth, v);
        b.choose(builder, depth, v);
        c.choose(builder, depth, v);
        d.choose(builder, depth, v);
        e.choose(builder, depth, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;
        SegmentFormattable              d = this.d;
        SegmentFormattable              e = this.e;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        Object                          w = other_arguments[0];

        if (expected == 2) {
            a.select_2(builder, v, w);
            b.select_2(builder, v, w);
            c.select_2(builder, v, w);
            d.select_2(builder, v, w);
            e.select_2(builder, v, w);

            return builder.finish__AND__recycle();
        }

        Object                          x = other_arguments[1];

        if (expected == 3) {
            a.select_3(builder, v, w, x);
            b.select_3(builder, v, w, x);
            c.select_3(builder, v, w, x);
            d.select_3(builder, v, w, x);
            e.select_3(builder, v, w, x);

            return builder.finish__AND__recycle();
        }

        Object                          y = other_arguments[2];

        if (expected == 4) {
            a.select_4(builder, v, w, x, y);
            b.select_4(builder, v, w, x, y);
            c.select_4(builder, v, w, x, y);
            d.select_4(builder, v, w, x, y);
            e.select_4(builder, v, w, x, y);

            return builder.toString();
        }

        Object                          z5 = other_arguments[3];

        a.select_5(builder, v, w, x, y, z5);
        b.select_5(builder, v, w, x, y, z5);
        c.select_5(builder, v, w, x, y, z5);
        d.select_5(builder, v, w, x, y, z5);
        e.select_5(builder, v, w, x, y, z5);

        return builder.finish__AND__recycle();
    }


    public void                         line(Zone z, int depth, Object v)
    {
        z.line(this.arrange(z, depth + 1, v));
    }


    public void                         line(Zone z, int depth, Object v, Object ... other_arguments)
    {
        z.line(this.arrange(z, depth + 1, v, other_arguments));
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_5 " + this.a.portray(z) + " " + this.b.portray(z) + " " + this.c.portray(z) + ">";
    }
}
