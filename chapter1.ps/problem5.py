from pathlib import Path

# Specify the folder path
folder_path = Path(r"C:\Users\shiva\OneDrive\Documents")

if folder_path.exists() and folder_path.is_dir():
    print("Files in the folder:")
    for file in folder_path.iterdir():
        if file.is_file():
            print(file.name)
else:
    print("Invalid folder path.")