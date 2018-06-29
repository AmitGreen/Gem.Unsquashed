//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import link.crystal.Silver.SilverObject;


public class    Inspection
    extends     SilverObject
//  extends     Object
{
    private static Inspection           inspection = Inspection.create("Silver.SilverObject");


    //
    //  Members
    //
    private String                      simple_class_name;


    //
    //  Constructor & Factory
    //
    private                             Inspection(String simple_class_name)
    {
        this.simple_class_name = simple_class_name;
    }


    public static Inspection            create(String simple_class_name)
    {
        return new Inspection(simple_class_name);
    }


    //
    //  Abstract SilverObject
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
