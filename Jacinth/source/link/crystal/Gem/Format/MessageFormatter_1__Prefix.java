//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.PortrayFunctions;


public class    MessageFormatter_1__Prefix
    extends     Gem_Object<Inspection>
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


    static public MessageFormatter_1__Prefix    create(String prefix)
    {
        String                          interned__prefix = intern_permenant_string(prefix);
            
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
    public String                       arrange(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1__Prefix.arrange: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        return this.prefix + PortrayFunctions.portray(first_argument);
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1__Prefix.line: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        standard_output.println(this.prefix + PortrayFunctions.portray(first_argument));
    }


    public String                       portray()
    {
        return "<MessageFormatter_1__Prefix " + PortrayFunctions.portray_string(this.prefix) + ">";
    }
}
