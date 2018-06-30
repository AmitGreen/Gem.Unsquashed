//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import link.crystal.Gem.GemObject;


public class    Inspection
    extends     GemObject
//  extends     Object
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
        return new Inspection(simple_class_name, false);
    }


    //
    //  Abstract GemObject
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
