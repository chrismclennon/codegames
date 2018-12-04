import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Problem04 {
    public static void main(String[] args) throws IOException {
        List<String> input = Files.readAllLines(Paths.get("adventofcode/2018/4/input.txt"));
        Collections.sort(input);
        partOne(input);
        partTwo(input);
    }

    public static int parseTimestamp(String event) {
        Pattern timePattern = Pattern.compile("\\[[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}):([0-9]{2})\\].*");
        Matcher timeMatcher = timePattern.matcher(event);
        timeMatcher.find();
        int hour = Integer.parseInt(timeMatcher.group(1));
        int minute = Integer.parseInt(timeMatcher.group(2));
        return hour * 60 + minute;
    }

    public static Map<Integer, LinkedList<boolean[]>> assembleGuardRecords(List<String> events) {
        Map<Integer, LinkedList<boolean[]>> guardRecords = new HashMap<>();
        Pattern guardIdPattern = Pattern.compile(".*Guard #([0-9]+).*");

        int index = 0;
        while (index < events.size()) {
            String event = events.get(index);
            boolean[] record = new boolean[1440];

            Matcher guardIdMatcher = guardIdPattern.matcher(event);
            guardIdMatcher.find();
            Integer guardId = Integer.parseInt(guardIdMatcher.group(1));
            index++;

            while (index < events.size() && !events.get(index).contains("Guard")) {
                event = events.get(index);
                int startTime = parseTimestamp(event);
                index++;

                event = events.get(index);
                int endTime = parseTimestamp(event);
                index++;

                for (int i = startTime; i < endTime; i++) {
                    record[i] = true;
                }
            }

            LinkedList<boolean[]> guardRecord = guardRecords.getOrDefault(guardId, new LinkedList<>());
            guardRecord.add(record);
            guardRecords.put(guardId, guardRecord);
        }
        return guardRecords;
    }

    public static void partOne(List<String> events) {
        Map<Integer, LinkedList<boolean[]>> guardRecords = assembleGuardRecords(events);
        // Find guard with most minutes asleep
        Integer maxSleepGuardId = null;
        int maxMinutesAsleep = -1;
        for (Integer guardId : guardRecords.keySet()) {
            LinkedList<boolean[]> records = guardRecords.get(guardId);
            int minutesAsleep = 0;
            for (boolean[] record : records) {
                for (int i = 0; i < record.length; i++) {
                    if (record[i]) {
                        minutesAsleep++;
                    }
                }
            }
            if (minutesAsleep > maxMinutesAsleep) {
                maxMinutesAsleep = minutesAsleep;
                maxSleepGuardId = guardId;
            }
        }
        System.out.println("Guard #" + maxSleepGuardId + " slept the most at " + maxMinutesAsleep + " minutes.");

        // Find minute that guard is asleep the most.
        LinkedList<boolean[]> records = guardRecords.get(maxSleepGuardId);
        int maxMinute = -1, maxCount = 0;
        int count = 0;
        for (int minute = 0; minute < records.get(0).length; minute++) {
            count = 0;
            for (boolean[] record : records) {
                if (record[minute]) {
                    count++;
                }
            }
            if (count > maxCount) {
                maxMinute = minute;
                maxCount = count;
            }
        }
        System.out.println("The guard is most asleep at minute: " + maxMinute);
        System.out.println("Part one: " + maxSleepGuardId * maxMinute);
        System.out.println();
    }

    public static void partTwo(List<String> events) {
        Map<Integer, LinkedList<boolean[]>> guardRecords = assembleGuardRecords(events);
        Map<Integer, int[]> guardSleepMinutes = new HashMap<>();
        for (Integer guardId : guardRecords.keySet()) {
            int[] sleepMinutes = new int[1440];
            LinkedList<boolean[]> records = guardRecords.get(guardId);
            for (boolean[] record : records) {
                for (int i = 0; i < record.length; i++) {
                    if (record[i]) {
                        sleepMinutes[i]++;
                    }
                }
            }
            guardSleepMinutes.put(guardId, sleepMinutes);
        }
        Integer maxSleepGuardId = null;
        int maxMinute = -1, maxFrequency = -1;
        for (Integer guardId : guardSleepMinutes.keySet()) {
            int[] sleepMinutes = guardSleepMinutes.get(guardId);
            for (int minute = 0; minute < sleepMinutes.length; minute++) {
                int frequency = sleepMinutes[minute];
                if (frequency > maxFrequency) {
                    maxMinute = minute;
                    maxFrequency = frequency;
                    maxSleepGuardId = guardId;
                }
            }
        }
        System.out.println("Guard #" + maxSleepGuardId + " is most frequently asleep at minute " + maxMinute);
        System.out.println("Part two: " + maxSleepGuardId * maxMinute);
    }
}