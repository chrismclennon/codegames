import common.Coordinate;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


class Problem02 {
    private enum Direction {
        UP, DOWN, LEFT, RIGHT;
    }

    private static class Keypad {
        char[][] keypad;
        int x_boundary, y_boundary;
        int start_x, start_y;
        Coordinate position;

        public Keypad(char[][] keypad, Coordinate position) {
           this.keypad = keypad;
           this.position = position;

           this.start_x = position.x;
           this.start_y = position.y;

           this.x_boundary = keypad[0].length-1;
           this.y_boundary = keypad.length-1;
        }

        public char getCurrentKey() {
            return keypad[this.position.y][this.position.x];
        }

        public void move(Direction direction) {
            if (direction == Direction.UP) {
                int y = Math.max(0, this.position.y-1);
                if (this.keypad[y][this.position.x] != 'X') {
                    this.position.y = y;
                }
            } else if (direction == Direction.DOWN) {
                int y = Math.min(this.y_boundary, this.position.y + 1);
                if (this.keypad[y][this.position.x] != 'X') {
                    this.position.y = y;
                }
            } else if (direction == Direction.RIGHT) {
                int x = Math.min(this.x_boundary, this.position.x+1);
                if (this.keypad[this.position.y][x] != 'X') {
                    this.position.x = x;
                }
            } else if (direction == Direction.LEFT) {
                int x = Math.max(0, this.position.x-1);
                if (this.keypad[this.position.y][x] != 'X') {
                    this.position.x = x;
                }
            }
        }

        public void resetCoordinate() {
            this.position = new Coordinate(this.start_x, this.start_y);
        }
    }

    public static void main(String[] args) throws IOException {
        HashMap<Character, Direction> directionMap = new HashMap<>();
        directionMap.put('U', Direction.UP);
        directionMap.put('D', Direction.DOWN);
        directionMap.put('L', Direction.LEFT);
        directionMap.put('R', Direction.RIGHT);

        List<String> lines = Files.readAllLines(Paths.get("adventofcode/2016/2/input.txt"));
        System.out.println("Part 1: " + partOne(lines, directionMap));
        System.out.println("Part 2: " + partTwo(lines, directionMap));
    }

    public static String partOne(List<String> lines, HashMap<Character, Direction> directionMap) {
        char[][] keypadLayout = new char[][]{
                new char[]{'1', '2', '3'},
                new char[]{'4', '5', '6'},
                new char[]{'7', '8', '9'}
        };
        Coordinate startingCoordinate = new Coordinate(0, 0);
        return solve(keypadLayout, lines, directionMap, startingCoordinate);
    }

    public static String partTwo(List<String> lines, HashMap<Character, Direction> directionMap) {
        char[][] keypadLayout = new char[][]{
                new char[]{'X', 'X', '1', 'X', 'X'},
                new char[]{'X', '2', '3', '4', 'X'},
                new char[]{'5', '6', '7', '8', '9'},
                new char[]{'X', 'A', 'B', 'C', 'X'},
                new char[]{'X', 'X', 'D', 'X', 'X'}
        };
        Coordinate startingCoordinate = new Coordinate(0, 2);
        return solve(keypadLayout, lines, directionMap, startingCoordinate);
    }

    public static String solve(char[][] keypadLayout, List<String> lines, HashMap<Character, Direction> directionMap,
                               Coordinate startingCoordinate) {
        Keypad keypad = new Keypad(keypadLayout, startingCoordinate);
        List<Character> result = new ArrayList<>();
        for (String line : lines) {
            for (char instruction : line.toCharArray()) {
                Direction direction = directionMap.get(instruction);
                keypad.move(direction);
            }
            result.add(keypad.getCurrentKey());
            keypad.resetCoordinate();
        }
        return result.toString();
    }
}
