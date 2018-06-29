class Hamming {

    String leftStrand, rightStrand;

    Hamming(String leftStrand, String rightStrand) {
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;

        if (leftStrand.length() != rightStrand.length()) {
            String message = "leftStrand and rightStrand must be of equal length.";
            throw new IllegalArgumentException(message);
        }
    }

    int getHammingDistance() {
        int hamming = 0;
        for (int index = 0; index < leftStrand.length(); index++) {
            if (leftStrand.charAt(index) != rightStrand.charAt(index)) {
                hamming += 1;
            }
        }
        return hamming;
    }

}
