//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
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
    public String                       arrange(Zone z, int depth, Object v)
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(Zone z, int depth, Object v, Object w)
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x)
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(Zone z, int depth, Object v, Object w, Object x, Object y)
    {
        z.INVALID_ROUTINE();
        return null;
    }

    
    public String                       arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        z.INVALID_ROUTINE();
        return null;
    }


    public String                       arrange(
            Zone                                z,
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
        z.INVALID_ROUTINE();
        return null;
    }


    public void                         line(Zone z, int depth, Object v)
    {
        z.line(this.arrange(z, depth + 1, v));
    }


    public void                         line(Zone z, int depth, Object v, Object w)
    {
        z.line(this.arrange(z, depth + 1, v, w));
    }


    public void                         line(Zone z, int depth, Object v, Object w, Object x)
    {
        z.line(this.arrange(z, depth + 1, v, w, x));
    }


    public void                         line(Zone z, int depth, Object v, Object w, Object x, Object y)
    {
        z.line(this.arrange(z, depth + 1, v, w, x, y));
    }


    public void                         line(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        z.line(this.arrange(z, depth + 1, v, w, x, y4, y5));
    }


    public void                         line(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        z.line(this.arrange(z, depth + 1, v, w, x, y4, y5, y6));
    }


    public void                         line(
            Zone                                z,
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
        z.line(this.arrange(z, depth + 1, v, w, x, y4, y5, y6, y7, other_arguments));
    }
}
