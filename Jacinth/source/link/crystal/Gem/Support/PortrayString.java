//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.BuildStringState;


//
//   KA = backslash_with_apostrophe         (can use python `String.__repr__` for optimization)
//   KQ = backslash_with_quotation_mark     (can use python `String.__repr__` for optimization)
//
//   KC = backslash_with_triple_apostrophe
//   KS = backslash_with_triple_quotation_mark
//
//   PA = normal_with_apostrophe            (can use python `String.__repr__` for optimization)
//   PQ = normal_with_quotation_mark        (can use python `String.__repr__` for optimization)
//
//   PC = normal_with_triple_apostrophe
//   PS = normal_with_triple_quotation_mark
//
//   RA = raw_with_apostrophe
//   RQ = raw_with_quotation_mark
//
//   RC = raw_with_triple_apostrophe
//   RS = raw_with_triple_quotation_mark
//
public abstract class   PortrayString
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    //
    //  Static members
    //
    public static final PortrayString   portray_string__invalid = (
            PortrayString_Backslash.create__ALLY__PortrayString("0", "invalid'", "'", 39)   //  39 = ordinal("'")
        );

    public static final PortrayString   backslash_with_apostrophe = (
            PortrayString_Backslash.create__ALLY__PortrayString("KA", "'", "'", 39)   //  39 = ordinal("'")
        );

    public static final PortrayString   backslash_with_quotation_mark = (
            PortrayString_Backslash.create__ALLY__PortrayString("KQ", "'", "'", 34)   //  34 = ordinal('"')
        );

    public static final PortrayString   backslash_with_triple_apostrophe = (
            PortrayString_TripleWithBackslash.create__ALLY__PortrayString(
                "KC",
                "'''",
                AsciiTable.table_with_boring_quotation_mark,
                39,                                                             //  39 = ordinal("'")
                BuildStringState.A_Start,
                BuildStringState.A_Normal//,
            )
        );

    public static final PortrayString   backslash_with_triple_quotation_mark = (
            PortrayString_TripleWithBackslash.create__ALLY__PortrayString(
                "KS",
                "\"\"\"",
                AsciiTable.table_with_boring_apostrophe,
                34,                                                             //  34 = ordinal('"')
                BuildStringState.Q_Start,
                BuildStringState.Q_Normal//,
            )
        );

    public static final PortrayString   normal_with_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("PA", "'", "'")
        );

    public static final PortrayString   normal_with_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("PQ", "\"", "\"")
        );

    public static final PortrayString   normal_with_triple_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("PC", "'''", "'''")
        );

    public static final PortrayString   normal_with_triple_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("PS", "\"\"\"", "\"\"\"")
        );

    public static final PortrayString   raw_with_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("RA", "r'", "'")
        );

    public static final PortrayString   raw_with_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("RQ", "r\"", "\"")
        );

    public static final PortrayString   raw_with_triple_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("RC", "r'''", "'''")
        );

    public static final PortrayString   raw_with_triple_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("RS", "r\"\"\"", "\"\"\"")
        );


    //
    //  Members
    //
    protected final String              abbreviation;
    protected final boolean             is_valid;


    //
    //  Constructor
    //
    protected                           PortrayString(final String abbreviation)
    {
        final boolean                   is_valid = ( ! abbreviation.equals("0"));

        this.abbreviation = abbreviation;
        this.is_valid     = is_valid;
    }


    //
    //  Abstract <me>
    //
    public abstract void                portray_string(final Gem_StringBuilder builder, final String s);


    //
    //  Public
    //
    public /*overrideable*/ String      portray_string(final String s)
    {
        final Zone                      z = Zone.current_zone();

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        this.portray_string(builder, s);

        return builder.finish_AND_recycle();
    }
}


final class             PortrayString_Backslash
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_Backslash");


    //
    //  Members
    //
    private final String                prefix;
    private final String                suffix;
    private final int                   quote_code_point;


    //
    //  Constructor & Factory
    //
    private                             PortrayString_Backslash(
            final String                        abbreviation,
            final String                        prefix,
            final String                        suffix,
            final int                           quote_code_point//,
        )
    {
        super(abbreviation);

        this.prefix           = prefix;
        this.suffix           = suffix;
        this.quote_code_point = quote_code_point;
    }


    public static final PortrayString_Backslash     create__ALLY__PortrayString(
            final String                        abbreviation,
            final String                        prefix,
            final String                        suffix,
            final int                           quote_code_point//,
        )
    {
        return new PortrayString_Backslash(abbreviation, prefix, suffix, quote_code_point);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayString_Backslash ", this.abbreviation, " ");
        builder.quote(this.prefix);
        builder.append(" ");
        builder.quote(this.suffix);
        builder.append(">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        final int                       quote_code_point = this.quote_code_point;

        final AsciiTable[]              table = AsciiTable.table;

        builder.append(this.prefix);

        /*:*/ int                       begin = 0;
        final int                       total = s.length();

        for (/*:*/ int                  i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            final int                   code_point = s.codePointAt(i);

            if (code_point < 128) {
                AsciiTable              ascii = table[code_point];

                if (ascii.is_boring_printable || code_point == quote_code_point) {
                    i ++;
                    continue;
                }

                if (begin < i) {
                    builder.append_slice(s, begin, i);
                }

                assert fact_pointer(ascii.portray_0, "ascii.portray_0");

                builder.append(ascii.portray_0);

                i ++;

                begin = i;

                continue;
            }

            i += Character.charCount(code_point);
        }

        if (begin < total) {
            builder.append_slice(s, begin);
        }

        builder.append(this.suffix);
    }
}


