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


public class    MessageFormatter_3
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_3");


    //
    //  Members
    //
    private int                         expected;
    private SegmentFormattable          a;
    private SegmentFormattable          b;
    private SegmentFormattable          c;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_3(
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
        this.c        = c;
    }


    static public MessageFormatter_3    create(
            Zone                            z,
            int                             expected,
            SegmentFormattable              a,
            SegmentFormattable              b,
            SegmentFormattable              c//,
        )
    {
        if ( ! (1 <= expected && expected <= 3)) {
            z.RAISE_runtime_exception("MessageFormatter_3.create: invalid value for `expected`<{0}>", expected);
        }

        return new MessageFormatter_3(expected, a, b, c);
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

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);
        this.c.choose(builder, depth, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        int                             expected = this.expected;

        int                             actual = 2;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        this.a.select_2(builder, v, w);
        this.b.select_2(builder, v, w);
        this.c.select_2(builder, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object ... other_arguments)
    {
        int                             expected = this.expected;

        int                             actual = 1 + other_arguments.length;

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;
        SegmentFormattable              c = this.c;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        if (expected == 2) {
            a.select_2(builder, v, w);
            b.select_2(builder, v, w);
            c.select_2(builder, v, w);

            return builder.finish__AND__recycle();
        }

        Object                          x = other_arguments[0];

        a.select_3(builder, v, w, x);
        b.select_3(builder, v, w, x);
        c.select_3(builder, v, w, x);

        return builder.finish__AND__recycle();
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_3 " + this.a.portray(z) + " " + this.b.portray(z) + " " + this.c.portray(z) + ">";
    }
}
