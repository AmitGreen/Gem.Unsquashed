//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringSet;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public class    Storehouse_String
    extends     Gem_StringSet  <Inspection>
//  extends     Gem_Map        <Inspection, String, String>
//  extends     HashMap                    <String, String>
//  extends     AbstractHashMap            <String, String>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_StringSet
{
    private static Inspection           inspection = Inspection.create("Gem.Support.Storehouse_String");


    //
    //  Private static
    //
    private static final int            initial_capacity = 1009;
    private static Storehouse_String    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_String(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    private static Storehouse_String    create(Zone z)
    {
        return new Storehouse_String(z, Storehouse_String.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Private
    //
    private static Storehouse_String    singleton(Zone z)
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_String.singleton = Storehouse_String.create(z);

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump(Zone z)
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton(z);
        }

        singleton.dump(z, "Storehouse_String.singleton");
    }


    public static String                intern_permenant_string(Zone z, String s)
    {
        if (s == null) {
            z.RUNTIME("`s` is null");
        }

        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton(z);
        }

        String                          previous = singleton.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
