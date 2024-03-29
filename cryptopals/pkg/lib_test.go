package pkg

import (
	"testing"
)

func TestHexToBase64(t *testing.T) {
	t.Run("S1C1", func(t *testing.T) {
		input := []byte("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

		actual, err := HexToBase64(input)
		expected := "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
		if err != nil {
			t.Errorf("unexpected error: %s", err)
		} else if string(actual) != expected {
			t.Errorf("mismatch %q != %q", actual, expected)
		}
	})
}

func TestFixedXor(t *testing.T) {
	t.Run("S1C2", func(t *testing.T) {
		a := []byte("1c0111001f010100061a024b53535009181c")
		b := []byte("686974207468652062756c6c277320657965")

		actual, err := FixedXor(a, b)
		expected := "746865206b696420646f6e277420706c6179"
		if err != nil {
			t.Errorf("unexpected error: %s", err)
		} else if string(actual) != expected {
			t.Errorf("mismatch %q != %q", actual, expected)
		}
	})

	t.Run("error: mismatched lengths", func(t *testing.T) {
		_, err := FixedXor([]byte("a"), []byte("abc"))
		if err == nil {
			t.Errorf("expected an error")
		}
	})
}

func TestSingleByteXorCipher(t *testing.T) {
	t.Run("S1C3", func(t *testing.T) {
		input := []byte("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

		expectedMsg := "Cooking MC's like a pound of bacon"
		expectedKey := "X"
		expectedScore := 204

		msg, key, score, err := SingleByteXorCipher(input)
		if err != nil {
			t.Errorf("unexpected error: %s", err)
		} else if string(msg) != expectedMsg {
			t.Errorf("incorrect message: %q != %q", msg, expectedMsg)
		} else if string(key) != expectedKey {
			t.Errorf("incorrect key: %q != %q", key, expectedKey)
		} else if score != expectedScore {
			t.Errorf("incorrect score: %d != %d", score, expectedScore)
		}
	})
}

func TestDetectSingleCharacterXor(t *testing.T) {
	t.Run("S1C4", func(t *testing.T) {
		actual, _, err := detectSingleCharacterXor()
		expected := "Now that the party is jumping\n"
		if err != nil {
			t.Errorf("unexpected error: %s", err)
		} else if actual != expected {
			t.Errorf("incorrect message: %q != %q", actual, expected)
		}
	})
}

func TestEncryptRepeatingKeyXor(t *testing.T) {
	t.Run("S1C5", func(t *testing.T) {
		key := []byte("ICE")
		input := []byte(`Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal`)
		expected := []byte(`0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f`)
		actual := EncodeHex(EncryptRepeatingKeyXor(input, key))

		if string(actual) != string(expected) {
			t.Errorf("mismatch %q != %q", actual, expected)
		}
	})
}
