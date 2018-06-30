//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.lang.RuntimeException;
import java.lang.String;
import java.lang.StringBuilder;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.GemObject;
import link.crystal.Gem.MessageFormattable;
import link.crystal.Gem.MessageFormatter_1;
import link.crystal.Gem.MessageFormatter_1__Suffix;


public abstract class   ParseFormat
    extends             GemObject<Inspection>
//  extends             Object
{
    //
    //  Public Static
    //
    public static final Matcher         braces_matcher  = Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?").matcher("");


    //
    //  Public
    //
    public static MessageFormattable    parse_format(String format)
    {
        braces_matcher.reset(format);

        boolean                         found = braces_matcher.find();

        if ( ! found) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format: format string does not contain the opening brace '{': "
                        + portray_string(format)
                    )
                );
        }

        int                             end_2 = braces_matcher.end(2);

        if (end_2 == -1) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format format string is malformed': "
                        + portray_string(format)
                    )
                );
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

        //line("start: " + start);
        //line("start_s: " + portray_string(start_s));
        //line("group: " + Integer.toString(first_number));
        //line("end_2: " + Integer.toString(end_2));
        //line("end_2: " + portray_string(end_s));

        found = braces_matcher.find();

        if (found) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format unimplemented, more than one '{#}': "
                        + portray_string(format)
                    )
                );
        }

        if (end_2 == format.length()) {
            return MessageFormatter_1.create(start_s);
        }


        return MessageFormatter_1__Suffix.create(start_s, format.substring(end_2));
    }
}
