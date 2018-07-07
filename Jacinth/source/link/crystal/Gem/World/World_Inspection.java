//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public class    World_Inspection
    extends     Inspection
//  extends     Gem_Object <World_Inspection>
//  extends     Object
    implements  Gem_Comparable,
                Inspectable<World_Inspection>//,                        //  Via Gem_Object
{
    private static final World_Inspection   inspection = World_Inspection.create("World_Inspection", 6);


    //
    //  Members
    //
    public final int                    class_order;


    //
    //  Constructor & Factory
    //
    protected                           World_Inspection(String simple_class_name, int class_order)
    {
        super(simple_class_name);

        this.class_order = class_order;
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


    public void                         portray(Gem_StringBuilder builder)
    {
        final World_Inspection          meta_inspection = this.inspect();

        builder.append("<", meta_inspection.simple_class_name, " ", this.simple_class_name, " ", this.class_order, ">");
    }
}


//
//  class_order
//      Inspection                          1
//      NormalSegmentFormatter_Inspection   2
//      PortraySegmentFormatter_Inspection  3
//      SegmentFormatter_Inspection         4
//      StringSegmentFormatter_Inspection   5
//      World_Inspection                    6
//
