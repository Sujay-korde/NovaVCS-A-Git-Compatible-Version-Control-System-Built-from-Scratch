# NovaVCS

A Git-inspired Version Control System built from scratch in Python.

NovaVCS is a systems programming project that reimplements the core concepts behind modern version control systems such as Git. The project explores content-addressable storage, object hashing, commit history, repository structures, branching, and version control internals through a clean Python implementation.

The goal of NovaVCS is not to replace Git, but to understand how distributed version control systems work internally by building one from first principles.

---

## Project Status

🚧 Active Development

Current Progress:

* [x] Project Setup
* [x] Command Line Interface Framework
* [x] Command Dispatcher
* [ ] Repository Initialization (`nova init`)
* [ ] Object Storage
* [ ] Blob Objects
* [ ] Tree Objects
* [ ] Commit Objects
* [ ] Branching
* [ ] Checkout
* [ ] Staging Area
* [ ] Repository Status
* [ ] Commit History

---

## Motivation

Most developers use Git every day but rarely understand how it works internally.

NovaVCS was created to gain a deeper understanding of:

* Content-Addressable Storage
* Cryptographic Hashing
* Object Databases
* Directed Acyclic Graphs (DAGs)
* Repository Structures
* Branch Management
* Version History Traversal
* Distributed Version Control Concepts

Instead of treating Git as a black box, NovaVCS reconstructs its architecture step-by-step.

---

## Features

### Command Line Interface

* Modular command architecture
* Argument parsing using Python argparse
* Git-style subcommands

Example:

```bash
nova init
nova commit
nova status
nova log
```

### Planned Repository Management

* Initialize repositories
* Manage repository metadata
* HEAD management
* Configuration support

### Planned Object Database

* Blob objects
* Tree objects
* Commit objects
* SHA-1 object hashing
* Object compression using zlib

### Planned Version Control Features

* Add files
* Create commits
* View commit history
* Create branches
* Switch branches
* Repository status tracking

---

## Architecture

NovaVCS stores repository data inside a dedicated `.nova` directory.

```text
.nova/
├── objects/
├── refs/
├── HEAD
├── config
└── index
```

Like Git, NovaVCS will use a content-addressable object database where every object is identified by its cryptographic hash.

---

## Current Project Structure

```text
NovaVCS/
│
├── nova
├── libnova.py
├── README.md
├── LICENSE
│
└── .gitignore
```

Future structure:

```text
NovaVCS/
│
├── nova
├── libnova.py
├── commands/
├── docs/
├── tests/
├── README.md
└── LICENSE
```

---

## Technologies Used

* Python 3
* argparse
* hashlib
* zlib
* configparser
* os
* sys
* datetime

---

## Technical Concepts Demonstrated

This project explores several important software engineering and systems programming concepts:

* Version Control Systems
* Content-Addressable Storage
* SHA-1 Hashing
* Data Compression
* File System Design
* Directed Acyclic Graphs (DAGs)
* Command Line Interface Design
* Software Architecture
* Systems Programming

---

## Example Usage

Initialize a repository:

```bash
nova init
```

Hash an object:

```bash
nova hash-object file.txt
```

View object contents:

```bash
nova cat-file <object-id>
```

Create a commit:

```bash
nova commit -m "Initial commit"
```

Display history:

```bash
nova log
```

---

## Development Roadmap

### Phase 1 — Core Repository

* [ ] Repository initialization
* [ ] Configuration management
* [ ] Repository discovery

### Phase 2 — Object Database

* [ ] Blob storage
* [ ] Object retrieval
* [ ] Object hashing
* [ ] Compression support

### Phase 3 — Trees and Commits

* [ ] Tree objects
* [ ] Commit objects
* [ ] Commit history

### Phase 4 — Branching

* [ ] References
* [ ] Branch creation
* [ ] Branch switching

### Phase 5 — Staging Area

* [ ] Index implementation
* [ ] Add command
* [ ] Status command

### Phase 6 — Advanced Features

* [ ] Merge support
* [ ] Clone support
* [ ] Remote repositories

---

## Learning References

This project is inspired by and built while studying:

* Write Yourself a Git (WYAG)
* Pro Git
* Official Git Documentation

The implementation is written independently as a learning and engineering exercise.

---

## Why This Project?

Building a version control system from scratch provides hands-on experience with:

* Real-world software architecture
* Storage systems
* Data structures
* Hashing algorithms
* File management
* Command line application development

NovaVCS serves as both a learning project and a demonstration of systems programming skills.

---

## License

This project is licensed under the MIT License.
