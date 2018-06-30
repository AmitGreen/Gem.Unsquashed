//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.GemObject;
import link.crystal.Gem.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.MessageFormattable;


class           MessageFormatter_1__Suffix
    extends     GemObject<Inspection>
//  extends     Object
    implements  MessageFormattable,
                Inspectable<Inspection>//,                              //  Via GemObject
{
    private static Inspection           inspection = Inspection.create("Gem.MessageFormatter_1__Suffix");


    //
    //  Members
    //
    private String                      prefix;                         //  May be `null`
    private String                      suffix;                         //  May be `null`


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Suffix(String prefix, String suffix)
    {
        this.prefix = prefix;
        this.suffix = suffix;
    }


    static public MessageFormatter_1__Suffix    create(String prefix, String suffix)
    {
        return new MessageFormatter_1__Suffix(prefix, suffix);
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
                          "MessageFormatter_1__Suffix.arrange: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        String                          prefix = this.prefix;
        String                          suffix = this.suffix;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix == null) {
            return first + suffix;
        }

        return prefix + first + suffix;
    }


    public void                         line(Object first_argument, Object ... other_arguments)
    {
        if (other_arguments.length != 0) {
            throw new RuntimeException(
                    (
                          "MessageFormatter_1__Suffix.line: "
                        + Integer.toString(1 + other_arguments.length)
                        + " arguments given (expected 1)"
                    )
                );
        }

        String                          prefix = this.prefix;
        String                          suffix = this.suffix;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix == null) {
            standard_output.println(first + suffix);
        }

        standard_output.println(prefix + first + suffix);
    }
}
