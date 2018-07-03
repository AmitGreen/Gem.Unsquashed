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


public class    MessageFormatter_Many
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_Many");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable[]        segment_many;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_Many(int expected, SegmentFormattable[] segment_many)
    {
        this.expected     = expected;
        this.segment_many = segment_many;
    }


    static public MessageFormatter_Many     create(Zone z, int expected, SegmentFormattable[] segment_many)
    {
        if ( ! (2 <= expected && expected <= segment_many.length)) {
            z.RAISE_runtime_exception("MessageFormatter_Many.create: invalid value for `expected`<{0}>", expected);
        }

        return new MessageFormatter_Many(expected, segment_many);
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
            z.RAISE_runtime_exception("MessageFormatter_Many.arrange: {0} arguments given (expected {1})",
                                      actual,
                                      expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        String                          argument_1 = z.portray(first_argument);
        String                          argument_2 = z.portray(other_arguments[0]);

        StringBuilder                   builder = new StringBuilder();

        if (expected == 2) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                builder.append(segment.select_2(z, argument_1, argument_2));
            }

            return builder.toString();
        }

        String                          argument_3 = z.portray(other_arguments[1]);

        if (expected == 3) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                builder.append(segment.select_3(z, argument_1, argument_2, argument_3));
            }

            return builder.toString();
        }

        String                          argument_4 = z.portray(other_arguments[2]);

        if (expected == 4) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                builder.append(segment.select_4(z, argument_1, argument_2, argument_3, argument_4));
            }

            return builder.toString();
        }

        String                          argument_5 = z.portray(other_arguments[3]);

        if (expected == 5) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                builder.append(segment.select_5(z, argument_1, argument_2, argument_3, argument_4, argument_5));
            }


            return builder.toString();
        }

        String[]                        argument_many = new String[expected];

        argument_many[0] = argument_1;
        argument_many[1] = argument_2;
        argument_many[2] = argument_3;
        argument_many[3] = argument_4;
        argument_many[4] = argument_5;

        for (int                        i = 5; i < expected; i ++) {
            argument_many[i] = z.portray(other_arguments[i - 1]);
        }

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            builder.append(segment.select_many(z, argument_many));
        }

        return builder.toString();
    }


    public void                         line(Zone z, Object first_argument, Object ... other_arguments)
    {
        z.line(this.arrange(z, first_argument, other_arguments));
    }


    public String                       portray()
    {
        int                             expected     = this.expected;
        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        StringBuilder                   builder = new StringBuilder();

        builder.append("<MessageFormatter_Many expected<");
        builder.append(Integer.toString(expected));
        builder.append("> total<");
        builder.append(Integer.toString(segment_total));
        builder.append(">;");

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            builder.append(" ");
            builder.append(segment.portray());
        }

        builder.append(">");

        return builder.toString();
    }
}
