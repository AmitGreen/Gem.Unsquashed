//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.OutputFunctions;
import link.crystal.Gem.Support.PortrayFunctions;


public class    MessageFormatter_2
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MessageFormatter_2");


    //
    //  Members
    //
    private SegmentFormattable          a;
    private SegmentFormattable          b;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_2(SegmentFormattable a, SegmentFormattable b)
    {
        this.a = a;
        this.b = b;
    }


    static public MessageFormatter_2    create(SegmentFormattable a, SegmentFormattable b)
    {
        return new MessageFormatter_2(a, b);
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
        SegmentFormattable              a = this.a;
        SegmentFormattable              b = this.b;

        int                             actual   = 1 + other_arguments.length;
        int                             expected = (a == b ? 1 : 2);

        if (actual != expected) {
            raise_runtime_exception("MessageFormatter_2.arrange: {0} arguments given (expected {1})",
                                    actual,
                                    expected);
        }

        String                          argument_1 = PortrayFunctions.portray(first_argument);

        if (expected == 1) {
            return argument_1 + argument_1;
        }

        String                          argument_2 = PortrayFunctions.portray(other_arguments[0]);

        return (
                     this.a.select_2(argument_1, argument_2)
                   + this.b.select_2(argument_1, argument_2)
               );
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        OutputFunctions.line(this.arrange(first_argument, other_arguments));
    }


    public String                       portray()
    {
        return "<MessageFormatter_2 " + this.a.portray() + " " + this.b.portray() + ">";
    }
}
