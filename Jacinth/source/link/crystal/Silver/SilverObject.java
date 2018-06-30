//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.MessageFormattable;
import link.crystal.Gem.ParseFormat;
import link.crystal.Silver.Inspection;


public abstract class   SilverObject
    extends             Object
{
    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;


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
        MessageFormattable              formattable = ParseFormat.parse_format(format);

        formattable.line(first_argument, other_arguments);
    }
}
