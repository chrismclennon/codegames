class SpaceAge {

    private double seconds;
    private final double earth_period = 31557600;

    SpaceAge(double seconds) {
        this.seconds = seconds;
    }

    double getSeconds() {
        return this.seconds;
    }

    double onEarth() {
        double period = earth_period;
        return getSeconds() / period;
    }

    double onMercury() {
        double period = 0.2408467 * earth_period;
        return getSeconds() / period;
    }

    double onVenus() {
        double period = 0.61519726 * earth_period;
        return getSeconds() / period;
    }

    double onMars() {
        double period = 1.8808158 * earth_period;
        return getSeconds() / period;
    }

    double onJupiter() {
        double period = 11.862615 * earth_period;
        return getSeconds() / period;
    }

    double onSaturn() {
        double period = 29.447498 * earth_period;
        return getSeconds() / period;
    }

    double onUranus() {
        double period = 84.016846 * earth_period;
        return getSeconds() / period;
    }

    double onNeptune() {
        double period = 164.79132 * earth_period;
        return getSeconds() / period;
    }

}
