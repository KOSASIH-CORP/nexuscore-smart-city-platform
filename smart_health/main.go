package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
)

func encrypt(data []byte, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	nonce:= make([]byte, gcm.NonceSize())
	encryptedData := gcm.Seal(nonce, nonce, data, nil)
	return encryptedData, nil
}

func main() {
	data := []byte("This is a secret message")
	key := []byte("YOUR_SECRET_KEY")
	encryptedData, err := encrypt(data, key)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(base64.StdEncoding.EncodeToString(encryptedData))
}
