//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.io.PrintStream;
import java.lang.Class;
import java.lang.Object;
import java.lang.String;
import java.lang.String;
import java.lang.System;


public abstract class   GemObject
    extends             Object
{
    //
    //  Static types
    //
    public static final Class<String>   String$class = String.class;


    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;


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


    public static String                portray(Object v)
    {
        return PortrayFunctions.portray(v);
    }


    public static String                portray_string(String s)
    {
        return PortrayFunctions.portray_string(s);
    }
}
