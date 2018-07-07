//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Mirror;


import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Silver.SilverProxy;


public class    Shape
    extends     SilverProxy<Shape, link.crystal.Jacinth.Shape>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Mirror.Shape");


    //
    //  Constructor & Factory
    //
    private                             Shape(Zone z, link.crystal.Jacinth.Shape client)
    {
        super(z, client);
    }


    public static Shape                 create(Zone z, String shape_name)
    {
        final Class<link.crystal.Jacinth.Shape>     meta = link.crystal.Jacinth.Shape.class;

        final link.crystal.Jacinth.Shape    client = link.crystal.Jacinth.Shape.create(z, shape_name);

        return new Shape(z, client);
    }


    //
    //  Interface Inspectable
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
        final link.crystal.Jacinth.Shape    client = this.client;

        line("Mirror.skew");

        client.skew();
    }
}
