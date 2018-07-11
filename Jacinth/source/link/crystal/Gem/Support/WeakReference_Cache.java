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
                            INSPECTION                extends Inspection,
                            CLIENT                    extends WeakReferenceable<CLIENT_INSPECTION>,
                            CLIENT_INSPECTION         extends Comparable_Inspection,
                            WEAK_REFERENCE            extends Gem_WeakReference<
                                                                  WEAK_REFERENCE_INSPECTION,
                                                                  CLIENT,
                                                                  CLIENT_INSPECTION//,
                                                              >,
                            WEAK_REFERENCE_INSPECTION extends Comparable_Inspection//,
                        >
    extends             Gem_Map        <INSPECTION, WEAK_REFERENCE, WEAK_REFERENCE>
//  extends             HashMap                    <WEAK_REFERENCE, WEAK_REFERENCE>
//  extends             AbstractHashMap            <WEAK_REFERENCE, WEAK_REFERENCE>
//  extends             Object
    implements          Inspectable    <INSPECTION>//,                  //  Via Gem_Map<?, ?, ?>
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
    public abstract INSPECTION          inspect();


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<", this.inspect().simple_class_name, " total<", this.size(), ">>");
    }


    //
    //  Abstract Gem_Map
    //
    public void                         dump(String name)
    {
        final String                    simple_class_name = this.inspect().simple_class_name;

        List<WEAK_REFERENCE>            keys = new ArrayList<WEAK_REFERENCE>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {} {}", simple_class_name, name);
        line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            final WEAK_REFERENCE        k = keys.get(i);

            line("  {}", k);
        }

        line("End of dump of {} {}", simple_class_name, name);
    }
}
