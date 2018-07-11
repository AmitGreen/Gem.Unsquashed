//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.InterruptedException;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.System;
import java.util.concurrent.TimeUnit;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.Inspection;


public class    Gem_ReferenceQueue
    extends     ReferenceQueue<WeakReferenceable<?>>
//  extends     Object
    implements  Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Gem_ReferenceQueue");


    //
    //  Constructor & Factory
    //
    private                             Gem_ReferenceQueue()
    {
        super();
    }


    public static Gem_ReferenceQueue    create__ALLY__Gem()
    {
        return new Gem_ReferenceQueue();
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<Gem_ReferenceQueue>");
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


    //
    //  Public
    //
    public int                          cleanup()
    {
        int                             total = 0;

        for (;;)
        {
            Reference<? extends WeakReferenceable<?>>   referent = this.poll();

            if (referent == null) {
                return total;
            }

            Gem_WeakReference<?, ?, ?>              weak_reference = (Gem_WeakReference<?, ?, ?>) referent;

            weak_reference.reap();

            total += 1;
        }
    }


    public int                          garbage_collect()
    {
        System.gc();

        return this.cleanup();
    }


    public int                          garbage_collect__AND__possible_sleep()
    {
        System.gc();

        final int                       total_1 = this.cleanup();

        if (total_1 > 0) {
            line("garbage collected: {} ... no need to sleep", total_1);

            return total_1;
        }

        line("No garbage collected ... sleeping for 1 second ...");

        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            line(" ... Sleep interrupted: {}", e);
        }

        System.gc();

        final int                       total_2 = this.cleanup();

        line("... after sleep ... garbage collected: {}", total_2);

        return total_2;
    }
}
