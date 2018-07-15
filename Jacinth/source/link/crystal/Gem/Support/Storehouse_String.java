//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringSet;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Storehouse_String__Interface;
import link.crystal.Gem.Inspection.Inspection;


public final class  Storehouse_String
    extends         Gem_StringSet<Inspection>
//  extends         Gem_Map      <Inspection, String, String>
//  extends         HashMap                  <String, String>
//  extends         AbstractHashMap          <String, String>
//  extends         Object
    implements      Storehouse_String__Interface,
                    Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Storehouse_String");


    //
    //  Private static
    //
    private static final int            initial_capacity = 1009;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_String(final Zone z, final int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static final Storehouse_String   create__ALLY__Zone(final Zone z)
    {
        return new Storehouse_String(z, Storehouse_String.initial_capacity);
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
    //  Interface Storehouse_String__Interface
    //
    public final String                 intern_permenant_string(final Zone z, final String s)
    {
        assert fact        (this.z == z, "this.z == z");
        assert fact_pointer(s, "s");

        final String                    previous = this.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }


    public final void                   insert_permenant_string(final Zone z, final String s)
    {
        this.insert(z, s, s);
    }
}
