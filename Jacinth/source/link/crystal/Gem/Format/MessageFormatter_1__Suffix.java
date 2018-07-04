//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.OutputFunctions;


public class    MessageFormatter_1__Suffix
    extends     Gem_Object<Inspection>
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
    public String                       arrange(Zone z, Object v)
    {
        String                          prefix_0 = this.prefix_0;
        String                          suffix = this.suffix;

        String                          first = z.portray(v);

        if (prefix_0 == null) {
            return first + suffix;
        }

        return prefix_0 + first + suffix;
    }


    public String                       arrange(Zone z, Object v, Object ... other_arguments)
    {
        z.RAISE_runtime_exception("should never get called");

        return null;
    }


    public void                         line(Zone z, Object v)
    {
        String                          prefix_0 = this.prefix_0;
        String                          suffix   = this.suffix;

        String                          first = z.portray(v);

        if (prefix_0 == null) {
            z.line(first + suffix);
            return;
        }

        z.line(prefix_0 + first + suffix);
    }


    public void                         line(Zone z, Object v, Object ... other_arguments)
    {
        z.RAISE_runtime_exception("should never get called");
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
