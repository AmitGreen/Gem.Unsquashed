//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Comparable_Inspection;


public interface    Gem_Comparable<INSPECTION extends Comparable_Inspection>
    extends         Comparable<Gem_Comparable<? extends Comparable_Inspection>>,
                    Inspectable   <INSPECTION>//,
{
    //
    //  Interface java.lang.Comparable
    //
    @Override
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that);


    //
    //  Interface Inspectable
    //
    @Override
    public INSPECTION                   inspect();                      //  NOTE: Different `INSPECTION`

    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    //  NOTE:
    //      None -- This interface is only used for clarity to indicate something is a "Gem Comparable";
    //      and the type of the first argument to `compareTo` is `Gem_Comparable<? extends Comparable_Inspection>`
    //      (See decleration above in `Interface java.lang.Comparable` for `compareTo`)
    //
}
