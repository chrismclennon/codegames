import java.util.Arrays;
import java.util.HashSet;

class Acronym {

    private String acronym;

    Acronym(String phrase) {
        this.acronym = computeAcronym(phrase);
    }

    String get() {
        return this.acronym;
    }

    private String computeAcronym(String phrase) {
        String[] words = phrase.split("[^a-zA-Z]");
        StringBuilder builder = new StringBuilder();
        for (String word : words) {
            if (word.length() > 0) {
                builder.append(Character.toUpperCase(word.charAt(0)));
            }
        }
       return builder.toString();
    }

}
