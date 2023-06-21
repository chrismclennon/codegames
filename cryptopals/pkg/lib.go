package pkg

import (
	"encoding/base64"
	"encoding/hex"
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

func EncodeBase64(src []byte) []byte {
	dst := make([]byte, base64.StdEncoding.EncodedLen(len(src)))
	base64.StdEncoding.Encode(dst, src)
	return dst
}
