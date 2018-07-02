//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Mirror;


import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Silver.SilverModule;
import link.crystal.Silver.SilverProxy;


public class    Shape
    extends     SilverProxy<Shape, link.crystal.Jacinth.Shape>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Mirror.Shape");


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
        line("Mirror.shape: create: {0}", shape_name);
        line("{0} + {1}", shape_name, "hello");

        link.crystal.Jacinth.Shape                   client = link.crystal.Jacinth.Shape.create(shape_name);

        return new Shape(client);
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
        link.crystal.Jacinth.Shape                   client = this.client;

        System.out.println("Mirror.skew");

        client.skew();
    }
}
