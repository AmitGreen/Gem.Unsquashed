//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.World.Inspection;


public abstract class   MessageFormatter_Base<INSPECTION extends Inspection>
    extends             Gem_Object           <INSPECTION>
//  extends             Object
    implements          MessageFormattable,
                        Inspectable          <INSPECTION>//,            //  Via Gem_Object
{
    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         augment(Gem_StringBuilder builder, int depth)
    {
        final INSPECTION                inspection = this.inspect();

        RUNTIME("invalid routine (derived class: {})", inspection.simple_class_name);
    }


    @Override
    public void                         augment(Gem_StringBuilder builder, int depth, Object v)
    {
        final INSPECTION                inspection = this.inspect();

        RUNTIME("invalid routine (derived class: {})", inspection.simple_class_name);
    }


    @Override
    public void                         augment(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        INVALID_ROUTINE();
    }


    @Override
    public void                         augment(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        INVALID_ROUTINE();
    }


    @Override
    public void                         augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public void                         augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public void                         augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public void                         augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        INVALID_ROUTINE();
    }
}
