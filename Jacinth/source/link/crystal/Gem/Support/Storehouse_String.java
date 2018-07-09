//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringSet;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.Interface.Interface__Storehouse_String;


public class    Storehouse_String
    extends     Gem_StringSet<Inspection>
//  extends     Gem_Map      <Inspection, String, String>
//  extends     HashMap                  <String, String>
//  extends     AbstractHashMap          <String, String>
//  extends     Object
    implements  Interface__Storehouse_String,
                Inspectable<Inspection>//,                              //  Via Gem_StringSet
{
    private static final Inspection     inspection = Inspection.create("Storehouse_String");


    //
    //  Private static
    //
    private static final int                initial_capacity = 1009;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_String(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static Storehouse_String     create__ALLY__Zone(Zone z)
    {
        return new Storehouse_String(z, Storehouse_String.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface Interface__Storehouse_String
    //
    public String                       intern_permenant_string(Zone z, String s)
    {
        assert fact        (this.z == z, "this.z == z");
        assert fact_pointer(s, "s");

        final String                    previous = this.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }


    public void                         insert_permenant_string(Zone z, String s)
    {
        this.insert(z, s, s);
    }
}
