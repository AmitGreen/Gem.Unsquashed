//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    MessageFormatter_Many
    extends     MessageFormatter_Base<Inspection>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("MessageFormatter_Many");


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
        assert fact_between(2, expected, segment_many.length);

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
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth)
    {
        if (this.expected != 0) {
            RUNTIME("0 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth);
        }
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        if (this.expected != 1) {
            RUNTIME("1 argument given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v);
        }
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            RUNTIME("2 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w);
        }
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        if (this.expected != 3) {
            RUNTIME("3 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x);
        }
    }


    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        )
    {
        if (this.expected != 4) {
            RUNTIME("4 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y);
        }
    }


    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        if (this.expected != 5) {
            RUNTIME("5 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5);
        }
    }


    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
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
            RUNTIME("6 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6);
        }
    }


    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
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
        final int                       actual = 7 + other_arguments.length;

        if (this.expected != actual) {
            RUNTIME("{} arguments given (expected {})", actual, this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (int                        i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6, y7, other_arguments);
        }
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        int                             expected     = this.expected;
        SegmentFormattable[]            segment_many = this.segment_many;

        int                             segment_total = segment_many.length;

        builder.append("<MessageFormatter_Many expected<", expected, "> total<", segment_total, ">;");

        for (int                        i = 0; i < segment_total; i ++) {
            SegmentFormattable          segment = segment_many[i];

            builder.append(" ");
            builder.portray(segment);
        }

        builder.append(">");
    }
}
