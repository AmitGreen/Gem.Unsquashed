//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;


public abstract class   ExceptionFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public
    //
    public static void                  RAISE_runtime_exception(Zone z, String error_message)
    {
        throw new RuntimeException(error_message);
    }


    public static void                  RAISE_runtime_exception(Zone z, String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        String                          error_message = formattable.arrange(z, 2, v);

        throw new RuntimeException(error_message);
    }


    public static void                  RAISE_runtime_exception(
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

        String                          error_message = formattable.arrange(z, 2, v, other_arguments);

        throw new RuntimeException(error_message);
    }
}
