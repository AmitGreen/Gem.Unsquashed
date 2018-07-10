//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Inspection;


public interface    WeakReferenceable<INSPECTION extends Inspection>
    extends         Inspectable      <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    @Override
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    //  NOTE:
    //      None yet -- This interface is only used for clarity to indicate something is a "Gem Reference"
    //      (Methods might be added in the future).
    //
    //
}
