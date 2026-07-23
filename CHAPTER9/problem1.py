# File name to save the tables
file_name = "tables_2_to_10.txt1"

# Open the file in write mode
with open(file_name, "w") as file:
    # Generate tables from 2 to 10
    for i in range(2, 11):
        file.write(f"Multiplication Table of {i}\n")
        file.write("-" * 30 + "\n")

        for j in range(1, 11):
            file.write(f"{i} x {j} = {i * j}\n")

        file.write("\n")  # Blank line after each table

print(f"Tables from 2 to 10 have been written to '{file_name}' successfully.")