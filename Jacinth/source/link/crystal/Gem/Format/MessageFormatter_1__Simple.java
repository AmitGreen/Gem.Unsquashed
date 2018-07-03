//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.OutputFunctions;
import link.crystal.Gem.Support.PortrayFunctions;


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
            RAISE_runtime_exception("MessageFormatter_1__Simple.arrange: {0} arguments given (expected 1)",
                                    1 + other_arguments.length);
        }

        return PortrayFunctions.portray(first_argument);
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            RAISE_runtime_exception("MessageFormatter_1__Simple.line: {0} arguments given (expected 1)",
                                    1 + other_arguments.length);
        }

        OutputFunctions.line(PortrayFunctions.portray(first_argument));
    }


    public String                       portray()
    {
        return "<MessageFormatter_1__Simple>";
    }
}
