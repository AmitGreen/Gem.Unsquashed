//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public class    Comparable_Inspection
    extends     Inspection
//  extends     Gem_Object    <World_Inspection>
//  extends     Object
    implements  Gem_Comparable<World_Inspection>,
                Inspectable   <World_Inspection>//,                     //  Via Gem_Object
{
    private static final World_Inspection   inspection = World_Inspection.create("Comparable_Inspection", 6);


    //
    //  Members
    //
    public final int                    class_order;
    public final boolean                is_world_inspection;


    //
    //  Constructor & Factory
    //
    protected                           Comparable_Inspection(
            String                          simple_class_name,
            int                             class_order,
            boolean                         is_world_inspection//,
        )
    {
        super(simple_class_name);

        this.class_order         = class_order;
        this.is_world_inspection = is_world_inspection;
    }


    public static Comparable_Inspection     create(String simple_class_name, int class_order)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Comparable_Inspection(
                   interned__simple_class_name,
                   class_order,
                   /*is_world_inspection=*/  false//,
               );
    }


    //
    //  Interface Inspectable
    //
    public World_Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        final World_Inspection          meta_inspection = this.inspect();

        builder.append("<", meta_inspection.simple_class_name, " ", this.simple_class_name, " ", this.class_order);

        if (this.is_world_inspection) {
            builder.append("; is_world_inspection");
        }

        builder.append(">");
    }
}


//
//  class_order
//      Inspection                           1
//      NormalSegmentFormatter_Inspection    2
//      PortraySegmentFormatter_Inspection   3
//      SegmentFormatter_Inspection          4
//      StringSegmentFormatter_Inspection    5
//      Comparable_Inspection                6
//      World_Inspection                     7
//      World_Integer                        8
//      World_Integer_WeakReference          9
//      World_String                        10
//      World_String_WeakReference          11
//
