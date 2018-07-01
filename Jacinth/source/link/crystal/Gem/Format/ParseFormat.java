//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.ArrayFunctions;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_1__Simple;
import link.crystal.Gem.Format.MessageFormatter_1__Suffix;
import link.crystal.Gem.Format.PermenantArgumentFormatter;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public abstract class   ParseFormat
    extends             Gem_Object//<Inspection>
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
                          "ParseFormat.parse_format: format string does not contain the opening brace '{': "
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
                          "ParseFormat.parse_format: format string is malformed: "
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
                              "ParseFormat.parse_format: format string must use {0} for only one argument: "
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
        //  Create array of SegmentFormattable
        //
        int                             many_total = 11;
        SegmentFormattable[]            many       = new SegmentFormattable[many_total];

        if (start_s == null) {
            many[0] = PermenantArgumentFormatter.conjure(argument_index);
        } else {
            throw new RuntimeException("ParseFormat.parse_format: unimplemented, segment with string");
        }

        int                             many_index = 1;


        //
        //  Subsequent arguments
        //
        for (;;) {
            int                         next_end_2 = braces_matcher.end(2);

            if (next_end_2 == -1) {
                throw new RuntimeException(
                        (
                              "ParseFormat.parse_format: format string is malformed: "
                            + PortrayFunctions.portray_string(format)
                        )
                    );
            }

            start          = braces_matcher.start();
            argument_index = 0;
            start_s        = null;

            if (next_end_2 - start == 3) {
                argument_index = format.codePointAt(start + 1) - 48;
            } else {
                argument_index = Integer.parseInt(braces_matcher.group(1));
            }

            if (end_2 < start) {
                start_s = format.substring(end_2, start);
            }

            Gem_Object.line("start: " + start);
            Gem_Object.line("start_s: " + portray(start_s));
            Gem_Object.line("group: " + portray(argument_index));
            Gem_Object.line("next_end_2: " + portray(next_end_2));


            if (many_index == many_total) {
                if (many_total == 101) {
                    throw new RuntimeException("ParseFormat.parse_format: maximum of 100 '{#}' allowed");
                }

                many = ArrayFunctions.<SegmentFormattable>grow_array(
                        many,
                        many_total,
                        new SegmentFormattable[101],
                        101//,
                    );

                many_total = 101;
            }

            if (start_s == null) {
                many[many_index] = PermenantArgumentFormatter.conjure(argument_index);
            } else {
                throw new RuntimeException("ParseFormat.parse_format: unimplemented, segment with string");
            }

            end_2 = next_end_2;

            many_index += 1;

            if ( ! braces_matcher.find()) {
                break;
            }
        }

        if (end_2 < format.length()) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format: unimplemented, more than one '{#}' (with trailing string): "
                        + PortrayFunctions.portray_string(format)
                    )
              );
        }

        if (many_index < many_total) {
            many = ArrayFunctions.<SegmentFormattable>shrink_array(
                    many,
                    many_total,
                    new SegmentFormattable[many_index],
                    many_index//,
                );

            many_total = many_index;
        }


        if (true) {
            for (int                        i = 0; i < many_total; i ++) {
                line(Integer.toString(i) + ": " + portray(many[i]));
            }
        }

        throw new RuntimeException(
                (
                      "ParseFormat.parse_format: unimplemented, more than one '{#}' (without trailing string): "
                    + PortrayFunctions.portray_string(format)
                )
            );
    }
}
