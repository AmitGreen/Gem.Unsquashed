//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_Map;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.Gem_Referenceable_Interface;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   Gem_ComparableReference_Cache<
                            INSPECTION        extends Inspection,
                            CLIENT            extends Gem_Referenceable_Interface<CLIENT_INSPECTION>,
                            CLIENT_INSPECTION extends Inspection,
                            REFERENCE         extends Gem_ComparableReference_Interface<
                                                          ? extends Gem_Reference_Inspection,
                                                          CLIENT,
                                                          CLIENT_INSPECTION//,
                                                      >//,
                        >
    extends             Gem_Map<INSPECTION, REFERENCE, REFERENCE>
//  extends             HashMap            <REFERENCE, REFERENCE>
//  extends             AbstractHashMap    <REFERENCE, REFERENCE>
//  extends             Object
    implements          Inspectable    <INSPECTION>//,
{
    //
    //  Constructor
    //
    protected                           Gem_ComparableReference_Cache(final Zone z, final int initial_capacity)
    {
        super(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    //
    public abstract INSPECTION          inspect();


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<", this.inspect().simple_class_name, " total<", this.size(), ">>");
    }


    //
    //  Abstract Gem_Map
    //
    public final void                   dump(final String name)
    {
        final String                    simple_class_name = this.inspect().simple_class_name;

        /*:*/ List<REFERENCE>           keys = new ArrayList<REFERENCE>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of {} {}", simple_class_name, name);
        line("      size: " + Integer.toString(total));

        for (/*:*/ int                  i = 0; i < total; i ++) {
            final REFERENCE             k = keys.get(i);

            line("  {}", k);
        }

        line("End of dump of {} {}", simple_class_name, name);
    }
}
