//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


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
    public final boolean                is_silver_proxy;


    //
    //  Constructor & Factory
    //
    protected                           Inspection(String simple_class_name, boolean is_silver_proxy)
    {
        this.simple_class_name = simple_class_name;
        this.is_silver_proxy   = is_silver_proxy;
    }


    public static Inspection            create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Inspection(interned__simple_class_name, false);
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
        final Inspection                meta_inspection = this.inspect();

        builder.append("<", meta_inspection.simple_class_name, " ", this.simple_class_name, ">");
    }
}
