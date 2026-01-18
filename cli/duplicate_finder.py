import os
import hashlib
import shutil

def file_hash(file_path):
    """Generate MD5 hash of a file based on content"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception:
        return None


def clean_duplicates(path):
    """
    Finds duplicate files by content and
    safely moves duplicates to _Duplicates_Trash
    """

    if not os.path.exists(path):
        print("❌ Path does not exist")
        return

    trash_dir = os.path.join(path, "_Duplicates_Trash")
    os.makedirs(trash_dir, exist_ok=True)

    seen_hashes = {}
    duplicates = []

    for root, _, files in os.walk(path):
        # Skip trash folder itself
        if "_Duplicates_Trash" in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            file_hash_value = file_hash(file_path)

            if not file_hash_value:
                continue

            if file_hash_value in seen_hashes:
                duplicates.append(file_path)
            else:
                seen_hashes[file_hash_value] = file_path

    if not duplicates:
        print("✅ No duplicate files found")
        return

    print(f"⚠ Found {len(duplicates)} duplicate file(s):")
    for dup in duplicates:
        print("-", dup)

    confirm = input("\nMove duplicates to _Duplicates_Trash? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Operation cancelled")
        return

    for dup in duplicates:
        destination = os.path.join(trash_dir, os.path.basename(dup))
        shutil.move(dup, destination)

    print(f"✅ {len(duplicates)} duplicate file(s) moved to _Duplicates_Trash safely")
