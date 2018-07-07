//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.StackTraceElement;
import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    MethodNameSegmentFormatter
    extends     MessageFormatter_Base<SegmentFormatter_Inspection>
//  extends     Gem_Object           <SegmentFormatter_Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable   <SegmentFormatter_Inspection>,
                Inspectable          <SegmentFormatter_Inspection>//,   //  Via Gem_Object
{
    private static SegmentFormatter_Inspection  inspection = (
            SegmentFormatter_Inspection.create("MethodNameSegmentFormatter")
        );


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
    //  Interface Inspectable
    //
    public SegmentFormatter_Inspection  inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth)
    {
        this.method_name(builder, depth + 1);
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth)
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        )
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        this.method_name(builder, depth + 1);
    }


    public void                         choose(
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
        this.method_name(builder, depth + 1);
    }


    public void                         choose(
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
        this.method_name(builder, depth + 1);
    }


    //
    //  public
    //
    public static void                  method_name(Gem_StringBuilder builder, int depth)
    {
        final Zone                      z = builder.z;

        final StackTraceElement[]       stack_trace_many = z.zone_thread.getStackTrace();
     
        final int                       total = stack_trace_many.length;

        if (false) {
            output("MethodNameSegmentFormatter.method_name: total<" + Integer.toString(total) + ">");

            for (int                    i = 0; i < total; i ++) {
                StackTraceElement       stack_trace = stack_trace_many[i];
                String                  class_name  = stack_trace.getClassName();
                int                     dot_index   = class_name.lastIndexOf(46);       //  46 = '.'

                if (dot_index != -1) {
                    class_name = class_name.substring(dot_index + 1);
                }

                output((
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
}
