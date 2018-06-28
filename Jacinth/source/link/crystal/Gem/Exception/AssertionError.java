//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Exception;


import java.lang.RuntimeException;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public final class      AssertionError
    extends             RuntimeException
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("AssertionError");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    private                             AssertionError(final Zone z, final String error_message)
    {
        super(error_message);

        this.z = z;
    }


    public static final AssertionError  create(final Zone z, final String error_message)
    {
        return new AssertionError(z, error_message);
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
        builder.append("<AssertionError ");
        builder.java_quote(this.getMessage());
        builder.append(">");
    }
}
