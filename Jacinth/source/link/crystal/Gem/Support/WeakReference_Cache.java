//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.Inspection;


public abstract class   WeakReference_Cache<
                            K                    extends Gem_WeakReference<REFERENCE_INSPECTION, REFERENCE_CLIENT>,
                            REFERENCE_INSPECTION extends Comparable_Inspection,
                            REFERENCE_CLIENT     extends WeakReferenceable//,
                        >
    extends             Gem_Map         <Inspection, K, K>
//  extends             HashMap                     <K, K>
//  extends             AbstractHashMap             <K, K>
//  extends             Object
    implements          Inspectable<Inspection>//,                      //  Via Gem_Map<?, ?, ?>
{
    //
    //  Constructor
    //
    protected                           WeakReference_Cache(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    //
    public abstract Inspection          inspect();


    public void                         portray(Gem_StringBuilder builder)
    {
        final Inspection                inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, " total<", this.size(), ">>");
    }


    //
    //  Abstract Gem_Map
    //
    public void                         dump(String name)
    {
        final String                    simple_class_name = this.inspect().simple_class_name;

        List<K>                         keys = new ArrayList<K>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {} {}", simple_class_name, name);
        line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            final K                     k = keys.get(i);

            line("  {}", k);
        }

        line("End of dump of {} {}", simple_class_name, name);
    }
}
