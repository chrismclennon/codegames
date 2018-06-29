class ReverseString {

    String reverse(String inputString) {
        char[] result = new char[inputString.length()];
        for (int index = 0; index < inputString.length(); index++) {
            result[index] = inputString.charAt(inputString.length()-1 - index);
        }
        return new String(result);
    }
  
}