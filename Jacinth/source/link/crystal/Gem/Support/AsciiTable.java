//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import link.crystal.Gem.Core.Gem_Object;
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
        AsciiTable.create(    "$", 0x03),  //  boring_printable
        AsciiTable.create(    "%", 0x03),  //  boring_printable
        AsciiTable.create(    "&", 0x03),  //  boring_printable
        AsciiTable.create(    "'", 0x03),  //  boring_printable
        AsciiTable.create(    "(", 0x03),  //  boring_printable
        AsciiTable.create(    ")", 0x03),  //  boring_printable
        AsciiTable.create(    "*", 0x03),  //  boring_printable
        AsciiTable.create(    "+", 0x03),  //  boring_printable
        AsciiTable.create(    ",", 0x03),  //  boring_printable
        AsciiTable.create(    "-", 0x03),  //  boring_printable
        AsciiTable.create(    ".", 0x03),  //  boring_printable
        AsciiTable.create(    "/", 0x03),  //  boring_printable
        AsciiTable.create(    "0", 0x03),  //  boring_printable
        AsciiTable.create(    "1", 0x03),  //  boring_printable
        AsciiTable.create(    "2", 0x03),  //  boring_printable
        AsciiTable.create(    "3", 0x03),  //  boring_printable
        AsciiTable.create(    "4", 0x03),  //  boring_printable
        AsciiTable.create(    "5", 0x03),  //  boring_printable
        AsciiTable.create(    "6", 0x03),  //  boring_printable
        AsciiTable.create(    "7", 0x03),  //  boring_printable
        AsciiTable.create(    "8", 0x03),  //  boring_printable
        AsciiTable.create(    "9", 0x03),  //  boring_printable
        AsciiTable.create(    ":", 0x03),  //  boring_printable
        AsciiTable.create(    ";", 0x03),  //  boring_printable
        AsciiTable.create(    "<", 0x03),  //  boring_printable
        AsciiTable.create(    "=", 0x03),  //  boring_printable
        AsciiTable.create(    ">", 0x03),  //  boring_printable
        AsciiTable.create(    "?", 0x03),  //  boring_printable
        AsciiTable.create(    "@", 0x03),  //  boring_printable
        AsciiTable.create(    "A", 0x03),  //  boring_printable
        AsciiTable.create(    "B", 0x03),  //  boring_printable
        AsciiTable.create(    "C", 0x03),  //  boring_printable
        AsciiTable.create(    "D", 0x03),  //  boring_printable
        AsciiTable.create(    "E", 0x03),  //  boring_printable
        AsciiTable.create(    "F", 0x03),  //  boring_printable
        AsciiTable.create(    "G", 0x03),  //  boring_printable
        AsciiTable.create(    "H", 0x03),  //  boring_printable
        AsciiTable.create(    "I", 0x03),  //  boring_printable
        AsciiTable.create(    "J", 0x03),  //  boring_printable
        AsciiTable.create(    "K", 0x03),  //  boring_printable
        AsciiTable.create(    "L", 0x03),  //  boring_printable
        AsciiTable.create(    "M", 0x03),  //  boring_printable
        AsciiTable.create(    "N", 0x03),  //  boring_printable
        AsciiTable.create(    "O", 0x03),  //  boring_printable
        AsciiTable.create(    "P", 0x03),  //  boring_printable
        AsciiTable.create(    "Q", 0x03),  //  boring_printable
        AsciiTable.create(    "R", 0x03),  //  boring_printable
        AsciiTable.create(    "S", 0x03),  //  boring_printable
        AsciiTable.create(    "T", 0x03),  //  boring_printable
        AsciiTable.create(    "U", 0x03),  //  boring_printable
        AsciiTable.create(    "V", 0x03),  //  boring_printable
        AsciiTable.create(    "W", 0x03),  //  boring_printable
        AsciiTable.create(    "X", 0x03),  //  boring_printable
        AsciiTable.create(    "Y", 0x03),  //  boring_printable
        AsciiTable.create(    "Z", 0x03),  //  boring_printable
        AsciiTable.create(    "[", 0x03),  //  boring_printable
        AsciiTable.create( "\\\\", 0x02),  //  backslash, printable
        AsciiTable.create(    "]", 0x03),  //  boring_printable
        AsciiTable.create(    "^", 0x03),  //  boring_printable
        AsciiTable.create(    "_", 0x03),  //  boring_printable
        AsciiTable.create(    "`", 0x03),  //  boring_printable
        AsciiTable.create(    "a", 0x03),  //  boring_printable
        AsciiTable.create(    "b", 0x03),  //  boring_printable
        AsciiTable.create(    "c", 0x03),  //  boring_printable
        AsciiTable.create(    "d", 0x03),  //  boring_printable
        AsciiTable.create(    "e", 0x03),  //  boring_printable
        AsciiTable.create(    "f", 0x03),  //  boring_printable
        AsciiTable.create(    "g", 0x03),  //  boring_printable
        AsciiTable.create(    "h", 0x03),  //  boring_printable
        AsciiTable.create(    "i", 0x03),  //  boring_printable
        AsciiTable.create(    "j", 0x03),  //  boring_printable
        AsciiTable.create(    "k", 0x03),  //  boring_printable
        AsciiTable.create(    "l", 0x03),  //  boring_printable
        AsciiTable.create(    "m", 0x03),  //  boring_printable
        AsciiTable.create(    "n", 0x03),  //  boring_printable
        AsciiTable.create(    "o", 0x03),  //  boring_printable
        AsciiTable.create(    "p", 0x03),  //  boring_printable
        AsciiTable.create(    "q", 0x03),  //  boring_printable
        AsciiTable.create(    "r", 0x03),  //  boring_printable
        AsciiTable.create(    "s", 0x03),  //  boring_printable
        AsciiTable.create(    "t", 0x03),  //  boring_printable
        AsciiTable.create(    "u", 0x03),  //  boring_printable
        AsciiTable.create(    "v", 0x03),  //  boring_printable
        AsciiTable.create(    "w", 0x03),  //  boring_printable
        AsciiTable.create(    "x", 0x03),  //  boring_printable
        AsciiTable.create(    "y", 0x03),  //  boring_printable
        AsciiTable.create(    "z", 0x03),  //  boring_printable
        AsciiTable.create(    "{", 0x03),  //  boring_printable
        AsciiTable.create(    "|", 0x03),  //  boring_printable
        AsciiTable.create(    "}", 0x03),  //  boring_printable
        AsciiTable.create(    "~", 0x03),  //  boring_printable
        AsciiTable.create("\\x7f", 0x00),
    };


    //
    //  Members
    //
    public final String                 portray;
    public final boolean                is_boring_printable;
    public final boolean                is_printable;


    //
    //  Constructor & Factory
    //
    private                             AsciiTable(
            final String                        portray,
            final boolean                       is_boring_printable,
            final boolean                       is_printable//,
        )
    {
        this.portray      = portray;
        this.is_boring_printable    = is_boring_printable;
        this.is_printable = is_printable;
    }


    private static final AsciiTable     create(final String s, final int bits)
    {
        final boolean                   is_boring_printable = ((bits & 0x01) != 0 ? true : false);
        final boolean                   is_printable        = ((bits & 0x02) != 0 ? true : false);

        return new AsciiTable(s, is_boring_printable, is_printable);
    }


    //
    //  Interface Inspectable
    //
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    //inherited public void             portray(Gem_StringBuilder builder)
}
