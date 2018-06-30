//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.io.PrintStream;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.GemObject;
import link.crystal.Gem.MessageFormattable;


class           MessageFormatter_1
    extends     GemObject
    implements  MessageFormattable
{
    //
    //  Members
    //
    private String                      prefix;                         //  May be `null`


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1(String prefix)
    {
        this.prefix = prefix;
    }


    static public MessageFormatter_1    create(String prefix)
    {
        return new MessageFormatter_1(prefix);
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

        String                          prefix = this.prefix;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix == null) {
            return first;
        }

        return prefix + first;
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

        String                          prefix = this.prefix;

        String                          first = ParseFormat.portray(first_argument);

        if (prefix == null) {
            standard_output.println(first);
        }

        standard_output.println(prefix + first);
    }
}
