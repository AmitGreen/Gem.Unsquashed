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


public class    MessageFormatter_2
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_2");


    //
    //  Members
    //
    private final int                   expected;
    private SegmentFormattable          a;
    private SegmentFormattable          b;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_2(int expected, SegmentFormattable a, SegmentFormattable b)
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
    }


    static public MessageFormatter_2    create(Zone z, int expected, SegmentFormattable a, SegmentFormattable b)
    {
        if (a == null) {
            z.RUNTIME("`a` == null");
        }

        if (b == null) {
            z.RUNTIME("`b` == null");
        }

        return new MessageFormatter_2(expected, a, b);
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

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        this.a.choose(builder, depth);
        this.b.choose(builder, depth);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v)
    {
        if (this.expected != 1) {
            z.RUNTIME("1 argument given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        if (this.expected != 2) {
            z.RUNTIME("2 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        this.a.choose(builder, depth, v, w);
        this.b.choose(builder, depth, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_2 " + this.a.portray(z) + " " + this.b.portray(z) + ">";
    }
}
