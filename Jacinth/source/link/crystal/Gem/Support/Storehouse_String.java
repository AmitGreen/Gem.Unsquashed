//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringSet;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.PortrayFunctions;


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
    private                             Storehouse_String(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static Storehouse_String    create()
    {
        return new Storehouse_String(Storehouse_String.initial_capacity);
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
    private static Storehouse_String    singleton()
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_String.singleton = Storehouse_String.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton();
        }

        singleton.dump("Storehouse_String.singleton");
    }


    public static String                intern_permenant_string(String s)
    {
        if (s == null) {
            RAISE_runtime_exception("Storehouse_String.intern_permenant_string: `s` is null");
        }

        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton();
        }

        String                          previous = singleton.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
