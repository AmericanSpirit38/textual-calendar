# Textual Calendar

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/AmericanSpirit38/textual-calendar/ci.yml?branch=main)](https://github.com/AmericanSpirit38/textual-calendar/actions)
[![Release](https://img.shields.io/github/v/release/AmericanSpirit38/textual-calendar?label=release)](https://github.com/AmericanSpirit38/textual-calendar/releases)
[![Stars](https://img.shields.io/github/stars/AmericanSpirit38/textual-calendar?style=social)](https://github.com/AmericanSpirit38/textual-calendar/stargazers)
[![Issues](https://img.shields.io/github/issues/AmericanSpirit38/textual-calendar)](https://github.com/AmericanSpirit38/textual-calendar/issues)
[![License](https://img.shields.io/github/license/AmericanSpirit38/textual-calendar)](https://github.com/AmericanSpirit38/textual-calendar/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Simple TUI calendar built on the Textual framework.

## Overview

Textual Calendar is a small terminal user interface (TUI) calendar application implemented with the Textual framework. The repository contains core modules for managing calendar state, time utilities, JSON persistence, and the application entry point.

Key files
- `Start.py` — application entry point (launches the Textual TUI)
- `CalendarManager.py` — calendar state and display helpers
- `TimeManager.py` — time/date related utilities
- `JsonManagement.py` — JSON-based persistence for events/settings
- `Data/` — data folder (stores saved JSON files)

## Requirements

- Python 3.8+ (newer recommended)
- Textual framework (install via pip)

Install Textual:

```bash
pip install textual
```

## Run

From the repository root, run:

```bash
python Start.py
```

or

```bash
python3 Start.py
```

This will launch the Textual TUI. Follow on-screen controls (arrow keys, shortcuts) provided by the UI. If the application expects persisted data, check or create files in the `Data/` folder.

## Data & Persistence

The repository contains `JsonManagement.py` which provides JSON read/write helpers. Saved events and configuration are expected to live in the `Data/` folder. Back up the `Data/` directory before making large changes.

## Development

1. Clone the repo:

```bash
git clone https://github.com/AmericanSpirit38/textual-calendar.git
cd textual-calendar
```

2. Install dependencies:

```bash
pip install textual
```

3. Run locally and iterate on the Python files listed above.
