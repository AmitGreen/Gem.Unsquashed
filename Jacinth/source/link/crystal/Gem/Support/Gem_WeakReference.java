//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.Gem_QueueableReference_Interface;
import link.crystal.Gem.Interface.Gem_Referenceable_Interface;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;


public abstract class   Gem_WeakReference<
                            INSPECTION        extends Gem_Reference_Inspection,
                            CLIENT            extends Gem_Referenceable_Interface<CLIENT_INSPECTION>,
                            CLIENT_INSPECTION extends Inspection//,
                        >
    extends             WeakReference<CLIENT>
//  extends             Reference    <CLIENT>
//  extends             Object
    implements          Gem_ComparableReference_Interface<INSPECTION, CLIENT, CLIENT_INSPECTION>,
                        Gem_QueueableReference_Interface <INSPECTION>,
                        Gem_Reference_Interface          <INSPECTION>,      //  Via Gem_*Reference_Interface
                        Gem_Comparable                   <INSPECTION>,      //  Via Gem_ComparableReference_Interface
                        Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                        Inspectable                      <INSPECTION>//,
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
    public abstract int                 compareTo(Gem_Comparable<? extends Comparable_Inspection> that);


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
    //  Interface Gem_ComparableReference_Interface
    //
    @Override
    public CLIENT                       client_OR_enqueue()
    {
        final CLIENT                    r = this.get();

        if (r != null) {
            return r;
        }

        this.enqueue();
        return null;
    }


    //
    //  Interface Gem_QueueableReference_Interface
    //
    public abstract void                reap();


    //
    //  Interface Gem_Reference_Interface
    //
    //<empty>


    //
    //  Public (ASSERT)
    //
    public static boolean               fact(boolean condition, String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, format);

        return false;
    }


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
