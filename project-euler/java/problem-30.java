//Project Euler, Problem 30
//Fifth Power Factor Sums

/**
 *	This program will record the numbers
 *	which can be expressed by the sum of
 *	their digits to the fifth power.
 */
 
 public class Problem30
 {
 	public static void main(String args[])
 	{
 		long lTime = System.nanoTime();
 		long n = 2;
 		long sum = 0;
 		
 		while(!(n == 1000000))
 		{
 			if(sum(n) == n)
 			{
 				System.out.println(n);
 				sum += n;
 			}
 			
 			n++;
 		}
 		
 		System.out.println("\n\nSum: "+sum);
 		System.out.println("\nRuntime: "+(System.nanoTime() - lTime)+" ns");
 	}
 	
 	public static long sum(long a)
 	{
 		String num = new Long(a).toString();
 		long sum = 0;
 		
 		for(int k=0; k<num.length(); k++)
 			sum += pow(Integer.valueOf(num.substring(k, k+1)), 5);
 		
 		return sum;
 	}
 	
 	public static long pow(int a, int pow)
 	{		
 		long ans = a;
 		
 		for(int k=1; k<pow; k++)
 			ans = ans * a;
 			
 		return ans;
 	}
 }