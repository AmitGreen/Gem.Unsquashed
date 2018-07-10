//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public class    UniqueName
    extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("UniqueName");


    //
    //  Members
    //
    private final String                prefix;
    private       int                   value;


    //
    //  Constructor & Factory
    //
    protected                           UniqueName(String prefix)
    {
        this.prefix = prefix;
        this.value  = 0;
    }


    public static UniqueName            create__ALLY__Gem(Zone z, String prefix)
    {
        final String                    interned_prefix = z.intern_permenant_string(prefix);

        return new UniqueName(prefix);
    }


    //
    //  Interface Inspectable
    //
    public Inspection               inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<UniqueName ");
        builder.quote(this.prefix);
        builder.append(" ", this.value,">");
    }


    //
    //  Ally
    //
    public void                         skip_value__ALLY__UnitTest(int value)
    {
        assert fact(this.value < value, "this.value < value");;

        this.value = value;
    }


    public int                          value__ALLY__UnitTest()
    {
        return this.value;
    }


    //
    //  Public
    //
    public String                       next()
    {
        final int                       value = this.value;

        assert fact(value >= 0, "this.value<{}> >= 0", value);

        this.value = value + 1;

        return this.prefix + Integer.toString(value);
    }
}
