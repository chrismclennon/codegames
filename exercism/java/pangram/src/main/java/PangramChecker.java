import java.util.HashSet;

public class PangramChecker {

    public boolean isPangram(String input) {
        HashSet<Character> alphabet = getAlphabet();
        for (Character character : input.toCharArray()) {
            character = Character.toLowerCase(character);
            if (alphabet.contains(character)) {
                alphabet.remove(character);
            }
        }
        return alphabet.isEmpty();
    }

    public HashSet<Character> getAlphabet() {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        HashSet<Character> alphabetSet = new HashSet<>();
        for (char letter : alphabet) {
            alphabetSet.add(letter);
        }
        return alphabetSet;
    }

}
