import java.util.*;

class Room {

    private boolean valid;
    private int sectorId;
    private String computedCheckSum;
    private String givenCheckSum;
    private String rawData;
    private String roomName;
    private String shiftedRoomName;

    Room(String rawData) {
        this.rawData = rawData;
        this.roomName = parseRoomName(rawData);
        this.givenCheckSum = parseCheckSum(rawData);
        this.sectorId = parseSectorId(rawData);
        this.computedCheckSum = computeCheckSum(rawData);
        this.valid = isValid(this.givenCheckSum, this.computedCheckSum);
        this.shiftedRoomName = shiftRoomName(this.roomName, this.sectorId);
    }

    private String computeCheckSum(String data) {
        // Build frequency map.
        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (int i = 0; i < data.length(); i++) {
            char currentLetter = data.charAt(i);
            if (currentLetter == '-') {
                continue;
            } else if (Character.isDigit(currentLetter)) {
                break;
            }
            int count = frequencyMap.getOrDefault(currentLetter, 0) + 1;
            frequencyMap.put(currentLetter, count);
        }
        // Sort frequency map by values.
        Comparator<Map.Entry<Character, Integer>> sortByValueComparator = new Comparator<Map.Entry<Character, Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> first, Map.Entry<Character, Integer> second) {
                // Sort in descending order by value.
                // If values are equal, sort in ascending order by key.
                Integer firstVal = first.getValue();
                Integer secondVal = second.getValue();
                int valueResult = secondVal.compareTo(firstVal);
                if (valueResult == 0) {
                    Character firstKey = first.getKey();
                    Character secondKey = second.getKey();
                    return firstKey.compareTo(secondKey);
                }
                return valueResult;
            }
        };
        SortedSet<Map.Entry<Character, Integer>> sortedEntries = new TreeSet<Map.Entry<Character, Integer>>(sortByValueComparator);
        sortedEntries.addAll(frequencyMap.entrySet());
        // Pull first five letters from sorted entries.
        Iterator<Map.Entry<Character, Integer>> sortedEntriesIterator = sortedEntries.iterator();
        StringBuilder resultBuilder = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            char currentLetter = sortedEntriesIterator.next().getKey();
            resultBuilder.append(currentLetter);
        }
        return resultBuilder.toString();
    }

    public String getComputedCheckSum() {
        return this.computedCheckSum;
    }

    public String getGivenCheckSum() {
        return this.givenCheckSum;
    }

    public int getSectorId() {
        return this.sectorId;
    }

    public String getRawData() {
        return this.rawData;
    }

    public String getRoomName() {
        return this.roomName;
    }

    public String getShiftedRoomName() {
        return this.shiftedRoomName;
    }

    public boolean getValid() {
        return this.valid;
    }

    private boolean isValid(String givenCheckSum, String computedCheckSum) {
        return givenCheckSum.equals(computedCheckSum);
    }

    private String parseCheckSum(String data) {
        int startIndex = data.indexOf('[') + 1;
        int endIndex = data.indexOf(']');
        String result = data.substring(startIndex, endIndex);
        return result;
    }

    private String parseRoomName(String data) {
        int endIndex = -1;
        for (int i = 0; i < data.length(); i++) {
            char current = data.charAt(i);
            if (Character.isDigit(current)) {
                endIndex = i - 1;
                break;
            }
        }
        return data.substring(0, endIndex);
    }

    private int parseSectorId(String data) {
        int endIndex = data.indexOf('[');
        int startIndex = endIndex - 1;
        while (Character.isDigit(data.charAt(startIndex-1))) {
            startIndex--;
        }
        int result = Integer.parseInt(data.substring(startIndex, endIndex));
        return result;
    }

    private String shiftRoomName(String roomName, int shiftNum) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < roomName.length(); i++) {
            char current = roomName.charAt(i);
            if (current == '-') {
                result.append(' ');
                continue;
            }
            int shiftedLetterNum = ((int) current - (int) 'a' + shiftNum) % 26 + (int) 'a';
            char shiftedLetter = (char) shiftedLetterNum;
            result.append(shiftedLetter);
        }
        return result.toString();
    }
}
