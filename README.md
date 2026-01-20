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

```

## Screenshots

<img width="1920" height="1020" alt="Screenshot 2026-01-20 231739" src="https://github.com/user-attachments/assets/d4c361d6-5072-45fa-bc4b-4e43f89ce045" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9f8d4c3f-ca14-47b6-87c9-b6ee2113f131" />
<img width="1097" height="680" alt="image" src="https://github.com/user-attachments/assets/35fcd259-a68c-4500-9bd2-a8900d401589" />



## Author

SoniG07

[https://github.com/sonig-07](https://github.com/sonig-07) 
[YT Demo](https://youtu.be/7Rt5Ce6T9NQ)

