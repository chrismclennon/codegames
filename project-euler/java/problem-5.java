package problem5;

/**
 *
 * @author Chris
 */
public class Main {
    public static void main(String[] args) {
        //The problem already told us that 2520 is divisible by numbers 1 thru 10
        long lTime = System.nanoTime();
        int nNum = 2520;

        while(!isDivisible(nNum))
            nNum++;

        System.out.println("Answer: "+nNum);
        System.out.println("Runtime: "+(System.nanoTime() - lTime)+" ns");
    }

    public static boolean isDivisible(int nNum){
        for(int k=11; k<=20; k++)
            if(nNum % k != 0)
                return false;

        return true;
    }

}
