import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class Problem06 {
    public static void main(String[] args) throws IOException {
        List<String> messages = Files.readAllLines(Paths.get("adventofcode/2016/6/input"));
        HashMap<Character, Integer>[] frequencies = new HashMap[messages.get(0).length()];
        for (String message : messages) {
            HashMap<Character, Integer> frequencyMap = null;
            for (int pos = 0; pos < message.length(); pos++) {
                char currentLetter = message.charAt(pos);
                if (frequencies[pos] == null) {
                    frequencyMap = new HashMap<>();
                } else {
                    frequencyMap = frequencies[pos];
                }
                int count = frequencyMap.getOrDefault(currentLetter, 0) + 1;
                frequencyMap.put(currentLetter, count);
                frequencies[pos] = frequencyMap;
            }
        }
        System.out.println("Part 1: " + repetitionCode(frequencies));

        Comparator<Integer> partTwoComparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (o1 == null) {
                    return -1;
                } else if (o1 < o2) {
                    return 1;
                } else if (o1 > o2) {
                    return -1;
                } else {
                    return 0;
                }
            }
        };
        System.out.println("Part 2: " + repetitionCode(frequencies, partTwoComparator));
    }

    public static String repetitionCode(HashMap<Character, Integer>[] frequencies) {
        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (o1 == null) {
                    return -1;
                } else if (o1 < o2) {
                    return -1;
                } else if (o1 > o2) {
                    return 1;
                } else {
                    return 0;
                }
            }
        };
        return repetitionCode(frequencies, comparator);

    }

    public static String repetitionCode(HashMap<Character, Integer>[] frequencies, Comparator<Integer> comparator) {
        StringBuilder finalMessage = new StringBuilder();
        for (HashMap<Character, Integer> frequencyMap : frequencies) {
            Character maxLetter = null;
            Integer maxValue = null;
            for (Map.Entry<Character, Integer> entry : frequencyMap.entrySet()) {
                int entryValue = entry.getValue();
                if (comparator.compare(maxValue, entryValue) == -1) {
                    maxValue = entryValue;
                    maxLetter = entry.getKey();
                }
            }
            finalMessage.append(maxLetter);
        }
        return finalMessage.toString();
    }
}