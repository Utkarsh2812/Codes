import os

# Specify the directory where you want to create the folders
directory = "D:\cv_project\yolov4\Label"

# Specify the number of folders you want to create
n = 45

# Specify the list of folder names
# Specify the list of folder names
folder_names = ["Stop", "Give Way", "Straight Prohibitor No Entry", "Pedestrian Prohibited", "Horn Prohibited",
                "No Parking", "No Stopping or Standing", "Speed Limited", "Right Hand Curve", "Left Hand Curve",
                "Right Hair Pin Bend", "Left Hair Pin Bend", "Narrow Road Ahead", "Narrow Bridge",
                "Pedestrian Crossing", "School Ahead", "Round About", "Dangerous Dip", "Hump or Rough", "Barrier Ahead",
                "Right Reverse Bend", "Left Reverse Bend", "Steep Ascent", "Steep Descent", "Narrow Road Ahead",
                "Road Wideness Ahead", "Slippery Road", "Cycle Crossing", "Men At Work", "Cattle", "Falling Rocks",
                "Ferry", "Public Telephone", "Petrol Pump", "Hospital", "First Aid Post", "Eating Place",
                "Light Refreshment", "Resting Place", "No Thorough Road", "No Thorough Side Road", "Park This Side",
                "Parking Lot Scooter and Motorcycle", "Parking Lot Cycle", "Parking Lot Cars"]
# Check if the number of folders matches the length of the list
if n == len(folder_names):
    # Loop through the list and create each folder
    for name in folder_names:
        # Join the directory and the folder name
        path = os.path.join(directory, name)
        # Create the folder if it does not exist
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"Created folder {name}")
        else:
            print(f"Folder {name} already exists")
else:
    print("The number of folders and the length of the list do not match")
