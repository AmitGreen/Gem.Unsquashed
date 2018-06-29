//   Copyright (c) 2018 Amit Green.  All rights reserved.


package crystal.link.Jacinth;


public class    Shape 
{
    public final String                 shape_name;


    //
    //  Constructor & Factory
    //
    private                             Shape(String shape_name)
    {
        this.shape_name = shape_name;
    }


    public static Shape                 create(String shape_name)
    {
        return new Shape(shape_name);
    }

    
    public void                         skew()
    {
        System.out.println("Shape.skew: " + this.shape_name);
    }
}
