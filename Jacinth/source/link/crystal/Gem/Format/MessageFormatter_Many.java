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
        if (this.expected != 1) {
            z.RAISE_runtime_exception("1 argument given (expected {})", this.expected);
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


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            z.RAISE_runtime_exception("2 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                    i = 0; i < segment_total; i ++) {
            SegmentFormattable      segment = segment_many[i];

            segment.choose(builder, v, w);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x)
    {
        if (this.expected != 3) {
            z.RAISE_runtime_exception("3 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, v, w, x);
        }

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x, Object y)
    {
        if (this.expected != 4) {
            z.RAISE_runtime_exception("4 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.choose(builder, v, w, x, y);
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
            z.RAISE_runtime_exception("5 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                    i = 0; i < segment_total; i ++) {
            SegmentFormattable      segment = segment_many[i];

            segment.choose(builder, v, w, x, y4, y5);
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
            z.RAISE_runtime_exception("6 arguments given (expected {})", this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        Object []                       other_arguments = new Object[1];

        other_arguments[0] = y6;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.select_many(builder, v, w, x, y4, y5, other_arguments);
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
            z.RAISE_runtime_exception("{} arguments given (expected {})", actual, this.expected);
        }

        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        int                             adjusted_total = actual - 5;
        Object []                       adjusted       = new Object[adjusted_total];

        adjusted[0] = y6;
        adjusted[1] = y7;

        for (int                        i = 2; i < adjusted_total; i ++) {
            adjusted[i] = adjusted[i - 2];
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            segment.select_many(builder, v, w, x, y4, y5, adjusted);
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
