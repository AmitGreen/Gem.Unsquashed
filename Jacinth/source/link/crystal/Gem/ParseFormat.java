//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.StringBuilder;
import java.lang.System;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.MessageFormattable;


public abstract class   ParseFormat
    extends             Object
{
    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;
    public static final Matcher         braces_matcher  = Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?").matcher("");


    //
    //  Public
    //
    public static void                  line()
    {
        standard_output.println();
    }


    public static void                  line(String s)
    {
        standard_output.println(s);
    }


    public static MessageFormattable    parse_format(String format)
    {
        braces_matcher.reset(format);

        boolean                         found = braces_matcher.find();

        if ( ! found) {
            throw new RuntimeException("SilverObject.line: format string does not contain the opening brace '{': " + portray_string(format));
        }

        int                             end_2 = braces_matcher.end(2);

        if (end_2 == -1) {
            throw new RuntimeException("SilverObject.line: format string is malformed': " + portray_string(format));
        }

        int                             start        = braces_matcher.start();
        int                             first_number = 0;
        String                          start_s      = null;

        if (end_2 - start == 3) {
            first_number = format.codePointAt(start + 1) - 48;
        } else {
            first_number = Integer.parseInt(braces_matcher.group(1));
        }

        if (start > 0) {
            start_s = format.substring(0, start);
        }

        line("start: " + start);
        line("start_s: " + portray_string(start_s));
        line("group: " + Integer.toString(first_number));
        line("end_2: " + Integer.toString(end_2));
        //line("end_2: " + portray_string(end_s));

        found = braces_matcher.find();

        if (found) {
            throw new RuntimeException("SilverObject.line: unimplemented, more than one '{#}': " + portray_string(format));
        }

        if (end_2 == format.length()) {
            return MessageFormatter_1.create(start_s);
        }

        String                          end_s = format.substring(end_2);

        throw new RuntimeException("SilverObject.line: #2");
    }
}


class           MessageFormatter_1
    extends     Object
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
}
