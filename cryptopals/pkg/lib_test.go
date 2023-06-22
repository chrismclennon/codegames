package pkg

import (
	"testing"
)

func TestHexToBase64(t *testing.T) {
	t.Run("set 1 challenge 1", func(t *testing.T) {
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
	t.Run("set 1 challenge 2", func(t *testing.T) {
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
