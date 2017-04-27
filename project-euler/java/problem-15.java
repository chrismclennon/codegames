/*
 * Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
 * How many in 20x20 grid?
 */

// Problem: number too big

public class TestClassPleaseIgnore 
{
	public static void main(String args[])
	{
		int length = 21;
		
		// Initialize grid
		long m[][] = new long[length][length];
		
		for(int n = 0; n < length; n++)
		{
			m[n][0] = 1;
			m[0][n] = 1;
		}
		
		// Parse grid
		for(int k = 1; k < length; k++)
		{
			for(int r = k; r < length; r++)
			{
				for(int c = k; c < length; c++)
				{
					m[r][c] = m[r][c - 1] + m[r - 1][c];
				}
			}
		}
		
		for(int k = 0; k < length; k++)
		{
			System.out.println(k + " " + m[k][k]);
		}
	}
}
