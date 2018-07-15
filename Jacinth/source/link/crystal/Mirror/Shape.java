//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Mirror;


import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Silver.SilverProxy;


public final class  Shape
    extends         SilverProxy<Shape, link.crystal.Jacinth.Shape>
//  extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Mirror.Shape");


    //
    //  Constructor & Factory
    //
    private                             Shape(final Zone z, final link.crystal.Jacinth.Shape client)
    {
        super(z, client);
    }


    public static final Shape           create(final Zone z, final String shape_name)
    {
        final Class<link.crystal.Jacinth.Shape>     meta = link.crystal.Jacinth.Shape.class;

        final link.crystal.Jacinth.Shape    client = link.crystal.Jacinth.Shape.create(z, shape_name);

        return new Shape(z, client);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public
    //
    public final void                   skew()
    {
        final link.crystal.Jacinth.Shape    client = this.client;

        line("Mirror.skew");

        client.skew();
    }
}
