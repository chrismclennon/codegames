/* 
 * Project Euler Problem #44
 * Written by Chris McLennon
 * May 18, 2014
 * 
 * PROBLEM STATEMENT:
 * https://projecteuler.net/problem=44
 */

import java.util.Arrays;

public class Problem44 {
	// Set up a table with the first 10,000 pentagonal values
	// The method isPentagonal() will search this table for values to affirm a true or false verdict
	public static long pentagonal[] = new long[10000];
	
	public static void main(String args[])
	{
		// Populate the pentagonal table
		for(long i = 1; i < 10000; i++)
		{
			pentagonal[(int) i] = (i * (3*i - 1) / 2);
		}
		
		// It's brute force. It works. It's fast.
		bruteForce();
	}
	
	public static void bruteForce()
	{
		for(int k = 1;; k++)
		{
			for(int j = k - 1; j > 0; j--)
			{
				if(isPentagonal(pentagonal(k) + pentagonal(j)) 
						&& isPentagonal(pentagonal(k) - pentagonal(j)))
				{
					System.out.println("Answer found: "+Math.abs(pentagonal(j) - pentagonal(k)));
					return;
				}
			}
		}
	}
	
	public static int pentagonal(int n)
	{
		return n * (3*n - 1) / 2;
	}
	
	public static boolean isPentagonal(long num)
	{
		// Binary search the pentagonal table for a value.
		if(Arrays.binarySearch(pentagonal, num) >= 0)
			return true;
		
		return false;
	}
}
