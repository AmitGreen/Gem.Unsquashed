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


public class    MessageFormatter_1__Suffix
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_1__Suffix");


    //
    //  Members
    //
    private String                      prefix_0;
    private String                      suffix;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Suffix(String prefix_0, String suffix)
    {
        this.prefix_0 = prefix_0;
        this.suffix   = suffix;
    }


    static public MessageFormatter_1__Suffix    create(Zone z, String prefix_0, String suffix)
    {
        String                          interned__prefix_0 = z.intern_permenant_string_0(prefix_0);
        String                          interned__suffix   = z.intern_permenant_string  (suffix);

        return new MessageFormatter_1__Suffix(interned__prefix_0, suffix);
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
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        final Zone                      z = builder.z;

        builder.append(this.prefix_0, z.portray(v), this.suffix);
    }

    
    public String                       portray(Zone z)
    {
        String                          prefix_0 = this.prefix_0;
        String                          suffix   = this.suffix;

        return (
                     "<MessageFormatter_1__Suffix "
                   + (prefix_0 == null ? "<null>" : z.quote_string(prefix_0))
                   + " "
                   + z.quote_string(suffix)
                   + ">"
              );
    }
}
