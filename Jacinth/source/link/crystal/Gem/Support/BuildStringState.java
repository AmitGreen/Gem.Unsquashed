//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class      BuildStringState
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("BuildStringState");


    //
    //  Static members (Apostrophe state machine)
    //
    public static final BuildStringState    A_Start  = BuildStringState.create("A_Start");
    public static final BuildStringState    A_Normal = BuildStringState.create("A_Normal");
    public static final BuildStringState    A_1      = BuildStringState.create("A_1");
    public static final BuildStringState    A_2      = BuildStringState.create("A_2");
    public static final BuildStringState    A_P0     = BuildStringState.create("A_P0");
    public static final BuildStringState    A_P1     = BuildStringState.create("A_P1");

    public static final BuildStringState    Q_Start  = BuildStringState.create("Q_Start");
    public static final BuildStringState    Q_Normal = BuildStringState.create("Q_Normal");
    public static final BuildStringState    Q_1      = BuildStringState.create("Q_1");
    public static final BuildStringState    Q_2      = BuildStringState.create("Q_2");
    public static final BuildStringState    Q_P0     = BuildStringState.create("Q_P0");
    public static final BuildStringState    Q_P1     = BuildStringState.create("Q_P1");


    private static final int            finish()
    {
        BuildStringState.A_Start .setup(null,   "\\'",      "'''",          BuildStringState.A_P0);
        BuildStringState.A_Normal.setup(null,   null,       "'''",          BuildStringState.A_1);
        BuildStringState.A_1     .setup("'",    null,       "\\''''",       BuildStringState.A_2);
        BuildStringState.A_2     .setup("''",   "''\\'",    "'\\''''",      BuildStringState.A_P0);
        BuildStringState.A_P0    .setup(null,   null,       "'''",          BuildStringState.A_P1);
        BuildStringState.A_P1    .setup("'",    "'\\'",     "\\''''",       BuildStringState.A_P0);

        BuildStringState.Q_Start .setup(null,   "\\\"",     "\"\"\"",       BuildStringState.Q_P0);
        BuildStringState.Q_Normal.setup(null,   null,       "\"\"\"",       BuildStringState.Q_1);
        BuildStringState.Q_1     .setup("\"",   null,       "\\\"\"\"\"",   BuildStringState.Q_2);
        BuildStringState.Q_2     .setup("\"\"", "\"\"\\\"", "\"\\\"\"\"\"", BuildStringState.Q_P0);
        BuildStringState.Q_P0    .setup(null,   null,       "\"\"\"",       BuildStringState.Q_P1);
        BuildStringState.Q_P1    .setup("\"",   "\"\\\"",   "\\\"\"\"\"",   BuildStringState.Q_P0);

        return 7;
    }


    private static final int            finished = finish();


    //
    //  Members
    //
    public final String                 name;
    public /*:*/ String                 normal_flush_0;
    public /*:*/ String                 add_flush_0;
    public /*:*/ String                 finish;
    public /*:*/ BuildStringState       add;


    //
    //  Constructor, Factory, & Setup
    //
    private                             BuildStringState(final String name)
    {
        this.name           = name;

    //  this.normal_flush_0 = vacant
    //  this.add_flush_0    = vacant
    //  this.finish         = vacant
    //  this.add            = vacant
    }


    public static final BuildStringState    create(final String name)
    {
        return new BuildStringState(name);
    }


    public final void                   setup(
            final String                        normal_flush_0,
            final String                        add_flush_0,
            final String                        finish,
            final BuildStringState              add//,
        )
    {
        this.normal_flush_0 = normal_flush_0;
        this.add_flush_0    = add_flush_0;
        this.finish         = finish;
        this.add            = add;
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.augment("<BuildStringState {}; {} {} {}; {}>",
                        String.format("%8s", this.name),
                        String.format("%6s", arrange("{p}", this.normal_flush_0)),
                        String.format("%10s", arrange("{p}", this.add_flush_0)),
                        String.format("%14s", arrange("{p}", this.finish)),
                        String.format("%4s", this.add.name));
    }


    //
    //  Public (debug)
    //
    public static final void            dump()
    {
        line("Dump of BuildStringState");
        line("   A_Start:  {p}", BuildStringState.A_Start);
        line("  A_Normal:  {p}", BuildStringState.A_Normal);
        line("       A_1:  {p}", BuildStringState.A_1);
        line("       A_2:  {p}", BuildStringState.A_2);
        line("      A_P0:  {p}", BuildStringState.A_P0);
        line("      A_P1:  {p}", BuildStringState.A_P1);

        line("---");
        line("   Q_Start:  {p}", BuildStringState.Q_Start);
        line("  Q_Normal:  {p}", BuildStringState.Q_Normal);
        line("       Q_1:  {p}", BuildStringState.Q_1);
        line("       Q_2:  {p}", BuildStringState.Q_2);
        line("      Q_P0:  {p}", BuildStringState.Q_P0);
        line("      Q_P1:  {p}", BuildStringState.Q_P1);
        line("End of dump of BuildStringState");
    }
}
