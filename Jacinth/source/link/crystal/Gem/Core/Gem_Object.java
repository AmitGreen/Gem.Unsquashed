//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Class;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.OutputFunctions;
import link.crystal.Gem.Support.PortrayFunctions;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;


public abstract class   Gem_Object<INSPECTION extends Inspection>
    extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Static types
    //
    public static final Class<String>   String$class  = String.class;
    public static final Class<Integer>  Integer$class = Integer.class;


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    public String                       portray()
    {
        INSPECTION                      inspection = this.inspect();

        String                          portrait_0 = inspection.portrait_0;

        if (portrait_0 == null) {
            throw new RuntimeException("Gem_Object.portray: `.inspect().portrait_0` is `null`");
        }

        return portrait_0;
    }


    //
    //  Public
    //
    public static String                intern_permenant_string(String s)
    {
        return Storehouse_String.intern_permenant_string(s);
    }


    public static String                intern_permenant_string_0(String s)
    {
        if (s == null) {
            return null;
        }

        return Storehouse_String.intern_permenant_string(s);
    }

    
    public static void                  line()
    {
        OutputFunctions.line();
    }


    public static void                  line(String s)
    {
        OutputFunctions.line(s);
    }


    public static void                  line(String format, Object first_argument, Object ... other_arguments)
    {
        OutputFunctions.line(format, first_argument, other_arguments);
    }


    public static int                   limit_to_between(int minimum, int v, int maximum)
    {
        if (v < minimum) {
            return minimum;
        }

        if (v > maximum) {
            return maximum;
        }

        return v;
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
