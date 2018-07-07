//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Exception;


import java.lang.RuntimeException;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public class        AssertionError
    extends         RuntimeException
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("AssertionError");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    private                             AssertionError(Zone z, String error_message)
    {
        super(error_message);

        this.z = z;
    }


    static public AssertionError        create(Zone z, String error_message)
    {
        return new AssertionError(z, error_message);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }

    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<AssertionError ");
        builder.quote(this.getMessage());
        builder.quote(">");
    }
}
