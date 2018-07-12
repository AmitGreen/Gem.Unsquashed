//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;


//
//  NOTE:
//      Saying that something `Gem_Referenceable_Interface` does not currently really say anything....
//
//      For now, this interface is only used for clarity to indicate something can be "referenced".
//
//      In the future, methods might be added ... in which case this interface becomes significant.
//
public interface    Gem_Referenceable_Interface<INSPECTION extends Inspection>
    extends         Inspectable                <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
}
