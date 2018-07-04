//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    MessageFormatter_1__Prefix
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_1__Prefix");


    //
    //  Members
    //
    private String                      prefix;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Prefix(String prefix)
    {
        this.prefix = prefix;
    }


    static public MessageFormatter_1__Prefix    create(Zone z, String prefix)
    {
        String                          interned__prefix = z.intern_permenant_string(prefix);
            
        return new MessageFormatter_1__Prefix(interned__prefix);
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
        return this.prefix + z.portray(v);
    }


    public String                       portray(Zone z)
    {
        return "<MessageFormatter_1__Prefix " + z.quote_string(this.prefix) + ">";
    }
}
