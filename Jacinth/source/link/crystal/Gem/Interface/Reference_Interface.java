//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Comparable_Inspection;


public interface    Reference_Interface      <INSPECTION extends Comparable_Inspection>
    extends         Gem_Comparable           <INSPECTION>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,             //  Via Gem_Comparable
                    Inspectable              <INSPECTION>//,            //  Via Gem_Object
{
    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
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
    //      None yet -- This interface is only used for clarity to indicate something is a "Gem Reference"
    //      (Methods might be added in the future).
    //
}
