//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;


public abstract class   Storehouse_SmallList<STOREHOUSE extends Storehouse_SmallList, ELEMENT extends Gem_Object>
    extends             Gem_Object<Inspection>
//  extends             Object
    implements          Inspectable<Inspection>//,                      //  Via Gem_Object
{
    //
    //  Members
    //
    protected final Zone                z;
    protected final ELEMENT[]           segment_many;


    //
    //  Constructor & Factory
    //
    protected                           Storehouse_SmallList(Zone z, ELEMENT[] segment_many)
    {
        this.z            = z;
        this.segment_many = segment_many;
    }


    //
    //  Public
    //
    public void                         insert(int argument_index, ELEMENT segment)
    {
        final ELEMENT[]                 segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        assert fact_between(0, argument_index, segment_allocated - 1);
        assert fact_null   (segment_many[argument_index], "segment_many[argument_index]");

        segment_many[argument_index] = segment;
    }


    public ELEMENT                      lookup(int argument_index)
    {
        final ELEMENT[]                 segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        assert fact_between(0, argument_index, segment_allocated - 1);

        return this.segment_many[argument_index];
    }


    public void                         dump(Zone z)
    {
        final Inspection                inspection = this.inspect();

        final String                    simple_class_name = inspection.simple_class_name;

        final ELEMENT[]                 segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        z.line("Dump of {}", simple_class_name);
        z.line("  size:  {}", segment_allocated);

        for (int                        i       = 0; i < segment_allocated; i ++) {
            final ELEMENT               segment = segment_many[i];

            if (segment == null) {
                continue;
            }

            z.line("  {}:  {}", i, segment);
        }

        z.line("End of dump of {}", simple_class_name);
    }
}
