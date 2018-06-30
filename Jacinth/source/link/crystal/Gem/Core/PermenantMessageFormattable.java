//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.MessageFormatter_1__Prefix;
import link.crystal.Gem.Core.MessageFormatter_1__Simple;
import link.crystal.Gem.Core.MessageFormatter_1__Suffix;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    PermenantMessageFormattable
    extends     HashMap<String, MessageFormattable>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.Core.PermenantMessageFormattable");


    //
    //  Private static
    //
    private static final Matcher                braces_matcher = (
            Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?").matcher("")
        );

    private static final int                    initial_capacity = 1009;
    private static PermenantMessageFormattable  singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             PermenantMessageFormattable(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static PermenantMessageFormattable  create()
    {
        return new PermenantMessageFormattable(PermenantMessageFormattable.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Private
    //
    private static PermenantMessageFormattable  singleton()
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            PermenantMessageFormattable.singleton = PermenantMessageFormattable.create();

        return singleton;
    }


    //
    //  Public
    //
    public static MessageFormattable    conjure(String format)
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        } else {
            MessageFormattable          previous = singleton.get(format);

            if (previous != null) {
                return previous;
            }
        }

        braces_matcher.reset(format);

        if ( ! braces_matcher.find()) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable.conjure: format string does not contain the opening brace '{': "
                        + PortrayFunctions.portray_string(format)
                    )
                );
        }

        int                             end_2 = braces_matcher.end(2);

        if (end_2 == -1) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable: format string is malformed': "
                        + PortrayFunctions.portray_string(format)
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
        //line("start_s: " + PortrayFunctions.portray_string(start_s));
        //line("group: " + Integer.toString(first_number));
        //line("end_2: " + Integer.toString(end_2));
        //line("end_2: " + PortrayFunctions.portray_string(end_s));

        if (braces_matcher.find()) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable: unimplemented, more than one '{#}': "
                        + PortrayFunctions.portray_string(format)
                    )
                );
        }

        MessageFormattable              r = null;

        if (end_2 == format.length()) {
            if (start_s == null) {
                r = MessageFormatter_1__Simple.create();
            } else {
                r = MessageFormatter_1__Prefix.create(start_s);
            }

            singleton.put(format, r);

            return r;
        }

        r = MessageFormatter_1__Suffix.create(start_s, format.substring(end_2));

        singleton.put(format, r);

        return r;
    }


    public static void                  dump()
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        GemObject.line("Dump of PermenantMessageFormattable");
        GemObject.line("  " + String.format("%30s", "size") + ": " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = values.get(i);
            MessageFormattable          v = singleton.get(k);

            GemObject.line("  " + String.format("%30s", PortrayFunctions.portray_string(k)) + ": " + v.portray());
        }

        GemObject.line("End of dump of PermenantMessageFormattable");
    }


    public static MessageFormattable    lookup(String k)
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        }

        return singleton.get(k);
    }
}
