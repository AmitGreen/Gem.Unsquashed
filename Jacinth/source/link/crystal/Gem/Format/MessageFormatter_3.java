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


public final class  MessageFormatter_3
    extends         MessageFormatter_Base<Inspection>
//  extends         Gem_Object           <Inspection>
//  extends         Object
    implements      MessageFormattable   <Inspection>,
                    Inspectable          <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("MessageFormatter_3");


    //
    //  Members
    //
    private final int                   expected;
    private final SegmentFormattable    a;
    private final SegmentFormattable    b;
    private final SegmentFormattable    c;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_3(
            final int                       expected,
            final SegmentFormattable        a,
            final SegmentFormattable        b,
            final SegmentFormattable        c//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
    }


    public static final MessageFormatter_3  create(
            final Zone                      z,
            final int                       expected,
            final SegmentFormattable        a,
            final SegmentFormattable        b,
            final SegmentFormattable        c//,
        )
    {
        return new MessageFormatter_3(expected, a, b, c);
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
        builder.append("<MessageFormatter_3 ");
        builder.portray(this.a);
        builder.append(" ");
        builder.portray(this.b);
        builder.append(" ");
        builder.portray(this.c);
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
    }
}
