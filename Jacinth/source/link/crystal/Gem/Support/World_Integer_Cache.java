//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.Support.World_Integer_WeakReference;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_Cache
    extends     WeakReference_Cache<World_Integer_WeakReference, Comparable_Inspection, World_Integer>
//  extends     Gem_Map         <Inspection, World_Integer_WeakReference, World_Integer_WeakReference>
//  extends     HashMap                     <World_Integer_WeakReference, World_Integer_WeakReference>
//  extends     AbstractHashMap             <World_Integer_WeakReference, World_Integer_WeakReference>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Map<?, ?, ?>
{
    private static final Inspection     inspection = Inspection.create("World_Integer_Cache");


    //
    //  Static members
    //
    private static final int            initial_capacity = 1009;


    //
    //  Constructor
    //
    private                             World_Integer_Cache(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static World_Integer_Cache   create__ALLY__Gem()
    {
        final Zone                      z = Zone.current_zone();

        return new World_Integer_Cache(z, World_Integer_Cache.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
