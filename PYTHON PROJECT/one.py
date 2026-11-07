import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("attendance.csv")

# 2. Validate data
valid_rows = []

for index, row in df.iterrows():

    held = row["Classes_Held"]
    attended = row["Classes_Attended"]

    if held <= 0:
        print(f"Row {index + 1} invalid: Classes held must be greater than 0.")
        continue

    if attended < 0:
        print(f"Row {index + 1} invalid: Attended cannot be negative.")
        continue

    if attended > held:
        print(f"Row {index + 1} invalid: attended ({attended}) cannot exceed held ({held}).")
        continue

    valid_rows.append(row)

# Create valid DataFrame
data = pd.DataFrame(valid_rows)

# 3. Calculate attendance percentage
if not data.empty:

    data["Percentage"] = (
        data["Classes_Attended"] /
        data["Classes_Held"]
    ) * 100

# 4. Display menu
print("\n===== COLLEGE ATTENDANCE ANALYZER =====")
print("1. Attendance Percentage")
print("2. Shortage List")
print("3. Subject-wise Average")
print("4. Exit")

choice = int(input("\nEnter your choice: "))

# OPTION 1: Attendance Percentage
if choice == 1:

    for index, row in data.iterrows():

        print(
            f'{row["Name"]}: '
            f'{row["Percentage"]:.2f}%'
        )

# OPTION 2: Shortage List
elif choice == 2:

    shortage = data[data["Percentage"] < 75]

    if shortage.empty:
        print("No student below 75%.")

        for index, row in data.iterrows():
            print(
                f'{row["Name"]} '
                f'({row["Percentage"]:.2f}%) is eligible.'
            )

    else:
        print("\nStudents below 75% attendance:")

        for index, row in shortage.iterrows():
            print(
                f'{row["Name"]}: '
                f'{row["Percentage"]:.2f}%'
            )

# OPTION 3: Subject-wise Average
elif choice == 3:

    subject_avg = data.groupby("Subject")["Percentage"].mean()

    print("\nSubject-wise Average:")

    print(subject_avg.round(2))

    # Bar Chart
    plt.figure(figsize=(8, 5))

    subject_avg.plot(kind="bar")

    plt.title("Subject-wise Average Attendance")
    plt.xlabel("Subject")
    plt.ylabel("Average Attendance (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # Pie Chart
    plt.figure(figsize=(7, 7))

    plt.pie(
        data["Percentage"],
        labels=data["Name"],
        autopct="%1.2f%%",
        startangle=90
    )

    plt.title("Student Attendance Distribution")
    plt.show()

elif choice == 4:
    print("Thank you for using Attendance Analyzer!")

else:
    print("Invalid choice! Please select 1 to 4.")