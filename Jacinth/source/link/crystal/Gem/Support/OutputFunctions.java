//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Core.Zone;
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
    public static void                  line(Zone z)
    {
        standard_output.println();
    }


    public static void                  line(Zone z, String s)
    {
        standard_output.println(s);
    }


    public static void                  line(Zone z, int depth, String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.line(z, depth + 1, v);
    }


    public static void                  line(Zone z, String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.line(z, 2, v);
    }


    public static void                  line(
            Zone                                z,
            String                              format,
            Object                              v,
            Object ...                          other_arguments//,
        )
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.line(z, 1, v, other_arguments);
    }
}
