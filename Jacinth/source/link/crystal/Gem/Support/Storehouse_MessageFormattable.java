//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    Storehouse_MessageFormattable
    extends     Gem_StringMap<Inspection,         MessageFormattable>
//  extends     HashMap                  <String, MessageFormattable>
//  extends     AbstractHashMap          <String, MessageFormattable>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Map<?, ?, ?>
{
    private static Inspection           inspection = Inspection.create_with_portrait("Storehouse_MessageFormattable");


    //
    //  Private static
    //
    private static final int                        initial_capacity = 1009;
    private static Storehouse_MessageFormattable    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_MessageFormattable(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    private static Storehouse_MessageFormattable    create(Zone z)
    {
        return new Storehouse_MessageFormattable(z, Storehouse_MessageFormattable.initial_capacity);
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
    private static Storehouse_MessageFormattable    singleton(Zone z)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_MessageFormattable.singleton = Storehouse_MessageFormattable.create(z);

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump(Zone z)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton(z);
        }

        singleton.dump(z, "Storehouse_MessageFormattable.singleton");
    }


    public static void                  insert(Zone z, String k, MessageFormattable v)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton(z);
        }

        MessageFormattable              previous = singleton.putIfAbsent(k, v);

        if (previous != null) {
            z.RUNTIME("previous value for {p} already exists: {}", k, z);
        }
    }


    public static MessageFormattable    lookup(Zone z, String k)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton(z);
        }

        return singleton.get(k);
    }
}
