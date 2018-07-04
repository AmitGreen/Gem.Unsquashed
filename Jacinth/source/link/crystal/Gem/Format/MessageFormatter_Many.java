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


public class    MessageFormatter_Many
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
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
            z.RUNTIME("invalid value for `expected`<{0}>", expected);
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
    public String                       arrange(Zone z, int depth)
    {
        if (this.expected != 0) {
            z.RUNTIME("0 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v)
    {
        if (this.expected != 1) {
            z.RUNTIME("1 argument given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            z.RUNTIME("2 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x)
    {
        if (this.expected != 3) {
            z.RUNTIME("3 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w, x);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x, Object y)
    {
        if (this.expected != 4) {
            z.RUNTIME("4 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y);
        }

        return builder.finish__AND__recycle();
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
        int                             expected = this.expected;

        if (this.expected != 5) {
            z.RUNTIME("5 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        if (this.expected != 6) {
            z.RUNTIME("6 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        int                             expected = this.expected;

        int                             actual = 7 + other_arguments.length;

        if (this.expected != actual) {
            z.RUNTIME("{} arguments given (expected {})", actual, this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6, y7, other_arguments);
        }

        return builder.finish__AND__recycle();
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
