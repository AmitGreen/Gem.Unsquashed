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


public class    MessageFormatter_2
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_2");


    //
    //  Members
    //
    private SegmentFormattable          a;
    private SegmentFormattable          b;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_2(SegmentFormattable a, SegmentFormattable b)
    {
        this.a = a;
        this.b = b;
    }


    static public MessageFormatter_2    create(Zone z, SegmentFormattable a, SegmentFormattable b)
    {
        return new MessageFormatter_2(a, b);
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
        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;

        int                             actual   = 1;
        int                             expected = (a == b ? 1 : 2);

        if (actual != expected) {
            z.RAISE_runtime_exception("{0} arguments given (expected {1})", actual, expected);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        depth += 1;

        a.choose(builder, depth, v);
        b.choose(builder, depth, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        a.select_2(builder, v, w);
        b.select_2(builder, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object ... other_arguments)
    {
        z.INVALID_ROUTINE();
        return null;
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
        return "<MessageFormatter_2 " + this.a.portray(z) + " " + this.b.portray(z) + ">";
    }
}
