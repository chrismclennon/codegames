import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneOffset;

class Gigasecond {

    private long gigasecond = (long) 1e9;
    private LocalDateTime birthDateTime;

    Gigasecond(LocalDate birthDate) {
        this.birthDateTime = birthDate.atStartOfDay();
    }

    Gigasecond(LocalDateTime birthDateTime) {
        this.birthDateTime = birthDateTime;
    }

    LocalDateTime getDate() {
        return this.birthDateTime.plusSeconds(gigasecond);
    }

}
