# Textual Calendar

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
- Other dependencies: none explicitly listed in the repo. If you encounter missing imports, install the required package(s) shown in the import errors.

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

## Contributing

- Open an issue or pull request for bugs and feature requests.
- Add tests or example data under `Data/` if you change persistence behavior.
- Consider adding a `requirements.txt` or `pyproject.toml` to make dependencies explicit.

## Notes & Next Steps

- The repo currently does not include an explicit license file or a requirements file. Consider adding a LICENSE and a requirements file (or pyproject) to clarify usage and dependencies.
- If you want, I can add this README.md to the repository and open a PR with the new file, or produce a commit you can apply locally.

---
If you'd like the README changed (more detail on controls, screenshots, or explicit dependency pins), tell me which details to include and I will update it.
