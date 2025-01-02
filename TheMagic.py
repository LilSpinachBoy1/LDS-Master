# IMPORTS
try:
    from os import listdir
    import pandas as pd
except ImportError:
    print("Pandas not installed. Please install pandas using 'pip install pandas'")
    exit()

# Access Data
"""
CHANGE THE data_path VARIABLE TO THE PATH OF THE DATA FOLDER ON YOUR COMPUTER
"""
data_path = r"C:\Users\Sam\OneDrive - Inspiration Trust\0 - A Levels\3 - Maths\3 - LDS\LDS as DB\DATA"
all_files = [data_path + "\\" + file for file in listdir(data_path)]
uk_files = [data_path + "\\" + file for file in listdir(data_path) if "UK" in file]
foreign_files = [data_path + "\\" + file for file in listdir(data_path) if "GLOBE" in file]


# Accessing data from the files
def find_max(files, category):
    wide_maxes = []  # The max for all files
    for file in files:
        narrow_maxes = []  # The max just for this file
        data = pd.read_csv(file)
        for i in data[category]:
            if i == "tr":
                continue
            else:
                narrow_maxes.append(i)
        wide_maxes.append(max(narrow_maxes))
    return max(wide_maxes)


def find_min(files, category):
    wide_min = []  # The max for all files
    for file in files:
        narrow_min = []  # The max just for this file
        data = pd.read_csv(file)
        for i in data[category]:
            if i == "tr":
                narrow_min.append(0)
            else:
                narrow_min.append(i)
        wide_min.append(min(narrow_min))
    return min(wide_min)


# Find the max temperature for each location
UK_max_temp = find_max(uk_files, "Daily Mean Temperature (0900-0900) (°C)")
GLOBE_max_temp = find_max(foreign_files, "Daily Mean Air Temperature")
print(f"UK MAX: {UK_max_temp}\nGLOBE MAX: {GLOBE_max_temp}")

# Find the min temperature for each location
UK_min_temp = find_min(uk_files, "Daily Mean Temperature (0900-0900) (°C)")
GLOBE_min_temp = find_min(foreign_files, "Daily Mean Air Temperature")
print(f"UK MIN: {UK_min_temp}\nGLOBE MIN: {GLOBE_min_temp}")