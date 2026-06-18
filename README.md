# SwitchBlade

An organised ecosystem of distinct Command Line Interface (CLI) tools built to handle media, data, and structural transformations across diverse formats. This repository serves as a centralised suite of specialised utilities, each developed in the programming language best suited to its operational constraints, computational complexity, and performance requirements.

## Architecture and Design Philosophy

The primary objective of SwitchBlade is to decouple format conversion tools from heavy graphical environments or monolithic dependencies, providing lightweight, reliable, and pipelable scripts and binaries.

## Core Principles
- **Single Responsibility**: Each subdirectory contains a standalone command-line application dedicated to a single domain of transformation.

- **Language Diversity**: Rather than enforcing a unified runtime environment, utilities leverage optimal language features (e.g., Go/Rust for high-concurrency binary transformations, Python for scriptable metadata manipulation, Node.js for structural data parsing).

- **CLI Interoperability**: Tools are designed around Unix philosophy standards, utilising standard input/output streams (stdin/stdout) and standard exit codes to enable seamless integration into broader deployment pipelines and shell scripts.

## Directory Structure

The repository maintains a strict separation of concerns based on the target domain of the converter. Dependencies, build files, and language-specific manifestations are isolated within their respective subdirectories to keep the root scope unpolluted.

```plaintext
.
├── .gitattributes             # Line ending configuration and binary attributes
├── .gitignore                 # Consolidated multi-language build artifact filters
├── LICENSE                    # Distribution and usage terms (MIT License)
├── README.md                  # System overview and repository documentation
│
├── code/                      # Converters specialized in syntax, schema, and structured serialization
│   ├── yaml-to-json/
│   │   └── main.go            # Streamlined Go executable for configuration parsing
│   └── sql-to-csv/
│       ├── converter.py       # Python script using native streams for record dumps
│       └── requirements.txt
│
├── image/                     # Graphical processing, compression, and matrix transformations
│   ├── webp-to-png/
│   │   ├── Cargo.toml         # Rust-based high-performance image decoding crate
│   │   └── src/
│   │       └── main.rs
│   └── svg-to-png/
│       └── package.json       # Node.js implementation using headless rendering
│
├── text/                      # String encoding, cryptographic hashing, and markup transformations
│   ├── markdown-to-html/
│   │   ├── main.py            # Python implementation using standard parsing libraries
│   │   └── requirements.txt
│   └── hex-to-binary/
│       └── main.c             # Low-level memory mapping interface in ANSI C
│
└── .../                       # More additions being added actively
```

## Guidelines for Directory Isolation

To preserve systemic modularity, contributors and maintainers must strictly enforce the following organisational rules:

- **Self-Containment**: All build manifests (package.json, Cargo.toml, go.mod, requirements.txt), compilation scripts, source code, and tool-specific testing suites must reside entirely within the individual sub-folder assigned to that converter. No global dependencies or cross-directory symlinks are permitted.

- **Local Documentation**: Every converter directory must feature its own localized README.md file specifying explicit execution parameters, runtime prerequisites, build instructions, input validation criteria, and operational flags.

## Environment Setup and Requirements

Given the polyglot composition of this ecosystem, prerequisites depend entirely on the specific tool being deployed.

### Runtime Dependencies

Depending on which utilities are utilised, the local system may require the following toolchains:

- Python 3.10 or higher

- Node.js 18.x or higher

- Rust toolchain (rustc and cargo stable)

- Go 1.20 or higher

- GCC or Clang for native C/C++ compilation

### Common Development Controls

Global baseline rules are defined at the root level via structural Git configurations:

- Line endings are normalised via [.gitattributes](/.gitattributes) to handle Unix-style line feeds (LF) uniformly for source assets across cross-platform environments.

- Build targets, execution binaries (.exe, .out), local lockfiles, tracking caches, and local virtual environments (.venv, node_modules) are aggressively suppressed by the global .gitignore file.

## Licensing and Compliance

This repository is distributed under the terms of the **MIT License**.

### Legal Implications

- **Permission to Modify and Distribute**: Individuals and commercial entities are granted unrestricted permission to use, duplicate, alter, merge, publish, or sell instances of these utilities.

- **Liability and Warranty**: The software is provided without warranty or guarantee of performance of any kind. Responsibility for unexpected run-time behaviors or execution faults rests solely with the end-user.

- **Notice Requirement**: The original copyright notice and text of the MIT License must remain embedded in all subsequent distributions or substantial portions of the source components found herein.

## System Integration Standards

To ensure compatibility with POSIX standards, all newly introduced or refactored tools within this suite must conform to the following baseline execution interface:

```bash
# General structural pipeline capability template
cat input_source.ext | [converter_command] [flags] > output_destination.ext
```

### Exit Codes

Every application in this repository must reliably return explicit exit codes to communicate execution states to the invoking shell:

- 0: Operation completed with complete success and without error.

- 1: General execution error or invalid file path parameters.

- 2: Argument parsing failure or missing mandatory operational flag.

- 127: External underlying system command or runtime binary not detected.

---
## Buy me a Coffee
If you think I deserve a little gift to support me and my creations, feel free to buy me a coffee (not the actual website, but a Revolut payment link)!

Please include your GitHub username in the "Note" section so I can add you to the contributor list on my profile!

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://revolut.me/andreygdl9)
