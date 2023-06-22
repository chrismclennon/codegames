package pkg

import (
	"fmt"
)

// S1C1
func HexToBase64(src []byte) ([]byte, error) {
	dst, err := DecodeHex(src)
	if err != nil {
		return nil, err
	}
	return EncodeBase64(dst), nil
}

// S1C2
func FixedXor(a, b []byte) ([]byte, error) {
	dA, err := DecodeHex(a)
	if err != nil {
		return nil, err
	}
	dB, err := DecodeHex(b)
	if err != nil {
		return nil, err
	}
	if len(dA) != len(dB) {
		return nil, fmt.Errorf("mismatched lengths")
	}

	res := make([]byte, len(dA))
	for i := range dA {
		res[i] = dA[i] ^ dB[i]
	}
	return EncodeHex(res), nil
}

// S1C3
func SingleByteXorCipher(src []byte) (msg []byte, key byte, score int, err error) {
	dst, err := DecodeHex(src)
	if err != nil {
		return
	}

	for i := 0; i < 256; i++ {
		k := byte(i)
		currentMsg := DecryptSingleByteXor(dst, k)
		currentScore := getBytesWeight(currentMsg)
		if currentScore > score {
			score = currentScore
			msg = currentMsg
			key = k
		}
	}
	return
}

func DecryptSingleByteXor(input []byte, b byte) []byte {
	res := make([]byte, len(input))
	for i := range input {
		res[i] = input[i] ^ b
	}
	return res
}

// getBytesWeight will sum the score of each byte based on English character frequency.
func getBytesWeight(input []byte) int {
	var weight int
	for _, c := range input {
		weight += getCharWeight(c)
	}
	return weight
}

// getCharWeight scores a character byte based on English character frequency.
// Characters with a higher score occur more frequently in English.
func getCharWeight(char byte) int {
	wm := map[byte]int{
		byte('U'): 2,
		byte('u'): 2,
		byte('L'): 3,
		byte('l'): 3,
		byte('D'): 4,
		byte('d'): 4,
		byte('R'): 5,
		byte('r'): 5,
		byte('H'): 6,
		byte('h'): 6,
		byte('S'): 7,
		byte('s'): 7,
		byte(' '): 8,
		byte('N'): 9,
		byte('n'): 9,
		byte('I'): 10,
		byte('i'): 10,
		byte('O'): 11,
		byte('o'): 11,
		byte('A'): 12,
		byte('a'): 12,
		byte('T'): 13,
		byte('t'): 13,
		byte('E'): 14,
		byte('e'): 14,
	}
	return wm[char]
}

// S1C4
func detectSingleCharacterXor() (msg string, score int, err error) {
	for _, line := range StaticSetOneChallengeFour {
		currMsg, _, currScore, err := SingleByteXorCipher([]byte(line))
		if err != nil {
			return "", 0, err
		}
		if currScore > score {
			score = currScore
			msg = string(currMsg)
		}
	}
	return
}

// S1C5
func EncryptRepeatingKeyXor(msg, key []byte) []byte {
	res := make([]byte, len(msg))
	for i := range msg {
		res[i] = msg[i] ^ key[i%len(key)]
	}
	return res
}
