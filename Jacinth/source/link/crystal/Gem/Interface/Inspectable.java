//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;


public interface    Inspectable<INSPECTION extends Inspection>
{
    public INSPECTION                   inspect();
    public String                       portray();
}
