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


public class    MessageFormatter_5
    extends     MessageFormatter_Base<Inspection>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("MessageFormatter_5");


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
            Zone                            z,
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c,
            SegmentFormattable              d,
            SegmentFormattable              e//,
        )
    {
        if ( ! (2 <= expected && expected <= 5)) {
            z.RUNTIME("invalid value for `expected`<{}>", expected);
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
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth)
    {
        if (this.expected != 0) {
            final Zone                  z = builder.z;

            z.RUNTIME("0 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth);
        this.b.choose(builder, depth);
        this.c.choose(builder, depth);
        this.d.choose(builder, depth);
        this.e.choose(builder, depth);
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        if (this.expected != 1) {
            final Zone                  z = builder.z;

            z.RUNTIME("1 argument given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);
        this.c.choose(builder, depth, v);
        this.d.choose(builder, depth, v);
        this.e.choose(builder, depth, v);
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            final Zone                  z = builder.z;

            z.RUNTIME("2 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w);
        this.b.choose(builder, depth, v, w);
        this.c.choose(builder, depth, v, w);
        this.d.choose(builder, depth, v, w);
        this.e.choose(builder, depth, v, w);
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        if (this.expected != 3) {
            final Zone                  z = builder.z;

            z.RUNTIME("3 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w, x);
        this.b.choose(builder, depth, v, w, x);
        this.c.choose(builder, depth, v, w, x);
        this.d.choose(builder, depth, v, w, x);
        this.e.choose(builder, depth, v, w, x);
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
            final Zone                  z = builder.z;

            z.RUNTIME("4 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w, x, y);
        this.b.choose(builder, depth, v, w, x, y);
        this.c.choose(builder, depth, v, w, x, y);
        this.d.choose(builder, depth, v, w, x, y);
        this.e.choose(builder, depth, v, w, x, y);
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
            final Zone                  z = builder.z;

            z.RUNTIME("5 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w, x, y4, y5);
        this.b.choose(builder, depth, v, w, x, y4, y5);
        this.c.choose(builder, depth, v, w, x, y4, y5);
        this.d.choose(builder, depth, v, w, x, y4, y5);
        this.e.choose(builder, depth, v, w, x, y4, y5);
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<MessageFormatter_5 ");
        builder.portray(this.a);
        builder.append(" ");
        builder.portray(this.b);
        builder.append(" ");
        builder.portray(this.c);
        builder.append(" ");
        builder.portray(this.d);
        builder.append(" ");
        builder.portray(this.e);
        builder.append(">");
    }
}
