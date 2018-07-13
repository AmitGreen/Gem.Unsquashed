//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.World_Inspection;


public abstract class   ArgumentSegmentFormatter_Inspection<ARGUMENT_SEGMENT extends ArgumentSegmentFormatter>
    extends             SegmentFormatter_Inspection
//  extends             Inspection
//  extends             Gem_Object <World_Inspection>
//  extends             Object
    implements          Inspectable<World_Inspection>//,
{
    //
    //  Constructor & Factory
    //
    protected                           ArgumentSegmentFormatter_Inspection(String simple_class_name)
    {
        super(simple_class_name);
    }


    //
    //  Abstract
    //
    public abstract ARGUMENT_SEGMENT    conjure_argument_segment(Zone z, int argument_index);
}
