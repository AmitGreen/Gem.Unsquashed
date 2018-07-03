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
    extends             Gem_Map<INSPECTION, String, V>
//  extends             HashMap            <String, V>
//  extends             AbstractHashMap    <String, V>
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
    public String                       portray(Zone z)
    {
        Inspection                      inspection = this.inspect();

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        builder.append("<", inspection.simple_class_name, " size<", total, ">");

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            if (i == 0) {
                builder.append("; ");
            } else {
                builder.append(", ");
            }

            builder.append(z.quote_string(k), " : ", z.portray(v));
        }

        builder.append(">");

        return builder.finish__AND__recycle();
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

        z.line("Dump of {0}", simple_class_name + " " + name);
        z.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            z.line("  " + String.format("%30s", z.quote_string(k)) + ": " + z.portray(v));
        }

        z.line("End of dump of {0}", simple_class_name + " " + name);
    }
}
