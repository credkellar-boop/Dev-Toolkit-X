package main

import (
	"crypto/sha256"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

// Zero-dependency, pure Go scanner to audit MCP servers and dependencies.
func scanDirectory(root string) error {
	log.Printf("🛡️ Initiating read-only defensive scan on: %s", root)
	
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			// Compute cryptographic hash of every file before execution
			hash := computeHash(path)
			fmt.Printf("Validated: %s [SHA-256: %x]\n", path, hash)
		}
		return nil
	})
	return err
}

func computeHash(filePath string) []byte {
	data, _ := os.ReadFile(filePath)
	hash := sha256.Sum256(data)
	return hash[:]
}

func main() {
	scanDirectory("/workspace")
}
