//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public final class  Shape
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Shape");


    //
    //  Members
    //
    public final String                 shape_name;


    //
    //  Constructor & Factory
    //
    private                             Shape(final String shape_name)
    {
        this.shape_name = shape_name;
    }


    public static final Shape           create(final Zone z, final String shape_name)
    {
        return new Shape(shape_name);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<Shape ", this.shape_name, ">");
    }


    //
    //  Public
    //
    public final void                   skew()
    {
        line("Shape.skew: " + this.shape_name);
    }
}
