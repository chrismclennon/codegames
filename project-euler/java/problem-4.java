package problem4;

/**
 *
 * @author Chris
 */
public class Main {
    public static void main(String[] args) {
        //ASSUMPTION: The largest two palindromic numbers are two numbers multiplied against each other that are each over 900
        long lTime = System.nanoTime();
        int nLargest = -1;

        for(int i=999; i>=900; i--)
            for(int j=999; j>=900; j--){
                if(isPalindrome(Integer.toString(i * j)))
                    if(i * j > nLargest)
                        nLargest = i * j;
            }

        System.out.println("Answer: "+nLargest);
        System.out.println("Runtime: "+(System.nanoTime() - lTime) + " ns");
    }

    public static boolean isPalindrome(String sForward){
        //Compare Strings sForward and sBackward
        int nLength = sForward.length();
        String sBackward = new String();

        for(int k=nLength-1; k>=0; k--){
            sBackward += new Character(sForward.charAt(k)).toString();
        }

        if(sForward.compareToIgnoreCase(sBackward) == 0)
            return true;

        return false;

    }
}