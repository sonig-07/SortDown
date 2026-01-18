import argparse
from classifier import classify_downloads
from duplicate_finder import find_duplicates
from previewer import preview_file
from undoer import undo_last_operation

def main():
    parser = argparse.ArgumentParser(description="SortDown - Smart Folder Organizer")
    subparsers = parser.add_subparsers(dest="command")

    classify = subparsers.add_parser("classify")
    classify.add_argument("--path", required=True)

    dup = subparsers.add_parser("duplicates")
    dup.add_argument("--path", required=True)

    preview = subparsers.add_parser("preview")
    preview.add_argument("file")

    subparsers.add_parser("undo")

    args = parser.parse_args()

    if args.command == "classify":
        classify_downloads(args.path)
    elif args.command == "duplicates":
        find_duplicates(args.path)
    elif args.command == "preview":
        preview_file(args.file)
    elif args.command == "undo":
        undo_last_operation()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
