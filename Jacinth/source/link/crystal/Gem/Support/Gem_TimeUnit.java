//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.InterruptedException;
import java.util.concurrent.TimeUnit;
import link.crystal.Gem.Core.Gem_Object;


public abstract class   Gem_TimeUnit
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    public static final void            test()
    {
        line("TimeUnit: {}", TimeUnit.class);
        line("TimeUnit.SECONDS: {}", TimeUnit.SECONDS);

        line("Sleeping for 1 second ...");

        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            line(" ... Sleep interrupted: {}", e);
        }
    }
}
