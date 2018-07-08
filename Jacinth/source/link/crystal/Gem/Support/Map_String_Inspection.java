//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public class    Map_String_Inspection
    extends     Gem_StringMap  <Inspection,         Inspection>
//  extends     Gem_Map        <Inspection, String, Inspection>
//  extends     HashMap                    <String, Inspection>
//  extends     AbstractHashMap            <String, Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_StringMap<?>
{
    private static final Inspection         inspection = Inspection.create("Map_String_Inspection");


    //
    //  Initialization
    //
    private static       Map_String_Inspection  singleton = Map_String_Inspection.singleton();


    //
    //  Static members
    //
    private static final int            initial_capacity = 101;
    private static       Inspection[]   cache            = null;
    private static final int            cache_allocated  = 10;
    private static       int            cache_index      = 0;


    //
    //  Constructor & Factory
    //
    private                             Map_String_Inspection(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static Map_String_Inspection     singleton()
    {
        Map_String_Inspection               singleton = Map_String_Inspection.singleton;

        if (singleton != null) {
            return singleton;
        }

        final Zone                      z = Zone.current_zone();

        singleton = new Map_String_Inspection(z, Map_String_Inspection.initial_capacity);

        //
        //  NOTE:
        //      In case of loops, that a routine we call, then calls `.cache_or_insert`, we want to make sure
        //      that `.singleton` is set when `.cache_or_insert` is called.
        //
        Map_String_Inspection.singleton = singleton;

        //
        //  Clear the cache ...
        //
        final Inspection[]              cache       = Map_String_Inspection.cache;
        final int                       cache_index = Map_String_Inspection.cache_index;

        for (int                        i        = 0; i < cache_index; i ++) {
            final Inspection            previous = cache[i];

            singleton.insert(z, previous.simple_class_name, previous);
        }

        Map_String_Inspection.cache       = null;
        Map_String_Inspection.cache_index = 0;


        //
        //  Overwrite `.singleton` with the [same] value.
        //
        return singleton;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public
    //
    public void                         dump(String name)
    {
        final Inspection                inspection = this.inspect();

        final String                    simple_class_name = inspection.simple_class_name;

        final ArrayList<Inspection>     values = new ArrayList<Inspection>(this.values());

        Collections.sort(values);

        final int                       total = values.size();

        line("Dump of {}", simple_class_name + " " + name);
        line("  size: {}", total);

        for (int                        i = 0; i < total; i ++) {
            final Inspection            v = values.get(i);

            line("  {}", v);
        }

        line("End of dump of {}", simple_class_name + " " + name);
    }


    public static void                  insert_or_cache(Inspection v)
    {
        final Map_String_Inspection     singleton = Map_String_Inspection.singleton;

        if (singleton != null) {
            final Zone                  z = singleton.z;

            singleton.insert(z, v.simple_class_name, v);

            return;
        }

        //
        //  NOTE:
        //      `singleton` has not yet been initialized ... so temporarily cache `v`
        //
        Inspection[]                    cache           = Map_String_Inspection.cache;
        final int                       cache_allocated = Map_String_Inspection.cache_allocated;
        final int                       cache_index     = Map_String_Inspection.cache_index;

        if (cache == null) {
            cache =
                Map_String_Inspection.cache = new Inspection[cache_allocated];
        }

        assert fact(cache_index < cache_allocated, "cache_index < cache_allocated");

        //output("Caching: " + v.simple_class_name);

        cache[cache_index] = v;

        Map_String_Inspection.cache_index = cache_index + 1;
    }
}
