import java.math.BigInteger;
import java.util.Stack;

public class Problem3
{
	public static void main(String args[])
	{
		long lTime = System.nanoTime();
		
		BigInteger nNum = new BigInteger("600851475143");
		BigInteger k = new BigInteger("2");
		Stack sAnswer = new Stack();
		
		while(k.compareTo(nNum) != 1)
		{
			if(isPrime(k))
			{
				BigInteger nTest = nNum.mod(k);
				
				while(nTest.compareTo(new BigInteger("0")) == 0)
				{
					nNum = nNum.divide(k);
					sAnswer.push(k);
					
					nTest = nNum.mod(k);
					
					System.out.println("New Prime Factor Found: " + k + "\tTime: " + (System.nanoTime() - lTime) + " ns");
				}
			}
			
			k = k.add(new BigInteger("1"));
		}
		
		System.out.println("\n"+sAnswer);
	}

	public static boolean isPrime(BigInteger k)
	{
		//Function boundary conditions: [3:infinity]
		
		BigInteger j = new BigInteger("2");
		
		while(j.compareTo(k.divide(new BigInteger("2"))) != 1)
		{
			BigInteger nTest = k.mod(j);
			
			if(nTest.compareTo(new BigInteger("0")) == 0)
				return false;		
			
			j = j.add(new BigInteger("1"));
		}
		
		return true;
	}
}