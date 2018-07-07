//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.World_Inspection;


public class    World_Inspection
    extends     Comparable_Inspection
//  extends     Inspection
//  extends     Gem_Object <World_Inspection>
//  extends     Object
    implements  Gem_Comparable,
                Inspectable<World_Inspection>//,                        //  Via Comparable_Inspection
{
    private static final World_Inspection   inspection = World_Inspection.create("World_Inspection", 7);


    //
    //  Constructor & Factory
    //
    private                             World_Inspection(String simple_class_name, int class_order)
    {
        super(
                simple_class_name,
                class_order,
                /*is_world_inspection=*/ true//,
            );
    }


    public static World_Inspection      create(String simple_class_name, int class_order)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new World_Inspection(interned__simple_class_name, class_order);
    }


    //
    //  Interface Gem_Comparable
    //
    public int                          compareTo(Gem_Comparable that)
    {
        INVALID_ROUTINE();

        return 0;
    }


    //
    //  Interface Inspectable
    //
    public World_Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }
}
