//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class  AsciiTable
    extends         Gem_Object <Inspection>
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("AsciiTable");


    //
    //  Static members
    //
    public static final AsciiTable[]    table = new AsciiTable[] {
        AsciiTable.create("\\x00", 0x00),
        AsciiTable.create("\\x01", 0x00),
        AsciiTable.create("\\x02", 0x00),
        AsciiTable.create("\\x03", 0x00),
        AsciiTable.create("\\x04", 0x00),
        AsciiTable.create("\\x05", 0x00),
        AsciiTable.create("\\x06", 0x00),
        AsciiTable.create("\\x07", 0x00),
        AsciiTable.create("\\x08", 0x00),
        AsciiTable.create(  "\\t", 0x00),
        AsciiTable.create(  "\\n", 0x00),
        AsciiTable.create("\\x0b", 0x00),
        AsciiTable.create("\\x0c", 0x00),
        AsciiTable.create(  "\\r", 0x00),
        AsciiTable.create("\\x0e", 0x00),
        AsciiTable.create("\\x0f", 0x00),
        AsciiTable.create("\\x10", 0x00),
        AsciiTable.create("\\x11", 0x00),
        AsciiTable.create("\\x12", 0x00),
        AsciiTable.create("\\x13", 0x00),
        AsciiTable.create("\\x14", 0x00),
        AsciiTable.create("\\x15", 0x00),
        AsciiTable.create("\\x16", 0x00),
        AsciiTable.create("\\x17", 0x00),
        AsciiTable.create("\\x18", 0x00),
        AsciiTable.create("\\x19", 0x00),
        AsciiTable.create("\\x1a", 0x00),
        AsciiTable.create("\\x1b", 0x00),
        AsciiTable.create("\\x1c", 0x00),
        AsciiTable.create("\\x1d", 0x00),
        AsciiTable.create("\\x1e", 0x00),
        AsciiTable.create("\\x1f", 0x00),
        AsciiTable.create(    " ", 0x03),  //  boring_printable
        AsciiTable.create(    "!", 0x03),  //  boring_printable
        AsciiTable.create( "\\\"", 0x02),  //  printable, quotation_mark
        AsciiTable.create(    "#", 0x03),  //  boring_printable
        AsciiTable.create(    "$", 0x07),  //  boring_printable, word
        AsciiTable.create(    "%", 0x07),  //  boring_printable, word
        AsciiTable.create(    "&", 0x03),  //  boring_printable
        AsciiTable.create(    "'", 0x02),  //  apostrophe, printable
        AsciiTable.create(    "(", 0x03),  //  boring_printable
        AsciiTable.create(    ")", 0x03),  //  boring_printable
        AsciiTable.create(    "*", 0x03),  //  boring_printable
        AsciiTable.create(    "+", 0x07),  //  boring_printable, word
        AsciiTable.create(    ",", 0x07),  //  boring_printable, word
        AsciiTable.create(    "-", 0x07),  //  boring_printable, word
        AsciiTable.create(    ".", 0x07),  //  boring_printable, word
        AsciiTable.create(    "/", 0x07),  //  boring_printable, word
        AsciiTable.create(    "0", 0x07),  //  boring_printable, word
        AsciiTable.create(    "1", 0x07),  //  boring_printable, word
        AsciiTable.create(    "2", 0x07),  //  boring_printable, word
        AsciiTable.create(    "3", 0x07),  //  boring_printable, word
        AsciiTable.create(    "4", 0x07),  //  boring_printable, word
        AsciiTable.create(    "5", 0x07),  //  boring_printable, word
        AsciiTable.create(    "6", 0x07),  //  boring_printable, word
        AsciiTable.create(    "7", 0x07),  //  boring_printable, word
        AsciiTable.create(    "8", 0x07),  //  boring_printable, word
        AsciiTable.create(    "9", 0x07),  //  boring_printable, word
        AsciiTable.create(    ":", 0x07),  //  boring_printable, word
        AsciiTable.create(    ";", 0x03),  //  boring_printable
        AsciiTable.create(    "<", 0x03),  //  boring_printable
        AsciiTable.create(    "=", 0x03),  //  boring_printable
        AsciiTable.create(    ">", 0x03),  //  boring_printable
        AsciiTable.create(    "?", 0x03),  //  boring_printable
        AsciiTable.create(    "@", 0x07),  //  boring_printable, word
        AsciiTable.create(    "A", 0x07),  //  boring_printable, word
        AsciiTable.create(    "B", 0x07),  //  boring_printable, word
        AsciiTable.create(    "C", 0x07),  //  boring_printable, word
        AsciiTable.create(    "D", 0x07),  //  boring_printable, word
        AsciiTable.create(    "E", 0x07),  //  boring_printable, word
        AsciiTable.create(    "F", 0x07),  //  boring_printable, word
        AsciiTable.create(    "G", 0x07),  //  boring_printable, word
        AsciiTable.create(    "H", 0x07),  //  boring_printable, word
        AsciiTable.create(    "I", 0x07),  //  boring_printable, word
        AsciiTable.create(    "J", 0x07),  //  boring_printable, word
        AsciiTable.create(    "K", 0x07),  //  boring_printable, word
        AsciiTable.create(    "L", 0x07),  //  boring_printable, word
        AsciiTable.create(    "M", 0x07),  //  boring_printable, word
        AsciiTable.create(    "N", 0x07),  //  boring_printable, word
        AsciiTable.create(    "O", 0x07),  //  boring_printable, word
        AsciiTable.create(    "P", 0x07),  //  boring_printable, word
        AsciiTable.create(    "Q", 0x07),  //  boring_printable, word
        AsciiTable.create(    "R", 0x07),  //  boring_printable, word
        AsciiTable.create(    "S", 0x07),  //  boring_printable, word
        AsciiTable.create(    "T", 0x07),  //  boring_printable, word
        AsciiTable.create(    "U", 0x07),  //  boring_printable, word
        AsciiTable.create(    "V", 0x07),  //  boring_printable, word
        AsciiTable.create(    "W", 0x07),  //  boring_printable, word
        AsciiTable.create(    "X", 0x07),  //  boring_printable, word
        AsciiTable.create(    "Y", 0x07),  //  boring_printable, word
        AsciiTable.create(    "Z", 0x07),  //  boring_printable, word
        AsciiTable.create(    "[", 0x03),  //  boring_printable
        AsciiTable.create( "\\\\", 0x02),  //  backslash, printable
        AsciiTable.create(    "]", 0x03),  //  boring_printable
        AsciiTable.create(    "^", 0x03),  //  boring_printable
        AsciiTable.create(    "_", 0x07),  //  boring_printable, word
        AsciiTable.create(    "`", 0x03),  //  boring_printable
        AsciiTable.create(    "a", 0x07),  //  boring_printable, word
        AsciiTable.create(    "b", 0x07),  //  boring_printable, word
        AsciiTable.create(    "c", 0x07),  //  boring_printable, word
        AsciiTable.create(    "d", 0x07),  //  boring_printable, word
        AsciiTable.create(    "e", 0x07),  //  boring_printable, word
        AsciiTable.create(    "f", 0x07),  //  boring_printable, word
        AsciiTable.create(    "g", 0x07),  //  boring_printable, word
        AsciiTable.create(    "h", 0x07),  //  boring_printable, word
        AsciiTable.create(    "i", 0x07),  //  boring_printable, word
        AsciiTable.create(    "j", 0x07),  //  boring_printable, word
        AsciiTable.create(    "k", 0x07),  //  boring_printable, word
        AsciiTable.create(    "l", 0x07),  //  boring_printable, word
        AsciiTable.create(    "m", 0x07),  //  boring_printable, word
        AsciiTable.create(    "n", 0x07),  //  boring_printable, word
        AsciiTable.create(    "o", 0x07),  //  boring_printable, word
        AsciiTable.create(    "p", 0x07),  //  boring_printable, word
        AsciiTable.create(    "q", 0x07),  //  boring_printable, word
        AsciiTable.create(    "r", 0x07),  //  boring_printable, word
        AsciiTable.create(    "s", 0x07),  //  boring_printable, word
        AsciiTable.create(    "t", 0x07),  //  boring_printable, word
        AsciiTable.create(    "u", 0x07),  //  boring_printable, word
        AsciiTable.create(    "v", 0x07),  //  boring_printable, word
        AsciiTable.create(    "w", 0x07),  //  boring_printable, word
        AsciiTable.create(    "x", 0x07),  //  boring_printable, word
        AsciiTable.create(    "y", 0x07),  //  boring_printable, word
        AsciiTable.create(    "z", 0x07),  //  boring_printable, word
        AsciiTable.create(    "{", 0x03),  //  boring_printable
        AsciiTable.create(    "|", 0x03),  //  boring_printable
        AsciiTable.create(    "}", 0x03),  //  boring_printable
        AsciiTable.create(    "~", 0x03),  //  boring_printable
        AsciiTable.create("\\x7f", 0x00),
    };


    public static final AsciiTable      unknown = AsciiTable.create(null, 0);


    //
    //  Members
    //
    public final String                 portray_0;
    public final boolean                is_boring_printable;
    public final boolean                is_printable;
    public final boolean                is_word;


    //
    //  Constructor & Factory
    //
    private                             AsciiTable(final String portray_0, final int bits)
    {
        this.portray_0            = portray_0;
        this.is_boring_printable = ((bits & 0x01) != 0 ? true : false);
        this.is_printable        = ((bits & 0x02) != 0 ? true : false);
        this.is_word             = ((bits & 0x04) != 0 ? true : false);
    }


    private static final AsciiTable     create(final String portray_0, final int bits)
    {
        return new AsciiTable(portray_0, bits);
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
        final String                    portray_0 = this.portray_0;

        builder.append("<AsciiTable ");

        if (portray_0 == null) {
            builder.append("<null>");
        } else {
            builder.quote(portray_0);
        }

        if (this.is_boring_printable) {
            assert fact(this.is_printable, "this.is_printable");

            builder.append("; is_boring_printable");
        } else if (this.is_printable) {
            builder.append("; is_printable");
        }

        if (this.is_word) {
            builder.append("; is_word");
        }

        builder.append(">");
    }


    //
    //  Public (debug)
    //
    public static final void            dump()
    {
        final AsciiTable[]              table = AsciiTable.table;

        final int                       total = table.length;

        line("Dump of AsciiTable");

        for (/*:*/ int                  i = 0; i < total; i ++) {
            line("  table[{}]: {}", i, table[i]);
        }

        line("    unknown: {}", AsciiTable.unknown);

        line("Dump of AsciiTable");
    }
}
