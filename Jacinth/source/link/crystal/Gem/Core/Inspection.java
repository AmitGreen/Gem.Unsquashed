//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public class    Inspection
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Inspection");


    //
    //  Members
    //
    public String                       simple_class_name;
    public String                       portrait_0;
    public boolean                      is_silver_proxy;


    //
    //  Constructor & Factory
    //
    private                             Inspection(String simple_class_name, String portrait_0, boolean is_silver_proxy)
    {
        this.is_silver_proxy   = is_silver_proxy;
        this.portrait_0        = portrait_0;
        this.simple_class_name = simple_class_name;
    }


    public static Inspection            create(String simple_class_name)
    {
        Zone                            z = Zone.current_zone();

        String                          interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Inspection(interned__simple_class_name, null, false);
    }


    public static Inspection            create_with_portrait(String simple_class_name)
    {
        Zone                            z = Zone.current_zone();

        String                          interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        String                          interned__portrait = z.intern_permenant_string("<" + simple_class_name + ">");

        return new Inspection(interned__simple_class_name, interned__portrait, false);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public String                       portray()
    {
        return "<Gem.Inspection " + this.simple_class_name + ">";
    }
}
