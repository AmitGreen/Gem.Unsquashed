//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;


public interface    Inspectable<INSPECTION extends Inspection>
{
    public INSPECTION                   inspect();
    public String                       portray(Zone z);
}
