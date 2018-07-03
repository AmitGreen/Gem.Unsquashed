//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.Core.Gem_Lane;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;


public abstract class   OutputFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public Static
    //
    public static final PrintStream     standard_output = System.out;


    //
    //  Public
    //
    public static void                  line(Gem_Lane z)
    {
        standard_output.println();
    }


    public static void                  line(Gem_Lane z, String s)
    {
        standard_output.println(s);
    }


    public static void                  line(
            Gem_Lane                            z,
            String                              format,
            Object                              first_argument,
            Object ...                          other_arguments//,
        )
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(format);

            Storehouse_MessageFormattable.insert(format, formattable);
        }

        formattable.line(first_argument, other_arguments);
    }


    public static void                  line(String s)
    {
        standard_output.println(s);
    }


    public static void                  line(String format, Object first_argument, Object ... other_arguments)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(format);

            Storehouse_MessageFormattable.insert(format, formattable);
        }

        formattable.line(first_argument, other_arguments);
    }
}
