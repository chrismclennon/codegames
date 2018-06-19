import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


class Problem01 {
    private enum Direction {
        NORTH, EAST, SOUTH, WEST;

        private Direction left, right;

        static {
            NORTH.left = WEST;
            NORTH.right = EAST;
            EAST.left = NORTH;
            EAST.right = SOUTH;
            SOUTH.left = EAST;
            SOUTH.right = WEST;
            WEST.left = SOUTH;
            WEST.right = NORTH;
        }

        public Direction turnLeft() {
            return this.left;
        }

        public Direction turnRight() {
            return this.right;
        }
    }

    private static class Coordinate extends common.Coordinate {
        Direction direction;

        public Coordinate() {
            this.x = 0;
            this.y = 0;
            this.direction = Direction.NORTH;
        }

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
            this.direction = Direction.NORTH;
        }

        public Coordinate(int x, int y, Direction direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
        }

        public Coordinate clone() {
            return new Coordinate(this.x, this.y, this.direction);
        }

        public int distanceFromRoot() {
            return Math.abs(this.x) + Math.abs(this.y);
        }

        public void executeInstruction(String instruction) {
            char direction = instruction.charAt(0);
            int distance = Integer.valueOf(instruction.substring(1));
            if (direction == 'L') {
                this.direction = this.direction.turnLeft();
            } else if (direction == 'R') {
                this.direction = this.direction.turnRight();
            }
            this.moveForward(distance);
        }

        public List<Coordinate> executeSteps(String instruction) {
            List<Coordinate> steps = new ArrayList<>();
            char direction = instruction.charAt(0);
            if (direction == 'L') {
                this.direction = this.direction.turnLeft();
            } else if (direction == 'R') {
                this.direction = this.direction.turnRight();
            }

            int distance = Integer.valueOf(instruction.substring(1));
            for (int stepNum = 0; stepNum < distance; stepNum++) {
                this.stepForward();
                steps.add(this.clone());
            }
            return steps;
        }

        public void moveForward(int distance) {
            if (this.direction == Direction.NORTH) {
                this.y += distance;
            } else if (this.direction == Direction.EAST) {
                this.x += distance;
            } else if (this.direction == Direction.SOUTH) {
                this.y -= distance;
            } else if (this.direction == Direction.WEST) {
                this.x -= distance;
            }
        }

        public void stepForward() {
            moveForward(1);
        }
    }

    public static void main(String[] args) {
        String input = null;
        try {
            File inputFile = new File("adventofcode/2016/1/input.txt");
            Scanner scanner = new Scanner(inputFile);
            input = scanner.nextLine();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        String[] instructions = input.split(", ");
        System.out.println("Part 1: " + partOne(instructions));
        System.out.println("Part 2: " + partTwo(instructions));
    }

    public static int partOne(String[] instructions) {
        Coordinate coordinate = new Coordinate();
        for (String instruction : instructions) {
            coordinate.executeInstruction(instruction);
        }
        return coordinate.distanceFromRoot();
    }

    public static int partTwo(String[] instructions) {
        Coordinate coordinate = new Coordinate();
        Set<Coordinate> visitedCoordinates = new HashSet<>();
        int result = -1;
        for (String instruction: instructions) {
            List<Coordinate> newSteps = coordinate.executeSteps(instruction);
            for (Coordinate step: newSteps) {
                if (visitedCoordinates.contains(step)) {
                    result = step.distanceFromRoot();
                    return result;
                }
                visitedCoordinates.add(step);
            }
        }
        return result;
    }
}
