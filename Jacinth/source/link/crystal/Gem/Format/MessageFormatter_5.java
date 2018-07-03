//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.OutputFunctions;
import link.crystal.Gem.Support.PortrayFunctions;


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
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d,
            SegmentFormattable              e//,
        )
    {
        if ( ! (2 <= expected && expected <= 5)) {
            throw new RuntimeException("MessageFormatter_5.create: invalid value for `expected`<" + Integer.toString(expected) + ">");
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
    public String                       arrange(Object first_argument, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual   = 1 + other_arguments.length;

        if (actual != expected) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_5.arrange: "
                        + Integer.toString(actual)
                        + " arguments given (expected "
                        + Integer.toString(expected)
                        + ")"
                    )
                );
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;
        SegmentFormattable              d = this.d;
        SegmentFormattable              e = this.e;

        String                          argument_1 = PortrayFunctions.portray(first_argument);
        String                          argument_2 = PortrayFunctions.portray(other_arguments[0]);

        StringBuilder                   builder = new StringBuilder();

        if (expected == 2) {
            builder.append(a.select_2(argument_1, argument_2));
            builder.append(b.select_2(argument_1, argument_2));
            builder.append(c.select_2(argument_1, argument_2));
            builder.append(d.select_2(argument_1, argument_2));
            builder.append(e.select_2(argument_1, argument_2));

            return builder.toString();
        }

        String                          argument_3 = PortrayFunctions.portray(other_arguments[1]);

        if (expected == 3) {
            builder.append(a.select_3(argument_1, argument_2, argument_3));
            builder.append(b.select_3(argument_1, argument_2, argument_3));
            builder.append(c.select_3(argument_1, argument_2, argument_3));
            builder.append(d.select_3(argument_1, argument_2, argument_3));
            builder.append(e.select_3(argument_1, argument_2, argument_3));

            return builder.toString();
        }

        String                          argument_4 = PortrayFunctions.portray(other_arguments[2]);

        if (expected == 4) {
            builder.append(a.select_4(argument_1, argument_2, argument_3, argument_4));
            builder.append(b.select_4(argument_1, argument_2, argument_3, argument_4));
            builder.append(c.select_4(argument_1, argument_2, argument_3, argument_4));
            builder.append(d.select_4(argument_1, argument_2, argument_3, argument_4));
            builder.append(e.select_4(argument_1, argument_2, argument_3, argument_4));

            return builder.toString();
        }

        String                          argument_5 = PortrayFunctions.portray(other_arguments[3]);

        builder.append(a.select_5(argument_1, argument_2, argument_3, argument_4, argument_5));
        builder.append(b.select_5(argument_1, argument_2, argument_3, argument_4, argument_5));
        builder.append(c.select_5(argument_1, argument_2, argument_3, argument_4, argument_5));
        builder.append(d.select_5(argument_1, argument_2, argument_3, argument_4, argument_5));
        builder.append(e.select_5(argument_1, argument_2, argument_3, argument_4, argument_5));

        return builder.toString();
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        OutputFunctions.line(this.arrange(first_argument, other_arguments));
    }


    public String                       portray()
    {
        return "<MessageFormatter_5 " + this.a.portray() + " " + this.b.portray() + " " + this.c.portray() + ">";
    }
}
