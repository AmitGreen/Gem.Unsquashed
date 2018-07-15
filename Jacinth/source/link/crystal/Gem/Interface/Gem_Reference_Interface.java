//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Inspectable;


public interface    Gem_Reference_Interface<INSPECTION extends Gem_Reference_Inspection>
    extends         Inspectable            <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    @Override                           //  NOTE: Different `INSPECTION`
    public INSPECTION                   inspect();

    public void                         portray(final Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    //<empty>
}
