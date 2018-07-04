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
    static String                       method_name(Zone z)
    {
        StackTraceElement[]             stack_trace_many = z.zone_thread.getStackTrace();

        int                             depth = 7;
        int                             total = stack_trace_many.length;

        if (depth < total) {
            StackTraceElement           stack_trace = stack_trace_many[depth];
            String                      class_name  = stack_trace.getClassName();
            int                         dot_index   = class_name.lastIndexOf(46);       //  46 = '.'

            if (dot_index != -1) {
                class_name = class_name.substring(dot_index + 1);
            }

            return class_name + "." + stack_trace.getMethodName();
        }

        return "???.???";
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
    public void                         select_1(Gem_StringBuilder builder, Object a)
    {
        final Zone                      z = builder.z;

        builder.append(this.method_name(z));
    }


    public void                         select_2(Gem_StringBuilder builder, Object a, Object b)
    {
        final Zone                      z = builder.z;

        builder.append(this.method_name(z));
    }


    public String                       select_2(Zone z, String a, String b)
    {
        return this.method_name(z);
    }


    public void                         select_3(Gem_StringBuilder builder, Object a, Object b, Object c)
    {
        final Zone                      z = builder.z;

        builder.append(this.method_name(z));
    }


    public void                         select_4(Gem_StringBuilder builder, Object a, Object b, Object c, Object d)
    {
        final Zone                      z = builder.z;

        builder.append(this.method_name(z));
    }


    public String                       select_5(Zone z, String a, String b, String c, String d, String e)
    {
        return this.method_name(z);
    }


    public String                       select_many(Zone z, String[] arguments)
    {
        return this.method_name(z);
    }


    public String                       portray(Zone z)
    {
        return "<MethodNameSegmentFormatter>";
    }
}
