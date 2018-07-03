//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.OutputFunctions;


public class    MessageFormatter_4
    extends     Gem_Object<Inspection>
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
    public String                       arrange(Zone z, Object first_argument, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual   = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("MessageFormatter_4.arrange: {0} arguments given (expected {1})",
                                    actual,
                                    expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;
        SegmentFormattable              d = this.d;

        String                          argument_1 = z.portray(first_argument);
        String                          argument_2 = z.portray(other_arguments[0]);

        StringBuilder                   builder = new StringBuilder();

        if (expected == 2) {
            builder.append(a.select_2(z, argument_1, argument_2));
            builder.append(b.select_2(z, argument_1, argument_2));
            builder.append(c.select_2(z, argument_1, argument_2));
            builder.append(d.select_2(z, argument_1, argument_2));

            return builder.toString();
        }

        String                          argument_3 = z.portray(other_arguments[1]);

        if (expected == 3) {
            builder.append(a.select_3(z, argument_1, argument_2, argument_3));
            builder.append(b.select_3(z, argument_1, argument_2, argument_3));
            builder.append(c.select_3(z, argument_1, argument_2, argument_3));
            builder.append(d.select_3(z, argument_1, argument_2, argument_3));

            return builder.toString();
        }

        String                          argument_4 = z.portray(other_arguments[2]);

        builder.append(a.select_4(z, argument_1, argument_2, argument_3, argument_4));
        builder.append(b.select_4(z, argument_1, argument_2, argument_3, argument_4));
        builder.append(c.select_4(z, argument_1, argument_2, argument_3, argument_4));
        builder.append(d.select_4(z, argument_1, argument_2, argument_3, argument_4));

        return builder.toString();
    }


    public void                         line(Zone z, Object first_argument, Object ... other_arguments)
    {
        z.line(this.arrange(z, first_argument, other_arguments));
    }


    public String                       portray()
    {
        return "<MessageFormatter_4 " + this.a.portray() + " " + this.b.portray() + " " + this.c.portray() + ">";
    }
}
