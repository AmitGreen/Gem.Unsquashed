//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Inspection;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Comparable_Inspection;


public class    World_Inspection
    extends     Comparable_Inspection
//  extends     Inspection
//  extends     Gem_Object    <World_Inspection>
//  extends     Object
    implements  Gem_Comparable<World_Inspection>,
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable   <World_Inspection>//,                             //  Via Gem_Comparable
{
    private static final World_Inspection   inspection = World_Inspection.create("World_Inspection");


    //
    //  Constructor & Factory
    //
    private                             World_Inspection(String simple_class_name)
    {
        super(
                simple_class_name,
                Comparable_Inspection.CLASS_ORDER__INSPECTION,
                /*is_world_inspection=*/ true//,
            );
    }


    public static World_Inspection      create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new World_Inspection(interned__simple_class_name);
    }


    //
    //  Interface Inspectable
    //
    public World_Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }
}
