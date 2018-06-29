//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Mirror;


public class    Shape 
{
    public final link.crystal.Jacinth.Shape          client;


    //
    //  Constructor & Factory
    //
    private                             Shape(link.crystal.Jacinth.Shape client)
    {
        this.client = client;
    }


    public static Shape                 create(String shape_name)
    {
        System.out.println("Mirror.shape: create(" + shape_name + ")");

        link.crystal.Jacinth.Shape                   client = link.crystal.Jacinth.Shape.create(shape_name);

        return new Shape(client);
    }

    
    public void                         skew()
    {
        link.crystal.Jacinth.Shape                   client = this.client;

        System.out.println("Mirror.skew");

        client.skew();
    }
}
