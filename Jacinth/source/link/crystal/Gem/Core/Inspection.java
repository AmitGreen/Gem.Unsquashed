//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Interface.Inspectable;


public class    Inspection
    extends     GemObject<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via GemObject
{
    private static Inspection           inspection = Inspection.create("Gem.Inspection");


    //
    //  Members
    //
    public String                       simple_class_name;
    public boolean                      is_silver_proxy;


    //
    //  Constructor & Factory
    //
    private                             Inspection(String simple_class_name, boolean is_silver_proxy)
    {
        this.simple_class_name = simple_class_name;
        this.is_silver_proxy   = is_silver_proxy;
    }


    public static Inspection            create(String simple_class_name)
    {
        String                          interned__simple_class_name = intern_permenant_string(simple_class_name);

        return new Inspection(interned__simple_class_name, false);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
