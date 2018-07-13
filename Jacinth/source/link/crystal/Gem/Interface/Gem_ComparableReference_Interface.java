//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_Referenceable_Interface;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;


//
//  NOTE:
//      This interface is needed for `Gem_ComparableReference_Cache` which needs interfaces for both:
//
//          1.  Comparable (used in `Gem_ComparableReference_Cache.dump`); and
//          2.  References (used in `Gem.conjure_{,enduring_}{integer,string}`).
//
public interface    Gem_ComparableReference_Interface<
                        INSPECTION        extends Gem_Reference_Inspection,
                        CLIENT            extends Gem_Referenceable_Interface<CLIENT_INSPECTION>,
                        CLIENT_INSPECTION extends Inspection//,
                    >
    extends         Gem_Reference_Interface<INSPECTION>,
                    Gem_Comparable         <INSPECTION>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                    Inspectable            <INSPECTION>//,
{
    //
    //  Interface java.lang.Comparable
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that);


    //
    //  Interface Gem_Comparable
    //
    //<empty>


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
