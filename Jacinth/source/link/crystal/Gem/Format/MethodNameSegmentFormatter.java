//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.StackTraceElement;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    MethodNameSegmentFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MethodNameSegmentFormatter");


    //
    //  Private static
    //
    private static MethodNameSegmentFormatter   singleton = null;



    //
    //  Constructor & Factory
    //
    private                             MethodNameSegmentFormatter()
    {
    }


    static public MethodNameSegmentFormatter    conjure(Zone z)
    {
        MethodNameSegmentFormatter      singleton = MethodNameSegmentFormatter.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            MethodNameSegmentFormatter.singleton = new MethodNameSegmentFormatter();

        return singleton;
    }


    //
    //  Private
    //
    static void                         method_name(Gem_StringBuilder builder, int depth)
    {
        final Zone                      z = builder.z;
        final StackTraceElement[]       stack_trace_many = z.zone_thread.getStackTrace();
       
        final int                       total = stack_trace_many.length;

        if (false) {
            z.line("MethodNameSegmentFormatter.method_name: total<" + Integer.toString(total) + ">");

            for (int                    i = 0; i < total; i ++) {
                StackTraceElement       stack_trace = stack_trace_many[i];
                String                  class_name  = stack_trace.getClassName();
                int                     dot_index   = class_name.lastIndexOf(46);       //  46 = '.'

                if (dot_index != -1) {
                    class_name = class_name.substring(dot_index + 1);
                }

                z.line((
                             "  "
                           + Integer.toString(i)
                           + ": "
                           + class_name
                           + "."
                           + stack_trace.getMethodName()
                           + "@"
                           + Integer.toString(stack_trace.getLineNumber())
                      ));
            }
        }

        //
        //  NOTE:
        //      The stack trace includes `Thread.GetStackTrace` as element 0.
        //
        //      So add `1` to `depth`
        //
        depth += 1;

        if (depth < total) {
            StackTraceElement           stack_trace = stack_trace_many[depth];
            String                      class_name  = stack_trace.getClassName();
            int                         dot_index   = class_name.lastIndexOf(46);       //  46 = '.'

            if (dot_index != -1) {
                class_name = class_name.substring(dot_index + 1);
            }

            builder.append(class_name, ".", stack_trace.getMethodName(), "@", stack_trace.getLineNumber());
            return;
        }

        builder.append("???.???@???");
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(Gem_StringBuilder builder, Object v, Object w)
    {
        this.method_name(builder, 0);
    }


    public void                         choose(Gem_StringBuilder builder, Object v, Object w, Object x)
    {
        this.method_name(builder, 0);
    }


    public void                         choose(Gem_StringBuilder builder, Object v, Object w, Object x, Object y)
    {
        this.method_name(builder, 0);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        this.method_name(builder, 0);
    }


    public void                         select_many(
            Gem_StringBuilder                   builder,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object ...                          other_arguments//,
        )
    {
        this.method_name(builder, 0);
    }


    public String                       portray(Zone z)
    {
        return "<MethodNameSegmentFormatter>";
    }
}
