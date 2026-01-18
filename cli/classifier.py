import os, shutil, json

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Applications": [".exe", ".msi"],
    "Installers": [".iso", ".dmg"]
}

INDEX_FILE = "data/index.json"

def classify_downloads(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return

    log = []

    for folder in FILE_TYPES:
        os.makedirs(os.path.join(path, folder), exist_ok=True)
    os.makedirs(os.path.join(path, "Others"), exist_ok=True)

    for item in os.listdir(path):
        src = os.path.join(path, item)
        if os.path.isdir(src):
            continue

        ext = os.path.splitext(item)[1].lower()
        moved = False

        for folder, exts in FILE_TYPES.items():
            if ext in exts:
                dst = os.path.join(path, folder, item)
                shutil.move(src, dst)
                log.append({"from": src, "to": dst})
                moved = True
                break

        if not moved:
            dst = os.path.join(path, "Others", item)
            shutil.move(src, dst)
            log.append({"from": src, "to": dst})

    with open(INDEX_FILE, "w") as f:
        json.dump({"last_operation": log}, f, indent=2)

    print(f"Classified {len(log)} files")
