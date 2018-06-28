package crystal.link;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;


public class JacinthTest 
    extends TestCase
{
    public                              JacinthTest(String testName)
    {
        super(testName);
    }


    public static Test                  suite()
    {
        return new TestSuite(JacinthTest.class);
    }


    public void                         testJacinth()
    {
        assertTrue(true);
    }
}
