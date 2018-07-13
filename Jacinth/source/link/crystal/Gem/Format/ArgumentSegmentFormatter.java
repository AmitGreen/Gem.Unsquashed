//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public abstract class   ArgumentSegmentFormatter<INSPECTION extends ArgumentSegmentFormatter_Inspection>
    extends             MessageFormatter_Base   <INSPECTION>
//  extends             Gem_Object              <INSPECTION>
//  extends             Object
    implements          MessageFormattable      <INSPECTION>,
                        SegmentFormattable      <INSPECTION>,
                        Inspectable             <INSPECTION>//,
{
    //
    //  Members
    //
    protected final int                 argument_index;


    //
    //  Constructor
    //
    protected                           ArgumentSegmentFormatter(int argument_index)
    {
        this.argument_index = argument_index;
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    //
    //  Interface MessageFormattable
    //
    public abstract void                augment(Gem_StringBuilder builder, int depth, Object v);


    //
    //  Interface SegmentFormattable
    //
    public abstract void                choose(Gem_StringBuilder builder, int depth);
    public abstract void                choose(Gem_StringBuilder builder, int depth, Object v);
    public abstract void                choose(Gem_StringBuilder builder, int depth, Object v, Object w);
    public abstract void                choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x);


    public abstract void                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        );


    public abstract void                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        );


    public abstract void                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );


    public abstract void                choose(
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
        );


    //
    //  Interface Inspectable
    //
    @Override
    public void                         portray(Gem_StringBuilder builder)
    {
        INSPECTION                      inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, " ", this.argument_index, ">");
    }
}
