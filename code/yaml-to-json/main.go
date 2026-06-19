package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"

	"gopkg.in/yaml.v3"
)

func main() {
	// Read everything from Stdin
	yamlBytes, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input: %v\n", err)
		os.Exit(1)
	}

	// Unmarshal the YAML into a generic interface structure
	var data interface{}
	err = yaml.Unmarshal(yamlBytes, &data)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing YAML: %v\n", err)
		os.Exit(1)
	}

	// Standardize map keys to string type for JSON compatibility
	data = cleanMapKeys(data)

	// Convert data structure to indented JSON bytes
	jsonBytes, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error converting to JSON: %v\n", err)
		os.Exit(1)
	}

	// Output the resulting JSON string to Stdout
	fmt.Println(string(jsonBytes))
}

// cleanMapKeys recursively converts map[interface{}]interface{} into map[string]interface{}.
// yaml.v3 may parse keys as generic interfaces, which the standard json encoder cannot process.
func cleanMapKeys(in interface{}) interface{} {
	switch x := in.(type) {
	case map[string]interface{}:
		for k, v := range x {
			x[k] = cleanMapKeys(v)
		}
		return x
	case map[interface{}]interface{}:
		m := make(map[string]interface{})
		for k, v := range x {
			m[fmt.Sprintf("%v", k)] = cleanMapKeys(v)
		}
		return m
	case []interface{}:
		for i, v := range x {
			x[i] = cleanMapKeys(v)
		}
		return x
	default:
		return x
	}
}
