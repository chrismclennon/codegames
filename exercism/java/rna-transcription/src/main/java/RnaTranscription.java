import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.stream.Collectors;

class RnaTranscription {

    String transcribe(String dnaStrand) {
        HashMap<String, String> translate = new HashMap<>();
        translate.put("G", "C");
        translate.put("T", "A");
        translate.put("C", "G");
        translate.put("A", "U");

        List<String> listOfDna = Arrays.asList(dnaStrand.split(""));
        String rnaStrand = listOfDna.stream()
                            .map(nucleotide -> translate.get(nucleotide))
                            .collect(Collectors.joining());
        return rnaStrand;
    }

}

