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

git clone https://github.com/itsar-t/taskforge.git
cd taskforge

### Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows



