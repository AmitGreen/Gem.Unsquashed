//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import link.crystal.Gem.Inspection;


public interface    Inspectable<INSPECTION extends Inspection>
{
    public INSPECTION                   inspect();
}
