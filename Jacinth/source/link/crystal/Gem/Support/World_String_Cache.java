//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_ComparableReference_Cache;
import link.crystal.Gem.Support.World_String_WeakReference;
import link.crystal.Gem.World.World_String;


public class    World_String_Cache
    extends     Gem_ComparableReference_Cache<
                    Inspection,
                    World_String,
                    Comparable_Inspection,
                    Gem_ComparableReference_Interface<
                        ? extends Gem_Reference_Inspection,
                        World_String,
                        Comparable_Inspection//,
                    >//,
                >
//  extends     Gem_Map        <Inspection, Gem_ComparableReference_Interface<?, ?, ?>, ...>
//  extends     HashMap        <Inspection, Gem_ComparableReference_Interface<?, ?, ?>, ...>
//  extends     AbstractHashMap<Inspection, Gem_ComparableReference_Interface<?, ?, ?>, ...>
//  extends     Object
    implements  Inspectable    <Inspection>//,                          //  Via Gem_Map<?, ?, ?>
{
    private static final Inspection     inspection = Inspection.create("World_String_Cache");


    //
    //  Static members
    //
    private static final int            initial_capacity = 1009;


    //
    //  Constructor
    //
    private                             World_String_Cache(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static World_String_Cache    create__ALLY__Gem()
    {
        final Zone                      z = Zone.current_zone();

        return new World_String_Cache(z, World_String_Cache.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
