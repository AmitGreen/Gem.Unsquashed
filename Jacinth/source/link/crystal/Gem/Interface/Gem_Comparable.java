//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Comparable_Inspection;


public interface    Gem_Comparable<INSPECTION extends Comparable_Inspection>
    extends         Comparable<Gem_Comparable>,
                    Inspectable   <INSPECTION>//,                       //  Via Gem_Object
{
    //
    //  Interface Inspectable
    //
    public INSPECTION                   inspect();                      //  NOTE: Different `INSPECTION`
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface
    //
    public int                          compareTo(Gem_Comparable that);
}
