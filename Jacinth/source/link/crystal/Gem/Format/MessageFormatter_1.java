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


public class    MessageFormatter_1
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_1");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable          a;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1(int expected, SegmentFormattable a)
    {
        this.expected = expected;
        this.a        = a;
    }


    static public MessageFormatter_1    create(Zone z, int expected, SegmentFormattable a)
    {
        if ( ! (0 <= expected && expected <= 1)) {
            z.RUNTIME("invalid value for `expected`<{}>", expected);
        }

        return new MessageFormatter_1(expected, a);
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

        this.a.choose(builder, depth + 1);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v)
    {
        if (this.expected != 1) {
            z.RUNTIME("1 arguments given (expected {})", this.expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.choose(builder, depth + 1, v);

        return builder.finish__AND__recycle();
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_2 " + Integer.toString(this.expected) + " " + this.a.portray(z) + ">";
    }
}
