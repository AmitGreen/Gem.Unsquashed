//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.lang.Object;


public class    Inspection
    extends     Object
{
    //
    //  Members
    //
    private static String               simple_class_name;


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
}
