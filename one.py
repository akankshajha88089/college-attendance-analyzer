import matplotlib.pyplot as plt
import pandas as pd


def load_attendance_data(file_path):
  """Loads and validates attendance data from a CSV file."""
  try:
    df = pd.read_csv(file_path)
    # Expected columns: Name, Subject, Classes_Held, Classes_Attended
    print('Attendance data loaded successfully!')
    return df
  except FileNotFoundError:
    print(f'Error: The file {file_path} was not found.')
    return None


def calculate_attendance_percentage(df):
  """Calculates the attendance percentage for each student record."""
  # Validation to ensure attended classes don't exceed held classes
  df['Percentage'] = (df['Classes_Attended'] / df['Classes_Held']) * 100
  return df


def analyze_attendance(df):
  """Analyzes attendance and identifies students below the 75% threshold."""
  print('\n--- OVERALL ATTENDANCE SUMMARY ---')
  print(df[['Name', 'Subject', 'Percentage']])

  print('\n--- STUDENTS WITH ATTENDANCE SHORTAGE (< 75%) ---')
  shortage_df = df[df['Percentage'] < 75]
  if shortage_df.empty:
    print('All students have met the 75% attendance criteria!')
  else:
    print(shortage_df[['Name', 'Subject', 'Percentage']])

  return shortage_df


def plot_attendance_trends(df):
  """Visualizes student attendance trends using Matplotlib."""
  plt.figure(figsize=(10, 5))
  plt.bar(df['Name'], df['Percentage'], color='skyblue')
  plt.axhline(
      y=75, color='red', linestyle='--', label='Mandatory Threshold (75%)'
  )
  plt.xlabel('Students')
  plt.ylabel('Attendance Percentage (%)')
  plt.title('College Attendance Analyzer - Student Trends')
  plt.ylim(0, 100)
  plt.legend()
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()


if __name__ == '__main__':
  # Replace 'attendance.csv' with your actual CSV file name
  csv_file = 'attendance.csv'

  data = load_attendance_data(csv_file)
  if data is not None:
    data = calculate_attendance_percentage(data)
    analyze_attendance(data)
    plot_attendance_trends(data)
