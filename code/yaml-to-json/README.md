# YAML to JSON Converter

A lightweight Go utility that reads YAML from `stdin` and outputs pretty-printed JSON to `stdout`.

## How to Run:

### 1. Navigate to this directory:
```bash
cd yaml-to-json
```
### 2. Build or run the tool:
```bash
# Run it directly
go run main.go < input.yaml

# Or build the binary
go build -o yaml-to-json main.go
```

### Usage Example:

```bash
echo "
status: success
code: 200
" | ./yaml-to-json
```
### Output:

```json
{
  "code": 200,
  "status": "success"
}
```
