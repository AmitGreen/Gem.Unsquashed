//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Inspection.Inspection;


public final class  MessageFormatter_4
    extends         MessageFormatter_Base<Inspection>
//  extends         Gem_Object           <Inspection>
//  extends         Object
    implements      MessageFormattable   <Inspection>,
                    Inspectable          <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("MessageFormatter_4");


    //
    //  Members
    //
    private final int                   expected;
    private final SegmentFormattable    a;
    private final SegmentFormattable    b;
    private final SegmentFormattable    c;
    private final SegmentFormattable    d;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_4(
            final int                       expected,
            final SegmentFormattable        a,
            final SegmentFormattable        b,
            final SegmentFormattable        c,
            final SegmentFormattable        d//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
        this.d        = d;
    }


    public static final MessageFormatter_4  create(
            final Zone                      z,
            final int                       expected,
            final SegmentFormattable        a,
            final SegmentFormattable        b,
            final SegmentFormattable        c,
            final SegmentFormattable        d//,
        )
    {
        return new MessageFormatter_4(expected, a, b, c, d);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<MessageFormatter_4 ");
        builder.portray(this.a);
        builder.append(" ");
        builder.portray(this.b);
        builder.append(" ");
        builder.portray(this.c);
        builder.append(" ");
        builder.portray(this.d);
        builder.append(">");
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public final void                   augment(final Gem_StringBuilder builder, int depth)
    {
        if (this.expected != 0) {
            RUNTIME("0 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth);
        this.b.choose(builder, depth);
        this.c.choose(builder, depth);
        this.d.choose(builder, depth);
    }


    @Override
    public final void                   augment(final Gem_StringBuilder builder, /*:*/ int depth, final Object v)
    {
        if (this.expected != 1) {
            RUNTIME("1 argument given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);
        this.c.choose(builder, depth, v);
        this.d.choose(builder, depth, v);
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w//,
        )
    {
        if (this.expected != 2) {
            RUNTIME("2 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w);
        this.b.choose(builder, depth, v, w);
        this.c.choose(builder, depth, v, w);
        this.d.choose(builder, depth, v, w);
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        )
    {
        if (this.expected != 3) {
            RUNTIME("3 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w, x);
        this.b.choose(builder, depth, v, w, x);
        this.c.choose(builder, depth, v, w, x);
        this.d.choose(builder, depth, v, w, x);
    }


    @Override
    public final void                   augment(
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

        depth += 1;

        this.a.choose(builder, depth, v, w, x, y);
        this.b.choose(builder, depth, v, w, x, y);
        this.c.choose(builder, depth, v, w, x, y);
        this.d.choose(builder, depth, v, w, x, y);
    }


    @Override
    public final void                   augment_1_plus(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object ...                    other_arguments//,
        )
    {
        final int                       actual = 1 + other_arguments.length;

        if (this.expected != actual) {
            RUNTIME("{} argument{} given (expected {})",
                    actual,
                    (actual == 1 ? "" : "s"),
                    this.expected);
        }

        depth += 1;

        if (actual == 1) {
            this.a.choose(builder, depth, v);
            this.b.choose(builder, depth, v);
            this.c.choose(builder, depth, v);
            this.d.choose(builder, depth, v);
            return;
        }

        final Object                    w = other_arguments[0];

        if (actual == 2) {
            this.a.choose(builder, depth, v, w);
            this.b.choose(builder, depth, v, w);
            this.c.choose(builder, depth, v, w);
            this.d.choose(builder, depth, v, w);
            return;
        }

        final Object                    x = other_arguments[1];

        if (actual == 3) {
            this.a.choose(builder, depth, v, w, x);
            this.b.choose(builder, depth, v, w, x);
            this.c.choose(builder, depth, v, w, x);
            this.d.choose(builder, depth, v, w, x);
            return;
        }

        assert fact(actual == 4, "actual == 4");

        final Object                    y = other_arguments[2];

        this.a.choose(builder, depth, v, w, x, y);
        this.b.choose(builder, depth, v, w, x, y);
        this.c.choose(builder, depth, v, w, x, y);
        this.d.choose(builder, depth, v, w, x, y);
    }
}
