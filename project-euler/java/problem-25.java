//Project Euler, Problem 25
//Fibonacci Sequence

/**
 *	This program will find the first number
 *	in the Fibonacci Sequence which contains
 *	one thousand digits.
 */

import java.math.BigInteger;

public class Problem25
{
	public static void main(String args[])
	{
		long lTime = System.nanoTime();
		
		int count = 2;
		BigInteger a = new BigInteger("1");
		BigInteger b = new BigInteger("1");
		
		while(numDigits(b) < 1000)
		{				
			count++;
			BigInteger c = a.add(b);
			BigInteger temp = b;
			a = b;
			b = c;
		}
		
		System.out.println(b);
		System.out.println("\nThe "+count+"th term");
		System.out.println("Runtime: "+(System.nanoTime() - lTime)+" ns");
	}
	
	public static int numDigits(BigInteger a)
	{
		return a.toString().length();
	}
}