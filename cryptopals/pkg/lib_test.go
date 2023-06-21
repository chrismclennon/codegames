package pkg

import (
	"testing"
)

func TestHexToBase64(t *testing.T) {
	t.Run("test", func(t *testing.T) {
		input := "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

		actual, err := HexToBase64([]byte(input))
		expected := "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
		if err != nil {
			t.Errorf("unexpected error: %s", err)
		} else if string(actual) != expected {
			t.Errorf("mismatch %q != %q", actual, expected)
		}
	})
}
