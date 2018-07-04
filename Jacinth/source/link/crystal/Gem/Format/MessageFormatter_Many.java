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
    public String                       arrange(Zone z, int depth, Object v)
    {
        int                             expected = this.expected;

        int                             actual = 1;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                    i = 0; i < segment_total; i ++) {
            SegmentFormattable      segment = segment_many[i];

            segment.choose(builder, depth, v);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        Object                          w = other_arguments[0];

        if (expected == 2) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                segment.select_2(builder, v, w);
            }

            return builder.finish__AND__recycle();
        }

        Object                          x = other_arguments[1];

        if (expected == 3) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                segment.select_3(builder, v, w, x);
            }

            return builder.finish__AND__recycle();
        }

        Object                          y = other_arguments[2];

        if (expected == 4) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                segment.select_4(builder, v, w, x, y);
            }

            return builder.toString();
        }

        Object                          z5 = other_arguments[3];

        if (expected == 5) {
            for (int                    i = 0; i < segment_total; i ++) {
                SegmentFormattable      segment = segment_many[i];

                segment.select_5(builder, v, w, x, y, z5);
            }


            return builder.finish__AND__recycle();
        }

        Object[]                        adjusted_other_arguments = new Object[expected - 5];

        for (int                        i = 5; i < expected; i ++) {
            adjusted_other_arguments[i - 5] = other_arguments[i - 1];
        }

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.select_many(builder, v, w, x, y, z5, adjusted_other_arguments);
        }

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
            builder.append(segment.portray(z));
        }

        builder.append(">");

        return builder.toString();
    }
}
