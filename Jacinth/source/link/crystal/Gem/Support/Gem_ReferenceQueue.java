//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.InterruptedException;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.System;
import java.util.concurrent.TimeUnit;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Gem_QueueableReference_Interface;
import link.crystal.Gem.Interface.Gem_Referenceable_Interface;
import link.crystal.Gem.Interface.Inspectable;


//
//  NOTE:
//      The generics used with `ReferenceQueue` *ARE* wrong.
//
//      The main reason for this is that `Reference` is *INCORRECTLY* a class, instead of an interface.
//
//  INCORRECT WAY:
//
//      class Reference
//      {
//          ...
//      };
//
//      class ReferenceQueue<T>
//      {
//          Reference<? extends T>      poll();
//          ...
//      }
//
//  CORRECT WAY:
//
//      [NOTE:
//          Here in the *CORRECT* WAY, we properly declare `Reference` to be an interface, this allows us now
//          to pass in a second parameter to `ReferenceQueue` that properly extends `Reference`.
//
//          For simple cases, you could still do the second paramter to `ReferenceQueue` without actually
//          changing `Reference` from a class to an interface; however, this would break even more horribly
//          [than it currently does] for the complicated cases.
//
//          Thus given the deficiency of the decleration of `Reference` as a class, the declaration of
//          `ReferenceQueue` as given `java.lang.ref.ReferenceQueue`, is a reasonable [wrong] solution.]
//
//      interface Reference<T>
//      {
//          ...
//          T                           get();
//          ...
//      }
//
//      class ReferenceQueue<ELEMENT, REFERENCE extends Reference<ELEMENT>>
//      {
//          REFERENCE                   poll();
//          ...
//      }
//
//  SINCE:
//      ... it was done incorrectly, then we cannot control the return paramter of `.poll()`
//      properly, and it always returns a `Reference` class instead of (what we want) a class that
//      extends `Reference` that we pass in.
//
//  IF:
//      ... it was done the correct way, then we could get the return type of `.poll()` to be correct by
//      passing in the correct generic as the second parameter to ReferenceQueue, in particular the
//      second parameter would be:
//
//                  Gem_QueueableReference_Interface<? extends Inspection>>
//
//      This would be a valid type as it would "extend" the second generic of `ReferenceQueue` which is declared as
//
//                  `REFERENCE extends Reference<ELEMENT>`
//
//      (However, as mentioned above this does not work since `Reference` is a class and
//      `Gem_QueueableReference_Interface` is an interface, and an interface is not allowed to "extend" as class).
//
//  THEREFORE:
//      We coerce the return type of `super.poll()` to be the proper type (as explained above).
//
public class    Gem_ReferenceQueue
    extends     ReferenceQueue<
                    Gem_Referenceable_Interface<? extends Inspection>//,
                //  Gem_QueueableReference_Interface<? extends Inspection>>//,
                >
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
            Reference<? extends Gem_Referenceable_Interface<? extends Inspection>>  referent = this.poll();

            if (referent == null) {
                break;
            }


            //
            //  NOTE:
            //      See explanation above, at start of this class, as to why this coercion is needed here.
            //
            @SuppressWarnings("unchecked")
            Gem_QueueableReference_Interface<? extends Inspection>   queueable_reference = (
                    (Gem_QueueableReference_Interface<? extends Inspection>) referent
                );

            queueable_reference.reap();

            total += 1;
        }

        return total;
    }


    public int                          garbage_collect()
    {
        System.gc();

        return this.cleanup();
    }


    public int                          garbage_collect__AND__possible_sleep()
    {
        int                             total_trash = 0;
        int                             zeros = 0;

        while (zeros < 3) {
            System.gc();

            final int                   current_trash = this.cleanup();

            total_trash += current_trash;

            if (zeros == 3) {
                line("garbage collected: {}", current_trash);
                break;
            }

            if (current_trash == 0) {
                zeros += 1;

                line("no garbage collected ... sleeping for 0.007 seconds ...");
            } else {
                zeros = 0;

                line("garbage collected: {} ... sleeping for 0.007 seconds ...", total_trash);
            }

            try {
                TimeUnit.MILLISECONDS.sleep(7);
            } catch (InterruptedException e) {
                line(" ... Sleep interrupted: {}", e);
            }
        }

        line("total garbage collected: {}", total_trash);

        return total_trash;
    }
}
