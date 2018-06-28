//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public final class  UniqueName
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UniqueName");


    //
    //  Members
    //
    private final String                prefix;
    private /*:*/ int                   value;


    //
    //  Constructor & Factory
    //
    protected                           UniqueName(final String prefix)
    {
        this.prefix = prefix;
        this.value  = 0;
    }


    public static final UniqueName      create__ALLY__Gem(final Zone z, final String prefix)
    {
        final String                    interned_prefix = z.intern_permenant_string(prefix);

        return new UniqueName(prefix);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection         inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<UniqueName ");
        builder.java_quote(this.prefix);
        builder.append(" ", this.value,">");
    }


    //
    //  Ally
    //
    public final void                   skip_value__ALLY__UnitTest(final int value)
    {
        assert fact(this.value < value, "this.value < value");;

        this.value = value;
    }


    public final int                    value__ALLY__UnitTest()
    {
        return this.value;
    }


    //
    //  Public
    //
    public final String                 next()
    {
        final int                       value = this.value;

        assert fact(value >= 0, "this.value<{}> >= 0", value);

        this.value = value + 1;

        return this.prefix + Integer.toString(value);
    }
}
