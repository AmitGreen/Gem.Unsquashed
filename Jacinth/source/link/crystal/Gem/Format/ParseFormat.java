//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_1__Simple;
import link.crystal.Gem.Format.MessageFormatter_1__Suffix;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.MessageFormattable;


public abstract class   ParseFormat
    extends             GemObject//<Inspection>
{
    private static Inspection           inspection = Inspection.create("Gem.Core.ParseFormat");


    //
    //  Private static
    //
    private static final Matcher                braces_matcher = (
            Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?").matcher("")
        );



    public static MessageFormattable    parse_format(String format)
    {
        braces_matcher.reset(format);

        if ( ! braces_matcher.find()) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable.conjure: format string does not contain the opening brace '{': "
                        + PortrayFunctions.portray_string(format)
                    )
                );
        }

        //
        //  First argument
        //
        int                             end_2 = braces_matcher.end(2);

        if (end_2 == -1) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable.conjure: format string is malformed: "
                        + PortrayFunctions.portray_string(format)
                    )
                );
        }

        int                             start          = braces_matcher.start();
        int                             argument_index = 0;
        String                          start_s        = null;

        if (end_2 - start == 3) {
            argument_index = format.codePointAt(start + 1) - 48;
        } else {
            argument_index = Integer.parseInt(braces_matcher.group(1));
        }

        if (0 < start) {
            start_s = format.substring(0, start);
        }

        if ( ! braces_matcher.find()) {
            if (argument_index != 0) {
                throw new RuntimeException(
                        (
                              "PermenantMessageFormattable.conjure: format string must use {0} for only one argument: "
                            + PortrayFunctions.portray_string(format)
                        )
                    );
            }

            MessageFormattable          r = null;

            if (end_2 == format.length()) {
                if (start_s == null) {
                    return MessageFormatter_1__Simple.create();
                }

                return MessageFormatter_1__Prefix.create(start_s);
            }

            return MessageFormatter_1__Suffix.create(start_s, format.substring(end_2));
        }


        //
        //  Second argument
        //
        int                         last = end_2;

        end_2 = braces_matcher.end(2);

        if (end_2 == -1) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable.conjure: format string is malformed: "
                        + PortrayFunctions.portray_string(format)
                    )
                );
        }

        start          = braces_matcher.start();
        argument_index = 0;
        start_s        = null;

        if (end_2 - start == 3) {
            argument_index = format.codePointAt(start + 1) - 48;
        } else {
            argument_index = Integer.parseInt(braces_matcher.group(1));
        }

        if (last < start) {
            start_s = format.substring(last, start);
        }

        GemObject.line("start: " + start);
        GemObject.line("start_s: " + PortrayFunctions.portray_string(start_s));
        GemObject.line("group: " + Integer.toString(argument_index));
        GemObject.line("end_2: " + Integer.toString(end_2));

        throw new RuntimeException(
                (
                      "PermenantMessageFormattable.conjure: unimplemented, more than one '{#}': "
                    + PortrayFunctions.portray_string(format)
                )
            );


        //
        //  Create array of MessageSegment
        //
    }
}
