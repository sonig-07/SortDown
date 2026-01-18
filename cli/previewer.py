import os, zipfile, time

def preview_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    ext = os.path.splitext(file_path)[1].lower()
    size = os.path.getsize(file_path)
    modified = time.ctime(os.path.getmtime(file_path))

    print("File Preview")
    print("------------")
    print("Name:", os.path.basename(file_path))
    print("Type:", ext)
    print("Size:", size, "bytes")
    print("Modified:", modified)

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            print("\nContent Preview:\n")
            print(f.read(300))

    elif ext == ".zip":
        print("\nZIP Contents:")
        with zipfile.ZipFile(file_path, "r") as z:
            for name in z.namelist()[:10]:
                print("-", name)
