import os

path = r"C:\Users\shiva\OneDrive\Desktop"

for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
        print(item)