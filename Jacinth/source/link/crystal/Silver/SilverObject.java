//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.System;
import link.crystal.Silver.Inspection;
import link.crystal.Gem.ParseFormat;


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
        ParseFormat.parse_format(format);
    }
}
