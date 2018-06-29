//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.String;
import java.lang.System;


public abstract class   JacinthObject
    extends             Object
{
    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;


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
