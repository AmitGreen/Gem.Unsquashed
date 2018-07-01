//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.ArrayFunctions;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_1__Simple;
import link.crystal.Gem.Format.MessageFormatter_1__Suffix;
import link.crystal.Gem.Format.MessageFormatter_2;
import link.crystal.Gem.Format.PermenantArgumentFormatter;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class   ParseFormat
    extends    Gem_Object<Inspection>
    implements Inspectable<Inspection>//,                               //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem.Core.ParseFormat");


    //
    //  Static members
    //
    private static Pattern              braces_pattern = Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?");


    //
    //  Members
    //
    private String                      format;
    private Matcher                     braces_matcher;
    private int                         segment_index;
    private int                         segment_total;
    private SegmentFormattable[]        segment_many;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             ParseFormat(String format, Matcher braces_matcher)
    {
        this.format         = format;
        this.braces_matcher = braces_matcher;
        this.segment_index  = 0;
        this.segment_total  = 0;
        this.segment_many   = null;
    }


    public static ParseFormat           create(String format)
    {
        Matcher                         braces_matcher = ParseFormat.braces_pattern.matcher(format);

        return new ParseFormat(format, braces_matcher);
    }


    public void                         recycle(String format)
    {
        this.format = format;
        this.braces_matcher.reset(format);
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
    private int                         grow_segments()
    {
        int                             previous_total = this.segment_total;
        int                             segment_total;

        if (previous_total == 0) {
            segment_total = 21;
        } else if (previous_total == 21) {
            segment_total = 201;
        } else {
            throw new RuntimeException("ParseFormat.grow_segments: maximum of 100 '{#}' allowed");
        }

        SegmentFormattable[]            segment_many = ArrayFunctions.<SegmentFormattable>grow_array(
                this.segment_many,
                previous_total,
                new SegmentFormattable[segment_total],
                segment_total//,
            );

        this.segment_many  = segment_many;
        this.segment_total = segment_total;

        return segment_total;
    }


    private SegmentFormattable[]        steal_segments()
    {
        SegmentFormattable[]            segment_many = this.segment_many;

        if (segment_many == null) {
            throw new RuntimeException("ParseFormat.steal_segments: no segments to steal");
        }

        this.segment_index = 0;
        this.segment_total = 0;
        this.segment_many  = null;

        return segment_many;
    }


    private MessageFormattable          parse_format__work()
    {
        String                          format         = this.format;
        Matcher                         braces_matcher = this.braces_matcher;

        if ( ! braces_matcher.find()) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format__work: format string does not contain the opening brace '{': "
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
                          "ParseFormat.parse_format__work: format string is malformed: "
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
                              "ParseFormat.parse_format__work: format string must use {0} for only one argument: "
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
        int                         segment_total = this.segment_total;

        if (segment_total == 0) {
            segment_total = this.grow_segments();
        }

        SegmentFormattable[]        segment_many = this.segment_many;

        if (start_s == null) {
            segment_many[0] = PermenantArgumentFormatter.conjure(argument_index);
        } else {
            throw new RuntimeException("ParseFormat.parse_format__work: unimplemented, segment with string");
        }

        int                         segment_index = 1;

        this.segment_index = segment_index;             //  Commit `segment_index` in catch exception is thrown


        //
        //  Subsequent arguments
        //
        for (;;) {
            int                         next_end_2 = braces_matcher.end(2);

            if (next_end_2 == -1) {
                throw new RuntimeException(
                        (
                              "ParseFormat.parse_format__work: format string is malformed: "
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

            if (segment_index == segment_total) {
                segment_total = this.grow_segments();
                segment_many  = this.segment_many;
            }

            if (start_s == null) {
                segment_many[segment_index] = PermenantArgumentFormatter.conjure(argument_index);
            } else {
                throw new RuntimeException("ParseFormat.parse_format__work: unimplemented, segment with string");
            }

            end_2 = next_end_2;

            segment_index += 1;

            this.segment_index = segment_index;             //  Commit `segment_index` in catch exception is thrown

            if ( ! braces_matcher.find()) {
                break;
            }
        }

        if (end_2 < format.length()) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format__work: unimplemented, more than one '{#}' (with trailing string): "
                        + PortrayFunctions.portray_string(format)
                    )
              );
        }

        if (true) {
            for (int                        i = 0; i < segment_index; i ++) {
                line(Integer.toString(i) + ": " + portray(segment_many[i]));
            }
        }


        if (segment_index == 2) {
            return MessageFormatter_2.create(segment_many[0], segment_many[1]);
        }


        SegmentFormattable[]        shrunk_many;
        int                         shrunk_total = segment_index;

        if (segment_index < segment_total) {
            shrunk_many = ArrayFunctions.<SegmentFormattable>shrink_array(
                                 segment_many,
                                 segment_total,
                                 new SegmentFormattable[segment_index],
                                 segment_index//,
                             );
        } else {
            shrunk_many = this.steal_segments();
        }


        throw new RuntimeException(
                (
                      "ParseFormat.parse_format__work: unimplemented, more than one '{#}' (without trailing string): "
                    + PortrayFunctions.portray_string(format)
                )
            );
    }


    //
    //  Null any references (for garbage collection purposes)
    //
    //  NOTE:
    //      Not really useful, since all the same data is saved elsewhere, and will never be garbage collectd ...
    //      ...  However, doing this just on principle anyway ...
    //
    private void                        scrub()
    {
        int                             segment_index = this.segment_index;

        this.format = null;
        this.braces_matcher.reset();

        if (segment_index > 0) {
            SegmentFormattable[]        segment_many = this.segment_many;

            for (int                    i = 0; i < segment_index; i ++) {
                segment_many[i] = null;
            }
           
            this.segment_index = 0;
        }
    }


    //
    //  Public static
    //
    public static MessageFormattable    parse_format(String format)
    {
        Gem_Lane                        z            = Gem_Lane.current_lane();
        ParseFormat                     parse_format = z.pop__parse_format__OR__null();

        if (parse_format == null) {
            parse_format = ParseFormat.create(format);
        } else {
            parse_format.recycle(format);
        }

        try {
            return parse_format.parse_format__work();
        } finally {
            parse_format.scrub();

            z.store_parse_format(parse_format);
        }
    }
}
