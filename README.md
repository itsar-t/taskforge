# Taskforge

![Tests](https://github.com/itsar-t/taskforge/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/github/license/itsar-t/taskforge)
![Coverage](https://img.shields.io/badge/coverage-79%25-brightgreen)

> A clean, minimal task tracking engine built with layered architecture, UUID identity, JSON persistence, and pytest-driven development.

---

## Features

- Clean layered architecture:
  - `domain`
  - `services`
  - `storage`
  - `cli`
- Stable UUID-based task identity
- JSON persistence
- Backward compatible data loading
- CLI with subcommands
- Pytest test suite
- GitHub Actions CI
- 79%+ test coverage

---

## Architecture Overview

```text
CLI
  ↓
Tracker (Application Service)
  ↓
Task (Domain Model)
  ↓
Repository Interface
  ↓
JSON Repository
```

## Desing Principles Used
* Single Responsibility Principle
* Dependency Inversion
* Encapsulation
* Backward Compatibility
* Separation of Concerns

## Installation

```bash
git clone https://github.com/itsar-t/taskforge.git
cd taskforge
```

### Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### Install editable:

```bash
pip install -e .
```

## Usage 

### Add a task:

```bash
taskforge add "Learn architecture"
```

### List tasks:

```bash
taskforge list
```
#### List pending tasks:
```bash
taskforge list --ispending
```
#### List done tasks:
```bash
taskforge list --isdone
```

### Mark done (using short UUID prefix):
```bash
taskforge done a1b2c3d4
```
### Mark undone (using short UUID prefix):
```bash
taskforge undone a1b2c3d4
```
### Switch done (using short UUID prefix):
```bash
taskforge switch a1b2c3d4
```
### Remove:
```bash
taskforge rm a1b2c3d4
```
## Example Output
```bash
1. [Undone] (a1b2c3d4) Learn architecture
2. [Done] (f8e9d123) Build portfolio project

```
## Running Tests
### Install pytest
```bash
pip install -e .[dev]
```
### Run:

```bash
pytest
```
### Example output:

```bash
7 passed in 0.24s
Coverage: 79%

```




