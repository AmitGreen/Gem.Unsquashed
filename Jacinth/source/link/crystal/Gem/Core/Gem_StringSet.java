//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


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
    public void                         portray(Gem_StringBuilder builder)
    {
        final INSPECTION                inspection = this.inspect();

        final List<String>              keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       keys_total = keys.size();

        builder.append("<", inspection.simple_class_name, " size<", keys_total, ">");

        for (int                        i = 0; i < keys_total; i ++) {
            final String                k = keys.get(i);

            if (i == 0) {
                builder.append("; ");
            } else {
                builder.append(", ");
            }

            builder.quote(k);
        }

        builder.append(">");
    }


    //
    //  Public
    //
    public void                         dump(String name)
    {
        final INSPECTION                inspection = this.inspect();

        final String                    simple_class_name = inspection.simple_class_name;

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {}", simple_class_name + " " + name);
        line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            final String                k = keys.get(i);

            line("  {}", k);
        }

        line("End of dump of {}", simple_class_name + " " + name);
    }
}
