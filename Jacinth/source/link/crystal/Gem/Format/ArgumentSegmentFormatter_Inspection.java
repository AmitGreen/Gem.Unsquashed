//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   ArgumentSegmentFormatter_Inspection<ARGUMENT_SEGMENT extends ArgumentSegmentFormatter>
    extends             Inspection
//  extends             Gem_Object<Inspection>
//  extends             Object
    implements          Inspectable<Inspection>//,                      //  Via Gem_Object
{
    //
    //  Constructor & Factory
    //
    protected                           ArgumentSegmentFormatter_Inspection(String simple_class_name)
    {
        super(simple_class_name, null, false);
    }


    //
    //  Abstract
    //
    public abstract ARGUMENT_SEGMENT    conjure_argument_segment(Zone z, int argument_index);
}
