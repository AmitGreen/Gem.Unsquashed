//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Mirror;


import link.crystal.Gem.Inspection;
import link.crystal.Silver.SilverModule;
import link.crystal.Silver.SilverProxy;


public class    Shape
    extends     SilverProxy<Shape, link.crystal.Jacinth.Shape>
{
    private static Inspection           inspection = Inspection.create("Mirror.Shape");


    //
    //  Constructor & Factory
    //
    private                             Shape(link.crystal.Jacinth.Shape client)
    {
        super(client);
    }


    public static Shape                 create(String shape_name)
    {
        if (SilverModule.startup) {
            SilverModule.initialize();
        }

        Class<link.crystal.Jacinth.Shape>   meta = link.crystal.Jacinth.Shape.class;

        line(meta.getCanonicalName());
        line("Mirror.shape: create({0})", shape_name);

        link.crystal.Jacinth.Shape                   client = link.crystal.Jacinth.Shape.create(shape_name);

        return new Shape(client);
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
        link.crystal.Jacinth.Shape                   client = this.client;

        System.out.println("Mirror.skew");

        client.skew();
    }
}
