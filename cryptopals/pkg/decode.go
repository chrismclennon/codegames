package pkg

import "encoding/hex"

func DecodeHex(src []byte) ([]byte, error) {
	dst := make([]byte, hex.DecodedLen(len(src)))
	if _, err := hex.Decode(dst, src); err != nil {
		return nil, err
	}
	return dst, nil
}
