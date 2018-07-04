//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.OutputFunctions;


public class    MessageFormatter_1__Simple
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_1__Simple");


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Simple()
    {
    }


    static public MessageFormatter_1__Simple    create(Zone z)
    {
        return new MessageFormatter_1__Simple();
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
        return z.portray(v);
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object ... other_arguments)
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public void                         line(Zone z, int depth, Object v)
    {
        z.line(z.portray(v));
    }


    public void                         line(Zone z, int depth, Object v, Object ... other_arguments)
    {
        z.RAISE_runtime_exception("should never get called");
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_1__Simple>";
    }
}
