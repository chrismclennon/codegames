//Problem1: Rewritten on December 19, 2010
//Chris McLennon
//
/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 */

package problem1;

/**
 *
 * @author Chris
 */
public class Main {
    public static void main(String[] args) {
        //Brute force method.

        long lTime = System.nanoTime();
        int sum = 0;

        for(int k=3; k<1000; k++){
            if(k % 3 == 0 || k % 5 == 0)
                sum += k;
        }

        System.out.println("Sum: "+sum);
        System.out.println("Runtime: "+(System.nanoTime() - lTime)+ "ns");
    }
}