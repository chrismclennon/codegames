import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

class Problem03 {
    private static class Triangle {
        int a, b, c;
        int[] edges;

        public Triangle(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
            this.edges = new int[]{a, b, c};
            Arrays.sort(this.edges);
        }

        public Triangle(int[] edges) {
            this.a = edges[0];
            this.b = edges[1];
            this.c = edges[2];
            this.edges = edges;
            Arrays.sort(this.edges);
        }

        public boolean isPossible() {
            return this.edges[0] + this.edges[1] > this.edges[2];
        }
    }

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("adventofcode/2016/3/input.txt"));
        System.out.println("Part 1: " + partOne(lines));
        System.out.println("Part 2: " + partTwo(lines));
    }

    public static int partOne(List<String> lines) {
        int numPossibleTriangles = 0;
        for (String line : lines) {
            String[] stringEdges = new String[] {
                    line.substring(0, 5),
                    line.substring(5, 10),
                    line.substring(10, 15)
            };
            int[] edges = new int[stringEdges.length];
            for(int index = 0; index < stringEdges.length; index++) {
                edges[index] = Integer.parseInt(stringEdges[index].trim());
            }

            Triangle triangle = new Triangle(edges);
            if (triangle.isPossible()) {
                numPossibleTriangles++;
            }
        }
        return numPossibleTriangles;
    }

    public static int partTwo(List<String> lines) {
        int numPossibleTriangles = 0;
        for (int lineNumber = 0; lineNumber < lines.size(); lineNumber += 3) {
            for (int column = 0; column < 3; column++) {
                String[] stringEdges = new String[] {
                        lines.get(lineNumber).substring(5*column, 5+5*column),
                        lines.get(lineNumber+1).substring(5*column, 5+5*column),
                        lines.get(lineNumber+2).substring(5*column, 5+5*column)
                };
                int[] edges = new int[stringEdges.length];
                for(int index = 0; index < stringEdges.length; index++) {
                    edges[index] = Integer.parseInt(stringEdges[index].trim());
                }

                Triangle triangle = new Triangle(edges);
                if (triangle.isPossible()) {
                    numPossibleTriangles++;
                }
            }
        }
        return numPossibleTriangles;
    }
}
