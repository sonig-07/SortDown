import json, os, shutil

INDEX_FILE = "data/index.json"

def undo_last_operation():
    if not os.path.exists(INDEX_FILE):
        print("No undo data found")
        return

    with open(INDEX_FILE, "r") as f:
        data = json.load(f)

    ops = data.get("last_operation", [])
    if not ops:
        print("Nothing to undo")
        return

    for op in reversed(ops):
        if os.path.exists(op["to"]):
            shutil.move(op["to"], op["from"])

    with open(INDEX_FILE, "w") as f:
        json.dump({"last_operation": []}, f, indent=2)

    print("Undo completed")