final class             PortrayString_Normal
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_Normal");


    //
    //  Members
    //
    private final String                prefix;
    private final String                suffix;


    //
    //  Constructor & Factory
    //
    protected                           PortrayString_Normal(
            final String                        abbreviation,
            final String                        prefix,
            final String                        suffix//,
        )
    {
        super(abbreviation);

        this.prefix = prefix;
        this.suffix = suffix;
    }


    public static final PortrayString_Normal    create__ALLY__PortrayString(
            final String                        abbreviation,
            final String                        prefix,
            final String                        suffix//,
        )
    {
        return new PortrayString_Normal(abbreviation, prefix, suffix);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayString_Normal ", this.abbreviation, " ");
        builder.quote(this.prefix);
        builder.append(" ");
        builder.quote(this.suffix);
        builder.append(">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        builder.append(this.prefix, s, this.suffix);
    }


    //
    //  Public
    //
    @Override
    public final String                 portray_string(final String s)
    {
        return this.prefix + s + this.suffix;
    }


}

final class             PortrayString_TripleWithBackslash
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_TripleWithBackslash");


    //
    //  Members
    //
    private final String                prefix;
    private final AsciiTable[]          table;
    private final int                   quote_code_point;
    private final BuildStringState      first_state;
    private final BuildStringState      normal_state;


    //
    //  Constructor & Factory
    //
    private                             PortrayString_TripleWithBackslash(
            final String                        abbreviation,
            final String                        prefix,
            final AsciiTable[]                  table,
            final int                           quote_code_point,
            final BuildStringState              first_state,
            final BuildStringState              normal_state//
        )
    {
        super(abbreviation);

        this.prefix           = prefix;
        this.table            = table;
        this.quote_code_point = quote_code_point;
        this.first_state      = first_state;
        this.normal_state     = normal_state;
    }


    public static final PortrayString_TripleWithBackslash   create__ALLY__PortrayString(
            final String                        abbreviation,
            final String                        prefix,
            final AsciiTable[]                  table,
            final int                           quote_code_point,
            final BuildStringState              first_state,
            final BuildStringState              normal_state//
        )
    {
        return new PortrayString_TripleWithBackslash(
                abbreviation,
                prefix,
                table,
                quote_code_point,
                first_state,
                normal_state//,
            );
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(final Gem_StringBuilder builder)
    {
        String                          table_name = "?";

        if (this.table == AsciiTable.table_with_boring_apostrophe) {
            table_name = "table_with_boring_apostrophe";
        } else {
            assert fact( this.table == AsciiTable.table_with_boring_quotation_mark,
                        "this.table == AsciiTable.table_with_boring_quotation_mark");

            table_name = "table_with_boring_quotation_mark";
        }

        String                          quote_code_point_name = "?";

        if (this.quote_code_point == 34) {
            quote_code_point_name = "'\"'";
        } else {
            quote_code_point_name = "\"'\"";
        }

        builder.append("<PortrayString_TripleWithBackslash ", this.abbreviation, " ");
        builder.quote(this.prefix);
        builder.append(" ", table_name, " ", quote_code_point_name, " ", this.first_state.name, " ", this.normal_state.name, ">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        builder.append(this.prefix);

        final BuildStringState          normal_state     = this.normal_state;
        final int                       quote_code_point = this.quote_code_point;
        final AsciiTable[]              table            = this.table;

        final BuildStringState          state_1 = normal_state.add;

        /*:*/ int                       begin       = 0;
        /*:*/ BuildStringState          state       = this.first_state;
        /*:*/ int                       state_begin = 0;                    //  Only used when `state != normal_state`
        final int                       total       = s.length();

        for (/*:*/ int                  i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            final int                   code_point = s.codePointAt(i);

            if (code_point >= 128) {
                i += Character.charCount(code_point);
                state = normal_state;

                continue;
            }

            final AsciiTable            ascii = table[code_point];

            if (ascii.is_boring_printable) {
                i ++;
                state = normal_state;

                continue;
            }

            if (code_point == quote_code_point) {
                i ++;

                if (state == normal_state) {
                    state       = state_1;
                    state_begin = i;
                    continue;
                }

                final String        add_flush_0 = state.add_flush_0;

                if (add_flush_0 != null) {
                    if (begin < state_begin) {
                        builder.append_slice(s, begin, state_begin);
                    }

                    builder.append(add_flush_0);

                    begin =
                        state_begin = i;
                }

                state = state.add;
                continue;
            }

            if (begin < i) {
                builder.append_slice(s, begin, i);
            }

            i ++;

            assert fact_pointer(ascii.portray_0, "ascii.portray_0");

            builder.append(ascii.portray_0);

            state = normal_state;
            begin = i;
        }

        if (state == normal_state) {
            if (begin < total) {
                builder.append_slice(s, begin);
            }

            return;
        }

        if (begin < state_begin) {
            builder.append_slice(s, begin, state_begin);
        }

        builder.append(state.finish);
    }
}
