//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;


public interface    Gem_Reference_Interface<
                        INSPECTION        extends Gem_Reference_Inspection,
                        CLIENT            extends Gem_WeakReferenceable_Interface<CLIENT_INSPECTION>,
                        CLIENT_INSPECTION extends Comparable_Inspection//,
                    >
    extends         Gem_Comparable<INSPECTION>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                    Inspectable   <INSPECTION>//,                                   //  Via Gem_Comparable
{
    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that);


    //
    //  Interface Inspectable
    //
    @Override                           //  NOTE: Different `INSPECTION`
    public INSPECTION                   inspect();

    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    public CLIENT                       client_OR_enqueue();
}
