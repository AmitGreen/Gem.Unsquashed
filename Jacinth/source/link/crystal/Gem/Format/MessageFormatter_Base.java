//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public abstract class   MessageFormatter_Base
    extends             Gem_Object<Inspection>
//  extends             Object
    implements          MessageFormattable,
                        Inspectable<Inspection>//,                      //  Via Gem_Object
{
    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth)
    {
        final Zone                      z = builder.z;

        Inspection                      inspection = this.inspect();

        z.RUNTIME("invalid routine (derived class: {0})", inspection.simple_class_name);
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        final Zone                      z = builder.z;

        Inspection                      inspection = this.inspect();

        z.RUNTIME("invalid routine (derived class: {0})", inspection.simple_class_name);
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }


    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }


    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        )
    {
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }

  
    @Override
    public void                         arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }


    @Override
    public void                         arrange(
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
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }


    @Override
    public void                         arrange(
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
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }
}
