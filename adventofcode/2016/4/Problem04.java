import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.List;

class Problem04 {

    public static void main(String[] args) throws IOException {
        List<String> roomData = Files.readAllLines(Paths.get("adventofcode/2016/4/input"));
        List<Room> rooms = new LinkedList<>();
        for (String data : roomData) {
            Room room = new Room(data);
            rooms.add(room);
        }
        int sumSectorId = 0;
        for (Room room : rooms) {
            if (room.getValid()) {
                sumSectorId += room.getSectorId();
            }
        }
        System.out.println("Part 1: " + Integer.toString(sumSectorId));
        for (Room room : rooms) {
            if (room.getValid() && room.getShiftedRoomName().contains("north")) {
                System.out.println("Part 2: " + room.getSectorId());
            }
        }
    }

}