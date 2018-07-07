//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.World.Inspection;


public interface    Inspectable<INSPECTION extends Inspection>
{
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);
}
