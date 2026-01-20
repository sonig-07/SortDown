import argparse
import sys
import os

# Fix import path
sys.path.append(os.path.dirname(__file__))

from classifier import classify_downloads
from duplicate_finder import clean_duplicates
from previewer import preview_file
from undoer import undo_last_operation
from searcher import search_files


def main():
    parser = argparse.ArgumentParser(description="SortDown - Smart Folder Organizer")
    subparsers = parser.add_subparsers(dest="command")

    # Classify
    classify = subparsers.add_parser("classify")
    classify.add_argument("--path", required=True)

    # Clean duplicates
    dup = subparsers.add_parser("clean-duplicates")
    dup.add_argument("--path", required=True)

    # Search
    search = subparsers.add_parser("search")
    search.add_argument("--path", required=True)
    search.add_argument("keyword")

    # Preview
    preview = subparsers.add_parser("preview")
    preview.add_argument("file")

    # Undo
    subparsers.add_parser("undo")

    args = parser.parse_args()

    if args.command == "classify":
        classify_downloads(args.path)

    elif args.command == "clean-duplicates":
        clean_duplicates(args.path)

    elif args.command == "search":
        search_files(args.path, args.keyword)

    elif args.command == "preview":
        preview_file(args.file)

    elif args.command == "undo":
        undo_last_operation()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
