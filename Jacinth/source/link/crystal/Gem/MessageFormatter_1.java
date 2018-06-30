//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    MessageFormatter_1
    extends     GemObject<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via GemObject
{
    private static Inspection           inspection = Inspection.create("Gem.MessageFormatter_1");


    //
    //  Members
    //
    private String                      prefix_0;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1(String prefix_0)
    {
        this.prefix_0 = prefix_0;
    }


    static public MessageFormatter_1    create(String prefix_0)
    {
        String                          interned__prefix_0 = intern_permenant_string_0(prefix_0);
            
        return new MessageFormatter_1(interned__prefix_0);
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
                          "MessageFormatter_1.arrange: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        String                          prefix_0 = this.prefix_0;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix_0 == null) {
            return first;
        }

        return prefix_0 + first;
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1.line: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        String                          prefix_0 = this.prefix_0;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix_0 == null) {
            standard_output.println(first);
        }

        standard_output.println(prefix_0 + first);
    }
}
