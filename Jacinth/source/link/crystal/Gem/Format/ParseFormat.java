//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.ArrayFunctions;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_1__Simple;
import link.crystal.Gem.Format.MessageFormatter_1__Suffix;
import link.crystal.Gem.Format.MessageFormatter_2;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_ArgumentSegmentFormatter;


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

    private SegmentFormattable[]        segment_many;
    private int                         segment_total;
    private int                         segment_index;

    private int[]                       used_index_many;
    private int                         used_index_total;
    private int                         used_index_allocated;

    private int[]                       missing_many;
    private int                         missing_total;
    private int                         missing_allocated;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             ParseFormat(String format, Matcher braces_matcher)
    {
        this.format         = format;
        this.braces_matcher = braces_matcher;

        this.segment_many   = null;
        this.segment_total  = 0;
        this.segment_index  = 0;

        this.used_index_many      = null;
        this.used_index_total     = 0;
        this.used_index_allocated = 0;

        this.missing_many      = null;
        this.missing_total     = 0;
        this.missing_allocated = 0;
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

        this.used_index_total = 0;

        this.missing_total = 0;
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
    private void                        add_missing(int missing)
    {
        int[]                           missing_many      = this.missing_many;
        int                             missing_total     = this.missing_total;
        int                             missing_allocated = this.missing_allocated;
        int                             needed            = missing_total + 1;

        if (missing_allocated < needed) {
            int                         new_allocated = limit_to_between(20, needed * 2, 100);

            missing_many = ArrayFunctions.grow_primitive_integer_array(
                    missing_many,
                    missing_total,
                    new int[new_allocated],
                    new_allocated//,
                );

            this.missing_many      = missing_many;
            this.missing_allocated = new_allocated;
        }

        missing_many[missing_total] = missing;

        this.missing_total = missing_total + 1;
    }


    private void                        add_used_index(int argument_index)
    {
        int[]                           used_index_many      = this.used_index_many;
        int                             used_index_total     = this.used_index_total;
        int                             used_index_allocated = this.used_index_allocated;
        int                             needed               = argument_index + 1;

        if (used_index_allocated < needed) {
            int                         new_allocated = limit_to_between(20, needed * 2, 100);

            used_index_many = ArrayFunctions.grow_primitive_integer_array(
                    used_index_many,
                    used_index_total,
                    new int[new_allocated],
                    new_allocated//,
                );

            this.used_index_many      = used_index_many;
            this.used_index_allocated = new_allocated;
        }

        for (int                    i = used_index_total; i <= argument_index; i ++) {
            used_index_many[i] = 0;
        }

        used_index_many[argument_index] += 1;

        if (used_index_total < needed) {
            this.used_index_total = needed;
        }
    }


    private void                        examine_missing()
    {
        int[]                           used_index_many  = this.used_index_many;
        int                             used_index_total = this.used_index_total;

        for (int                        i = 0; i < used_index_total; i ++) {
            if (used_index_many[i] == 0) {
                this.add_missing(i);
            }
        }

        int                             missing_total = this.missing_total;

        if (missing_total == 0) {
            return;
        }

        int[]                           missing_many = this.missing_many;

        if (missing_total == 1) {
            throw new RuntimeException(
                    (
                          "ParseFormat.examine_missing: format string is missing {"
                        + Integer.toString(missing_many[0])
                        + "}: "
                        + portray_string(this.format)
                    )
                );
        }

        if (missing_total == 2) {
            throw new RuntimeException(
                    (
                          "ParseFormat.examine_missing: format string is missing {"
                        + Integer.toString(missing_many[0])
                        + "} and {"
                        + Integer.toString(missing_many[1])
                        + "}: "
                        + portray_string(this.format)
                    )
                );
        }


        StringBuilder                   b = new StringBuilder();

        for (int                        i = 0; i < missing_total; i ++) {
            if (i == missing_total - 1) {
                b.append(", and ");
            } else if (i > 0) {
                b.append(", ");
            }

            b.append("{" + Integer.toString(missing_many[i]) + "}");
        }

        throw new RuntimeException(
                (
                      "ParseFormat.examine_missing: format string is missing "
                    + b.toString()
                    + ": "
                    + portray_string(this.format)
                )
            );
    }


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
                        + portray_string(format)
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
                        + portray_string(format)
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
                            + portray_string(format)
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
            segment_many[0] = Storehouse_ArgumentSegmentFormatter.conjure(argument_index);
        } else {
            throw new RuntimeException("ParseFormat.parse_format__work: unimplemented, segment with string");
        }

        int                         segment_index = 1;

        this.segment_index = segment_index;             //  Commit `segment_index` in catch exception is thrown

        add_used_index(argument_index);


        //
        //  Subsequent arguments
        //
        for (;;) {
            int                         next_end_2 = braces_matcher.end(2);

            if (next_end_2 == -1) {
                throw new RuntimeException(
                        (
                              "ParseFormat.parse_format__work: format string is malformed: "
                            + portray_string(format)
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

            //line("start: " + start);
            //line("start_s: " + portray(start_s));
            //line("group: " + portray(argument_index));
            //line("next_end_2: " + portray(next_end_2));

            if (segment_index == segment_total) {
                segment_total = this.grow_segments();
                segment_many  = this.segment_many;
            }

            if (start_s == null) {
                segment_many[segment_index] = Storehouse_ArgumentSegmentFormatter.conjure(argument_index);
            } else {
                throw new RuntimeException("ParseFormat.parse_format__work: unimplemented, segment with string");
            }

            end_2 = next_end_2;

            segment_index += 1;

            this.segment_index = segment_index;             //  Commit `segment_index` in catch exception is thrown

            add_used_index(argument_index);

            if ( ! braces_matcher.find()) {
                break;
            }
        }

        if (end_2 < format.length()) {
            throw new RuntimeException(
                    (
                          "ParseFormat.parse_format__work: unimplemented, more than one '{#}' (with trailing string): "
                        + portray_string(format)
                    )
              );
        }

        this.examine_missing();

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
                    + portray_string(format)
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
