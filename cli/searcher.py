import os

def search_files(path, keyword):
    if not os.path.exists(path):
        print("❌ Path does not exist")
        return

    keyword = keyword.lower()
    results = []

    for root, _, files in os.walk(path):
        for file in files:
            if keyword in file.lower():
                results.append(os.path.join(root, file))

    if not results:
        print("❌ No files found")
        return

    print(f"✅ Found {len(results)} file(s):")
    for r in results:
        print(r)
