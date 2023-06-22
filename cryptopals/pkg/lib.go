package pkg

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func HexToBase64(src []byte) ([]byte, error) {
	dst, err := DecodeHex(src)
	if err != nil {
		return nil, err
	}
	return EncodeBase64(dst), nil
}

func DecodeHex(src []byte) ([]byte, error) {
	dst := make([]byte, hex.DecodedLen(len(src)))
	if _, err := hex.Decode(dst, src); err != nil {
		return nil, err
	}
	return dst, nil
}

func EncodeHex(src []byte) []byte {
	dst := make([]byte, hex.EncodedLen(len(src)))
	hex.Encode(dst, src)
	return dst
}

func EncodeBase64(src []byte) []byte {
	dst := make([]byte, base64.StdEncoding.EncodedLen(len(src)))
	base64.StdEncoding.Encode(dst, src)
	return dst
}

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
