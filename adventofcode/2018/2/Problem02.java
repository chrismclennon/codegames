import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class Problem02 {
    public static void main(String[] args) throws IOException {
        List<String> sampleCaseOne = Arrays.asList("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab");
        List<String> sampleCaseTwo = Arrays.asList("abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz");
        List<String> boxIds = Files.readAllLines(Paths.get("adventofcode/2018/2/input.txt"));
        System.out.println("Part one, sample: " + partOne(sampleCaseOne));
        System.out.println("Part one: " + partOne(boxIds));
        System.out.println("Part two, sample: " + partTwo(sampleCaseTwo));
        System.out.println("Part two: " + partTwo(boxIds));
    }

    public static Map<Character, Integer> getCharacterFrequencyMap(String boxId) {
        Map<Character, Integer> characterFrequencyMap = new HashMap<>();
        for (Character letter : boxId.toCharArray()) {
            Integer currentCount = characterFrequencyMap.getOrDefault(letter, 0);
            characterFrequencyMap.put(letter, ++currentCount);
        }
        return characterFrequencyMap;
    }

    public static String getCommonCharacters(String first, String second) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < first.length(); i++) {
            char firstChar = first.charAt(i), secondChar = second.charAt(i);
            if (firstChar == secondChar) {
                sb.append(firstChar);
            }
        }
        return sb.toString();
    }

    public static int partOne(List<String> boxIds) {
        int twoLetterAppearance = 0, threeLetterAppearance = 0;
        for (String boxId : boxIds) {
            Map<Character, Integer> characterFrequencyMap = getCharacterFrequencyMap(boxId);
            Collection<Integer> characterFrequencies = characterFrequencyMap.values();
            if (Collections.frequency(characterFrequencies, 2) >= 1) {
                twoLetterAppearance++;
            }
            if (Collections.frequency(characterFrequencies, 3) >= 1) {
                threeLetterAppearance++;
            }
        }
        int checksum = twoLetterAppearance * threeLetterAppearance;
        return checksum;
    }

    public static String partTwo(List<String> boxIds) {
        TreeSet<String> sortedBoxIds = new TreeSet<>(boxIds);
        String first = sortedBoxIds.pollFirst(), second = sortedBoxIds.pollFirst();
        while (sortedBoxIds.size() > 0) {
            String commonCharacters = getCommonCharacters(first, second);
            if (commonCharacters.length() == first.length()-1) {
                return commonCharacters;
            }
            first = second;
            second = sortedBoxIds.pollFirst();
        }
        return null;
    }
}