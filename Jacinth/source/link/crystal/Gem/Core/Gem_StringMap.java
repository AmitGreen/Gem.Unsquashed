//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   Gem_StringMap<INSPECTION extends Inspection, V>
    extends             Gem_Map      <INSPECTION, String,            V>
//  extends             HashMap                  <String,            V>
//  extends             AbstractHashMap          <String,            V>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Constructor
    //
    protected                           Gem_StringMap(final Zone z, final int initial_capacity)
    {
        super(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        final Inspection                inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, " size<", this.size(), ">>");
    }


    //
    //  Public
    //
    public /*overrideable*/ void        dump(final String name)
    {
        final Inspection                inspection = this.inspect();

        final String                    simple_class_name = inspection.simple_class_name;

        final List<String>              keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {} {}", simple_class_name, name);
        line("  size: {}", total);

        for (/*:*/ int                  i = 0; i < total; i ++) {
            final String                k = keys.get(i);
            final V                     v = this.get(k);

            line("  {}: {}", String.format("%40s", z.quote_string(k)), v);
        }

        line("End of dump of {} {}", simple_class_name, name);
    }


    public final V                      find(final String k)
    {
        assert fact_pointer(k, "k");

        final V                         r = this.get(k);

        if (r == null) {
            RUNTIME("cannot find key {}", k);
        }

        return r;
    }
}
