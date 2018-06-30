//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    MessageFormatter_1__Simple
    extends     GemObject<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via GemObject
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_1__Simple");


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Simple()
    {
    }


    static public MessageFormatter_1__Simple    create()
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
    public String                       arrange(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1__Simple.arrange: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        return PortrayFunctions.portray(first_argument);
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1__Simple.line: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        standard_output.println(PortrayFunctions.portray(first_argument));
    }


    public String                       portray()
    {
        return "<MessageFormatter_1__Simple>";
    }
}
