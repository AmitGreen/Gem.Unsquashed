//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.StringBuilder;
import java.lang.System;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Silver.Inspection;


public abstract class   SilverObject
    extends             Object
{
    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;
    public static final Matcher         braces_matcher  = Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?").matcher("");


    //
    //  Abstract
    //
    public abstract Inspection          inspect();


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


    public static void                  line(String format, Object first_argument, Object ... other_arguments)
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

        int                             start  = braces_matcher.start();
        int                             number = Integer.parseInt(braces_matcher.group(1));

        line("start: " + Integer.toString(start));
        line("group: " + Integer.toString(number));
        line("end_2: " + Integer.toString(end_2));
    }


    public static String                portray_string(String s)
    {
        if (s == null) {
            throw new RuntimeException("SilverObject.portray_string: `s` is null");
        }

        StringBuilder                   b     = null;
        int                             start = 0;
        int                             total = s.length();

        for (int                        i = 0; i < total; i ++) {
            int                         code_point = s.codePointAt(i);

            if (code_point == 34) {
                if (start < i) {
                    if (b == null) {
                        b = new StringBuilder(1 + 2 * total + 1);

                        b.append("\\\"");
                    }

                    b.append(s.substring(start, i));
                    b.append("\\\"");
                    start = i + 1;
                    continue;
                }
            }

            if (code_point == 92) {
                if (start < i) {
                    if (b == null) {
                        b = new StringBuilder(1 + 2 * total + 1);

                        b.append("\\\"");
                    }

                    b.append(s.substring(start, i));
                    b.append("\\\\");
                    start = i + 1;
                    continue;
                }
            }
        }

        if (b == null) {
            return "\"" + s + "\"";
        }

        b.append(s.substring(start));
        b.append("\"");

        return b.toString();
    }
}
