import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;


public class Problem05 {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String doorId = "ugkcyxxp";
        System.out.println("Part 1: " + partOne(doorId));
        System.out.println("Part 2: " + partTwo(doorId));
    }

    public static String partOne(String doorId) throws NoSuchAlgorithmException {
        StringBuilder result = new StringBuilder();
        MessageDigest md = MessageDigest.getInstance("MD5");
        int num = 0;
        while (result.length() < 8) {
            String message = doorId + num;
            byte[] bytesOfMessage = message.getBytes();
            md.update(bytesOfMessage);
            byte[] digest = md.digest();
            String hash = DatatypeConverter.printHexBinary(digest);
            if (hash.startsWith("00000")) {
                result.append(hash.charAt(5));
            }
            num++;
        }
        return result.toString();
    }

    public static String partTwo(String doorId) throws NoSuchAlgorithmException {
        Character[] result = new Character[8];
        MessageDigest md = MessageDigest.getInstance("MD5");
        int num = 0;
        while (hasNull(result)) {
            String message = doorId + num;
            byte[] bytesOfMessage = message.getBytes();
            md.update(bytesOfMessage);
            byte[] digest = md.digest();
            String hash = DatatypeConverter.printHexBinary(digest);
            if (hash.startsWith("00000")) {
                int position = Character.getNumericValue(hash.charAt(5));
                if (position >= result.length || result[position] != null) {
                    num++;
                    continue;
                }
                char ch = hash.charAt(6);
                result[position] = ch;
            }
            num++;
        }
        StringBuilder sb = new StringBuilder();
        for (Character ch : result) {
            sb.append(ch);
        }
        return sb.toString();
    }

    public static boolean hasNull(Character[] arr) {
        for (Character element : arr) {
            if (element == null) {
                return true;
            }
        }
        return false;
    }
}