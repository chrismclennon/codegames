import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

class Problem07 {
    public static void main(String[] args) throws IOException {
        String testCaseOne = "abba[mnop]qrst";
        testCase(testCaseOne, true);

        String testCaseTwo = "abcd[bddb]xyyx";
        testCase(testCaseTwo, false);

        String testCaseThree = "aaaa[qwer]tyui";
        testCase(testCaseThree, false);

        String testCaseFour = "ioxxoj[asdfgh]zxcvbn";
        testCase(testCaseFour, true);

        System.out.println();

        List<String> ipAddresses = Files.readAllLines(Paths.get("adventofcode/2016/7/input"));
        int count = 0;
        for (String ipAddress : ipAddresses) {
//            testCase(ipAddress, true);
            if (supportsTls(ipAddress)) {
                count++;
            }
        }
        System.out.println("Part 1: " + count);
    }

    public static boolean isAbba(String s) {
        if (s.length() != 4) {
            return false;
        }
        if (s.charAt(0) == s.charAt(3) && s.charAt(1) == s.charAt(2) && s.charAt(0) != s.charAt(1)) {
            return true;
        }
        return false;
    }

    public static boolean supportsTls(String ipAddress) {
        boolean result = false;
        boolean inBrackets = false;
        for (int i = 0; i < ipAddress.length() - 3; i++) {
            char current = ipAddress.charAt(i);
            if (current == '[') {
                inBrackets = true;
                continue;
            } else if (current == ']') {
                inBrackets = false;
                continue;
            }
            String substring = ipAddress.substring(i, i+4);
            boolean abbaCheck = isAbba(substring);
            if (abbaCheck && inBrackets == false) {
                result = true;
            } else if (abbaCheck && inBrackets == true) {
                return false;
            }
        }
        return result;
    }

    public static void testCase(String testCase, boolean expected) {
        if (supportsTls(testCase) == expected) {
            System.out.println("Test case: " + testCase + " : PASS");
        } else {
            System.out.println("Test case: " + testCase + " : FAIL");
        }
    }
}