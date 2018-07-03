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
        String                          interned__prefix_0 = intern_permenant_string_0(prefix_0);
        String                          interned__suffix   = intern_permenant_string  (suffix);

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
    public String                       arrange(Zone z, Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            z.RAISE_runtime_exception("MessageFormatter_1__Suffix.arrange: {0} arguments given (expected 1)",
                                    1 + other_arguments.length);
        }

        String                          prefix_0 = this.prefix_0;
        String                          suffix = this.suffix;

        String                          first = portray(first_argument);

        if (prefix_0 == null) {
            return first + suffix;
        }

        return prefix_0 + first + suffix;
    }


    public void                         line(Zone z, Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            z.RAISE_runtime_exception("MessageFormatter_1__Simple.line: {0} arguments given (expected 1)",
                                    1 + other_arguments.length);
        }

        String                          prefix_0 = this.prefix_0;
        String                          suffix   = this.suffix;

        String                          first = portray(first_argument);

        if (prefix_0 == null) {
            z.line(first + suffix);
            return;
        }

        z.line(prefix_0 + first + suffix);
    }


    public String                       portray()
    {
        String                          prefix_0 = this.prefix_0;
        String                          suffix   = this.suffix;

        return (
                     "<MessageFormatter_1__Suffix "
                   + (prefix_0 == null ? "<null>" : portray_string(prefix_0))
                   + " "
                   + portray_string(suffix)
                   + ">"
              );
    }
} 
