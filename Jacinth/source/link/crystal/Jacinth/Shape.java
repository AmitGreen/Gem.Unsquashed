//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.GemObject;
import link.crystal.Gem.Inspection;


public class    Shape 
    extends     GemObject
{
    private static Inspection           inspection = Inspection.create("Shape");


    //
    //  Members
    //
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


    //
    //  Abstract GemObject
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public
    //
    public void                         skew()
    {
        line("Shape.skew: " + this.shape_name);
    }
}
