//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.PortrayFunctions;


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
    protected                           Gem_StringMap(int initial_capacity)
    {
        super(initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public String                       portray()
    {
        Inspection                      inspection = this.inspect();

        StringBuilder                   b = new StringBuilder();

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        b.append("<");
        b.append(inspection.simple_class_name);
        b.append(" size<");
        b.append(Integer.toString(total));
        b.append(">");

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            if (i == 0) {
                b.append("; ");
            } else {
                b.append(", ");
            }

            b.append(PortrayFunctions.portray_string(k));
            b.append(" : ");
            b.append(PortrayFunctions.portray(v));
        }

        b.append(">");

        return b.toString();
    }


    //
    //  Public
    //
    public void                         dump(String name)
    {
        Inspection                      inspection = this.inspect();

        String                          simple_class_name = inspection.simple_class_name;

        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        line("Dump of {0}", simple_class_name + " " + name);
        line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            V                           v = this.get(k);

            line(
                      "  "
                    + String.format("%30s", PortrayFunctions.portray_string(k))
                    + ": "
                    + PortrayFunctions.portray(v)
                );
        }

        line("End of dump of {0}", simple_class_name + " " + name);
    }
}
