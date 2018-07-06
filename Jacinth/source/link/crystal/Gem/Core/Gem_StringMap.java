//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


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
    protected                           Gem_StringMap(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public V                            find(String k)
    {
        if (k == null) {
            final Zone                  z = this.z;

            z.RUNTIME("`k` is null");
        }

        V                               r = this.get(k);

        if (r == null) {
            final Zone                  z = this.z;

            z.RUNTIME("cannot find key {}", k);
        }

        return r;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        Inspection                      inspection = this.inspect();

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        builder.append("<", inspection.simple_class_name, " size<", total, ">");

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            if (i == 0) {
                builder.append("; ");
            } else {
                builder.append(", ");
            }

            builder.arrange("{p} : {}", k, v);
        }

        builder.append(">");
    }


    //
    //  Public
    //
    public void                         dump(Zone z, String name)
    {
        Inspection                      inspection = this.inspect();

        String                          simple_class_name = inspection.simple_class_name;

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        z.line("Dump of {}", simple_class_name + " " + name);
        z.line("      size: {}", total);

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            z.line("  {}: {}", String.format("%30s", z.quote_string(k)), v);
        }

        z.line("End of dump of {}", simple_class_name + " " + name);
    }
}
