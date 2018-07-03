//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public class    Shape 
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
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


    public static Shape                 create(Zone z, String shape_name)
    {
        return new Shape(shape_name);
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
        return "<Shape " + this.shape_name + ">";
    }


    //
    //  Public
    //
    public void                         skew(Zone z)
    {
        z.line("Shape.skew: " + this.shape_name);
    }
}
