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
    private static Inspection           inspection = Inspection.create_with_portrait("Mirror.Shape");


    //
    //  Constructor & Factory
    //
    private                             Shape(Zone z, link.crystal.Jacinth.Shape client)
    {
        super(z, client);
    }


    public static Shape                 create(Zone z, String shape_name)
    {
        Class<link.crystal.Jacinth.Shape>   meta = link.crystal.Jacinth.Shape.class;

        z.line(meta.getCanonicalName());
        z.line("Mirror.shape: create: {0}", shape_name);
        z.line("{0} + {2} = {1}; and even more {3} -- yep", shape_name, "hello", "greetings", "stuff");

        link.crystal.Jacinth.Shape      client = link.crystal.Jacinth.Shape.create(z, shape_name);

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
    public void                         skew(Zone z)
    {
        link.crystal.Jacinth.Shape                   client = this.client;

        System.out.println("Mirror.skew");

        client.skew(z);
    }
}
