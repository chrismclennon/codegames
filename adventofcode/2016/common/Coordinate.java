package common;


import java.util.Objects;

public class Coordinate {
    public int x, y;

    public Coordinate() {
        this.x = 0;
        this.y = 0;
    }

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public Coordinate clone() {
        return new Coordinate(this.x, this.y);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass()) {
            return false;
        }
        Coordinate other = (Coordinate) obj;
        return this.x == other.x && this.y == other.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
