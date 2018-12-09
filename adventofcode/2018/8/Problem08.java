import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class Problem08 {
    public static void main(String[] args) throws IOException {
        String realData = Files.readAllLines(Paths.get("adventofcode/2018/8/input.txt")).get(0);
        String sampleData = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2";
        String data = realData;
//        String data = sampleData;

        Deque<Integer> partOneData = new LinkedList<>();
        Deque<Integer> partTwoData = new LinkedList<>();
        for (String element : data.split(" ")) {
            partOneData.add(Integer.parseInt(element));
            partTwoData.add(Integer.parseInt(element));
        }

        System.out.println("Part one: " + partOne(partOneData));
        System.out.println("Part two: " + partTwo(partTwoData));
    }

    public static int partOne(Deque<Integer> data) {
        int numChildren = data.pollFirst();
        int numMetadata = data.pollFirst();

        int sumMetadata = 0;
        for (int i = 0; i < numChildren; i++) {
            sumMetadata += partOne(data);
        }
        for (int i = 0; i < numMetadata; i++) {
            sumMetadata += data.pollFirst();
        }
        return sumMetadata;
    }

    public static int partTwo(Deque<Integer> data) {
        int numChildren = data.pollFirst();
        int numMetadata = data.pollFirst();

        if (numChildren == 0) {
            int output = 0;
            for (int i = 0; i < numMetadata; i++) {
                output += data.pollFirst();
            }
            return output;
        }

        List<Integer> children = new ArrayList<>();
        for (int i = 0; i < numChildren; i++) {
            children.add(partTwo(data));
        }

        int output = 0;
        for (int i = 0; i < numMetadata; i++) {
            int metadata = data.pollFirst();
            if (metadata > children.size()) {
                continue;
            }
            output += children.get(metadata-1);
        }
        return output;
    }

}