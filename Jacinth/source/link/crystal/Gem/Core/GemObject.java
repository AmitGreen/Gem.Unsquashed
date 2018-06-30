//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.Class;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PermenantMessageFormattable;
import link.crystal.Gem.Core.PermenantString;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public abstract class   GemObject<INSPECTION extends Inspection>
    extends             Object
    implements          Inspectable<INSPECTION>//,
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
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    //
    //  Public
    //
    public static String                intern_permenant_string(String s)
    {
        return PermenantString.intern_permenant_string(s);
    }


    public static String                intern_permenant_string_0(String s)
    {
        if (s == null) {
            return null;
        }

        return PermenantString.intern_permenant_string(s);
    }

    
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
        MessageFormattable              formattable = PermenantMessageFormattable.conjure(format);

        formattable.line(first_argument, other_arguments);
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
