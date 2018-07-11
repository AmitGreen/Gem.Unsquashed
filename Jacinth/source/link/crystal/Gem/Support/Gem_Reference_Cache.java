//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Gem_WeakReferenceable_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   Gem_Reference_Cache<
                            INSPECTION                extends Inspection,
                            CLIENT                    extends Gem_WeakReferenceable_Interface<CLIENT_INSPECTION>,
                            CLIENT_INSPECTION         extends Comparable_Inspection,
                            REFERENCE                 extends Gem_Reference_Interface<
                                                                  ? extends Comparable_Inspection,
                                                                  CLIENT,
                                                                  CLIENT_INSPECTION//,
                                                              >,
                            WEAK_REFERENCE            extends Gem_WeakReference<
                                                                  WEAK_REFERENCE_INSPECTION,
                                                                  CLIENT,
                                                                  CLIENT_INSPECTION//,
                                                              >,
                            WEAK_REFERENCE_INSPECTION extends Comparable_Inspection//,
                        >
    extends             Gem_Map<INSPECTION, REFERENCE, REFERENCE>
//  extends             HashMap            <REFERENCE, REFERENCE>
//  extends             AbstractHashMap    <REFERENCE, REFERENCE>
//  extends             Object
    implements          Inspectable    <INSPECTION>//,                  //  Via Gem_Map<?, ?, ?>
{
    //
    //  Constructor
    //
    protected                           Gem_Reference_Cache(Zone z, int initial_capacity)
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

        List<REFERENCE>                 keys = new ArrayList<REFERENCE>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {} {}", simple_class_name, name);
        line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            final REFERENCE             k = keys.get(i);

            line("  {}", k);
        }

        line("End of dump of {} {}", simple_class_name, name);
    }
}
