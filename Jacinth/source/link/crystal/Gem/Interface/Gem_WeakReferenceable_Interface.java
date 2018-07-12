//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Comparable_Inspection;


public interface    Gem_WeakReferenceable_Interface<INSPECTION extends Comparable_Inspection>
    extends         Gem_Comparable                 <INSPECTION>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                    Inspectable                    <INSPECTION>//,                  //  Via Gem_Comparable
{
    //
    //  Interface java.lang.Comparable (see `Interface Gem_Comparable`)
    //


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
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that);


    //
    //  Interface <me>
    //
    //  NOTE:
    //      None yet -- This interface is only used for clarity to indicate something is a "Gem Reference"
    //      (Methods might be added in the future).
    //
    //
}
