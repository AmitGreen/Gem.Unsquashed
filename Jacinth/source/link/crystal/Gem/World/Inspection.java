//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.World_Inspection;


public class    Inspection
    extends     Gem_Object    <World_Inspection>
//  extends     Object
    implements  Gem_Comparable<World_Inspection>,
                Inspectable   <World_Inspection>//,                     //  Via Gem_Object
{
    private static final World_Inspection   inspection = World_Inspection.create("Inspection", 1);


    //
    //  Members
    //
    public final String                 simple_class_name;


    //
    //  Constructor & Factory
    //
    protected                           Inspection(String simple_class_name)
    {
        this.simple_class_name = simple_class_name;

        Map_String_Inspection.insert_or_cache(this);
    }


    public static Inspection            create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Inspection(interned__simple_class_name);
    }


    //
    //  Interface Gem_Comparable
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        if (this == that) {
            return 0;
        }

        final Comparable_Inspection     that_inspection = that.inspect();

        if ( ! that_inspection.is_world_inspection) {
            final World_Inspection      this_inspection = this.inspect();

            final int                   r = this_inspection.class_order - that_inspection.class_order;

            assert fact(r != 0, "r != 0");

            return r;
        }

        final Inspection                that_2 = (Inspection) that;

        final int                       r = this.simple_class_name.compareTo(that_2.simple_class_name);

        assert fact(r != 0, "r != 0");

        return r;
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
        assert fact_pointer(this,    "this");
        assert fact_pointer(builder, "builder");

        final World_Inspection          meta_inspection = this.inspect();

        //
        //  NOTE:
        //      During startup initialization, it could be that any (or all) of the following could be null:
        //
        //      1.  `meta_inspection`,
        //      2.  `meta_inspection.simple_class_name`, AND/OR
        //      3.  `this.simple_class_name`
        //
        builder.append(
            "<",
            (
                (meta_inspection == null || meta_inspection.simple_class_name == null)
                    ? "<INSPECTION extends World_Inspection>"
                    : meta_inspection.simple_class_name
            ),
            " ",
            (
                this.simple_class_name == null
                    ? "<INSPECTION extends Inspection>"
                    : this.simple_class_name
            ),
            ">"
        );
    }
}
