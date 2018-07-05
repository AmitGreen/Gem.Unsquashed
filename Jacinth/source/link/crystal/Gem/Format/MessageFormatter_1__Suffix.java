//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    MessageFormatter_1__Suffix
    extends     MessageFormatter_Base<Inspection>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("MessageFormatter_1__Suffix");


    //
    //  Members
    //
    private String                      prefix;
    private String                      suffix;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Suffix(String prefix, String suffix)
    {
        this.prefix = prefix;
        this.suffix = suffix;
    }


    static public MessageFormatter_1__Suffix    create(Zone z, String prefix, String suffix)
    {
        String                          interned__prefix = z.intern_permenant_string(prefix);
        String                          interned__suffix = z.intern_permenant_string(suffix);

        return new MessageFormatter_1__Suffix(interned__prefix, suffix);
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
        builder.append(this.prefix);
        builder.portray(v);
        builder.append(this.suffix);
    }

    
    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<MessageFormatter_1__Suffix ");
        builder.quote(this.prefix);
        builder.append(" ");
        builder.quote(this.suffix);
        builder.append(">");
    }
}
