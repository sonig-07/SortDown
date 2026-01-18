# SortDown

SortDown is a Python-based command-line utility to organize folders by file type, detect and clean duplicate files, search files by name, and safely preview files.

## Features
- Classify files into folders (Documents, Images, Videos, Archives, etc.)
- One-level undo for last classification
- Detect and safely clean duplicate files (move to trash folder)
- Search files by name across folders
- File preview (text, zip, metadata)
- Optional Tkinter GUI for non-CLI users

## Requirements
- Python
- Windows OS
- Standard library only

## How to Run (CLI)

```bash
python cli/main.py classify --path "<folder-path>"
python cli/main.py undo
python cli/main.py clean-duplicates --path "<folder-path>"
python cli/main.py search --path "<folder-path>" <keyword>
python cli/main.py preview "<file-path>"
