class ArmstrongNumbers {

	boolean isArmstrongNumber(int numberToCheck) {
		int[] digits = makeIntegerArray(numberToCheck);
		int sum = 0, power = digits.length;
		for (int digit : digits) {
			sum += Math.pow(digit, power);
		}
		return sum == numberToCheck;
	}

	int[] makeIntegerArray(int number) {
		char[] digits = String.valueOf(number).toCharArray();
		int[] result = new int[digits.length];
		for (int index = 0; index < digits.length; index++) {
			int digit = Character.getNumericValue(digits[index]);
			result[index] = digit;
		}
		return result;
	}

}
