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
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface
    //


    //TO BE DONE
}
