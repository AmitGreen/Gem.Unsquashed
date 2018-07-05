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
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.ExceptionFunctions;
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

        final String                    portrait_0 = inspection.portrait_0;

        if (portrait_0 == null) {
            final Zone                  z = builder.z;

            z.RUNTIME("`{0}.inspect().portrait_0` is `null`", inspection.simple_class_name);
        }

        builder.append(portrait_0);
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
}
