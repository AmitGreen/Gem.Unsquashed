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


public class    MessageFormatter_3
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_3");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable          a;
    private SegmentFormattable          b;
    private SegmentFormattable          c;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_3(
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
    }


    static public MessageFormatter_3    create(
            Zone                            z,
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c//,
        )
    {
        if ( ! (1 <= expected && expected <= 3)) {
            z.RAISE_runtime_exception("MessageFormatter_3.create: invalid value for `expected`<{0}>", expected);
        }

        return new MessageFormatter_3(expected, a, b, c);
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
    public String                       arrange(Zone z, Object v, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual   = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("MessageFormatter_3.arrange: {0} arguments given (expected {1})",
                                      actual,
                                      expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        if (expected == 1) {
            a.select_1(builder, v);
            b.select_1(builder, v);
            c.select_1(builder, v);

            return builder.finish__AND__recycle();
        }

        Object                          w = other_arguments[0];

        if (expected == 2) {
            a.select_2(builder, v, w);
            b.select_2(builder, v, w);
            c.select_2(builder, v, w);

            return builder.finish__AND__recycle();
        }

        Object                          x = other_arguments[1];

        a.select_3(builder, v, w, x);
        b.select_3(builder, v, w, x);
        c.select_3(builder, v, w, x);

        return builder.finish__AND__recycle();
    }


    public void                         line(Zone z, Object v, Object ... other_arguments)
    {
        z.line(this.arrange(z, v, other_arguments));
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_3 " + this.a.portray(z) + " " + this.b.portray(z) + " " + this.c.portray(z) + ">";
    }
}
