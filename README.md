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

## Commands & Shortcuts

The application defines the following custom keybindings and actions (extracted from `Start.py`):

- a — Add Event
  - action: add_event
  - What it does: opens the add-event flow (implemented via the app's AddEvent routine)

- t — Today
  - action: today
  - What it does: filters the events table to show events for today

- ctrl+t — Tomorrow
  - action: tomorrow
  - What it does: filters the events table to show events for tomorrow

- w — This Week
  - action: week
  - What it does: displays events within the current week

- n — Next Week
  - action: next_week
  - What it does: displays events within the next week

- / — Focus Search
  - action: focus_search
  - What it does: focuses the search input so you can type a query immediately

- Escape — Clear Search / Unfocus
  - action: clear_search
  - What it does: clears the search input, resets the query filter, and blurs the search box

## Data & Persistence

The repository contains `JsonManagement.py` which provides JSON read/write helpers. Saved events and configuration are expected to live in the `Data/` folder. Back up the `Data/` directory before making large changes.
