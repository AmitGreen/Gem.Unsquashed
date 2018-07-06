//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Map_String_Inspection;


public class    Inspection
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Inspection");


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
    }


    public static Inspection            create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        final Inspection                r = new Inspection(interned__simple_class_name);

        Map_String_Inspection.insert_or_cache(r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        assert fact_pointer(this,    "this");
        assert fact_pointer(builder, "builder");

        final Inspection                meta_inspection = this.inspect();

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
                    ? "<INSPECTION extends Inspection>"
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
