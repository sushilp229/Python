# File name where tables will be saved
file_name = "tables_2_to_10.txt"

# Open the file in write mode
with open(file_name, "w") as file:
    # Generate tables from 2 to 10
    for i in range(2, 11):
        file.write(f"Multiplication Table of {i}\n")
        file.write("-" * 30 + "\n")

        for j in range(1, 11):
            file.write(f"{i} x {j} = {i * j}\n")

        file.write("\n")  # Blank line between tables

print(f"Tables from 2 to 10 have been written to '{file_name}' successfully.")