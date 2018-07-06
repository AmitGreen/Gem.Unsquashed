//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Class;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;


public abstract class   Gem_Object<INSPECTION extends Inspection>
    extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Static types
    //
    public static final Class<Gem_StringBuilder[]>  Gem_StringBuilder$array$class = Gem_StringBuilder[].class;
    public static final Class<Integer>              Integer$class                 = Integer.class;
    public static final Class<String>               String$class                  = String.class;
    public static final Class<Thread>               Thread$class                  = Thread.class;


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    public void                         portray(Gem_StringBuilder builder)
    {
        final INSPECTION                inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, ">");
    }


    //
    //  Public
    //
    public static void                  assert_null(Object p, String name)
    {
        if (p == null) {
            return;
        }

        final Zone                      z = Zone.current_zone();

        ExceptionFunctions.ASSERT(2, "`{}` is not null", name);
    }


    public static void                  assert_pointer(Object p, String name)
    {
        if (p != null) {
            return;
        }

        final Zone                      z = Zone.current_zone();

        ExceptionFunctions.ASSERT(2, "`{}` is null", name);
    }


    //
    //  Public
    //
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


    //
    //  Public (ERRORS)
    //
    public void                         INVALID_ROUTINE()
    {
        ExceptionFunctions.RUNTIME(2, "invalid routine");
    }


    public void                         RUNTIME(String error_message, Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }
}
