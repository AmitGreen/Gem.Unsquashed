//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Interface__Gem_Reference;
import link.crystal.Gem.World.Comparable_Inspection;


public interface    WeakReferenceable        <INSPECTION extends Comparable_Inspection>
    extends         Interface__Gem_Reference <INSPECTION>,
                    Gem_Comparable           <INSPECTION>,
                    Comparable<Gem_Comparable<INSPECTION>>,             //  Via Gem_Comparable
                    Inspectable              <INSPECTION>//,            //  Via Gem_Object
{
    //
    //  Interface java.lang.Comparable
    //
    @Override
    public int                          compareTo(Gem_Comparable<INSPECTION> that);


    //
    //  Interface Inspectable
    //
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface Gem_Comparable
    //
    //  NOTE:
    //      None -- This interface is only used for clarity to indicate something is a "Gem Comparable";
    //      and the type of the first argument to `compareTo` is `Gem_Comparable<INSPECTION>`
    //      (See decleration above in `Interface java.lang.Comparable` for `compareTo`)
    //


    //
    //  Interface <me>
    //
    //  NOTE:
    //      None yet -- This interface is only used for clarity to indicate something is a "Gem Reference"
    //      (Methods might be added in the future).
    //
    //
}
