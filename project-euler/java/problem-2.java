public class Problem2
{
	public static void main(String args[])
	{
		long lTime = System.nanoTime();
		int nSum = 0;
		int nFib = 1;
		int nFibLast = 1;
		
		while(nFib <= 4000000)
		{
			System.out.println(nFib);
			
			if(nFib % 2 == 0)
				nSum += nFib;
			
			int nTemp = nFib;
			nFib += nFibLast;
			nFibLast = nTemp;
		}
		
		System.out.println("Sum: "+nSum);
		System.out.println("Runtime: "+(System.nanoTime() - lTime)+" ns");
	}
}