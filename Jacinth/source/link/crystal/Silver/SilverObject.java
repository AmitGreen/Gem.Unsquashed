//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
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
    public void                         line()
    {
        standard_output.println();
    }


    public void                         line(String s)
    {
        standard_output.println(s);
    }
}
