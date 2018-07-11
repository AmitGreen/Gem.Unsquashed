//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Interface__Gem_Reference;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.World.Comparable_Inspection;


public abstract class   Gem_WeakReference<
                            INSPECTION        extends Comparable_Inspection,
                            CLIENT            extends WeakReferenceable<CLIENT_INSPECTION>,
                            CLIENT_INSPECTION extends Comparable_Inspection//,
                        >
    extends             WeakReference<CLIENT>
//  extends             Reference    <CLIENT>
//  extends             Object
    implements          Interface__Gem_Reference <INSPECTION>,
                        Gem_Comparable           <INSPECTION>,          //  Via Interface__Gem_Reference
                        Comparable<Gem_Comparable<INSPECTION>>,         //  Via Gem_Comparable
                        Inspectable              <INSPECTION>//,        //  Via Gem_Comparable
{
    //
    //  Constructor
    //
    protected                           Gem_WeakReference(CLIENT client, Gem_ReferenceQueue reference_queue)
    {
        super(client, reference_queue);
    }


    //
    //  Interface java.lang.Comparable
    //
    public abstract int                 compareTo(Gem_Comparable<INSPECTION> that);


    //
    //  Interface Interface__Gem_Reference
    //
    //<empty>


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract void                portray(Gem_StringBuilder builder);


    //
    //  Abstract
    //
    public abstract void                reap();


    //
    //  Public (ERRORS)
    //
    public static void                  INVALID_ROUTINE()
    {
        ExceptionFunctions.RUNTIME(2, "invalid routine");
    }


    public static void                  RUNTIME(String error_message, Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }


    //
    //  Public (line)
    //
    public static void                  line()
    {
        Gem.line();
    }


    public static void                  line(String format)
    {
        Gem.line(2, format);
    }


    public static void                  line(String format, Object v)
    {
        Gem.line(2, format, v);
    }


    public static void                  line(String format, Object v, Object w)
    {
        Gem.line(2, format, v, w);
    }


    public static void                  line(String format, Object v, Object w, Object x)
    {
        Gem.line(2, format, v, w, x);
    }


    public static void                  line(String format, Object v, Object w, Object x, Object y)
    {
        Gem.line(2, format, v, w, x, y);
    }


    public static void                  line(String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        Gem.line(2, format, v, w, x, y4, y5);
    }


    public static void                  line(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        Gem.line(2, format, v, w, x, y4, y5, y6);
    }


    public static void                  line(
            String                              format,
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
        Gem.line(2, format, v, w, x, y4, y5, y6, y7, other_arguments);
    }
}
