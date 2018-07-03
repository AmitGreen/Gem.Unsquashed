//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   Gem_StringSet<INSPECTION extends Inspection>
    extends             Gem_Map<INSPECTION, String, String>
//  extends             HashMap            <String, String>
//  extends             AbstractHashMap    <String, String>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Constructor
    //
    protected                           Gem_StringSet(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public String                       portray(Zone z)
    {
        INSPECTION                      inspection = this.inspect();

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        builder.append("<", inspection.simple_class_name, " size<", total, ">");

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);

            if (i == 0) {
                builder.append("; ");
            } else {
                builder.append(", ");
            }

            builder.append(z.quote_string(k));
        }

        builder.append(">");

        return builder.finish__AND__recycle();
    }


    //
    //  Public
    //
    public void                         dump(Zone z, String name)
    {
        INSPECTION                      inspection = this.inspect();

        String                          simple_class_name = inspection.simple_class_name;

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        z.line("Dump of {0}", simple_class_name + " " + name);
        z.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);

            z.line("  " + z.quote_string(k));
        }

        z.line("End of dump of {0}", simple_class_name + " " + name);
    }
}
